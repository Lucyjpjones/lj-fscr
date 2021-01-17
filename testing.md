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

### **Testing user stories**

#### <ins>Viewing and Navigation</ins>

**1. Discover FSCR’s purpose and goals**

I created an 'about' and 'meet the coaches' page so any site visitor can learn about the brand and the coaches behind it. Both pages are easily accessible via the main nav menu.

<img src="media/us-1.png">

**2. View a list of products**

I created a 'products' page including a list of all products, displaying product image, name, price, and rating, with the option to select an individual card for more details.

<img src="media/us-2.png">

**3. View a list of programmes**

I created a 'programmes' page including a list of all programmes, displaying product image, name,price, and rating, with the option to select an individual card for more details.

<img src="media/us-3.png">

**4. View a specific category of products or programmes**

I added a filter option to both the products and programmes page giving users the ability to quickly find what they are searching for. 
`(More specific details on this in user story 17)`

**5. View individual product details**

Each individual product page displays the products description, price, available sizes, product image and rating. There is also the ability to add to bag or redirect back to the products page.

<img src="media/us-4.png">

**6. View individual programme details**

Each individual programme page displays the programmes description, price, available sizes, programme image and rating. There is also the ability to add to bag or redirect back to the programmes page.

<img src="media/us-5.png">

**7. Easily access contact details**

I have included a contact form on the home page which is also easily navigated to via the main nav menu. This has been set up using EmailJS with my own customised email template to assist with organisation of user enquiries.

<img src="media/us-6.png">

**8. See reviews and ratings on products and programmes**

Testimonials are visible on the homepage and reviews are available on the programmes detail page. Users are also able to see the rating for each individual product/programme under each item on the products/programmes page and additionally on the product/programme details page.

> **NB:** As this is a startup which hasn't yet started business the testimonials, reviews and ratings are currently only mockups.

<img src="media/us-7.png">

**9. Browse associated blogs, articles and recent new stories**

I created a blog app that can only be viewed by site members. The page is available through the nav menu and there is also the option for the user to direct to the latest blogs via the homepage. When a user is not logged in and they click on the blog they will be directed to the login/register page. If a user is a member and logged in they will be directed to the blog page where they can view blogs posted by the admin user. Members also have the ability to add and delete their own comments on blog posts creating further user interaction.

<img src="media/us-8.png">

**10. Access a member forum**

I created a forum app that can only be accessed by site members. When a user is not logged in and they click on the forum they will be directed to the login/register page. If a user is a member and logged in they will be directed to the forum page where they will have the option to view threads by other users and add their own. They also have the capability of replying to any thread which displays both their logged in username and date/time posted.

<img src="media/us-9.png">

#### <ins>Registration and user accounts</ins>

**10. Easily register for an account**

A fully functioning register page where a user is able to enter their details to create an account. The user can access this page by clicking on the recognisable user icon and selecting 'register'.

<img src="media/us-10.png">

**11. Receive an email confirmation after registering**

After registering the user is directed to a registration success page where they are informed that they will receive an email to validate their email address and complete registration.

<img src="media/us-11.png">

**12. Easily login or logout**

When a user is registered they have the ability to easily log into their account. The user can click on the profile icon, then select log in and enter their details to sign into their account. Once logged in the user will be able to log out via the profile icon.

I also decided to add social logins to allow my user to log in more quickly. The user can choose their preferred platform (Facebook, Google or Twitter) and follow the authorisation for the specified site. (Facebook screenshots included below).

<img src="media/us-12.png">

**13. Easily update my personal details**

Each registered user has their own profile page where they can store their personal details including name, email and delivery details. This information can be easily updated by filling in any field and then clicking 'update details'.

<img src="media/us-13.png">

**14. Easily recover my password in case I forget it**

If a user forgets their password they have the option to click the 'forgot password' link. This will direct them to another page which will inform the user that an email has been sent to them to recover their password.

<img src="media/us-14.png">

**15. Have a personalised user profile**

The profile page is specific to each user with a personalised username greeting,the option to save their own entered details and a log of their order history.

<img src="media/us-15.png">

**16. Enable my details to be prefilled**

If the user has filled in their profile information, these details will be prefilled at checkout. The user also has the option to tick the save details options on checkout which will automatically save details to their profile page.

<img src="media/us-16.png">

#### <ins>Sorting and Searching</ins>

**17. Sort and filter the list of available products and programmes**

I have added a sort and filter option to the products and programmes page to allow a user to easily find what they are looking for. I also decided to add this function to the blog page as I think it will be useful to the user as more blogs get posted over time.

The pages also feature a count functionality showing the user how many items are being displayed on the page. For example if the user filtered the products page by accessories they would see all the accessories and the number of products found. If no products are found the user would be displayed with the message "Sorry no search results found".

<img src="media/us-17.png">

**18. Search the site by keywords**

A search bar features in the main site header. Users can search by keywords on the product and programme page to filter by specific items.

<img src="media/us-18.png">

**19. Easily see what I’ve searched for and the number of results**

The products, programmes and blog page all feature a results count to show the user how many items are available to them. (View user story 17 and 18 for screenshots)


#### <ins>Purchasing and checkout</ins>

**20. Easily select the size and quantity of a product/programme when purchasing it**

The product detail page allows a user to select a specific size, if the product is sized, and the quantity of a product.
The programme detail page allows a user to select a quantity of a programme to add to their bag.

<img src="media/us-20.png">

**21. View items in my bag to be purchased**

The bag view allows the user to view all the products and programmes they have added to their bag before continuing to the checkout.

<img src="media/us-21.png">

**22. Adjust the quantity of individual items in my bag**

The user has the ability to adjust the quantity of products and programmes in their bag before continuing to checkout.

<img src="media/us-22.png">

**23. Easily enter my payment information and feel my personal and payment information is safe and secure**

The checkout page features a payment form allowing the user to easily enter their card details for a quick checkout.

<img src="media/us-23.png">

**25. View an order confirmation after checkout**

Once the user has made a purchase they are directed to a checkout success page where they can see a summary of their order so they are able to check that they haven't made any mistakes.

<img src="media/us-25.png">

**26. Receive an email confirmation after checking out**

Once the user has made a purchase they are sent an email with a summary of their order to keep for their own records.

<img src="media/us-26.png">

#### <ins>>Admin and Store Management</ins>

**27. Add a product/programme**

When logged in as the admin user, the user has the option of 'product management' and 'programme management' when clicking on the profile icon on the main site header. After clicking the link they are directed to a page displayed with a form to enter all the information needed to add a new product/programme.

<img src="media/us-27.png">

**28. Edit/Update a product/programme**

When logged in as admin user, the user has an edit button displayed under each product/programme card on the products/programmes page, as well as on each product/programme detail page. After clicking 'edit' from either view the user is directed to the edit product/programme page which is a pre-filled out form allowing the fields to be ammended manually from the site. Once the user has finished with their edits they can click 'update information' and the new product/programme information will be saved, and they will be redirected back to the products/programmes page.

<img src="media/us-28.png">

**29. Delete a product/programme**

When logged in as admin user, the user has a delete button displayed next to the edit button. After clicking 'delete' from either view, the product/programme is permanently deleted from the site and will no longer show on the products/programmes page.

(See user story above displaying the delete button)

**30. Add a blog**

When logged into the admin, the admin user can add a new blog to the site. I didn't think it was nessessary to add a manual function for adding a blog as these will be posted less frequently and have little chance of needing modifications after being posted.

### **Manual function testing**

To ensure my site was working correctly I carried out some manual function testing;

#### General

- I hovered over my `button elements` to ensure the font styling changed as expected.

- I hovered over the `icon elements` to ensure the opacity filter was working as expected.

- I hovered over my button and link elements to check the `cursor pointer` was showing as expected.

- I created a custom `404 page` for my user so if they are directed to a non-existent domain, they are presented with an appealing page and an easy navigation button back to the homepage.

    <img src="media/404-page.png">

#### Navigation bar
    
  - I tested the links on the site `dropdown menu` by clicking on each one and checking I was directed to the right page template.
  - I clicked on the `brand logo` from every page to confirm it correctly navigated back to the homepage.
  - I individually tested every icon on the navbar to check they were working as expected;
    - `Search icon:`
        - I checked that the search bar was showing the correct format based on the device size by testing on both mobile and larger devices. 
        - I entered keywords into the search bar and clicked enter/search icon to ensure I was correctly directed to the search page template with logical results.
    - `Profile icon:`
        - When not logged in I made sure that the profile icon displayed the options 'register' and 'login'.
        - When logged in I made sure that the profile icon displayed the options 'My profile' and 'logout'.
        - When logged in as admin I made sure that I had the added options of 'product management' and 'programme management' available to me.
        - All links displayed on the profile dropdown menu were clicked to ensure they lead to the correct page.
    - `Bag icon:`
        - I checked the bag icon link was working correctly by clicking on the icon and making sure I was directed to the bag template.
        - Before adding anything to the bag I checked that the page displayed the correct html for an empty bag.
        - I added products/programmes to the bag and then directed to the bag page to check the template displayed the items I had added.

#### Sort and Filter

- To check the `sort functionality` was working I selected each option from the dropdown to make sure the items were displayed in the expected order. The was tested on the products, programmes and blog page.
- To check the `filter functionality` was working I selected each option to make sure only items that matched the chosen critera were displayed. The was tested on the products, programmes and blog page.

#### Authorisation

  - To check the `login functionality` was working I first clicked on the profile icon and clicked 'login' to ensure I was directed to the correct page. When presented with the login template I conducted various checks;
    - I filled out the login form with an already registered username and password then clicked 'Login'.
    - I filled out the login form with a new username and password then clicked 'Login'.
    - I tested the social account logins by clicking on each specific link to confirm I was directed to the correct external platform for authorisation.

- To check the `Register functionality` was working I first clicked on the profile icon and clicked 'Register' to ensure I was directed to the correct page. When presented with the register template I conducted various checks;
  - I filled out the registration form with a new username and password then clicked 'Register'.
  - I filled out the login form with an already registered username and password then clicked 'Register'.

#### Home
- I tested the `callout carousel` by making sure it automatically cycled through a series of callout messages. I also tested the links featured to ensure I was directed to the expected page.
- I clicked on the `product and programme card links` to ensure I was directed the correct pages.
- I clicked on the `latest blog` 'read more' buttons to ensure I was directed to the correct post detail template.
- I tested the `testimonial carousel` by making sure it automatically cycled through a series of testimonials.
- I checked the `contact form` was working correctly by filling out the form and clicking submit. As expected I received a browser 'SUCCESS' response, the form cleared and I recieved an email, so I knew the functionality was working.
- On the Meet the Coaches page, I checked the opacity filter was working correctly by clicking on the `profile image tabs` and ensuring the opaque effect was only adopted on the inactive tab.

#### Products

- I clicked on each product card to make sure I was directed to the product detail page displaying the correct information.
- I tested the `quantity selector` was working correctly by clicking the increment and decrement, and checking the values updated as expected.
- I tested the `size selector` was working correctly by selecting a value from the dropdown and checking the field updated correctly.
- I checked that products were adding to the bag correctly by clicking 'add to bag', and navigating to the bag to check it match what i'd added.

<ins>Admin</ins>

- I logged in as admin user to check that the product management option was displayed in the profile menu, and it was. I then filled out the form and submitted and checked that the product was added to the products page.

- When logged in as admin user I checked that the edit button was visible for all products on the programmes page, as well as on each individual view page. I then tested the functionality but clicking on the button and checking that i was directed to the edit page with all fields pre-filled with current information. I then made an amendment and clicked 'save changes' and checke that the information had been updated.

- I checked the delete function buttons were all visible when logged in as admin and that when clicked the product was removed from the site.

#### Programmes

- I clicked on each programme card to make sure I was directed to the programme detail page displaying the correct information.
- I tested the `quantity selector` was working correctly by clicking the increment and decrement, and checking the values updated as expected.
- I checked that programmes were adding to the bag correctly by clicking 'add to bag', and navigating to the bag to check it match what i'd added.

<ins>Admin</ins>

- I logged in as admin user to check that the programme management option was displayed in the profile menu, and it was. I then filled out the form and submitted and checked that the programme was added to the programmes page.

- When logged in as admin user I checked that the edit button was visible for all programmes on the programmes page, as well as on each individual view page. I then tested the functionality but clicking on the button and checking that i was directed to the edit page with all fields pre-filled with current information. I then made an amendment and clicked 'save changes' and checke that the information had been updated.

- I checked the delete function buttons were all visible when logged in as admin and that when clicked the programme was removed from the site.

#### Bag

- I tested the 'add to bag' functionality by adding a range of products and programmes to the bag and checking all details were listed in the bag template as expected. 
    - To ensure the type of item added to the bag was correct I had to add category to my bag session to differentiate the products from programmes.

- I clicked on the 'shop products' button to confirm I was navigated to the products page as expected.

- I clicked on the 'shop programmes' button to confirm I was navigated to the programmes page as expected.

- I clicked on the 'checkout' button to confirm I was navigated to the checkout page as expected.

- I tested I was able to `update the quanity` by clicking the increment and decrement, and clicking update. I also entered numeric values into the field to check this also worked. 

- I tested I was able to `delete the product` by clicking 'remove' and confirming the product was no longer displayed in the bag. I also checked I was able to delete the product by entering 0 into the quantity field, and clicking update.


#### Checkout

<u>Completing stripe payment</u>

<u>Pre-filled checkout details</u>

#### Blog

- I clicked on the 'read me' button link for each blog to make sure I was directed to the post detail page, displaying the correct information.

- I clicked the `references collapse button` to test that the text became visible as expected. I then clicked it again to make sure the text became hidden.

- I entered a comment into the text field and clicked 'post' to check that my post was added successfully. I checked that the datetime field displayed correctly and logged in as various users to check the username appeared as expected.

- To check I was only able to delete my own comments, I logged in as various users and made sure the trash icon was only visible on own comments. I then tested the delete functionality by clicking on the icon and making sure the comment was deleted as expected.

**Forum**

- I clicked on the 'topic' for each thread within the forum to make sure I was directed to the thread detail page, displaying the correct information.

- I entered a reply into the text field and clicked 'reply' to check that my post was added successfully. I checked that the datetime field displayed correctly and logged in as various users to check the username appeared as expected.

- To check I was only able to delete my own replies, I logged in as various users and made sure the trash icon was only visible on own replies. I then tested the delete functionality by clicking on the icon and making sure the comment was deleted as expected.

- I checked the `'add a thread'` functionality was working by clicking 'add thread' on the forums page and making sure I was directed to the 'add thread template'. After filling in the details and clicking 'post' I could see that my thread had been added to the forum page so I knew it was working correctly. I also checked that my username and date was displayed correctly below the thread.

- To check I was only able to edit my own thread posts, I logged in as various users, navigated to the thread detail page, and made sure the edit icon was only visible as expected. I then tested the edit functionality by clicking on the icon and making sure I was redirected to the edit thread page with fields already prefilled with current information. I then amended the content and clicked 'edit' and checked the information had been updated on the thread.

#### Profile




### **Automated testing**

I also decided to use Django's testing framework to create some automated tests for my project.

#### **Unit Testing**

I added a tests.py file to each of my apps containing my written unit tests.

To run all the tests I used the following command;

`$ python3 manage.py test`

To run tests in a specific app I used the following command;

`python3 manage.py test <app name>`

The results from each test were displayed in the terminal, letting me know if the tests were successful or had failed.

#### **Coverage**

I used **Coverage** to identify the percentage of code the tests had covered and to determine which areas to focus on. Due to time constraints my aim was to reach a minimum of 50% coverage on all my apps. However I will continue to add tests to get as close to 100% as I can. 

To set up and use Coverage, I used the following commands;

* To Install:

    `$ pip3 install coverage`

* To run all the tests written in a certain app and generate a report (second command is to view this report in the terminal).

    `$ coverage run --source=<'app name'> manage.py test`

    ` $ coverage report`

* I used the following command to create an interactive HTML report to see more specifically what I was missing. This created a 'htmlcov' folder containing a index.html file.

    `$ command html`

* To open the file in my browser and see an interactive version of the report I used the below command;
    
    `$ python3 - m http.server`


### **Validator checks**

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. The code was entered through direct input. JS hint was used to check for any errors with my Javascript files. 
JS was also tested by opening the developer console window on Chrome and checking for any errors as I clicked through the site.
I used the PEP8 online checking tool to inspect my Python code against the style conventions in PEP 8.

- [**HTML Validator**](https://validator.w3.org/)


- [**CSS Validator**](https://jigsaw.w3.org/css-validator/)


- [**JS hint**](https://jshint.com/)


- **Developer tools**


- [**PEP8 online check**](http://pep8online.com/checkresult)


### **Audits**

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to run a series of audits to improve the quality of web pages. Overall performance and errors are highlighted below.

### **Responsive Design**

- Site created as a mobile-first design.

- Responsive layout achieved through utilising the Boostrap grid system and applying my own media queries.

- Viewport tag included in the head of HTML files to tell the browser how to respond to different resolutions, particularly mobile ones.

### **Additional Testing**

### **Bugs**

|     | Bug                                                                           | Action                                                            |
|-----|-------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [] | Homepage vh including address bar on mobile so cropping bottom of element                   |  need to solve |
