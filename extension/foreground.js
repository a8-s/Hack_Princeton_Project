console.log("foreground test")
//Domain blocker
findAllURL = function changeAllURL(text){
    var current = window.location.href;
    var myName = "david";
    var search_word ="konfu";

    if(current.startsWith(text)){


      // console.log("Sending message now");
      // chrome.runtime.sendMessage({message: "listeners"}, function(response){})

      $.ajax({
        url: "http://127.0.0.1:12345/_get_data/",
        crossDomain:true,
        type: "POST",
        dataType: "json",
        data: {siteURL:current,
               username:myName},
        success: function(resp){
          console.log(resp["unlocked"]);

          if(!resp["unlocked"]){
            document.documentElement.innerHTML = '';
            document.documentElement.innerHTML = 'Domain is blocked until Challenge 1 is completed';
            document.documentElement.scrollTop = 0;
          }

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

  