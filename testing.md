## <ins>Testing</ins>

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

### **Testing user stories**

#### <ins>Viewing and Navigation</ins>

**1. Discover FSCR’s purpose and goals**

I created an 'about' and 'meet the coaches' page so any site visitor can learn about the brand and the coaches behind it. Both pages are easily accessible via the main nav menu.

<img src="readme/media/us-1.png">

**2. View a list of products**

I created a 'products' page including a list of all products, displaying product image, name, colour, price, and rating, with the option to select an individual card for more details.

<img src="readme/media/us-2.png">

**3. View a list of programmes**

I created a 'programmes' page including a list of all programmes, displaying programme image, name, price, and rating, with the option to select an individual card for more details.

<img src="readme/media/us-3.png">

**4. View a specific category of products or programmes**

I added a filter option to both the products and programmes page giving users the ability to quickly find what they are searching for. 

`(More specific details on this in user story 17)`

**5. View individual product details**

Each product detail page displays the product's image, name, colour, price, rating, description, and available sizes. There is also a quantity selector, the ability to add a product to bag or redirect back to the products page.

<img src="readme/media/us-4.png">

**6. View individual programme details**

Each programme detail page displays the programme's image, name, price, rating, description, what's included, and reviews. There is also a quantity selector, the ability to add a programme to bag or redirect back to the programmes page.

<img src="readme/media/us-5.png">

**7. Easily access contact details**

I have included a contact form on the home page which is also easily navigated to via the main nav menu. This has been set up using EmailJS with my own customised email template to assist with the organisation of user enquiries.

<img src="readme/media/us-6.png">

**8. See reviews and ratings on products and programmes**

Testimonials are visible on the homepage and reviews are available on the programmes detail page. Users are also able to see the rating for each individual product/programme under each item on the products/programmes page and additionally on the product/programme details page.

> **NB:** As this is a startup that hasn't yet started the business the testimonials, reviews, and ratings are currently only mockups.

<img src="readme/media/us-7.png">

**9. Browse associated blogs, articles, and recent new stories**

I created a blog app that can only be viewed by site members. The page is available through the nav menu and there is also the option for the user to direct to the latest blogs via the homepage. When a user is not logged in and they click on the blog they will be directed to the login/register page. If a user is a member and logged in they will be directed to the blog page where they can view blogs posted by the admin user. Members also have the ability to add and delete their own comments on blog posts creating further user interaction.

<img src="readme/media/us-8.png">

- The delete function has a confirmation modal which gives an extra step for users to consider their action.

<img src="readme/media/us-88.png">

**10. Access a member forum**

I created a forum app that can only be accessed by site members. When a user is not logged in and they click on the forum they will be directed to the login/register page. If a user is a member and logged in they will be directed to the forum page where they will have the option to view threads by other users and add/edit their own. They also have the capability of replying to any thread, with the logged in username and date/time automatically saved.

<img src="readme/media/us-9.png">

- The delete function has a confirmation modal which gives an extra step for users to consider their action.

<img src="readme/media/us-99.png">

#### <ins>Registration and user accounts</ins>

**10. Easily register for an account**

A fully functioning register page where a user can enter their details to create an account. The user can access this page by clicking on the recognisable user icon and selecting 'Register'.

<img src="readme/media/us-10.png">

**11. Receive an email confirmation after registering**

After registering the user is directed to a registration success page where they are informed that they will receive an email to validate their email address and complete registration.

<img src="readme/media/us-11.png">

**12. Easily login or logout**

When a user is registered they have the ability to easily log into their account. The user can click on the profile icon, then select login and enter their details to sign into their account. Once logged in the user will be able to log out via the profile icon.

I also decided to add social logins to allow my user to login more quickly. The user can choose their preferred platform (Facebook, Google, or Twitter) and follow the authorisation for the specified site. (Facebook screenshots included below).

<img src="readme/media/us-12.png">

**13. Easily update my personal details**

Each registered user has their own profile page where they can store their personal details including name, email, and delivery details. This information can be easily updated by filling in any field and then clicking 'update details'.

<img src="readme/media/us-13.png">

**14. Easily recover my password in case I forget it**

If a user forgets their password they have the option to click the 'forgot password' link. This will direct them to another page which will inform the user that an email has been sent to them to recover their password. The email contains a link that redirects the user to the change password page where they can enter a new password for their account. After submitting a new password the user is redirected to the login in page and can login using their new password.

<img src="readme/media/us-14.png">

**15. Have a personalised user profile**

The profile page is specific to each user with a personalised username greeting, the option to save their own entered details, and a log of their order history.
- I added the 'dictsortreversed' filter with key 'date' to ensure orders are listed in descending order with most recent showing first.

<img src="readme/media/us-15.png">

**16. Enable my details to be prefilled**

If the user has filled in their profile information, these details will be prefilled at checkout. The user also has the option to tick the save details options on checkout which will automatically save details to their profile page.

<img src="readme/media/us-16.png">

#### <ins>Sorting and Searching</ins>

**17. Sort and filter the list of available products and programmes**

I have added a sort and filter option to the products and programmes page to allow a user to easily find what they are looking for. There is a 'clear all' option at the top of the filter dropdown which allows a user to remove the filter and display all items. 
- I also decided to add this function to the blog page as I think it will be useful to the user as more blogs get posted over time. 

The pages also feature a count functionality showing the user how many items are being displayed on the page. For example, if the user filtered the products page by accessories they would see all the accessories and the number of products found. If no products are found the user would be displayed with the message "Sorry no search results found".

<img src="readme/media/us-17.png">

**18. Search the site by keywords**

A search bar features in the main site header and allows users to search by keywords to find specific items. On larger screens the search bar is visible and on smaller devices, the search bar is collapsed from the search icon.
- The filtered queries include product name, product description, programme name, programme description, and blog post title.
- 'icontains' has been used making the search case-insensitive. Although some results aren't always seen as logical I wanted to continue to use icontains over iexact as it creates a more flexible search. As the site develops I will look into other ways of creating a more robust search.

<img src="readme/media/us-18.png">

**19. Easily see what I’ve searched for and the number of results**

The products, programmes and blog page all feature a results count to show the user how many items are available to them. (View user story 17 and 18 for screenshots)


#### <ins>Purchasing and checkout</ins>

**20. Easily select the size and quantity of a product/programme when purchasing it**

The product detail page allows a user to select a specific size, if the product is sized, and the quantity of a product.
The programme detail page allows a user to select a quantity of a programme to add to their bag.

<img src="readme/media/us-20.png">

**21. View items in my bag to be purchased**

The bag view allows the user to view all the products and programmes they have added to their bag before continuing to the checkout.

<img src="readme/media/us-21.png">

**22. Adjust the quantity of individual items in my bag**

The user has the ability to adjust the number of products and programmes in their bag before continuing to checkout.

<img src="readme/media/us-22.png">

**23. Easily enter my payment information and feel my personal and payment information is safe and secure**

The checkout page features a payment form allowing the user to easily enter their card details for a quick checkout.

<img src="readme/media/us-23.png">

**25. View an order confirmation after checkout**

Once the user has made a purchase they are directed to a checkout success page where they can see a summary of their order so they can check that they haven't made any mistakes.

<img src="readme/media/us-25.png">

**26. Receive an email confirmation after checking out**

Once the user has made a purchase they are sent an email with a summary of their order to keep for their own records.

<img src="readme/media/us-26.png">

#### <ins>Admin and Store Management</ins>

**27. Add a product/programme**

When logged in as the admin user, the user has the option of 'product management' and 'programme management' when clicking on the profile icon on the main site header. After clicking the link they are directed to a page displayed with a form to enter all the information needed to add a new product/programme. Once the user has finished adding the product/programme details they can click 'add product'/'add programme' and will be redirected to the product/programme detail page for the new item.


<img src="readme/media/us-27.png">

**28. Edit/Update a product/programme**

When logged in as admin user, the user has an edit button displayed under each product/programme card on the products/programmes page, as well as on each product/programme detail page. After clicking 'edit' from either view the user is directed to the edit product/programme page which is a pre-filled out form allowing the fields to be amended manually from the site. Once the user has finished with their edits they can click 'update information' and the new product/programme information will be saved, and they will be redirected back to the product/programme detail page.

<img src="readme/media/us-28.png">

**29. Delete a product/programme**

When logged in as admin user, the user has a delete button displayed next to the edit button. After clicking 'delete' from either view, the product/programme is permanently deleted from the site and will no longer show on the products/programmes page or in the admin.

<img src="readme/media/us-29.png">

**30. Add a blog**

When logged into the admin, the admin user can add a new blog to the site. 
- I didn't think it was necessary to add a manual function for adding a blog as these will be posted less frequently and have a smaller chance of needing modifications after being posted.

**31. Links to FSCR social media platforms**

Social media platform links are featured in the page footer below the copyright statement.
- At present no social accounts exist for FSCR so all links direct the user to the homepage of the external site.

    <img src="readme/media/us-31.png">

## [&#8679;](#testing)
---

### **Manual function testing**

To ensure my site was working correctly I carried out manual function testing on all my apps;

#### General

- [x] Font styling changes as expected when hovering over my button elements
- [x] Opacity filter works as expected when hovering over icon elements
- [x] cursor pointer is present when hovering button and link elements 
- [x] User is directed to a custom 404 page if directed to a non-existent domain

    <img src="readme/media/404-page.png">

#### Navigation bar

- [x] The user can toggle the menu by clicking on the menu/close icon
- [x] The user can close the menu when open by clicking outside the menu area
- [x] If the user clicks a social icon on the footer the expected page opens on a new tab
- [x] The 'about' link on main dropdown menu directs the user to the about page
- [x] The 'meet the coaches' link on main dropdown menu directs the user to the meet the coaches page
- [x] The 'products' link on main dropdown menu directs the user to the products page displaying all products
- [x] The 'programmes' link on main dropdown menu directs the user to the programmes page displaying all programmes
- [x] If the user is not logged in, the 'blog' link on main dropdown menu directs the user to the register page
- [x] If the user is logged in, the 'blog' link on main dropdown menu directs the user to the blog page
- [x] If the user is not logged in, the 'forum' link on main dropdown menu directs the user to the register page
- [x] If the user is logged in, the 'forum' link on main dropdown menu directs the user to the forum page
- [x] If the user is not logged in, the 'blog' link on main dropdown menu directs the user to the register page
- [x] If the user clicks the 'contact' link they are directed to the contact form on the homepage
- [x] If the user is not logged in, the 'blog' link on main dropdown menu directs the user to the register page
- [x] The 'Join now' link is only visible on the main menu when a user is not logged in
- [x] Clicking the brand logo from any page on the site navigates the user back to the homepage
- [x] Search bar showing the correct format based on device size
- [x] After entering keywords and hitting enter or the search icon, user is directed to the search page template with appropriate results
- [x] If user enters a keyword with no results the correct message is displayed
- [x] If user submits a search with no keywords they are directed to the search page with no results and the appropriate error message
- [x] When not logged, under the profile icon user has the options of 'register' and 'login'
- [x] When logged in, under the profile icon user has the options of 'My Profile' and 'logout'
- [x] When logged in as admin, under the profile icon user has the added options of 'product management' and 'programme management'
- [x] All links displayed on the profile dropdown menu direct the user to the expected page
- [x] When the bag icon is clicked user is directed to the bag template
- [x] Before adding to bag, user is directed to the correct empty bag template
- [x] After adding to bag, user is directed to the bag template displaying the items they have added

#### Sort and Filter

- [x] The sort functionality returns items in the order expected. 
    - This was tested on the products, programmes, and blog page
- [x] The filter functionality returns only items matching the chosen criteria
    - This was tested on the products, programmes, and blog page
- [x] If user selects 'clear all' the filter is removed and all items are displayed
    - This was tested on the products, programmes, and blog page

#### Authorisation

- [x] On the register page, if the user clicks 'sign in' they are redirected to the login page
- [x] If the user completes the registration form with non-existent user details their registration is successful
- [x] After successful registration the user is navigated to the 'verification email sent' page and an email is sent to the user with link to confirm
- [x] After user clicks link in email they are redirected to 'verify your email' page 
- [x] After user clicking 'confirm' on verify your email' page they receive a success message and are redirected to the login page
- [x] If the user completes the registration form with an already registered username and password they receive an error message
- [x] On the login page, if the user clicks 'sign up' they are redirected to the register page
- [x] If the user completes the login form with an already registered username and password they are logged in successfully
- [x] If the user completes the login form with non-existent user details they receive an error message
- [x] If the user selects a social login option they are directed to the correct external platform for authorisation
- [x] If the user clicks 'forgot password' they are directed to the forgotten password page as expected
- [x] If the user enters their email and clicks 'reset my password' they are directed to the password reset page as expected
- [x] If the user enters their email and clicks 'reset my password' they receive an email with a link to reset their password
- [x] After user clicks the link in their email they are redirected to the 'change password' page
- [x] After submitting a new password the user is presented with a success message 'Your password is now changed' and they can login with their new password
- [x] If the user clicks 'Remember me' they are directed to the forgotten password page as expected
- [x] If a user is logged in, the logout option is visible in the profile icon menu
- [x] If a user clicks 'logout' they are directed to the logout page where they can confirm their action

#### Home
- [x] The callout carousel automatically cycles through a series of callout messages with expected interval time
- [x] The messages on the callout carousel are displayed appropriately dependent on whether a user is logged in or not
- [x] The links featured on the callout carousel direct the user to the expected page
- [x] The product and programme card links direct the user to the expected page.
- [x] The 'read me' link on the latest blogs direct the user to the correct post detail page
- [x] The testimonial carousel automatically cycles through a series of testimonials with expected interval time
- [x] The testimonial carousel pauses on hover and pointer is present
- [x] If user information entered in contact form is valid, the form submission is successful and an email is sent to the expected Gmail account
- [x] After submission the input fields are cleared
- [x] When input is missing in a required field there is an error response
- [x] When input format is incorrect the field validation errors are present
- [x] On the Meet the Coaches page, I checked the opacity filter was working 

#### Meet the coaches

- [x] The opaque CSS is working as expected on profile image tabs

#### Products

- [x] Each product card directs the user to the product detail page displaying the correct information
- [x] Clicking the increment and decrement on the quantity selector changes the value as expected
- [x] User can not decrement below 0 or increment above 99
- [x] User can not type in a value out of the range 1-99
- [x] Selecting a value from the size selector dropdown updates the field correctly
- [x] Product is added to the bag successfully after clicking 'add to bag'
- [x] If product is already in bag, quantity is incremented and product is not duplicated

<ins>Admin</ins>

When logged in as Admin user...
- [x] The product management option is available in the profile menu
- [x] After successfully adding a new product I am redirected to the product detail page with the correct information
- [x] When input is missing in a required field there is an error response
- [x] When input format is incorrect the field validation errors are present
- [x] If not image is added to the form submission, the expected 'no image' png file is present 
- [x] The edit button is visible on the products page and each product detail page
- [x] Clicking the edit button directs the user to the edit product page with fields prefilled with current information
- [x] After selecting an image the file name appears as expected
- [x] Selecting 'Remove' and saving changes removes current image as expected
- [x] After submitting the edit form user is redirected to the product detail page with updated the information
- [x] The delete button is visible on the products page and each product detail page
- [x] After clicking the 'delete' button the product is removed from the site and no longer visible in Django admin

#### Programmes

- [x] Each programme card directs the user to the programme detail page displaying the correct information
- [x] Clicking the increment and decrement on the quantity selector changes the value as expected
- [x] User can not decrement below 0 or increment above 99
- [x] User can not type in a value out of the range 1-99
- [x] Programme is added to the bag successfully after clicking 'add to bag'
- [x] If programme is already in bag, quantity is incremented and programme is not duplicated
- [x] The review carousel automatically cycles through a series of callout messages with expected interval time
- [x] The review carousel controls allow the user to scroll back and forth

<ins>Admin</ins>

When logged in as Admin user...
- [x] The programme management option is available in the profile menu
- [x] After successfully adding a new programme I am redirected to the programme detail page with the correct information
- [x] When input is missing in a required field there is an error response
- [x] When input format is incorrect the field validation errors are present
- [x] If not image is added to the form submission, the expected 'no image' png file is present 
- [x] The edit button is visible on the programmes page and each programme detail page
- [x] Clicking the edit button directs the user to the edit programme page with fields prefilled with current information
- [x] After selecting an image the file name appears as expected
- [x] Selecting 'Remove' and saving changes removes current image as expected
- [x] After submitting the edit form user is redirected to the programme detail page with the updated information
- [x] The delete button is visible on the programmes page and each programme detail page
- [x] After clicking the 'delete' button the programme is removed from the site and no longer visible in Django admin

#### Bag

- [x] After adding to bag all details are listed in the bag template as expected. 
    - To ensure the type of item added to the bag was correct I had to add category to my bag session to differentiate the products from programmes.
- [x] Clicking 'shop products' navigates the user back to the products page
- [x] Clicking 'shop programmes' navigates the user back to the programmes page
- [x] Clicking 'secure checkout' navigates the user to the checkout page as expected
- [x] By using the increment and decrement buttons, and clicking 'update' I can to amend the quantity of an item in the bag
- [x] I can enter a numeric value into the field to update the quantity
- [x] I am not able to enter a non-numeric value into the fields
- [x] I am not able to update quantity with value outside of range 0-99
- [x] I can remove the item from the bag by clicking 'remove'
- [x] I can remove the item from the bag by entering 0 into the quantity field and clicking 'update'
- [x] If amendments are made in the bag subtotal is updated accordingly

#### Checkout

- [x] The order summary contains the correct details of the items listed in the bag
- [x] If a site visitor the user input fields are all empty 
- [x] If a site member and details have been previously saved in 'my profile' the checkout fields are already prefilled
- [x] When input is missing in a required field there is an error response
- [x] When input format is incorrect the field validation errors are present
- [x] If user enters details and checks 'Save this delivery information to my profile', the information is saved to their profile after submission
- [x] If user enters details and doesn't check 'Save this delivery information to my profile', the information is not saved to their profile after submission
- [x] After entering details and clicking 'checkout' the loading page is present
- [x] The user is redirected to the checkout success page after completing order
- [x] The checkout success page contains all the correct personal details for the user and items purchased
- [x] After successful checkout the user receives an email with their order details
- [x] User is able to checkout successfully as both a site user (not logged in) and member (logged in)
- [x] The delivery amount is showing as 10% of the subtotal cost
- [x] If the order is over $40 the delivery amount is 0

#### Blog

- [x] The 'read me' link for each blog directs the user to the post detail page, displaying the correct information
- [x] The user can toggle references making text visible or hidden
- [x] If user enters a comment and clicks submit their comment is added successfully
- [x] The posted comment is displayed with the correct DateTime and logged in username
- [x] After submitting a comment the input field is cleared
- [x] The trash icon is only visible on comments the logged in user has posted 
- [x] After clicking the trash icon the comment is removed from the page as expected

#### Forum

- [x] Clicking on a 'topic' link directs the user to the thread detail page, displaying the correct information
- [x] If user enters a reply and clicks submit their reply is added successfully
- [x] The posted reply is displayed with the correct DateTime and logged in username
- [x] After submitting a reply the input field is cleared
- [x] The trash icon is only visible on replies the logged in user has posted 
- [x] After clicking the trash icon the reply is removed from the page as expected
- [x] The 'add thread' button directs the user to the add thread page as expected
- [x] After successfully adding a new thread I am redirected to the thread detail page with the correct information
- [x] When input is missing in a required field there is an error response
- [x] The edit button is only visible on threads the logged in user has posted
- [x] Clicking the edit button directs the user to the edit thread page with fields prefilled with current information
- [x] After submitting the edit form user is redirected to the thread detail page with updated the information

#### Profile

- [x] The welcome message is personalised with the correct username for the logged in user
- [x] The user's order history is listed with previous purchases
- [x] The order history is listed in date descending order with most recent showing first
- [x] After clicking 'View order details' the user is directed to the checkout success page showing all details of their order
- [x] On the checkout success page, clicking 'back to profile' navigates the user back to their profile
- [x] If user enters details and clicks 'update information' their details are saved to their profile
- [x] If user edits their details and clicks 'update information' their details are updated on their profile
- [x] No fields on user profile are required allowing user to only fill in desired fields
- [x] If user updates their information in their profile this is reflected on the checkout page


## [&#8679;](#testing)
---

### **Automated testing**

I also decided to use Django's testing framework to create some automated tests for my project.

#### **Unit Testing**

I added a tests.py file to each of my apps containing my written unit tests.

As my automated testing was only small for this project I kept the tests all in the same file within each app, however for larger project testing, I would create a 'tests' folder and group tests by what i'm testing e.g. test_models.py, test_views.py, test_forms.py etc.

To run all the tests I used the following command;

`$ python3 manage.py test`

To run tests in a specific app I used the following command;

`python3 manage.py test <app_name>.tests`

The results from each test were displayed in the terminal, letting me know if the tests were successful or had failed.

#### **Coverage**

I used **Coverage** to identify the percentage of code the tests had covered and to determine which areas to focus on. Due to time constraints, I aimed to reach a minimum of 50% coverage for models, forms and views, across all my apps. However, I will continue to add tests to get as close to 100% as I can. 

<p>
<details>
<summary>Coverage Summary</summary>
<p>
<img src="readme/media/coverage.png">
</details>

<p>
<details>
<summary>Setting up Coverage</summary>
<p>
To set up and use Coverage, I used the following commands;

* To Install:

    `$ pip3 install coverage`

* Freeze .coverage to requirements file:

    `$ pip3 freeze > requirements.txt`

* To run all the tests written in a certain app and generate a report (second command is to view the report in the terminal).

    `$ coverage run --source=<'app name'> manage.py test`

    ` $ coverage report`

* I used the following command to create an interactive HTML report to see more specifically what I was missing. This created a 'htmlcov' folder containing a index.html file.

    `$ coverage html`

* To open the file in my browser and see an interactive version of the report I used the below command;
    
    `$ python3 -m http.server`

</details>

## [&#8679;](#testing)
---

### **Validator checks**

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. The code was entered through direct input. 

- [**HTML Validator**](https://validator.w3.org/)

    No error or warning messages were received.

    - To get the most accurate read of my HTML for validation, I ran my app and extracted my code from the 'View page source'.


- [**CSS Validator**](https://jigsaw.w3.org/css-validator/)

    No error or warning messages were received.


[**JS hint**](https://jshint.com/) was used to check for any errors with my Javascript files. 
JS was also tested by opening the developer console window on Chrome and checking for any errors as I clicked through the site.

- Warnings received;

    `let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).`
    `'template literal syntax' is only available in ES6 (use 'esversion: 6').`

    Warnings occurred as JShint is using ECMAScript 5.1 specification and my code uses ECMAScript 6 specific syntax. However, all code is valid.

- Undefined variable;

    `$`

    `emailjs`

    `stripe`

    $ (Jquery), emailjs and stripe are all defined in base.html.

    - Unused variable;

    `sendMail`

    sendMail used in index.html for emailJS

[**PEP8 online checking tool**](http://pep8online.com/checkresult) was used to inspect my Python code against the style conventions in PEP 8.

[**Flake8**](http://pep8online.com/checkresult) was a python code linting tool also used to help verify pep8, pyflakes and circular complexity. By using the following command I was able to check the problems across all my files without having to open each individual file.

`$ python3 - m flake8`

<ins>PEP8 Issues:</ins>
- I chose to ignore any warnings on migration files since these are automatically generated files so may ignore style rules for efficiency reasons. Also as developers, we usually don't need to touch them so they don't need to be perfectly readable.

- `DJ01 Avoid using null=True on string-based fields`

    As referenced on [stackoverflow](https://stackoverflow.com/questions/59836736/django-why-only-string-based-field-cant-have-null-true), Django allows the use of NULL in string-based fields but it is suggested to avoid it and use '' to represent the empty value. As in most cases both values (NULL and '') represent the same thing for string-based fields I have chosen to disregard this warning. 

- `E501 line too long`

    This error has been fixed on the majority of my code but some lines have been left to avoid breaking up variables.

    `F401 'checkout.signals' imported but unused`
    `F841 local variable 'e' is assigned to but never used`

## [&#8679;](#testing)
---

### **Audits**

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to run a series of audits to improve the quality of web pages. Overall performance and errors are highlighted below.

<img src="readme/media/lighthouse-review.png">

<p>
<details>
<summary>More specific details</summary>
<p>

<ins>Performance</ins>

The low-performance review was mainly driven by the following metrics:

`Serve images in next-gen formats`;

I tried converting my images to JPEG 2000 as suggested, however, the images were not loading due to their limitations of only working on certain browsers. Therefore I kept my images in a PNG and JPG format.

`Properly size images`;

As images are uploaded through the image URL form input I am not able to take any action on adjusting image sizes.

<ins>Accessibility</ins>

`Background and foreground colors do not have a sufficient contrast ratio`

I didn't take any actions as none of my users experienced difficulty reading the text in question. 

<ins>SEO</ins>

`Links do not have descriptive text`

I didn't take any actions as the error was for displaying 'read more' which I believe is a conventional text link for users. This is also very similar to the suggested generic link text 'learn more'.

</details>

## [&#8679;](#testing)
---

### **Responsive Design**

- Site created as a mobile-first design.

- Responsive layout achieved through utilising the Bootstrap grid system and applying my own media queries.

- Viewport tag included in the head of HTML files to tell the browser how to respond to different resolutions, particularly mobile ones.

## [&#8679;](#testing)
---

### **Additional Testing**

- The Website was tested on Google Chrome, Safari browsers, Firefox, and Microsoft Edge.

- The website was viewed on a variety of devices including HP Laptop, Macbook pro, Ipad, IPhones (Version SE, 6, 7, 8, 11, 12, 12 max pro), Huawei P20 pro.

- Friends and family members were asked to review the site to point out any bugs, user experience issues, and/or suggestions.

  > **NB:** All appropriate suggestions have been added to my future plans.

    Feedback action:
    - Ability to pay using apple pay
    - More search queries so I can search forum topics
    - Add a number count onto the bag icon so I can easily see how many items are in my bag
    - Ability to autofill address by entering postcode 
- Project posted on Slack, asking for feedback from fellow students.

## [&#8679;](#testing)
---

### **Bugs**

|     | Bug                                                                           | Action                                                            |
|-----|-------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [] | Homepage vh including address bar on mobile so cropping bottom of element                   |  I found a solution on [css-tricks](https://css-tricks.com/the-trick-to-viewport-units-on-mobile/) but as this updates the value of --vh, it will trigger a repaint of the page, and the user may experience a jump as a result. As this is only a layout issue on IOS and doesn't hinder UX I decided not to implement this solution. |
| [x] | Item is removed from order history if deleted by admin                   |  This bug was fixed by following [this thread](https://app.slack.com/client/T0L30B202/CGWQJQKC5/thread/C7HS3U3AP-1597961336.047800) found on slack. I added a discontinued field to my models (with default False), updated delete view to change discontinued to true instead of physically deleting item and then referenced to this field in my templates  |
| [x] | Comment reposts on page refresh                   |  Redirect path added to views after post request  |
| [x] | User able to type in any quantity value for item when in shopping bag                  |  Changed 'quantity > 0' to 'quantity in range(1, 99)' and added elif statement for any value over 99 to send an error message to the user   |
| [x] | Success toast showing shopping bag when not appropriate                  |  Added a variable called on_page to the product and programme detail page and used this as a filter within my success toast template. This ensures that the bag view is only displayed on the success message when a user is on these specific pages.     |
| [x] | Plural suffix returned when value is 1                   |  I added 'pluralize' tag to my count filters to ensure text was presented with correct spelling |
| [x] | If filter by category then sort items, filter is removed                   |  Changed sort from dropdown to selector with options, added my own custom styling. Styling involved replacing the custom arrow and adding my own text with absolute positioning. I also replaced the default dropdown arrow by removing the 'dropdown-toggle' class so that the arrow style matched. |
| [x] | Unable to migrate changes, error meesage received `psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type integer: "test"`               | This happened a couple of times and was solved by resetting my migrations using this [link](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html) recommended by a tutor     |
| [x] | Unable to make migrate even after resetting migrations              | My old database was corrupted so this was solved by resetting my Heroku database as advised by a tutor. I logged into Heroku, selected app, navigated to Resources, selected Heroku PostGres, then in new window clicked Settings then Reset Database.     |
