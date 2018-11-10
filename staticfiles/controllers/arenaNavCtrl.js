angular.module('myApp', ['ngMaterial']).controller('teacherHomeCtrl', function($scope) {
  /*
    $scope.answer;
    $scope.operand1 = Math.floor(Math.random() * 12) + 1;
    $scope.operand2 = Math.floor(Math.random() * 12) + 1;
    $scope.correctCount = 0;
    $scope.totalCount = 0;
    $scope.streakMessage = '';

    $scope.checkAnswer = function(){
        $scope.totalCount++;
        if($scope.answer == $scope.operand1 * $scope.operand2){
            $scope.correctCount++;
        }
        else{
            console.log("You are one mistake closer to mastering math!");
        }
        $scope.answer = '';
        if($scope.totalCount - $scope.correctCount < 2)
            $scope.streakMessage = "You are on a streak!";
        else
            $scope.streakMessage = '';
        $scope.generateQuestion();
    }

    $scope.generateQuestion = function(){
        $scope.operand1 = Math.floor(Math.random() * 12) + 1;
        $scope.operand2 = Math.floor(Math.random() * 12) + 1;
    }
*/
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
