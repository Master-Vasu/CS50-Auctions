from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Listing, Categories, Comments, Bid


def index(request):
    activeListings = Listing.objects.filter(isActive=True)
    currentUser = request.user
    context = {
        "listings": activeListings,
        "message": "All Categories"
    }
    if currentUser.is_authenticated:    
        numOfWatchlist = len(currentUser.listingWatchlist.all())
        context["numOfWatchlist"] = numOfWatchlist

    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    

def create(request):
    currentUser = request.user
    numOfWatchlist = len(currentUser.listingWatchlist.all())
    if request.method == "GET":
        return render(request, "auctions/create.html", {
            "allCategories": Categories.objects.all(),
            "numOfWatchlist": numOfWatchlist,
        })
    else:
        title = request.POST["title"]
        desc = request.POST["desc"]
        imageUrl = request.POST["imageUrl"]
        price = (request.POST["price"])
        lister = request.user
        category = request.POST["category"]
        categoryName = Categories.objects.get(categoryName=category)

        bid = Bid(bid=int(price), bidder=lister)
        bid.save()

        newListing = Listing(
            title=title,
            description=desc,
            imageURL=imageUrl,
            price=bid,
            lister=lister,
            category=categoryName
        )
        newListing.save()

        return HttpResponseRedirect(reverse(index))
    

def categories(request):
    currentUser = request.user
    context = {"allCategories": Categories.objects.all()}
    if currentUser.is_authenticated:
        numOfWatchlist = len(currentUser.listingWatchlist.all())
        context["numOfWatchlist"] = numOfWatchlist

    return render(request, "auctions/categories.html", context)


def categoryListing(request, name):
    if name == "allCategories":
        return HttpResponseRedirect(reverse("index"))
    else:
        # Use get_object_or_404 to handle the case where the category does not exist
        categoryName = get_object_or_404(Categories, categoryName=name)
        activeListings = Listing.objects.filter(isActive=True, category=categoryName)
        currentUser = request.user
        context = {
            "listings": activeListings,
            "message": categoryName.categoryName,
        }
        if currentUser.is_authenticated:
            numOfWatchlist = len(currentUser.listingWatchlist.all())
            context["numOfWatchlist"] = numOfWatchlist

        return render(request, "auctions/index.html", context)
    

def listing(request, id):
    currentUser = request.user
    if currentUser.is_authenticated:
        listingData = Listing.objects.get(pk=id)
        isInWatchlist = request.user in listingData.watchlist.all()
        isOwner = request.user.username == listingData.lister.username
        numOfWatchlist = len(currentUser.listingWatchlist.all())
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "isInWatchlist": isInWatchlist,
            "allComments": Comments.objects.filter(listing=listingData),
            "isOwner": isOwner,
            "numOfWatchlist": numOfWatchlist,
        })
    else:
        return render(request, "auctions/login.html")


def removeWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))


def addWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))


def watchlist(request):
    currentUser = request.user
    listings = currentUser.listingWatchlist.all()
    numOfWatchlist = len(currentUser.listingWatchlist.all())
    return render(request, "auctions/watchlist.html", {
        "listings": listings,
        "numOfWatchlist": numOfWatchlist,
    })

def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['newComment']
    newComment = Comments(author=currentUser, listing=listingData, comment=message)
    newComment.save()
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def addBid(request, id):
    newBid = request.POST["addBid"]
    listingData = Listing.objects.get(pk=id)
    isInWatchlist = request.user in listingData.watchlist.all()
    currentUser = request.user
    numOfWatchlist = len(currentUser.listingWatchlist.all())
    isOwner = request.user.username == listingData.lister.username
    if int(newBid) > listingData.price.bid:
        if not isInWatchlist:
            listingData.watchlist.add(currentUser)
            isInWatchlist = True
        updateBid = Bid(bidder=request.user, bid=int(newBid))
        updateBid.save()
        listingData.price = updateBid
        listingData.save()        
        numOfWatchlist = len(currentUser.listingWatchlist.all())
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "isInWatchlist": isInWatchlist,
            "isOwner": isOwner,
            "allComments": Comments.objects.filter(listing=listingData),
            "message": "Congratulations, Bid is submitted!",
            "updation": True,
            "numOfWatchlist": numOfWatchlist,
        })
    else:
        numOfWatchlist = len(currentUser.listingWatchlist.all())
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "isInWatchlist": isInWatchlist,
            "allComments": Comments.objects.filter(listing=listingData),
            "isOwner": isOwner,
            "message": "Bid is not submitted!, Enter bid more than its actual price",
            "updation": False,
            "numOfWatchlist": numOfWatchlist,
        })
    
def closeBid(request, id):
    listingData = Listing.objects.get(pk=id)
    listingData.isActive = False
    listingData.save()
    isOwner = request.user.username == listingData.lister.username
    isInWatchlist = request.user in listingData.watchlist.all()
    currentUser = request.user
    numOfWatchlist = len(currentUser.listingWatchlist.all())
    return render(request, "auctions/listing.html", {
            "listing": listingData,
            "isInWatchlist": isInWatchlist,
            "allComments": Comments.objects.filter(listing=listingData),
            "isOwner": isOwner,
            "message": "Congratulations, Your Bid is Closed.",
            "updation": True,
            "numOfWatchlist": numOfWatchlist,
        })