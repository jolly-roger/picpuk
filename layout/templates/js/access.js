if(typeof(hyperload) == "undefined"){
    hyperload = {};
};

hyperload._access = function(){
    this.logout = function(){
        $.get("/access/logout", function(data){
            window.location = data;
        });
    };

    this.login = function(loginType){
        if(loginType == "fb"){
            FB.login(function(response) {
                if (response.authResponse && response.authResponse.accessToken &&
                    response.authResponse.userID) {
                    $.post( "/access/fblogin", "accessToken=" + response.authResponse.accessToken +
                        "&userID=" + response.authResponse.userID, function(data){
                            if(data){
                                window.location = data;
                            }
                    });
                } else {
                  alert('User cancelled login or did not fully authorize.');
                }
            });
        }else if(loginType == "ggl"){
            window.open("https://accounts.google.com/o/oauth2/auth?" +
                "scope=https://www.googleapis.com/auth/userinfo.email+" +
                "https://www.googleapis.com/auth/userinfo.profile&" +
                "response_type=token&" +
                "redirect_uri=http://hyperload.net/access/gglcallbackhandler&" +
                "state=/profile&" +
                "client_id=863631441711.apps.googleusercontent.com","_blank",
                "height=400,width=400,status=yes,toolbar=no,menubar=no,location=no");
        };
        
        return false;
    };
};

hyperload.access = new hyperload._access();