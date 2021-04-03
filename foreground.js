console.log("foreground test")
alert("Don't get all excited")
//Domain blocker
findAllURL = function changeAllURL(text){
    var current = window.location.href;
    if(current.startsWith(text)){
      document.documentElement.innerHTML = '';
      document.documentElement.innerHTML = 'Domain is blocked until Challenge 1 is completed';
      document.documentElement.scrollTop = 0;
    }
  }


  findAllURL("https://www.hbo.com/");

  