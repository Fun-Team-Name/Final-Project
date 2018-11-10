var p1score = 0;
var dict = new Object();

var answer;
var operand1 = Math.floor(Math.random() * 12) + 1;
var operand2 = Math.floor(Math.random() * 12) + 1;
var correctCount = 0;
var totalCount = 0;
var streakMessage = '';
var streak = 0;
var scoreTag = document.getElementById("score");
var streakTag = document.getElementById("streak");
var streakMessageTag = document.getElementById("streakMessage");
var otherScores = document.getElementById("otherScores");
var questionTag = document.getElementById("question");
var answerTag = document.getElementById("answer");
var studentAnswerForm = document.getElementById("studentAnswerForm");
var otherScoresTag = document.getElementById("otherScores");
var heartbeat_msg = '--heartbeat--', heartbeat_interval = null, missed_heartbeats = 0;

updateLocal();

function checkAnswer() {
  answer = parseInt(answerTag.value);
  totalCount++;
  if(answer == operand1 * operand2){
      correctCount++;
      streak++;
  }
  else{
    streak = 0;
    console.log("You are one mistake closer to mastering math!");
  }
  answer = '';
  if( streak >= 2){
      streakMessage = "You are on a streak!";
    }
  else{
      streakMessage = '';
  }
  generateQuestion();
  updateLocal();
  send ();
}

function displayOtherScores(){
  otherScores.innerHTML = "";
  for (player in dict){
      otherScores.innerHTML = otherScores.innerHTML + player +": "+ dict[player]+ "<br>";
  }
}
function generateQuestion (){
    operand1 = Math.floor(Math.random() * 12) + 1;
    operand2 = Math.floor(Math.random() * 12) + 1;
}

function updateLocal (){
  studentAnswerForm.reset();
  scoreTag.innerHTML = alias+"'s Score: "+correctCount+" / "+totalCount;
  questionTag.innerHTML = operand1 + " X " + operand2+" =";
  streakTag.innerHTML = "Streak: "+ streak;
  streakMessageTag.innerHTML = streakMessage;
}

var arenaSocket = new WebSocket(
  'ws://' + window.location.host +
  '/ws/arena/' + arenaName + '/');

arenaSocket.onmessage = function(e) {
  var data = JSON.parse(e.data);
  var message = data['message'];
  otherName = data['userName'];

  /* heart beat. reagular pings to channels to confirm connection
  if (message === heartbeat_msg) {
        // reset the counter for missed heartbeats
        missed_heartbeats = 0;
        console.log(message+otherName+message);
        return;
  }
  */

  //otherName = data['userName'];
  console.log("receiveing: "+otherName);


  var otherScore = parseInt( message,10);
  //document.querySelector('#arena-log').value += (otherName +": "+ message + '\n');

  // update other username's score
  if(otherName != alias){

    dict [otherName]= otherScore;
    displayOtherScores();
  }

};
arenaSocket.onopen = function(e){
  console.log(alias+" connected");
  arenaSocket.send(JSON.stringify({
      userName: alias,
      message: correctCount
  }));

  /* heart beat. reagular pings to channels to confirm connection
  if (heartbeat_interval === null) {
        missed_heartbeats = 0;
        heartbeat_interval = setInterval(function() {
            try {
                missed_heartbeats++;
                if (missed_heartbeats >= 3)
                    throw new Error("Too many missed heartbeats.");
                arenaSocket.send(JSON.stringify({
                    userName: alias,
                    message: heartbeat_msg
                }));
            } catch(e) {
                clearInterval(heartbeat_interval);
                heartbeat_interval = null;
                console.warn("Closing connection. Reason: " + e.message);
                arenaSocket.close();
            }
        }, 5000);
    }
    */

}
arenaSocket.onclose = function(e) {
  console.error('Arena socket closed unexpectedly');
};

function send (){
  console.log("sending: "+alias);
  arenaSocket.send(JSON.stringify({
      userName: alias,
      message: correctCount
  }));
}

function displayOtherScores(){
  otherScores.innerHTML = "";
  for (player in dict){
      otherScores.innerHTML = otherScores.innerHTML + player +": "+ dict[player]+ "<br>";
  }

}
