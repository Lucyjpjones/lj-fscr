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

**products**

<u>View product functionality</u>

<u>Add product functionality</u>

<u>Edit product functionality</u>

<u>Delete product functionality</u>


**programmes**

<u>View prgramme functionality</u>

<u>Add programme functionality</u>

<u>Edit programme functionality</u>

<u>Delete programme functionality</u>

**bag**

<u>Add to bag functionality</u>

<u>View bag functionality</u>

**checkout**

**blog**

<u>Commenting on blog</u>

**forum**

<u>Adding Thread</u>

<u>Commenting on forum</u>

#### Automated testing

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