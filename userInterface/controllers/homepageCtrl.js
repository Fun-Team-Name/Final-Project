angular.module('myApp', ['ngMaterial']).controller('homepageCtrl', function($scope) {
   $scope.username = '';
   $scope.password = '';
   $scope.invalidLogin = false;
    $scope.login = function(){
        if($scope.username == 'teacher' && $scope.password == 'teacher'){
            $scope.invalidLogin = false;
            window.location.href="teacherHome.html"
        }
        else if($scope.username == 'student' && $scope.password == 'student'){
            $scope.invalidLogin = false;
            window.location.href="studentHome.html"
        }
        else{
            $scope.invalidLogin = true;
        }
    }

    $scope.goto = function(dest){
        if(dest == 'home'){
            window.location.href="index.html";
        }
        else if(dest == 'page2'){
            window.location.href="page2.html";
        }
        else
            console.log("That shouldn't work");

    }
});
