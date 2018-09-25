angular.module('myApp', ['ngMaterial']).controller('teacherHomeCtrl', function($scope, $mdDialog) {
    $scope.count  = 3;
    $scope.skills = ["mult", "div", "add", "sub", "fraction", "longDiv"];
    $scope.rooms  = [{num: 1, name: "Test1", skillsActive: ["mult", "div"]}, {num: 2, name: "Test2", skillsActive: ["add", "sub"]}, {num:3, name: "Test3", skillsActive:["fraction", "longDiv"]}];
    $scope.editRoomToggle = false;
    $scope.editForm;
    $scope.roomBeingEdited;
    $scope.studentsInRoom = [{fname: "Ross", lname: "Wagner"}, {fname: "Cassidy", lname:"Lyons"}, {fname: "Darien", lname: "Craig"}, {fname: "Annavay", lname: "Kean"}];
    console.log($scope.studentsInRoom);
    $scope.adjustCount = function(key){
    if(key == 'up')
        $scope.count += 1;
    else
        $scope.count -= 1;
 }
 $scope.addStudent = function(){
     //first name, last name, student number
             // Appending dialog to document.body to cover sidenav in docs app
             var confirm = $mdDialog.prompt()
             .title('Add New Student')
             .placeholder('Student Name')
             .ariaLabel('Student Name')
             .required(true)
             .ok('Add')
             .cancel('Cancel');
       
             $mdDialog.show(confirm).then(function(result) {
                var temp = result.split(" ");
                $scope.studentsInRoom.push({lname: temp[1], fname: temp[0]});
            }, function() {        
            });
 }
 
 $scope.deleteStudent = function(student){
    // Appending dialog to document.body to cover sidenav in docs app
    var confirm = $mdDialog.confirm()
          .title('Confirm Deletion')
          .textContent('Are you sure you want to delete this student? All data will be lost.')
          .ok('Confirm')
          .cancel('Cancel');

    $mdDialog.show(confirm).then(function() {
        console.log("deleting" + $scope.studentsInRoom.indexOf(student))
        $scope.studentsInRoom.splice($scope.studentsInRoom.indexOf(student), 1);
    }, function() {        
    });
}

 $scope.newRoom = function(){
     $scope.count++;
     var newRoomObject = {num: $scope.count, name: "Test" + ($scope.count).toString(), skillsActive:[]};
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
            console.log("deleting" + $scope.rooms.indexOf(room))
            $scope.rooms.splice($scope.rooms.indexOf(room), 1);
        }, function() {        
        });
}

$scope.editRoom = function(room){
    var index = $scope.rooms.indexOf(room)
    $scope.editRoomToggle = true;
    $scope.editForm = room;
    $scope.roomBeingEdited = index;
}
$scope.addSkill = function(){
    var confirm = $mdDialog.prompt()
        .title('What skill would you like to add?')
        .placeholder('Skill Name Here')
        .ok('Add Skill')
        .cancel('Cancel');

    $mdDialog.show(confirm).then(function(result){
        console.log($scope.rooms[$scope.roomBeingEdited].skillsActive)
        $scope.rooms[$scope.roomBeingEdited].skillsActive.push(result);
    })
        
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
