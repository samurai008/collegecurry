$(function() {

  function toggle_element(btn, divtohide){
    $(btn).on('click', function() {
      if ($(divtohide).css("display") == "block") {
        $(divtohide).css({
          "display":"none",
        })
        $(btn).html("<i class=\"fa fa-arrow-down\"></i>&nbsp;show");
      } else {
          $(divtohide).css({
            "display":"block",
          })
          $(btn).html("<i class=\"fa fa-arrow-up\"></i>&nbsp;Hide");
      }
    })
  }

  toggle_element("#toggle-search", "#search-form")


})
