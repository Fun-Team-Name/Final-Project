# How I Django'd..

[I watched this playlist](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW "YouTube playlist")

I watched the first 12 videos in a row, following step by step, and by then I felt pretty good about just picking and choosing what to watch based on what I wanted to do

## BUG FIX
 **loading html pages from Ctrl.js files now working**
### Fix one bug and find a new one..
The teacherHome.html and studentHome.html pages do not look how they should. The coding style seems a little inconsistent (defining style in .css file and then also defining the style from within the html pages) so it was a little confusing

I will let you (Annavay) take it from here as planned.. sorry I couldn't help myself , I knew the js pages should have been able to load the html pages with the code you already had in place. I had to try one more time

#### What I did wrong
instead of

 window.location.href= "static/templates/teacherHome.html"

 I had

 window.location.href= " ../templates/teacherHome.html"

 plus many other incorrect paths that looked like they could be right
