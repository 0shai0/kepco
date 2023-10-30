$("#password").on("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    $(".login_button").triggerHandler("click");
  } else {
    if (this.value) {
      $("#keyShow").css("display", "inline-block");
    } else {
      $("#keyShow").hide();
    }
  }
}).focus();

$("#keyShow").on("click", function() {
  if ($("#password").attr("type") == "password") {
    $("#password").attr("type", "text");
    $($(this)).text("H I D E");
  } else {
    $("#password").attr("type", "password");
    $($(this)).text("SHOW");
  }
});

