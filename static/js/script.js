$(document).ready(function () { 

    /* Sidebar Toggle */
    /* Menu icon change (toggle) [Code taken from 'https://stackoverflow.com/questions/28247310/bootstrap-mobile-menu-icon-change-to-x-close' with personal modifications] */

    $("#sidebarCollapse").on("click", function () {
        $("#sidebar").toggleClass("active");
        $(".overlay").toggleClass("enabled");
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