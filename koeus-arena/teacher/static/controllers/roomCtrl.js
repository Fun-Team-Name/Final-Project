angular.module('myApp', ['ngMaterial']).controller('roomCtrl', function($scope, $mdDialog) {
    $scope.ts = TeacherServ;
    $scope.studentsInRoom = [{fname: "Ross", lname: "Wagner"}, {fname: "Cassidy", lname:"Lyons"}, {fname: "Darien", lname: "Craig"}, {fname: "Annavay", lname: "Kean"}];
    $scope.roomInQuestion = ts.getEditRoom()
 $scope.addStudent = function(){
     //first name, last name, student number
             // Appending dialog to document.body to cover sidenav in docs app
      
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
    else
        console.log("That shouldn't work");

}
 });


