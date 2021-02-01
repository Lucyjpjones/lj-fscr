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