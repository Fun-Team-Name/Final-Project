angular.module('myApp', ['ngMaterial']).controller('teacherHomeCtrl', function($scope) {
    $scope.count = 3;
    $scope.rooms = [{num: 1, name: "Test1", skill: ["mult", "div"]}, {num: 2, name: "Test2", skill: ["add", "sub"]}, {num:3, name: "Test3", skill:["fraction", "longDiv"]}];
    $scope.adjustCount = function(key){
    if(key == 'up')
        $scope.count += 1;
    else
        $scope.count -= 1;
 }
 $scope.newRoom = function(){
     $scope.count++;
     var newRoomObject = {num: $scope.count, name: "Test" + ($scope.count).toString()};
     $scope.rooms.push(newRoomObject);
}

 $scope.goto = function(dest){
    if(dest == 'home'){
        window.location.href= window.location.href;
    }
    else if(dest == 'page2'){
        window.location.href="page2.html";
    }
    else if(dest == 'logout'){
        //code to end user session here
        window.location.href="static/templates/index.html";
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
