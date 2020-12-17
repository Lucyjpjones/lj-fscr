<div align="center">
  <img src="static/assets/images/readme/responsive-fscr.png">
  <img src="static/assets/images/readme/title.png">
<hr>

**FSCR (Football Strength Conditioning Rehab) focuses on providing structured and detailed fitness programmes for football related injuries.**

This app was built using [GitHub](https://pages.github.com/) and deployed to [Heroku](https://www.heroku.com/).

[View Site](https://lj-fscr.herokuapp.com/)

</div>

---

## <u>Table of contents</u>

**<details><summary> User Experience (UX)</summary>**
  - [Purpose](#purpose)
  - [Design](#design)
  - [User stories](#user-stories)
  - [Wireframes](#wireframes)
</details>

**<details><summary> Features</summary>**
  - [Features used](#features-used)
  - [To do list](#to-do-list)
  - [Status](#status)
</details>

**<details><summary> Technologies</summary>**
  - [Languages](#languages)
  - [Frameworks, Libraries & Programs](#frameworks-libraries-programs)
</details>

**<details><summary> Deployment</summary>**
  - [Deploy to Heroku](#deploy-to-heroku)
  - [Accessing code](#accessing-code)
</details>

**<details><summary> Testing</summary>**
  - [Testing Documentation](https://github.com/Lucyjpjones/wean-cuisine/blob/master/testing.md)
</details>

**<details><summary> Credits</summary>**
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)
</details>

**<details><summary> Contact</summary>**
  - [Contact details](#contact-details) 
</details>
---

# &rarr; **User Experience (UX)**

### **<u>Purpose</u>**

**FSCR** (Football Strength Conditioning Rehab) focuses on providing structured and detailed fitness programmes for football-related injuries. This is a full-stack site that has been created around business logic and used to control a centrally-owned dataset.

This application was built for a client who is currently looking to utilise their expertise in football rehabilitation by creating easy-to-follow fitness programmes. Rehabilitation after an injury can often be overlooked and my client is extremely passionate about ensuring athletes get the full recovery they need to get back to their sport and prevent further injury.

By completing this project I will have shown greater experience in HTML, CSS, and Javascript, and demonstrated my understanding of Python+Django. I will have also shown my competency in using a relational database, setting up an authentication mechanism, and providing payment transactions using stripe payments. 


### **<u>Design</u>**

**Structure**

**Colour scheme**

<img src="media/palette.png">

**Typography**

**Research**

- I spent some time researching other fitness and retail sites to gain inspiration and created a mood board with a collection of elements that caught my eye.


  <img src="media/moodboard.png">

**Logo Design**

When it comes to creating a business, the logo is the central visual element in helping customers find, recognise and remember a brand. Taking this into consideration, I decided to spend some time creating a logo for FSCR which would represent the brand well.

I set up a meeting with my client and presented them with a moodboard of different designs and gathered their feedback.

  <img src="media/logo-designs.png">

My final design with client approval below;

<img src="media/final-logo.png">


### **<u>User Stories</u>**

<img src="lj_fscr/media/flowchart.png">

<u>**User profiles**</u>

**User profile: Site Visitor**

**User profile: Site Member**

**User profile: Site Owner**

<u>**User stories**</u>

**User stories: Site Visitor**

**User stories: Site Member**

**User stories: Site Owner**

### **<u>Wireframes</u>**

As part of the design process, I created wireframes using [Balsamiq](https://balsamiq.com/?gclid=Cj0KCQjw28T8BRDbARIsAEOMBczzBYzsoMjbTtqNXQaE1EgOWA2u_Qux7sLl2IUHe-p0lDC-294BfVgaAr-oEALw_wcB). Creating these mock-ups helped me plan the basic structure and arrangement of the features for my site.

- [Homepage](wireframes/wf-homepage.pdf)
- [Meet the Coaches](wireframes/wf-meet-the-coaches.pdf)
- [Profile](wireframes/wf-profile.pdf)
- [Products](wireframes/wf-products.pdf)
- [Product View](wireframes/wf-product-view.pdf)
- [Programmes](wireframes/wf-programmes.pdf)
- [Programme View](wireframes/wf-programme-view.pdf)
- [Shopping bag](wireframes/wf-bag.pdf)
- [Checkout](wireframes/wf-checkout.pdf)
- [Blog](wireframes/wf-blog.pdf)
- [Blog View](wireframes/wf-blog-view.pdf)
- [Forum](wireframes/wf-forum.pdf)
- [Forum View](wireframes/wf-forum-view.pdf)
---

## &rarr; **Features**

### **Features used**

- **Responsive on all device sizes**
  - Mobile-first design, responsive on all devices through using the Bootstrap grid system and CSS media queries.

- **A user-friendly interface with easy navigation throughout the site**
  - Attractive, minimalistic design with visuals and information presented clearly and concisely.

  - Easily readable fonts and simple navigation throughout the site.
    - Fixed navigation bar visible on every page including a menu dropdown, recognisable icons and brand logo to link back to the homepage.

  - An aesthetically pleasing 404 page if the user is directed to a non-existent page.

- **Buttons**
    - Clear interactive buttons used for a effortless user journey.

- **Forms**
  - Forms used for contact form, login and register, adding/editing products and programmes, adding forum threads,user comments, and checkout details.

  - Crispy forms used for elegant formatting.

- **Tabs**
  - Interactive tab used on 'meet the coaches' page used to switch between individuals details.

- **Card Listings**
  - Used to display products, programmes, and blogs.

  - Image included contributing to the visual look.

- **Carousel**
  - Used for testimonials and products displayed on the homepage.

- **Search bar**
  - Allows the user to search the site by keywords.

- **Sort**
  - Allows the user to sort.

- **Filter**
  - Allows the user to filter.

- **Toasts**
  - Used for success and error responses to add to the user journey.

- **Payments**




### **To do list**

#### Status

**Future Development plans**

---

## &rarr; **Technologies**

#### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

#### Frameworks, Libraries & Programs

- [**Django**](#)

- [**AWS**](#)

- [**Stripe**](#)

- [**Temp Mail**](https://temp-mail.org/en/)

- [**Google fonts**](https://fonts.google.com/)

  - Google fonts were used to import the fonts into the CSS file which is used on all pages throughout the project.

- [**Font Awesome 4.7.0**](https://fontawesome.com/)

  - Font Awesome was used to add icons for aesthetic and UX purposes.

- [**jQuery:**](https://jquery.com/)

  - jQuery came with Materialize to make the components used responsive.
  - Included at end of body tag within HTML file to ensure a smooth running of HMTL and CSS.

- [**Git**](https://git-scm.com/)

  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.

- [**GitHub**](https://github.com/)

  - GitHub is used to store the project code after being pushed from Git.

- [**Heroku**](https://github.com/)

  - Heroku is the app platform I deployed my project to.

- [**Flaticon**](https://www.flaticon.com/)

  - Provided icons throughout site.

- [**Balsamiq**](https://balsamiq.com/)

  - Balsamiq was used to create the wireframes during the design process.

- [**Grammarly**](https://www.grammarly.com/)

  - Grammarly was used to ensure any grammar errors are eliminated.

- [**HTML Formatter**](https://www.freeformatter.com/html-formatter.html) and [**CSS Formatter**](https://www.freeformatter.com/css-beautifier.html)

  - Used to format my HTML and CSS file with the desired indentation level for optimal readability.

- [**Tables Generator**](https://www.tablesgenerator.com/markdown_tables)

  - Used to create tables in my readme file.

- [**Favicon**](https://favicon.io/)
    - Used to create a favicon, displaying my logo on a web browser next to the web address bar, the browser tab, and the bookmarks bar.
---

## &rarr; **Deployment**

#### Deploy to Heroku


#### Accessing code

---

## &rarr; **Credits**

#### Content

- Code used to help create blog and forum app [here](https://djangocentral.com/building-a-blog-application-with-django/)

- Code used to help create sidenav [here](https://bootstrapious.com/p/bootstrap-sidebar)

- Code used to help with [linking to id on a page using Django](https://stackoverflow.com/questions/31643670/link-a-div-in-another-page-in-url-with-an-anchor-tag-django)

- Site used to remove background from logo [here](https://www.remove.bg/upload)

- Site used to change colour of image for logo design [here](https://pinetools.com/colorize-image)


- [Stack overflow](https://stackoverflow.com/):
  - [Help with setting the size of the column width in bootstrap](https://stackoverflow.com/questions/25385289/how-to-set-the-size-of-a-column-in-a-bootstrap-responsive-table/25385798).
  - [Help with removing labels from crispy forms](https://stackoverflow.com/questions/11472495/remove-labels-in-a-django-crispy-forms).
  - [Help with reducing the inbox size in crispy forms](https://stackoverflow.com/questions/38684753/django-reducing-the-size-of-input-box-in-crispy-forms).
  - [Using slugify for detailed urls](https://stackoverflow.com/questions/45847278/django-use-slugify-for-detail-url).


#### Media

#### Acknowledgments

- My Mentor, Aaron for his continuous help and support throughout the project.

- The help and support received from the tutors at [Code Institute](https://codeinstitute.net/).

- The [Code Institute](https://codeinstitute.net/) Slack Community.

- Friends & Family for continuous feedback and support.

## &rarr; **Contact**

#### Contact details

Created by @lucyjpjones

If you have any problems, questions or, suggestions for my project please contact me on the email below:

```
lucyjpjones@gmail.com
```

Thanks for visiting.

&copy;
LucyJPJones