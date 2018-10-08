# TEAM
Can we please check off what we have and finish up the items we dont have? :smiley:

- [x] Vision Statement [1 point]

- [X] Product Backlog [1 point]

- [X] Sprint Backlog [2 points] (plan for ~5-10 user stories per sprint)
- [X] Burndown Chart [2 points] (can be as simple as a google spreadsheet)
- [x] Requirements [1 point] `(user stories for functional, dependencies listed in requirements.txt)`
- [x] Design Documents [2 points] (UML diagrams)
  - [x] Architecture Diagram
  - [x] Class Diagrams
- [x] Code [2 points]
- [x] Tests [2 points] (automatic testing, instructions below build instructions, also demonstrated in demo video)
- [x] Demonstration [2 point] (link below build instructions)


# **Vision Statement**

## **Our Goal**

Elementary school students have to spend a lot of time memorizing multiplication and division facts.  Traditional methods such as flashcards and timed worksheets feel tedious to children with already short attention spans, damaging overall math interest.  Previous gamification attempts frequently add bright and colorful tedium without fixing the underlying problem.  We seek to offer a streamlined game that alleviates tedium with the well proven incentive of competition.


## **Our Product**

Our product will consist of a web-based application that allows a teacher to to create an isolated environment for just their class or grade.  Students can then log in and are sorted into rooms by skill level where they "battle" by quickly and correctly answering multiplication, division, addition, and/or subtraction.  Our software then keeps metrics on each students skill that the teacher can access.  This takes grading pressure off of the teacher while increasing accuracy compared to paper systems as well as reduce environmental cost.  

### **User Stories / Product Backlog**
#### **Complete**
* As a user I want to be able to load the webpage

* As a student I want to be able to do practice problems locally in my browser

* As a teacher I want to be able to create an account so that I can log in

* As a teacher I want to be able to log in
* As a teacher I want to be able to save my email
* As a student I want to be able to see if I got a question right
* As a student I want to compete against my classmates



#### **Incomplete**
* As a teacher I want to add students

* As a teacher I want to remove students

* As a teacher I want my students to only compete among equivalent skill levels

* As a teacher I want to be able to see my students scores

* As a teacher I want to be able to see my students answer times

* As a teacher I want to be able to create virtual rooms where my students can practice with and compete against each other

* As a student I want to be able to quickly recover my password

* As a sysadmin I want the application to be containerized

* As a developer I want to the code I have to maintain be modular and understandable

# Sprint 2


## Members:
* Darien Craig
* Annavay Kean
* Cassidy Lyons
* Ross Wagner

## Build Instructions:  
**These build instructions assume you have python 3 and pip installed**

1. `pip install virtualenv`
2. create a new folder on your desktop
3. chage working directory to new folder
4. `virtualenv ENV`
5. `source bin/activate` if on a mac or `.Scripts/activate` for windows
6. `git clone https://github.com/Fun-Team-Name/Koeus.git`
7. `cd koeus`
8. `cd koeus-arena`
9. `pip install -r requirements.txt`
10. `python manage.py runserver`
11. in your browser go to **localhost:8000**
12. **As Teacher** click teacher tab 
13. click sign up button to create account
14. log in with credentials navigate cite

**As Student** from login page click student tab, enter student for username and student for password and navigate cite

**NOTES: cookie clicker will not work unless you have docker installed. In the case docker is already installed and running,
right before step 10 do the following
`docker run -p 6379:6379 -d redis:2.8 `

now pick back up with `python manage.py runserver` and continue


 


please view the demo video before building:

[Build Instruction Video](https://youtu.be/NH2pk6iJvkI)

## Testing
To run unit tests:

navigate to koeus-arena folder from cloned repo

run the following command:

`python manage.py test teacher -v 2`

source code is in the test.py file (/koeus/koeus-arena/teacher/test.py)

Manual Testing:

Solve multiplication problems from student page after logging in as a student



## **Diagrams**
![Architecture  Diagram](https://raw.githubusercontent.com/Fun-Team-Name/Koeus/master/Documentation/djangoChannelWebSoc.png)

from: https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django

## **Class Diagram**
![UML Class Diagram](https://raw.githubusercontent.com/Fun-Team-Name/Koeus/master/Documentation/spr2UML.png)

## **Front-End Diagram**  
![Front End Diagram](https://raw.githubusercontent.com/Fun-Team-Name/Koeus/master/Documentation/FrontEndDiagram.png)

## [**Burndown Chart and Backlog**](https://docs.google.com/spreadsheets/d/1HtfZup9SnPOCrz9b8pf-G5Kyj8an78QmAuQqOf-cqz8/edit#gid=0)

##

# Sprint 1

## **Class Diagram**

![UML Class Diagram](https://raw.githubusercontent.com/Fun-Team-Name/Koeus/master/Documentation/spr2UML.png)

## [**Burndown Chart**](https://docs.google.com/spreadsheets/d/19vf88oTctJ-OZ2_OGCEM8ZfFbThggKwMdxrUroNmdWw/edit?usp=sharing)


# Members:
* Darien Craig
* Annavay Kean
* Cassidy Lyons
* Ross Wagner

