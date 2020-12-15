$(document).ready(function () {
    /* Sidebar Toggle*/
    $("#sidebarCollapse").on("click", function () {
        $("#sidebar").toggleClass("active");
        $(".overlay").toggleClass("enabled");
    });

    /* Menu icon change (toggle) - Code taken from 'https://stackoverflow.com/questions/28247310/bootstrap-mobile-menu-icon-change-to-x-close' */
    $("#sidebarCollapse").on("click", function () {
        $("#navbar-bars").toggleClass("d-none");
        $("#navbar-close").toggleClass("d-none");
    });

    // First we get the viewport height and we multiple it by 1% to get a value for a vh unit
    let vh = window.innerHeight * 0.01;
    // Then we set the value in the --vh custom property to the root of the document
    document.documentElement.style.setProperty('--vh', `${vh}px`);

});
