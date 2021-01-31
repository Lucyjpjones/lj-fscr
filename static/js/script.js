$(document).ready(function () { 

    /* Sidebar Toggle */
    $("#sidebarCollapse").on("click", function () {
        $("#sidebar").toggleClass("active");
        $(".overlay").toggleClass("enabled");
        /* Menu icon change (toggle) - Code taken from 'https://stackoverflow.com/questions/28247310/bootstrap-mobile-menu-icon-change-to-x-close' */
        $("#navbar-bars").toggleClass("d-none");
        $("#navbar-close").toggleClass("d-none");
    });

    /* Sidebar close on outside click */
    $(".overlay").on("click", function () {
        $("#sidebar").addClass("active");
        $(".overlay").removeClass("enabled");
        $("#navbar-bars").removeClass("d-none");
        $("#navbar-close").addClass("d-none");
    });

});

// Code taken from EmailJS.com with small personal amendments
// EmailJS sendmail function with 'service ID', 'template ID', 'template parameters'
// Template parameters linked to name attributes in form template

function sendMail(contactForm) {
  emailjs
    .send("lucyjpjones@gmail.com", "fscr", { 
      from_name: contactForm.fname.value,
      from_email: contactForm.email.value,
      topic: contactForm.topic.value,
      message: contactForm.message.value,
    })
    .then(
      function (response) {
        // If message is sent successfully, alert "message sent"
        console.log("SUCCESS", response); 
        //sweet alerts2 //
        Swal.fire({
        icon: "success",
        title: "Message sent!",
        showConfirmButton: false,
        timer: 2000,
        });
        contactForm.reset();
      },
      function (error) {
        // If message fails to send, alert "sending failed"
        console.log("ERROR", error); 
        //sweet alerts2 //
        Swal.fire({
        icon: "error",
        title: "Error sending message",
        text: 'Please try again',
        showConfirmButton: false,
        timer: 2000,
        });
      }
    );
  return false; // To block from loading a new page
}
