angular.module('myApp', ['ngMaterial']).controller('teacherHomeCtrl', function($scope, $mdDialog) {
    $scope.count = 3;
    $scope.rooms = [{num: 0, name: "Test1", skill: ["mult", "div"]}, {num: 1, name: "Test2", skill: ["add", "sub"]}, {num:2, name: "Test3", skill:["fraction", "decimals"]}];
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

$scope.deleteRoom = function(room){

        // Appending dialog to document.body to cover sidenav in docs app
        var confirm = $mdDialog.confirm()
              .title('Confirm Deletion')
              .textContent('Are you sure you want to delete this room? All data will be lost.')
              .ok('Confirm')
              .cancel('Cancel');
    
        $mdDialog.show(confirm).then(function() {
            $scope.rooms.splice($scope.rooms.indexOf(room), 1);
        }, function() {
         
        });


    

}

 $scope.goto = function(dest){
    if(dest == 'home'){
        window.location.href= window.location.href;
    }
    else if(dest == 'leaderboard'){
        window.location.href="leaderboard.html";
    }
    else if(dest == 'logout'){
        //code to end user session here
        window.location.href="index.html";
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
 