$(document).ready(function () { 



    /* If sidebar active
    if ( $("#sidebar").hasClass('active') ) {
        $(document).on("click", function(event) {
            if (!$(event.target).closest("#sidebar").length) {
                $("#sidebar").toggleClass("active");
                $(".overlay").toggleClass("enabled");
                $("#navbar-bars").toggleClass("d-none");
                $("#navbar-close").toggleClass("d-none");
            }
        });
    }
    */

    /* Sidebar Toggle */
    $("#sidebarCollapse").on("click", function () {
        $("#sidebar").toggleClass("active");
        $(".overlay").toggleClass("enabled");
        /* Menu icon change (toggle) - Code taken from 'https://stackoverflow.com/questions/28247310/bootstrap-mobile-menu-icon-change-to-x-close' */
        $("#navbar-bars").toggleClass("d-none");
        $("#navbar-close").toggleClass("d-none");
    });

    // First we get the viewport height and we multiple it by 1% to get a value for a vh unit
    let vh = window.innerHeight * 0.01;
    // Then we set the value in the --vh custom property to the root of the document
    document.documentElement.style.setProperty('--vh', `${vh}px`);

});

// Code taken from EmailJS.com with small personal amendments
// EmailJS sendmail function with 'service ID', 'template ID', 'template parameters'
// Template parameters linked to name attributes in form template
function sendMail(contactForm) {
  emailjs
    .send("lucyjpjones@gmail.com", "fscr", { 
      fname: contactForm.fname.value,
      lname: contactForm.lname.value,
      from_email: contactForm.email.value,
      topic: contactForm.topic.value,
      message: contactForm.message.value,
    })
    .then(
      function (response) {
        alert("MESSAGE SENT", response); // If message is sent successfully, alert "message sent"
        contactForm.reset()
      },
      function (error) {
        alert("SENDING FAILED", error); // If message fails to send, alert "sending failed"
      }
    );
  return false; // To block from loading a new page
}
