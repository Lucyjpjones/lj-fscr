$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
  });

  /* https://stackoverflow.com/questions/28247310/bootstrap-mobile-menu-icon-change-to-x-close*/
  
  $("#sidebarCollapse").on("click", function () {
    $("#navbar-bars").toggleClass("d-none");
    $("#navbar-close").toggleClass("d-none");
  });
});
