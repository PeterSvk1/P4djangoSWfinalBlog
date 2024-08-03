# StarWars blog

# Table of content
- [StarWars blog](#starwars-blog)
  * [Introduction](#introduction)
  * [User Experience](#user-experience)
  * [User stories](#user-stories)
  * [Scopes](#scopes)
  * [Agile Methodology](#agile-methodology)
- [Design](#design)
  * [WireFrames](#wireframes)
  * [Fonts](#fonts)
  * [color Scheme](#color-scheme)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Python packages](#python-packages)
- [Deployement](#deployement)
  * [Deploying on Heroku](#deploying-on-heroku)
  * [To Fork this repository:](#to-fork-this-repository-)
  * [Cloning this Project](#cloning-this-project)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


## Introduction
This is a Star Wars Blog Project using Django Framework with an Agile methodology approach. This project is a web application deployed on Heroku that allows fans to share their insights, theories, and adventures within the Star Wars universe. The blog is built using the powerful Django framework for Python.

The aim of this project is to create a community where Star Wars enthusiasts can document their thoughts, showcase artwork, and connect with like-minded individuals. With a user-friendly design, navigating the website to find relevant information is a breeze. Additionally, the project includes an admin interface that allows the administrator to manage content, users, and other aspects of the website.

## User Experience
The goal of this project is to provide a platform for users where they share their stories with other users and find inspiration.

![Responsice Mockup](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/assets/responsive_pic.png)

## User stories
|      | As a non-logged in user |
| ---      | ---       |
| 1 |  	I want to browse the travel blog and view its content without having to create an account.         |
| 2 |   I want to register to the website.      |
| 3 |   I want to contact the site owner via email form without registration needed.     |
| 4 |   I want to to read something about website before I register.     |
| 5 |   I want to log in to the website once registered.     |

|      | As a logged in user |
| ---      | ---       |
| 1 |  	I want to comment on blog posts and interact with other users.         |
| 2 |   I want to like/unlike the blog posts.      |
| 3 |   I want to edit profile, such as BIO.    |
| 4 |   I want to logout from the website.     |
| 5 |   I want to create new blog category    |
| 6 |  	I want to create blog posts so other user can read it.        |
| 7 |  	I want to edit/delete my blog posts        |
| 8 |  	I want to delete my comments.        |
| 9 |   I want to downvote and upvote comments    |

|      | As a superuser |
| ---      | ---       |
| 1 |  	I want to access all of the website features and settings in admin panel         |
| 2 |   I want to manage all user accounts in admin panel      |
| 3 |   I want to give users authority to staff or superuser.    |

## Scopes
- Create responsive and user-friendly website allowing users to browse, read blogs, search posts.
- Include user authentication that allows users to register, login to the website for commenting and liking posts.
- Include email API that allows users to send email directly from the website.
- Inluclude summernote text editor for creating new posts.
- Optimize website performance, security, and accessibilty using best practices in web development.

## Agile Methodology

My Star wars blog project was developed using Agile methodology. Its first time I used agile methology and it was very confusing, I kept on forgetting to do user stories and just kept on working on my project.
It was very interresting experience and I made lots of mess during development of my project. Please find user stories over [here](https://github.com/users/PeterSvk1/projects/4/views/1)

# Design

## WireFrames
Please find Wireframes for deskop and mobile phones [here](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/wireframes.md) .
I did wireframes for phones and deskop only because everyone uses these devices.

## Fonts
I used regular roboto fonts from google fonts, nothing fancy.
![Fonts](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/assets/fonts.png)

## color Scheme
![Color_scheme](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/assets/color_scheme.png)

Also used background picture from google.


# Testing
Code Validation:
Python 
- Python code was tested using PEP8 Code Institute [Python Linter Validator](https://pep8ci.herokuapp.com/)
- Python validations can be accessed [here](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/pythonvalidation.md)

HTML checker, CSS, Jscript can be found here

HTML code was tested using [W3 Validator](https://validator.w3.org/)
CSS code was tested using [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
Javascript code was tested using [JSHint](https://jshint.com/)

The website has been tested thoroughly on several different browsers.

Google Chrome
Mozilla Firefox
Microsoft Edge
Safari
Opera


# Technologies Used
- HTML 5: Provides the main structure of the website.
- CSS 3: Used for styling the website.
- Bootstrap: Used for general styling and responsiveness of the website.
- Python: Used for the website's backend development.
- JavaScript: Used for website scripts
- Django: Used as the web framework.
- Cloudinary: Used for storing the website's static files.
- Database was provided by codeintitute
- Heroku: Used for hosting the website.
- GitHub: Used to store the repository.
- GitPod: Used as the workspace for the project.
- Balsamiq: Used for wireframe planning.
- Font Awesome: Used for icons on the website.
- Google Fonts: Used for fonts on the website.
- Favicon.ico: Used for generating the website favicon.
- colorcodefinder: used to find color pallette for project
- Google Chrome: Used for main testing of the website on all devices.
- Google Chrome Lighthouse: Used for testing the performance of each page.
- W3C HTML Validator: Used for validating the HTML code.
- Jigsaw CSS Validator: Used for validating the CSS code.
- Ci Python Linter: Used for validating the Python code.
- JSHint: Used for validating the JavaScript code.

# Python packages
- asgiref==3.8.1
- cloudinary==1.36.0
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==5.0.7
- django-allauth==0.57.2
- django-crispy-forms==2.3
- django-summernote==0.8.20.0
- django-widget-tweaks==1.5.0
- gunicorn==22.0.0
- oauthlib==3.2.2
- psycopg2==2.9.9
- PyJWT==2.8.0
- python3-openid==3.2.0
- pytz==2024.1
- requests-oauthlib==2.0.0
- sqlparse==0.5.1
- urllib3==1.26.15
- whitenoise==5.3.0

# Deployement

## Deploying on Heroku
For deployment this project on Heroku, please follow these steps:
1. Create Pipfile with all the required dependencies by running the command "pip3 > freeze > requirements.txt" in the terminal.
2. Go to the Heroku website and create a [Heroku](www.heroku.com) account if you haven't already done so.
3. Create a new app by clicking the "New" button and selecting "Create a new app".
4. Choose a name for your app and select your location.
5. Get your database from codeinstitute.
6. Back in the Heroku open settings tab and paste database url from codeinstitute and Secret key to Config Vars.
7. Go to the "Deploy" tab and click on "Connect to GitHub" to connect your Heroku app to your GitHub Depositary
8. Finally, choose the main branch for deploying. Enable automatic deployment, and then select "manual deploy" to build your app.

## To Fork this repository:
1. Navigate to GitHub project repository [P4djangoSWfinalBlog ](https://github.com/PeterSvk1/P4djangoSWfinalBlog)
2. Click on the "Fork" section in the right-hand corner.
3. Select an owner for the forked repository.
4. Click "Create fork" button.

## Cloning this Project
1. Visit [P4djangoSWfinalBlog ](https://github.com/PeterSvk1/P4djangoSWfinalBlog)
2. Click green button "<> Code", then "Clone or download" button and copy the URL provided.
3. Open a terminal and navigate to the directory whre you want to clone the project.
4. Type following command and paste url "git clone <url>"
5. Press Enter and the project will be cloned to you local machine.

# Credits
- Creating search bar https://www.youtube.com/watch?v=VL5ZNCjXEbw
- https://www.youtube.com/@AdrianTwarog (Creating the navbar)
- https://www.youtube.com/@Codemycom (Django walkthrough)
- Inspiration and some of the code of this project were taken from [Code Institute walkthrough project](https://github.com/Code-Institute-Solutions/Django3blog) and fellow students at Code Institue.

# Acknowledgements
- I want to thanks to Code Institute for learning material and support.
- Slack Code Institute community for all issues resolved and support.