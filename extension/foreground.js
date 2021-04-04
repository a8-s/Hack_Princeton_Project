console.log("foreground test")
//Domain blocker
    var current = window.location.href;
    var myName = "david";
    var search_word ="konfu";



      // console.log("Sending message now");
      // chrome.runtime.sendMessage({message: "listeners"}, function(response){})

      var htmlTemplate = '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>\n<script src="js/bootstrap.min.js"></script>\n <h1 style="position:absolute; top:50%; left:50%; transform: translate(-50%, -50%); font-family: \'Georgia\';">'

      $.ajax({
        url: "http://127.0.0.1:12345/_get_data/",
        crossDomain:true,
        type: "POST",
        dataType: "json",
        data: {siteURL:current,
               username:myName},
        success: function(resp){
          console.log(resp);

          if(!resp["unlocked"]){
            document.documentElement.innerHTML = '';
            document.documentElement.innerHTML = htmlTemplate + resp["title"] + resp["hostName"] + '!</h1>';
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



  