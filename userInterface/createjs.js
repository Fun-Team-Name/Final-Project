var  tabButtons=document.querySelectorAll(".tabContainer .buttonContainer button");
var  tabPanels=document.querySelectorAll(".tabContainer .tabPanel");

function showPanel(panelIndex, colorCode){
  tabButtons.forEach(function(node){
    node.style.backgroundColor = "";
    node.style.color = "";

  });
   tabButtons[panelIndex].style.backgroundColor = colorCode;
   tabButtons[panelIndex].style.color = "white";
   tabPanels.forEach(function(node){
     node.style.display = "none";
  });
  tabPanels[panelIndex].style.display = "block";
  tabPanels[panelIndex].style.backgroundColor = colorCode;
}
showPanel(1,'blue');
showPanel(0,'blue');
// testing out routing to other pages. I can make a new file for this .js code if it agrees with common standards to do so
var  menbar = angular.module('menbar', ['ngRoute']);

menbar.config(['$routeProvider', function($routeProvider){
  $routeProvider
  .when('/index', {
    templateUrl: '/index.html'
  })
  .when('/create', {
    templateUrl: '/create.html'
  })
  .otherwise({
    redirectTo: '/index'
  });

}]);
