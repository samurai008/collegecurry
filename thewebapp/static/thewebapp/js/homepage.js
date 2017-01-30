$(function() {
  $("#btn-location").on('click', function(e) {
    e.preventDefault();

    $("#query-box").html("<center><div class=\"loading\"></div></center>");
  })

  $("#mylightbox-btn").on('click', function(e) {
    e.preventDefault();
    $("#mylightbox").load("http://localhost:8000/college/col-det-particular/");
  })

  $("#nav-toggle").on('click', function(e) {
    if ($("#main-nav").css("display") == "none")
      $("#main-nav").css("display", "block");
    else {
      $("#main-nav").css("display", "none");
    }
  })
})
