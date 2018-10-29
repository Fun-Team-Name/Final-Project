angular.module('myApp', ['ngMaterial']).controller('teacherHomeCtrl', function($scope, $mdDialog) {
    $scope.setEditRoom;
    $scope.newStudBool = false;
    $scope.newStudent = {fname: '', lname: '', snum: '', score: '0%', rank: 'last', avgTime: '0', totalTime: '0'};
    $scope.count  = 3;
    $scope.rooms  = [{num: 1, name: "Test1", skillsActive: ["mult", "div"]}, {num: 2, name: "Test2", skillsActive: ["add", "sub"]}, {num:3, name: "Test3", skillsActive:["fraction", "longDiv"]}];
    $scope.editForm;
    $scope.confirm = false;
    $scope.roomBeingEdited;
    $scope.studentsInRoomL1 = [{fname: "Ross", lname: "Wagner", snum: "123456789", score: '50%', rank: "2", avgTime: "2", totalTime: "3"},
                             {fname: "Cassidy", lname:"Lyons", snum: "987654321", score: '40%', rank: "3", avgTime: "5", totalTime: "10"},
                             {fname: "Darien", lname: "Craig", snum: "135791357", score: '70%', rank: "1", avgTime: "3", totalTime: "56"},
                             {fname: "Annavay", lname: "Kean", snum: "000111999", score: '10%', rank: "4", avgTime: "1", totalTime: "100"}];
    $scope.studentsInRoomL2 = [{fname: "Ross", lname: "Wagner", snum: "123456789", score: '50%', rank: "2", avgTime: "2", totalTime: "3"},
                             {fname: "Cassidy", lname:"Lyons", snum: "987654321", score: '40%', rank: "3", avgTime: "5", totalTime: "10"},
                             {fname: "Darien", lname: "Craig", snum: "135791357", score: '70%', rank: "1", avgTime: "3", totalTime: "56"},
                             {fname: "Annavay", lname: "Kean", snum: "000111999", score: '10%', rank: "4", avgTime: "1", totalTime: "100"}];
 $scope.addStudent = function(){
    $scope.studentsInRoomL1.push($scope.newStudent);
    $scope.newStudent = {fname: '', lname: '', snum: '', score: '0%', rank: 'last', avgTime: '0', totalTime: '0'};
 }
$scope.newStud = function(){
    $scope.newStud = true;
}
$scope.editRoom = function(obj) {
    $scope.setEditRoom = obj;
    $scope.setEditRoomIndex = $scope.studentsInRoom.indexOf(obj)
    $scope.goto('room');

}

$scope.deleteRoom = function(room){
    $scope.confirm = true;
}

 $scope.newRoom = function(){
     $scope.count++;
     var newRoomObject = {num: $scope.count, name: "Test" + ($scope.count).toString(), skillsActive:[]};
     $scope.rooms.push(newRoomObject);
}


 $scope.goto = function(dest){
    if(dest == 'home'){
        window.location.href = "/static/templates/teacherHome.html";
    }
    else if(dest == 'leaderboard'){
        window.location.href="/static/templates/leaderboard.html";
    }
    else if(dest == 'logout'){
        //code to end user session here
        window.location.href="/static/templates/index.html";
    }
    else if (dest == 'room') {
        window.location.href="/static/templates/room.html";
    }
    else
        console.log("That shouldn't work");

}
 });

 function DialogCtrl($scope, $mdDialog) {
    $scope.cancel = function() {
      $mdDialog.cancel();
    };
};
