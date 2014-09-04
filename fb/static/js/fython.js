function sendPOS(userData) {
  console.log(userData)
  $.ajax({
    url: '/login/',
    type: 'POST',
    data: {
      jsonStr: userData
    },
    success: function(result){
      window.location=result
    },
  });
}

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}

// This is called with the results from from FB.getLoginStatus().
function statusChangeCallback(response) {
  console.log('statusChangeCallback');
  console.log(response);
  // The response object is returned with a status field that lets the
  // app know the current login status of the person.
  // Full docs on the response object can be found in the documentation
  // for FB.getLoginStatus().
  if (response.status === 'connected') {
    // Logged into your app and Facebook. 
    logon();
  } else if (response.status === 'not_authorized') {
    // The person is logged into Facebook, but not your app.
    document.getElementById('status').innerHTML = 'Please log ' +
      'into this app.';
  } else {
    // The person is not logged into Facebook, so we're not sure if
    // they are logged into this app or not.
    document.getElementById('status').innerHTML = 'Please log ' +
      'into Facebook.';
  }
}

function logon(){
  FB.login(function(response){
    // Handle the response object, like in statusChangeCallback() in our demo
    // code.
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
    // Logged into your app and Facebook.
      FB.api('/me', function(response) {
        console.log(JSON.stringify(response))
        sendPOS(JSON.stringify(response))
      });
      JSON.stringify(response);
 
    } else if (response.status === 'not_authorized') {
    // The person is logged into Facebook, but not your app.
      //document.getElementById('status').innerHTML = 'Please log ' +
      //'into this app.';
    } else {
    // The person is not logged into Facebook, so we're not sure if
    // they are logged into this app or not.
      //document.getElementById('status').innerHTML = 'Please log ' +
      //'into Facebook.';
    }
  });
} 

function logout(){
  FB.logout()
  window.location='/logout'
}

function getImage(){
  FB.api(
    "/me/picture",
    {
      "redirect": false,
      "height": "50",
      "type": "normal",
      "width": "50"
    },
    function (response) {
      console.log(response)
      if (response && !response.error) {
        console.log('aqui')
        
      //return JSON.stringify(response.data);
        $('.circular').css('background-image', 'url(' + response.data.url + ')');
      }
    }
  );
}