angular.module('myApp', ['ngMaterial']).controller('cookieCtrl', function($scope, $mdDialog) {
    $scope.p1score = 0;
    $scope.p2score = 0;

    $scope.countUp = function(){
        $scope.p1score++;
    }

});