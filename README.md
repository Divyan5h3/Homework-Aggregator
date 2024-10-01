<!---
# course-project-group-63
course-project-group-63 created by GitHub Classroom

Pitch
A homework aggregator: Students have their homework assignments scattered across different LMS (Learning Management Systems) platforms – like PriarieLearn, Gradescope, Canvas. The Homework Aggregator will allow students to simply sign in with their NetID and display all homework assignments in one place, allowing students to keep track of and manage their deadlines better.

Functions
Be able to sign in with UofI NetID.
Users can access all their homework from different LMS through one page.
Users can click on the homework and it will take them to the respective website. 
Displays deadlines of each homework in a calendar
Users can see how many points each homework is worth.


Components
Web Scraper: We will be building a web scraper to scrape homework details from the LMS platforms listed above. To build the web scraper, we will be using Beautiful Soup, a Python library widely used for this same purpose replete with detailed documentation. The data scraped by the web scraper will be passed to the backend. The scraper will be tested by scraping data from LMS platforms of one of the team members.

Backend: The backend will serve as an interface between the web scraper and the frontend of our website. We will be using Django for building the backend of the website, since it is also a Python library and allows for easy integration with other components of the project. The backend will receive HTTPS requests from the frontend and make a call to webs scraper. The backend will respond to the frontend call with the data returned by the scraper. 

Frontend: We will be using Flutter Web and Dart to build out our website. Additionally, Dart will also be responsible for the authentication API calls, syncing with LMS) platforms, displaying scraped results and enabling desired functionality for users. The frontend will make HTTPS requests to the backend and display the data returned by the backend.

Continuous Integration
We will be using the Google Python Style guide throughout our code
We will be using PyTest to run our tests.
We will use Pylint to check whether our code matches the style guide.
We will use Coverage.py to compute test coverage.
We plan to open PR’s bi-weekly. One reviewer from the other team will review the code. As there are two members in one group, any one of them can review the code.
We plan to avoid merge conflicts by communicating clearly which person will review the code beforehand.

Schedule

Week 1: 
Finalize pages and all page designs 
Familiarize ourselves with Django-Flutter and Django-Beautiful Soup integration

Weeks 2: 
Create preliminary login page
Continue learning Django and integration with Beautiful Soup



Week 3:
Create user home page
Experiment with Beautiful Soup 
Understand how to authenticate into LMS using the Web Scraper, beginning with Canvas

Week 4:
Finalize login page and begin authentication API integration
Build automated LMS authentication to allow web scraping of student homework data

Week 5:
Build a calendar UI that displays user’s assignments along with deadlines
Build automated LMS authentication to allow web scraping of student homework data
Build backend API in Django

Week 6:
Integrate calendar UI with LMS scraper to show students’ data and transition away from placeholder data
Build automated LMS authentication to allow web scraping of student homework data
Build backend API in Django

Week 7:
Integrate Web Scraper, Frontend with Django
Begin testing using PyTest for user authentication, automated LMS authentication, scraping, UI integration with Django API, etc.
Exhibit product to potential users (classmates) and solicit feedback to help improve the product 

Week 8:
Incorporate additional functionality, improve page design, eliminate confusing UI features, etc. based on feedback from Week 7
Find and debug any errors present
Test final product and its features to make sure it functions work properly 
Risks
Potential risks include inability to scrape the above-listed websites due to the security design of Shibboleth, the authentication service that UofI uses. 
UofI Tech Services is planning to introduce two-factor authentication. This might significantly set us back since scraping LMS platforms would become substantially harder.
Implementing the backend in Django and integrating with other frameworks and SDKs in the project (Flutter and Beautiful Soup) might prove harder than expected since none of us have used the library before.


Teamwork
Being a group of 4 people we decided to equally split up into two teams, a front-end team (Akash and Rohan) and a back-end team (Arjun, Divyansh). We will set-up a github repository and work individually in our groups on a standardized editing environment.
-->

# Introduction:
Homework Aggregator is a website where students can view assignment deadlines across different learning platforms. The need for this project arose when one of our team members almost missed a deadline because they forgot to check one of the numerous learning platforms used by UIUC. While DateCat has similar functionality to our project, it is unable to extract assignment deadlines from prairielearn and gradescope. Along with that, when we began working on the project no similar service existed. 

# Installation Instructions:
After downloading the project files, run the following commands to install the required dependencies:
    `pip3 install selenium`
    `pip3 install flask`
Once the dependencies have been installed, run 
    `flask run`

# Application Architecture:
Our project has 3 main components:
1. The frontend has a login page made using HTML requests login credentials from user and passes it to the backend.  It also consists of the display page where we get the assignment data from the scraper and display it to the user.
2. The backend in Flask gets login input and sends it to the scraper. It also routes the login page to the assignment page after getting scraper data.
3. The data scraper gets assignment data from online platforms and returns them to the backend. It was written using                       Selenium and BeautifulSoup

![alt text](https://github.com/CS222-UIUC/course-project-group-63/blob/main/architecture.png)
 
# Group Member Contributions:
 - Akash - Worked on frontend and flask.
 - Rohan - Worked on frontend and flask.
 - Arjun - Built scraper for getting data from online platforms and made .
 - Divyansh - Helped with troubleshooting problems and with scraper.
 
