angular.module('myApp', ['ngMaterial']).controller('signupCtrl', function($scope) {
 $scope.fname = '';
 $scope.lname = '';
 $scope.email = '';
 $scope.password = '';
 $scope.passwordVerify = '';
 $scope.submit = function(){
     
 }
 $scope.goto = function(dest){
    if(dest == 'home'){
        window.location.href= window.location.href;
    }
    else if(dest == 'leaderboard'){
        window.location.href="/static/templates/leaderboard.html";
    }
    else if(dest == 'logout'){
        //code to end user session here
        window.location.href="/static/templates/index.html";
    }
    else if(dest == 'grades'){

    }
    else if(dest == 'skills'){

    }
    else if(dest == 'settings'){

    }
    else
        console.log("That shouldn't work");

}
 });
