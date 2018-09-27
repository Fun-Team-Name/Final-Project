
//var myApp = angular.module('myApp', ['ngMaterial']);
  angular.module('myApp', ['ngMaterial']).controller('homepageCtrl', function($scope) {
   $scope.username = '';
   $scope.password = '';
   $scope.invalidLogin = false;
   $scope.selectedState;
   $scope.stateList = ["FL", "TX", "CA"];
   $scope.countyList = [{name: "Orange County Public Schools", abbrev: "OCPS"}, {name: "Brevard County Public Schools", abbrev: "BCPS"}];
   $scope.login = function(){
        if($scope.username == 'teacher' && $scope.password == 'teacher'){
            $scope.invalidLogin = false;

              window.location.href= "/static/templates/teacherHome.html"
        }
        else if($scope.username == 'student' && $scope.password == 'student'){
            $scope.invalidLogin = false;
            window.location.href = "/static/templates/studentHome.html"
        }
        else{
            $scope.invalidLogin = true;
        }
    }

    $scope.goto = function(dest){
        if(dest == 'home'){
            window.location.href="/static/templates/index0.html";
        }
        else if(dest == 'leaderboard'){
            window.location.href="/static/templates/leaderboard.html";
        }
        else if(dest == 'signup'){
            window.location.href="/static/templates/signup0.html"
        }
        else
            console.log("That shouldn't work");

    }
});
