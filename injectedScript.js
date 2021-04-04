console.log("Made it here.");

$.ajax({
    url: "http://127.0.0.1:12345/_get_data/",
    type: "POST",
    success: function(resp){
      console.log(resp);
    },
    error: function(e, s, t) {
      console.log("ERROR OCCURRED");
      console.log(e);
      console.log(s);
      console.log(t);
    }
});