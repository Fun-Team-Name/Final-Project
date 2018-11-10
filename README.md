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
14. log in with credentials navigate site

**As Student** from login page click student tab, enter student for username and student for password and navigate site

**NOTES: cookie clicker will not work unless you have docker installed. In the case docker is already installed and running,
right before step 10 do the following
`docker run -p 6379:6379 -d redis:2.8 `

now pick back up with `python manage.py runserver` and continue





please view the demo video before building:

[Build Instruction Video](https://youtu.be/NH2pk6iJvkI)

Video Notes:
In the video, some build instructions are skipped since dependencies are already installed (and docker command was already running)

## Testing
To run unit tests:

In your terminal from the root directory
```bash
ls
```
if manage.py is listed you are in the right place! now

run the following command:

```bash
python manage.y runserver

```
Now open a new terminal window (keep the server running in the first window!)

Navigate back to the new folder where the virtualenv ENV was created and you cloned the koeus repo

run the following commands

if on a mac

```bash
`source bin/activate`  
cd Koeus
python manage.py test teacher -v 2

```
for windows
```bash
`.Scripts/activate`
cd Koeus
python manage.py test teacher -v 2
```


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

## [**Burndown Chart and Backlog**](https://drive.google.com/open?id=1HtfZup9SnPOCrz9b8pf-G5Kyj8an78QmAuQqOf-cqz8)

##

# Sprint 1

## **Class Diagram**

![UML Class Diagram](https://raw.githubusercontent.com/Fun-Team-Name/Koeus/master/Documentation/spr2UML.png)

## [**Burndown Chart**](https://drive.google.com/open?id=19vf88oTctJ-OZ2_OGCEM8ZfFbThggKwMdxrUroNmdWw)


# Members:
* Darien Craig
* Annavay Kean
* Cassidy Lyons
* Ross Wagner
