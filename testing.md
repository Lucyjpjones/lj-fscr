## &rarr; **Testing**

**<details open><summary> Testing Documentation</summary>**
  - [Testing user stories](#testing-user-stories)
  - [Manual function testing](#manual-function-testing)
  - [Automated testing](#automated-testing)
  - [Validator checks](#validator-checks)
  - [Audits](#audits)
  - [Responsive Design](#responsive-design)
  - [Additional Testing](#additional-testing)
  - [Bugs](#bugs)
</details>

---

#### Testing user stories

<u>Viewing and Navigation</u>

1. Discover FSCR’s purpose and goals

I created an 'about' and 'meet the coaches' page so any site visitor can learn about the brand and the coaches behind it.

<img src="media/about-coaches.png">

2. View a list of products

I created a 'products' page incluing a list of all products, displaying product image, name and price, with the option to select an individual card for more details.

<img src="media/products-page.png">

3. View a list of programmes

I created a 'programmes' page incluing a list of all programmes, displaying product image, name and price, with the option to select an individual card for more details.

<img src="media/programmes-page.png">

4. View a specific category of products or programmes

I added a sort and filter option to both the products and programmes page. Users have the ability to sort alphabetically, by price or by highest rated. They also have the option to filter by category.

<img src="media/filter-page.png">

5. View individual product details

Each individual product page displays the products description, price, available sizes, product image and rating. There is also the ability to add to bag or redirect back to the products page.

<img src="media/product-details.png">

6. View individual programme details

Each individual programme page displays the programmes description, price, available sizes, programme image and rating. There is also the ability to add to bag or redirect back to the programmes page.

<img src="media/programme-details.png">

7. Easily access contact details

I have included a contact form on the home page which is also easily navigated to via the main nav menu. This has been set up using EmailJS with a custom template for organised recieving of user enquiries.

<img src="media/contact-form.png">

8. Browse associated blogs, articles and recent new stories

I created a blog app that can only be viewed by site members. When a user is not logged in and they click on the blog they will be directed to the login/register page. If a user is member and logged in they will be directed to the blog page where they can view blogs posted by the admin user. Members also have the ability to comment on blog posts creating user interaction.

<img src="media/blog-page.png">

9. Access a member forum

I created a forum app that can only be accessed by site members. When a user is not logged in and they click on the forum they will be directed to the login/register page. If a user is member and logged in they will be directed to the forum page where they will have the option to view threads by other users and add their own. They also have the capability of adding a message to any thread which displays both their logged in username and date/time posted.

<img src="media/forum-page.png">



<u>Registration and user accounts</u>

<u>Sorting and Searching</u>

<u>Purchasing and checkout</u>

<u>Admin and Store Management</u>

#### Manual function testing

To ensure my site was working correctly I carried out some manual function testing;

**Navigation**
  - I checked the site dropdown menu was working correctly by starting on the home-page and navigating around the site from and to every screen the user would be faced with.
  - I checked the logo homepage navigation was working by clicking on the brand image from every page.

**Authorisation**

  - To check the login functionality was working I first clicked on the profile icon and clicked 'login' to ensure I was directed to the correct page. When presented with the modal I conducted various checks;
    - I filled out the login form with an already registered username and password then clicked 'Login'.
    - I filled out the login form with a new username and password then clicked 'Login'.

- To check the Register functionality was working I first clicked on the profile icon and clicked 'register' to ensure I was directed to the correct page.
  - I filled out the registration form with a new username and password then clicked 'Register'.
  - I filled out the login form with an already registered username and password then clicked 'Register'.

<u>Site user/member</u>
  - Once I was logged in, the options available under the profile icon changed to 'my profile' and 'log out'. I was also able to access the blog and forum page.

<u>Site Owner</u>
- Once I was logged in, the options available under the profile icon changed to 'my profile', log out', 'product management' and 'programme management'. I was also able to access the blog and forum page.

**Form validation**

**Home**

**Products**

<u>View product functionality</u>

- I clicked on each product card to make sure it displayed the correct information to me when navigated to the view product HTML template, and it did.

<u>Add product functionality</u>

I logged in as admin user to check that the product management option was displayed in the profile menu, and it was. I then filled out the form and submitted and checked that the product was added to the products page.

<u>Edit product functionality</u>

When logged in as admin user I checked that the edit button was visible for all products on the programmes page, as well as on each individual view page. I then tested the functionality but clicking on the button and checking that i was directed to the edit page with all fields pre-filled with current information. I then made an amendment and clicked 'save changes' and checke that the information had been updated.

<u>Delete product functionality</u>

I checked the delete function buttons were all visible when logged in as admin and that when clicked the product was removed from the site.

**Programmes**

<u>View prgramme functionality</u>

- I clicked on each programme card to make sure it displayed the correct information to me when navigated to the view programme HTML template, and it did.

<u>Add programme functionality</u>

I logged in as admin user to check that the programme management option was displayed in the profile menu, and it was. I then filled out the form and submitted and checked that the programme was added to the programmes page.

<u>Edit programme functionality</u>

When logged in as admin user I checked that the edit button was visible for all programmes on the programmes page, as well as on each individual view page. I then tested the functionality but clicking on the button and checking that i was directed to the edit page with all fields pre-filled with current information. I then made an amendment and clicked 'save changes' and checke that the information had been updated.

<u>Delete programme functionality</u>

I checked the delete function buttons were all visible when logged in as admin and that when clicked the programme was removed from the site.

**Bag**

<u>Add to bag functionality</u>

I checked that my add to bag function was working by selecting a range of products and programmes and adding them to the bag to check there was no errors. Whilst creating this function I did experience difficulty adding from using id's to target products from different apps. I rectified this by adding in category to the url so i could differentiate products from programmes.

<u>View bag functionality</u>

**Checkout**

<u>Completing stripe payment</u>

<u>Pre-filled checkout details</u>

**Blog**

<u>Commenting on blog</u>

When logged in as a member/admin I clicked onto a variety of forums and entered a comment into the text field and clicked 'post'. I could see that the comment had been added below with the correct logged in username and date/time so I knew the functionality was working correctly.

**Forum**

<u>Adding Thread</u>

I checked that the functionality for adding a thread to the forum was working by logging in as a member/admin and clicking 'add thread' on the forums page. I was directed to a form to fill and when clicking 'post' I could see that my thread had been added to the forum page so I knew it was working correctly.

<u>Commenting on forum</u>

When logged in as a member/admin I clicked onto a variety of forums and entered a comment into the text field and clicked 'post'. I could see that the comment had been added below with the correct logged in username and date/time so I knew the functionality was working correctly.

#### Automated testing

I also decided to use Django's testing framework to create some automated tests for my prpject.


#### Validator checks

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. The code was entered through direct input. JS hint was used to check for any errors with my Javascript files. 
JS was also tested by opening the developer console window on Chrome and checking for any errors as I clicked through the site.
I used the PEP8 online checking tool to inspect my Python code against the style conventions in PEP 8.

- [**HTML Validator**](https://validator.w3.org/)


- [**CSS Validator**](https://jigsaw.w3.org/css-validator/)


- [**JS hint**](https://jshint.com/)


- **Developer tools**


- [**PEP8 online check**](http://pep8online.com/checkresult)


#### Audits

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to run a series of audits to improve the quality of web pages. Overall performance and errors are highlighted below.

#### Responsive Design

- Site created as a mobile-first design.

- Viewport tag included in the head of HTML files to tell the browser how to respond to different resolutions, particularly mobile ones.

- Media queries used in the CSS file to target larger devices.

#### Additional Testing

#### Bugs

|     | Bug                                                                           | Action                                                            |
|-----|-------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [] | Search icon showing border on ios                     |  need to solve |
| [] | Homepage postioning not filling screen as including search bar in vh                     |  need to solve |