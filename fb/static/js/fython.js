function sendPOS(userData) {
  $.ajax({
    url: pagePath + '?action=login',
    type: 'POST',
    data: {
      jsonStr: userData,
    },
  });
}

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
  FB.api('/me', function(response) {
    console.log(JSON.stringify(response))
    sendPOS(JSON.stringify(response))
  });
}