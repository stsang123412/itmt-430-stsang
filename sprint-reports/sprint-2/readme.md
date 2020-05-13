# Sprint-02 Report

## Team Number 5 -- Goals for Sprint 2

- Stephan Tsang : IT Infrastructure & Operations
- Randy Mai : Project Manager & UI/UX Developer
- Zayaan Haider : IT Infrastructure & Operations
- Mohmedamir Arther : Developer Role 
- Mohammed Wasfi : Jr Developer Role

## Project Manager Report

## UI/UX Report

Main page fully developed. Had to implement several features that would make the user experience better on a smaller scale. Unlike the other two websites used to design this webpage, Offerup and Craigslist, the user experience on a smaller screen seemed a bit lacking. This is probably due to the fact that they might want user to use the app if not on a computer. Our web app has now a collapsable filter and footer when the screen is at a smaller width.

Feed:
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/newsfeed.png "Feed")

Closed footer:
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/html-features/footer_closed.png "closed footer")

Toggled footer:
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/html-features/footer_toggled.png "toggled footer")

Filter option on a smaller screen:
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/html-features/small_vw_filter.png "small screen filter")

Filter option on a large screen:
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/html-features/large_vw_filter.png "large screen filter")


## IT Infrastructure Report - Stephen and Zayaan 
 
**Completed**
* Figure out necessary dependencies we'll need for our project  
   * Create shell-script to automate the installation of those dependencies
   * Mapping out the system architecture | Figuring out which programs to use
   * Servers, Database connection, Passing information back and forth  
   * Created Database Schema
   * Get everyone on the same page for running servers and database

**In-Progress:**  
* Do research on PostgresSQL 
  * Need to figure out syntax + how to write the database file 
  * Current we're using a sqlite file for our test users. We plan on migrating to Postgres a little later on.

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/db_schema.png "db schema")


**Artifacts:**
Created an install folder directory which will contain instructions to install the application on a local env.  
```
sudo apt-get update -y  

sudo apt-get install python3.6 -y
sudo apt-get install python3-pip -y
pip3 install Django
pip3 install pillow
pip3 install django-crispy-forms
```  
Currently our application uses python 3.6, pip3, Django, Pillow, and django's crispy forms. More TBD.  

**Application Architecture (WiP)**  
Made a prototype of our application architecture. Will have to write out the details and add features + other parts as we go.
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/stephan/diagrams/images/sybook-app-architecture.jpg "app-arch.jpg")

## Developer Report

  - Goals for this sprint
    1. Create database schema
    2. Populated database with Users and their Posts
    3. Create a User registration page
    4. Create Admin portal for admin role users to manipulate users and their posts to either create, read, update, and/or delete.

  All the goals for this sprint were met. Starting with creating the database schema on sql-lite in the Django framework. The Schema currently includes 2 tables: Users and Posts. Currently User and Post creation, update, and delete is only available through the admin portal. Users are also able to sign up and create their account using the register form. 

  Admin Portal Login:
  ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/admin_login.png "admin-login")

  Admin Portal:
  ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/admin_portal.png "admin-portal")

  Admin Portal Users:
  ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/users.png "users")

  Update user:
  ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/user_update.png "user-update")

  Admin Portal Posts:
  ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/posts.png "posts")

  Posts Creation:
  ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/posts_creation.png "posts-creation")

  User Registeration Form:
  ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/user_signup.png "user-signup")

## Junior Developer and Security Assumptions

Created the login page and implemented login authenticantion so that only created users are able to view the feed and also implememented a logout to allow users to go back to login page incase they like to switch accounts.

Login Page:
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/login.png "log in")


## Atomic Goals for Sprint-03

  - UI/UX Goals
    1. Continue editing to have better a UI/UX
    2. Assist, if needed, developers with making their pages have better UX
    3. Create product selected page based on the developer's form.

  - IT Infrastructure Goals
    1. Begin using Postgres as our main DB engine. 
    2. If one user has admin access on their AWS account (the one who created the RDS instances + EC2 instances) then how does deployment onto AWS's servers work when we're in a team enviroment? 
    3. Related to #2, we should look toward creating EC2 server instances for hosting our application, S3 buckets for storing user / product images, RDS instances for hosting our Postgres DB. 
    4. Automate the creation of our infrastructure
    5. Include chat function into the schema

  - Developer Goals
    1. Users to be able to create Posts from their accounts.
    2. Different UI for Authenticated Users
    3. Different UI for Unauthenticated Users 
    4. User Profile page for user to update their personal information
    5. Better UI page i.e better page structures, text fonts size and styles, color scheme, etc. 

  - Junior Developer and Security Assumptions
    1. Display differernent views for different users based on the permission they have and who they are signed in as. 
    2. Continue assisting the Developer with the Developer goals.
