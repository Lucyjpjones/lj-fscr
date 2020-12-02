$(document).ready(function () {

/* Sidebar Toggle*/
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
  });

/* Menu icon change (toggle) - Code taken from 'https://stackoverflow.com/questions/28247310/bootstrap-mobile-menu-icon-change-to-x-close' */
  $("#sidebarCollapse").on("click", function () {
    $("#navbar-bars").toggleClass("d-none");
    $("#navbar-close").toggleClass("d-none");
  });
  
});
