# CS50 Auctions

This project is a part of the CS50's Web Programming with Python and JavaScript course. It is an eBay-like e-commerce auction site that allows users to post auction listings, place bids, comment on listings, and add listings to a watchlist.

## Table of Contents
- [Project Specifications](#project-specifications)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Views](#views)
- [Templates](#templates)
- [Admin Interface](#admin-interface)
- [Contributing](#contributing)
- [Acknowledgments](#Acknowledgments)
- [Contact](#Contact)

## Project Specifications

The project requirements include the following:

1. **Models**: 
    - User model (inherited from `AbstractUser`)
    - Auction listings model
    - Bids model
    - Comments model
2. **Create Listing**: 
    - Users can create a new auction listing with a title, description, starting bid, optional image URL, and category.
3. **Active Listings Page**: 
    - Displays all active auction listings with title, description, current price, and photo.
4. **Listing Page**: 
    - Shows details of a specific listing with options to add to watchlist, bid on the item, close the auction, and add comments.
5. **Watchlist**: 
    - Displays all listings added to the user's watchlist.
6. **Categories**: 
    - Lists all categories and shows active listings in each category.
7. **Django Admin Interface**: 
    - Admin can view, add, edit, and delete listings, comments, and bids.

## Features

- User authentication (register, login, logout)
- Create, edit, and manage auction listings
- Place bids on listings
- Add/remove listings to/from a watchlist
- Comment on listings
- Close auctions to declare winners
- View listings by category
- Admin interface for managing the site

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Master-Vasu/CS50-Auctions.git
    cd CS50-Auctions
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Make migrations and migrate the database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser for the admin interface**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Visit the application**:
    Open your browser and go to `http://127.0.0.1:8000`

## Usage

- Register for an account and log in.
- Create new auction listings from the "Create Listing" page.
- View and manage active listings on the home page.
- Add listings to your watchlist and manage them from the "Watchlist" page.
- Place bids on listings from their individual pages.
- Comment on listings and close auctions if you are the creator.

## Models

- **User**: Inherits from `AbstractUser`, includes default fields.
- **Auction Listing**: Title, description, starting bid, current bid, image URL, category, active status, creator.
- **Bid**: User, amount, associated listing.
- **Comment**: User, content, associated listing.

## Views

- **Index**: Displays all active listings.
- **Listing**: Detailed view of a specific listing.
- **Create Listing**: Form for creating a new listing.
- **Watchlist**: Shows all listings added to the user's watchlist.
- **Categories**: Displays all categories and active listings within them.

## Templates

- **layout.html**: Base layout for all templates.
- **index.html**: Home page with active listings.
- **listing.html**: Detailed view of a single listing.
- **create_listing.html**: Form for creating a new listing.
- **watchlist.html**: User's watchlist.
- **categories.html**: List of categories and their listings.

## Admin Interface

- Admins can manage users, auction listings, bids, and comments through the Django admin interface at `http://127.0.0.1:8000/admin`.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue with your suggestions. Please follow the guidelines below when contributing:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

## Acknowledgments

- [CS50 Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/) - The course that inspired this project.
- The amazing team and community at Harvard University and CS50.
- [Django](https://www.djangoproject.com/) - For the web framework.

## Contact

If you have any questions or feedback, feel free to reach out:

- GitHub: [Master-Vasu](https://github.com/Master-Vasu)
- Twitter/X: [Vasu_arcR](https://x.com/Vasu_arcR)
- vasumoradiya@gmail.com
