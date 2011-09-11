<?php

$app_id = "APP_ID_HERE";
$fb_cookie = $_COOKIE['fbs_' . $app_id];

if ($fb_cookie) {
  // The user has authenticated, let's go get their name
  $stuff = '<img id="image"/><div id="name"></div>';
} else {
  // The user has not yet authenticated, show the login button
  $stuff = '<fb:login-button>Login with Facebook</fb:login-button>';
}

?>

<html>
    <head>
      <title>Sly Black Horse</title>
    </head>
    <body>
      <div id="fb-root"></div>
      <script src="http://connect.facebook.net/en_US/all.js"></script>
      <script>
         FB.init({ 
            appId:<?php echo $app_id?>, cookie:true, 
            status:true, xfbml:true 
         });
         FB.api('/me', function(user) {
           if(user != null) {
              var image = document.getElementById('image');
              image.src = 'https://graph.facebook.com/' + user.id + '/picture';
              var name = document.getElementById('name');
              name.innerHTML = user.name
           }
         });
      </script>
      <script src="http://muriello.net/jquery-1.6.3.min.js"></script>
      <?php echo $stuff ?>
    </body>
 </html>
