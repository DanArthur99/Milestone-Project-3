# Music Gear Review Site

![Review Site shown on various screens](docs/readme-images/responsive.png)

Deployed Website: [Music Gear Review Site](https://gear-review-0801b9de8ec9.herokuapp.com/)


![Languages: 3](https://img.shields.io/badge/LANGUAGES-3-yellow)
![W3C HTML: Validated](https://img.shields.io/badge/W3C_HTML-VALIDATED-orange)
![W3C CSS: Validated](https://img.shields.io/badge/W3C_CSS-VALIDATED-blue)
![Contrubutors: 1](https://img.shields.io/badge/CONTRIBUTORS-1-green)


## CONTENTS

* [Project Goal](#Project-Goal)

* [User Experience (UX)](#User-Experience-UX)
  * [User Stories](#User-Stories)

  * [Design](#Design)
    * [Wireframes](#Wireframes)
    * [Typography](#Typography)
    * [Colour Scheme](#Colour-Scheme)
    * [Features](#Features)
    * [Accessibility](#Accessibility)

* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Frameworks & Other Libraries/Programs Used](#Frameworks--Other-LibrariesPrograms-Used)

* [Features](#Features)

* [Database Schema](#Database-Schema)
  * [Entity Relationship Diagram](#Entity-Relationship-Diagram)

* [Deployment & Local Development](#Deployment--Local-Development)
  * [Deployment](#Deployment)
  * [Local Development](#Local-Development)
    * [Forking a Repository](#Forking-a-Repository)
    * [Cloning a Repository](#Cloning-a-Repository)

* [Testing](#Testing)
  
* [Credits](#Credits)
  * [Code](#Code)
  * [Media](#Media)

## Project Goal 

The goal for this project was to create a simple review site where users can select or add a music product to review. 
Users can create an account and see reviews of other users for different gear.
This site makes for a very convenient and quick way for users to review and see reviews for different music equipment they are interested to purchasin.

## User Experience (UX)

### User Stories

#### Overall Client Goals

1. To be able to search for items within the database
2. To be able leave reviews for different items within the database
3. To be able to add new products to the database, if a user cannot see their desired product

#### First Time Visit Goals

1. To be able to sign up to the site with a unique username and password
2. To be able to leave/delete their own reviews for a specific product
3. To be able to see other peoples reviews of a specific product
4. To be able to search for a product using the site's search functionalities

#### Returning Visitor Goals

1. To be able to have a unique account that they can login into (created from signing up)
2. To be able to edit their account information, i.e. username and password
3. To be able to view their own reviews easily.
4. To be able to delete their personal accounts if they wish

### Design

#### Wireframes

##### Home Page

###### Logged Out

![Home Page Logged Out](docs/wireframes/home-page-logged-out.png)

###### Logged In

![Home Page Logged In](docs/wireframes/home-page-logged-in.png)

###### Mobile View

![Home Page Logged Out](docs/wireframes/home-page-mobile.png)

##### Search Page 

![Search Page](docs/wireframes/search-page.png)

##### Add Product Page 

![Add Product](docs/wireframes/add-product.png)

##### Add Review Page 

![Add Review](docs/wireframes/add-review.png)

##### About Gear Page

![About Gear](docs/wireframes/about-gear.png)

##### Categories Page

![Categories](docs/wireframes/categories-page.png)

##### Brands Page

![Brands](docs/wireframes/brands-page.png)

#### Typography

The Website primarily uses 3 different fonts throughout, obtained from Google Fonts. These fonts were:

Bungee Tint ('sans-serif')
Montserrat ('sans-serif')
New Amsterdam ('sans-serif')

"Bungee Tint" is used for the title page, as it is a very stylish looking font.

"Montserrat" is used as the default font for the website text, and "New Amsterdam" is used for the titles of each page, as it is a much bolder looking font, while not being as overly stylistic as "Bungee Tint."

#### Colour Palette

![Colour Palette](docs/readme-images/colour-palette.png)

### Technologies Used

#### Languages Used

The programming languages used for this project were:

* HTML5
* CSS3
* Python3

#### Frameworks & Other Libraries/Programs Used

* Git - Version Control
* Github - To save and store changes to the project
* [Bootstrap (v5.3.2)](https://getbootstrap.com/) - CSS and JS framework used. Used mainly for the navbar, grid structure, and button styling.
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Python Framework
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - Used to provide session management.
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/) - Integration of Flask and WTForms, used for Form validation.
* [bcrypt](https://pypi.org/project/bcrypt/) - Library used for password hashing.
* [Google Fonts](https://fonts.google.com/)- Imported selected fonts into external stylesheet, namely "Bungee Tint", "Montserrat", and "New Amsterdam."
* [Figma](https://www.figma.com/) - Used to create the wireframes.
* [Coolors](https://coolors.co/) - Used to create the colour palette images.
* [Favicon.io](https://favicon.io/) - To create favicon icons.
* [Shields.io](https://shields.io/) - Used to create badges.
* [Am I Responsive?](https://ui.dev/amiresponsive) - Used to create the multi-screen image you see at the start of this document.
* [W3C Markup Validation Service](https://validator.w3.org/) - Used for testing HTML validation.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used for testing CSS validation.
* [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/extension/) - Used for testing webpage accessibility. 


### Features

#### Main User Features

* Upon entering the size, the user is greeted with the home page, which just welcomes the user.

![Home Page](docs/readme-images/home-page.png)

* The user has the option, to sign up, login, or search for a product by either filtering through, brands, categories, or search for a specific item using the search bar.
* If the user hasn't already, they can sign up using the sign section. This stores, their username, email, and hashed password within the database

![Sign Up](docs/readme-images/sign-up.png)

* Once they sign up, they can then log in and access their own personal account.

![Login](docs/readme-images//login-page.png)

* They now have access to their own account dashboard, which allows them to view and edit their username and email, as well as give them the option to change their password, or even delete their account

![Dashboard](docs/readme-images/dashboard.png)

* Users can also see all the reviews they have written inside it's own "Your Reviews" section.

![User Reviews](docs/readme-images/your-reviews.png)

* Users can search for products and see reviews written by other users, and if they have an account they can write a review themselves

![Search](docs/readme-images/search-results.png)
![About Gear](docs/readme-images/product-reviews-list.png)

* Users also have the option to add a new product to the system, which themselves and other users can write reviews on.

![Add Product](docs/readme-images/add-product.png)

* Users are also able to update and delete their own reviews

![Update Review](docs/readme-images/edit-review.png)
![Delete Review](docs/readme-images/delete-review.png)

* As well as the search bar, the user is also able to browse through the categories and brands in order to find the item they are looking for
  * Brands:
![Brands](docs/readme-images/brands.png)
![Brands Gear List](docs/readme-images/brand-gear-list.png)
  * Categories:
![Categories](docs/readme-images/categories.png)
![Category Gear List](docs/readme-images/category-gear-list.png)

#### Validation

##### Unathorized Access

* Measures have been implemented so that users are always unable to access pages that they should. This could be, for example, a user being able to another user's dashboard, being able to edit and delete other people's reviews, or regular users access admin only pages and functions.

* If a user ever manages to find themselves accessing the URL of a page they shouldn't, they will be immediately booted out and an error message will display.

![Unauthorized](docs/readme-images/not-authorised.png)

* A similar feature is implement should a user try to access an account functionality when not logged in. For example, a user cannot leave a review should they not be logged in, nor can they access any dashboards, as well as other features.

![Login Required](docs/readme-images/login-required.png)

* If the user trys to sign up using an existing email or username, then it was display a flash error message and reload the sign up page

![Sign Up Error](docs/readme-images/sign-up-error.png)

* Likewise, if the user tries to write a review for a product they have already reviewed, then it'll redirect the user and display a flash message.

![Review Duplicate](docs/readme-images/review-duplicate-message.png)

##### 

#### Admin Only Features

* If a user is also an admin user, then they will have access to significantly more functonality. 
* This includes, being able to add, edit and delete brands and categories from the database.

![Admin Brands](docs/readme-images/admin-brands.png)
![Admin Categories](docs/readme-images/admin-categories.png)

* Admin users are also able to search through users and access their dashboards, close user accounts, and edit or delete any review

![Search Users](docs/readme-images/search-users.png)

#### Potential Future Feautures

Some potential features that I would like to include include:

* Admin users being able to change whether other users are admin or not
* More interactivity, such as having a phyical star rating that they can select, rather than a drop down 0-5 menu
* 

#### Going Through the Code

### Database Schema

#### Entity Relationship Diagram

![Entity Relationship Diagram](docs/readme-images/entity-relationship-diagram.png)


## Deployment & Local Development

### Deployment

Github Pages and Heroku was used to deploy the live website. The instructions to achieve this are below:

1. Login to Heroku


### Local Development

#### Forking a Repository

To fork the repository:

  1. Log in or Sign Up to Github.
  2. Go to the repository for this project, DanArthur99 / Milestone-Project-3.
  3. Click the Fork button in the top right corner.

#### Cloning a Repository

To clone the repository:

  1. Log in or Sign Up to GitHub.
  2. Go to the repository for this project, DanArthur99 / Milestone-Project-3.
  3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
  4. Open the terminal in your IDE and set your working directory to the location you want to use for the cloned repository.
  5. Type 'git clone' into the terminal window, and paste the link from step 3, then press enter.
  6. Your cloned repository should now be located in your chosen directory
  7. Open your terminal window, and type in the following command, " pip install -r requirements.txt ". This will install all dependencies for this project onto your local machine
  8. You are now ready ready for local development.


## Testing

## Credits

### Code


### Other References 






