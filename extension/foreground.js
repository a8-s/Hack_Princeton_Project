console.log("foreground test")
//Domain blocker
findAllURL = function changeAllURL(text){
    var current = window.location.href;
    if(current.startsWith(text)){
      document.documentElement.innerHTML = '';
      document.documentElement.innerHTML = 'Domain is blocked until Challenge 1 is completed';
      document.documentElement.scrollTop = 0;

      console.log("Sending messsageg now");
      chrome.runtime.sendMessage({message: "listeners"}, function(response){})

      $.ajax({
        url: "http://127.0.0.1:12345/_get_data/",
        crossDomain:true,
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

    }
  }


  findAllURL("https://www.hbo.com/");

  