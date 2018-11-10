angular.module('myApp', ['ngMaterial']).controller('studentHomeCtrl', function ($scope) {
    $scope.answer;
    $scope.operand1 = Math.floor(Math.random() * 12) + 1;
    $scope.operand2 = Math.floor(Math.random() * 12) + 1;
    $scope.correctCount = 0;
    $scope.totalCount = 0;
    $scope.streakMessage = '';
    $scope.checkAnswer = function () {
        $scope.totalCount++;
        if ($scope.answer == $scope.operand1 * $scope.operand2) {
            $scope.correctCount++;
        }
        else {
            console.log("You are one mistake closer to mastering math!");
        }
        $scope.answer = '';
        if ($scope.totalCount - $scope.correctCount == 0 && $scope.totalCount > 0)
            $scope.streakMessage = "You are on a streak!";
        else
            $scope.streakMessage = '';
        $scope.generateQuestion();
    }

    $scope.generateQuestion = function () {
        $scope.operand1 = Math.floor(Math.random() * 12) + 1;
        $scope.operand2 = Math.floor(Math.random() * 12) + 1;
    }

   
});
