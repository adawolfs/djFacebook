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
  console.log('logon')
  FB.login(function(response){
    console.log('statusChangeCallback');
    console.log(response)
    if (response.authResponse) {
      var accessToken = response.authResponse.accessToken;
      console.log(accessToken)
      $.cookie('fb_access_token', '', $.extend({}, '', { expires: -1, path:'/'}));
      $.cookie('fb_access_token', accessToken);
      setTimeout(function() {
        window.location="/login/"
      }, 2000);
    }
  });
} 

function logoff(){
  //FB.logout()
  console.log('logoff')
  $.cookie('fb_access_token', '', $.extend({}, '', { expires: -1,path:'/'}));
  window.location="/logout/"
}

function fqlQuery(){
         FB.api('/me', function(response) {
              var query = FB.Data.query('select name,email,hometown_location, sex, pic_square from user where uid={0}', response.id);
              query.wait(function(rows) {
                uid = rows[0].uid;
                document.getElementById('name').innerHTML =
                  'Your name: ' + rows[0].name + "<br />" +
                  'Your email: ' + rows[0].email + "<br />" +
                  'Your hometown_location: ' + rows[0].hometown_location + "<br />" +
                  'Your sex: ' + rows[0].sex + "<br />" +
                  'Your uid: ' + rows[0].uid + "<br />" +
                  '<img src="' + rows[0].pic_square + '" alt="" />' + "<br />";
              });
         });
     }