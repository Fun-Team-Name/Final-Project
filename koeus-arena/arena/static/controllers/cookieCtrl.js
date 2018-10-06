angular.module('myApp', ['ngMaterial']).controller('cookieCtrl', function($scope, $mdDialog) {
    $scope.p1score = 0;
    $scope.p2score = 0;

    $scope.countUp = function(){
        $scope.p1score++;
    }

    $scope.goto = function(dest){
        if(dest == 'home'){
            window.location.href = "/static/templates/cookie.html";
        }
        else if(dest == 'leaderboard'){
            window.location.href="/static/templates/leaderboard.html";
        }
        else if(dest == 'logout'){
            //code to end user session here
            window.location.href="/static/templates/index.html";
        }
        else
            console.log("That shouldn't work");
    
    }

});