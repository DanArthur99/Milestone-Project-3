# Music Gear Review - Testing Document

## CONTENTS
* [Manual Testing](#Manual-Testing)
  * [Full Testing](#Full-Testing)
    * [Login and Sign Up](#login-and-sign-up-testing)
    * [CRUD Functionality](#crud-functionality)
    * [User Validation](#user-validation)
    * [Admin Features](#admin-features)
* [PythonLinter](#python-linter)
* [W3C Validator](#W3C-Validator)
* [Wave Accessibiliy Testing](#Wave-Accessibility-TSesting)
* [Bugs](#Bugs)
  * [Solved Bugs](#Solved-Bugs)
* [Testing User Stories](#Testing-User-Stories)

## Manual Testing

### Full Testing

The site was tested on the following systems:

* Cyberpower Ryzen 5 - OS: Windows 11 v23H2
* Samsung Galaxy A52S 5G

This was also tested on the following browsers:

* Google Chrome - Version 125.0.6422.77 (64-bit)
* Microsoft Edge - Version 125.0.2535.51 (64-bit)
* Mozilla Firefox - Version 126.0 (64-bit)

#### Login and Sign Up Testing

**Test**|**Expected Outcome**|**Test Action**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Create User Account|Users data is added to the databse|Signed Up with a new username and email|New account created|Pass
Login test|The user should be logged in once they type in their email password to the login page|Enter email and passord|User is logged on|Pass
Incorrect email login test|The user should be informed that the user is not recognised|Enter wrong email and click submit|"Flash message appears| user is not logged on"
Incorrect password login test|The user should be informed that the password is not recognised|Enter wrong password and click submit|"Flash message appears| user is not logged on"
Incorrect email format test|The site should prompt the user to enter an email in the correct format|Enter an incorrect email format in the email field|Message pops up saying to use a valid email format|Pass
Unique Email and Username |The user cannot sign up with an email or username that already exists|Enter an existing email or username on the sign up page|"Flash message appears saying an error occurred| account is not created"
Update Details|"The user can change their username or email address to whatever they wish| and the database will update"|Click update details and change username|Username changed 
Unique Email and Username #2|User cannot change their email or password to one that already exists|Enter a usernasme or email that already exists|"Flash message appears saying an error occurred| user is not updated"
Update Password|"User is able to update their password from their dashboard| this can be whatever they wish| they can then log in using the new password"|Change password then attempt to log in
Closing user account|"Th user can  choose to close their account| if they wish| which deletes their account. They'll no longer be able to log in with their details"|Attempt to login with old details
Login and sign up blank field test|"If the user tries to submit either of these forms with a blank field| then it will not submit the form and a message will appear saying the field is requeired"|submit sign up form with blank field|"User is prompted to fill in field

#### CRUD Functionality

**Test**|**Expected Outcome**|**Test Action**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Search function|User is able to use the search bar to search for for products in the database|"Type in ""fender"" in the search bar and click submit"|Results appear on next page|Pass
Search blank test|"User cannnot do a blank search| the form should not submit when nothing in the search bar"|Blank search|"User is prompted to enter something in the search bar
Add review|"The user is able to select a product and write a review for this product| which is then publically displayed"|review is submitted|Review is now display on the product dashboard
Add review blank test|The user cannot submit a review with a blank field|Submit review with blank field|"User is prompted to fill in field| form is not submitted"
Add review duplicate test|"The user cannot write more than one review per product| it will display a message saying you've already submitted a review"|Try to submit a second review for a product|Flash message appears saying you've already written a review
Add Product Test|The user can add a new product to the system to review if not already there|Enter details for a new product|Product is added to the database|Pass
Add Product Blank field test|"If a form field is blank| then the user will be prompted to fill in the field"|try to the form with a blank field|User prompted for field data 
Add Product duplicate|user cannot add a product in the database that already exists|Attempt to submit a product with an existing name|"Flash message appears saying an error occurred| product is not added"
Edit review test|user is able to edit their own reviews|Click edit review and change the contents of the review|The review is updated and the changed are displayed|Pass
Delete review test|user is able to delete their own reviews|Click delete review|"The review is removed from the database| review is no longer displayed"

#### User Validation

**Test**|**Expected Outcome**|**Test Action**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
User dashboard access test|The user is not authorised to access the dashboard of any other user|"Copy user dashboard url| then log into another user (non-admin)| and paste url"
User edit review access test|The user is not authorised to access the edit review page of any other user|"Copy user edit review url| then log into another user (non-admin)| and paste url"
User update details access test|The user is not authorised to access the update details page of any other user|"Copy user edit review url| then log into another user (non-admin)| and paste url"
User delete user access test|The user is not authorised to delete any other user|"Copy user delete user url| then log into another user (non-admin)| and paste url"
User delete review access test|The user is not authorised to delete any other user's reviews|"Copy user delete review url| then log into another user (non-admin)| and paste url"
User add brand access test|"The user is not authorised to access the add brand page| as this admin-only"|"Copy user add brand url from an admin account| then log into another user (non-admin)
User add category access test|"The user is not authorised to access the add category page| as this admin-only"|"Copy user add brand url from an admin account| then log into another user (non-admin)
User delete product access test|"The user is not authorised to access the delete product page| as this admin-only"|"Copy user delete product url from an admin account| then log into another user (non-admin)
User edit brand access test|"The user is not authorised to access the edit brand page| as this admin-only"|"Copy user edit brand url from an admin account| then log into another user (non-admin)
User delete brand access test|"The user is not authorised to access the delete brand page| as this admin-only"|"Copy user delete brand url from an admin account| then log into another user (non-admin)
User edit category access test|"The user is not authorised to access the edit category page| as this admin-only"|"Copy user edit category url from an admin account| then log into another user (non-admin)
User delete category access test|"The user is not authorised to access the delete category page| as this admin-only"|"Copy user delete category url from an admin account| then log into another user (non-admin)

#### Admin Features

Test,Expected Outcome,Test Action,Result,Pass/Fail
Admin search users,The admin user is able to search for users in the database,"click ""search users"" and type in the search bar",users are displayed,Pass
Admin search users blank test,The admin user search bar cannot be submitted blank,click search users submit button with empty search bar,user is prompted for field data,Pass
Admin dashboard access,The admin user is able to acess the dashboard of any other user,"Copy user (non-admin) dashbooard url, then log into another user (admin), and paste url",User dashboard loads,Pass
Admin update details,The admin user is able to access the update details page of any user,"from the user dashboard, click update details",User's update details page loads,Pass
Admin delete user,the admin user is able to delete any user from the database,"From the user dashboard, click delete user","Modal appears for a double check, then user is deleted from database when yes is clicked",Pass
Admin add brand,The admin user is able to add a new brand to the database,"Click Add Brand from the brands page, enter the brand name and click submit",brand is now added to the database and displayed on the brands screen,Pass
Admin add category,The admin user is able to add a new category to the database,"Click Add Category from the categories page, enter the brand name and click submit",category is now added to the database and displayed on the brands screen,Pass
Admin edit brand,The admin user is able to edit a brand name,"Click on any edit brand from the brands page, then write the new brand name",Brand name is now updated,Pass
Admin edit category,The admin user is able to edit a category name,"Click on any edit category from the categories page, then write the new brand name",Category name is now updated,Pass
Admin delete brand,"The admin user is able to delete a brand, along with all product under that brand",Click delete brand on one of the brands from the brands page,"The chosen brand is delete from the database, along with all products an their reviews",Pass
Admin delete category,"The admin user is able to delete a category, along with all product under that category",Click delete category on one of the categories from the categories page,"The chosen category is delete from the database, along with all products an their reviews",Pass
Add Brand blank test,The admin user cannot submit a blank field ,Click add brand and click submit while brand name field is empty,user is prompted for field data,Pass
Add Category blank test,The admin user cannot submit a blank field ,Click add category and click submit while category name field is empty,user is prompted for field data,Pass
Edit Brand blank test,The admin user cannot submit a blank field ,Click edit brand and click submit while brand name field is empty,user is prompted for field data,Pass
Edit Category blank test,The admin user cannot submit a blank field ,Click edit category and click submit while category name field is empty,user is prompted for field data,Pass
Add Brand duplcate test,The admin user cannot add a brand name that already exists,Submit a brand name that already exists in the database,"Flash message appears saying an error occurred, brand is not added to database",Pass
Add Category duplicate test,The admin user cannot add a category name that already exists,Submit a category name that already exists in the database,"Flash message appears saying an error occurred, category is not added to database",Pass
Edit Brand duplicate test,The admin user cannot add a brand name that already exists,Submit a brand name that already exists in the database,"Flash message appears saying an error occurred, brand is not updated",Pass
Edit Category duplicate test,The admin user cannot add a category name that already exist,Submit a category name that already exists in the database,"Flash message appears saying an error occurred, category is not updated",Pass
Admin delete product test,"The admin is able to delete any product from the database, along with its reviews",Click delete product on the product dashboard,"Modal appears for a double check, then product is deleted from database when yes is clicked, along with all reviews of that product",Pass
Admin edit reviews,The admin is able to edit any user's reviews ,"Click on a user's dashboard, then click on the link to see their reviews, choose any review, and edit it","the edit review page loads, and when the admin user clicks submit, the edited review is displayed",Pass
Admin delete reviews,The admin is able to delete any user's reviews ,"Click on a user's dashboard, then click on the link to see their reviews, choose any review, and click ""delete review""","Modal appears for a double check, then review is deleted from database when yes is clicked",Pass

## Python Linter

### __init.py

* The only error I am getting here is the fact that the import line is not at the top of the page, however in this case, this is required for the program to function properly

![Init.py Linter](docs/readme-images/init-linter.png)

### run.py

![Run.py Linter](docs/readme-images/linter-pass.png)

### forms.py

![Forms.py Linter](docs/readme-images/linter-pass.png)

### model.py

![Model.py Linter](docs/readme-images/linter-pass.png)

### routes.py

![Routes.py Linter](docs/readme-images/linter-pass.png)

## W3C Validator

* On pages that use 2 different forms, there are 2 different csrf tokens which generate the same id name. 
I have used JavaScript to edit on the id names when the DOM Content is loaded.

![id Name Change](docs/readme-images/js-id-name-change.png)

### Home Page

![Home]

### Login Page

![W3C Home Page](docs/readme-images/home-page-html-validation.png)

### Sign Up Page

![W3C Sign Up](docs/readme-images/w3c-html-sign-up.png)

### Brands Page

![W3C Brands](docs/readme-images/w3c-brands-page.png)

### Categories Page

![W3C Categories](docs/readme-images/w3c-html-categories.png)

### Search Page

![W3C Search](docs/readme-images/w3c-search.png)

### Add Product Page

![W3C Add Product](docs/readme-images/w3c-html-add-product.png)

### Dashboard

![W3C Dashboard](docs/readme-images/w3c-html-dashboard.png)

### Stylesheet Validator

![W3C-Stylesheet](docs/readme-images/w3c-stylesheet.png)

## Wave Accessibility Testing

### Home Page

![Wave Home Page](docs/readme-images/wave-home-page.png)

### Sign Up Page

![Wave Sign Up](docs/readme-images/wave-sign-up.png)

### Login Page

![Wave Login](docs/readme-images/wave-login-page.png)

### Brands Page

![Wave Brands Page](docs/readme-images/wave-brands.png)

### Categories Page

![Wave Categories Page](docs/readme-images/wave-categories.png)

### Search Page

![Wave Search](docs/readme-images/wave-search.png)

## Bugs

### Solved Bugs

* The main issues I had were to do with user validation. I had problems where users were able to access pages that they should not have authorization to. The fix was fairly simple, and used an if statement to check if the current_user was admin, or if the current_user.id matched that of the review.user_id, or the dashboard user_id, etc.

![Validity Checker](docs/readme-images/validity-chcker-if-statement.png)

This checker and variations of it has been used throughout the routes.py file to check if the user has the correct authorisation.

## Testing User Stories

### Overall Client Goals

1. To be able to search for items within the database

![Search](docs/readme-images/search-results.png)

2. To be able read reviews for different items within the database

!![Read Reviews](docs/readme-images/read-reviews.png)

3. To be able to add new products to the database, if a user cannot see their desired product

![Add Product](docs/readme-images/add-product.png)

### First Time Visit Goals

1. To be able to sign up to the site with a unique username and password

![Sign Up](docs/readme-images/sign-up.png)
![Dashboard](docs/readme-images/dashboard.png)

2. To be able to leave/delete their own reviews for a specific product

![Add Review](docs/readme-images/add-review.png)
![Your Reviews](docs/readme-images/your-reviews.png)

### Returning Visitor Goals

1. To be able to have a unique account that they can login into (created from signing up)

![Login](docs/readme-images/login-page.png)
![Dashboard](docs/readme-images/dashboard.png)

2. To be able to edit their account information, i.e. username and password

![Update Details](docs/readme-images/update-details.png)
![Update Password](docs/readme-images/update-password.png)

3. To be able to view their own reviews easily.

![Your Reviews](docs/readme-images/your-reviews.png)

4. To be able to delete their personal accounts if they wish

![Close Account Modal](docs/readme-images/delete-account-modal.png)
![User Deleted](docs/readme-images/user-deleted.png)



