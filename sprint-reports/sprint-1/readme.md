# Sprint-01 Report

## Team Number 2020-5r

- Stephan Tsang : stsang@hawk.iit.edu | IT Operations
- Randy Mai : rmai@hawk.iit.edu | UI/UX developer
- Zayaan Haider : zhaider1@hawk.iit.edu | Project Manager
- Mohmedamir Arther : marther@hawk.iit.edu | Jr. Developer/ UI/UX Developer
- Mohammed Wasfi : mwasfi@hawk.iit.edu | Developer

### Atomic Goals for Sprint-01

- Choose Project
- Research DB
- Create Skeleton Pages
- Create User Story
- Decide on Security Options
- Create Kanban Board

## UI/UX Report - Randy Mai

For the design choice, it was a combination of OfferUp and Craigslist. We took what we believe was the best part of their UX/UI. OfferUps overall layout with Craigslist detailed list items. This way users get to see everything but without the mess like Craigslist and with more info per post unlike OfferUp.

The web app will
- be user and mobile friendly. 
- have users signup or signin though signing in isn’t nessecary to use web application. 
- users will be able to contact seller via the web application. 
- admin will have a very similar layout as the users. They will be able to delete and edit post at will.
- be integrated with python. 

## Developer Report - Mohammed Wasfi

We have decided to use Python as our main language for this project as it one of the most rapid growing langauges at the moment. The framework that we will be using is Django as it is best for python programming and it offers a lot of templates, models, authentican system, and many more other features that will be very helpful in reaching our goals for this project. Another reason is that we haven't used python to build web applications before so we thought it would be interesting to learn that as we go and add it to our skills to use later on in the future. Companies such as Facebook, Netflix, and Spotify use Python as one of their top programming languages for their applications.

## IT Infrastructure Report - Stephen Tsang

This sprint was fairly relaxed. Our big focus was laying down the groundwork / foundation of our project. To do so:

- We set up slack channels and got all the team members accustomed to the tool.
  - Basic channels were set up. (capstone-itm, general, links-resources, etc)
  - Github integration was set up in `general`. (Lots of pings so mute channel if it gets overbearing)
  - Trello integration was also set up, but not sure of its functionality within the Slackspace yet.
- We got all the members accustomed to the pushing and pulling workflow/process on the team-repo.
- Created a very basic prototype of our potential schema for the database. Need to flesh that out some more.
- Started research on different cloud providers. We're likely to use AWS for our provider. The next step would be figuring out how
  that is going to look like in our workflow / architecture of the platform.

## Developer and Security Assumptions - Mohmedamir Arther

Development - Creating a base structure of the html is very important to keep the code DRY (Don't Repeat Yourself) which is why I had created a base html page where the opening of the html head (css scripts), head, body (navigation bar), and footer (JavaScript/JQuery) can stay in one place. And for the rest of the pages they can use the base file to pull the structure that normally everyfile would have without creating a redundancy.

Security Assumptions - We mainly focused our security to be on the user and data autentication of the web app. We belive that, if we can have a strong user creation/login authentication and verification system in place along with data input validation we can secure our site and mainly the Database from invalid data. Also to protect ourselves from databreaches as such from SQL injections, Cross-site Scripting (XSS), brute force attacks, etc. Some examples include hashing passwords/key data, storing and retrieve data from a database, a set number of attempts for login, 2 Factor Authentication (2FA), Read/write permissions for different types of users (admin, customer, seller), use Cloud Web Firewall (CloudFlare or AWS WAF) to protect the site from attackers to eavesdrop traffic, display false information, or to simply slow or take down the website using DDoS.

## User Story

Sign Up Page
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/fluidui/signup_page.png "sign-up.png")

Login Page
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/fluidui/login_page.png "login.png")

Main/Home Page
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/fluidui/main_page.png "main")

Create Page
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/fluidui/create_page.png "Create-ui")

Messaging Popup  
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/fluidui/messaging_popup.png "msg-ui")

My Posts Page
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/fluidui/mypost_page.png "my-listings")

Product Page
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/fluidui/product_page.png "product-listing-ui")

## Admin Story

The admin's role here is to overlook all the users and posts they make. For instance, the admin user will have the ability or permissions above any user. The admin will be able to create, read, update, and delete any information of a user/s or the user itself along with any posts they created for re-selling books. This can keep the web app clear from unwanted listings (such as furnitures, electronics, etc) and troublesome users (users who aren't verified IIT students/faculty). 

## Atomic Goals for Sprint-02

1. Create Admin Story
2. Create database and 15 test users
3. Implement security Operations
4. Fill Skeletal Pages
5. Implement Login Authorization
6. Draw out the entire infrastructure of our platform.
   - Frontend, backend, data storage system
   - Reactjs(tentative), Django (+ it's REST) framework, MySQL, S3 buckets, etc.
   - Discuss security and work out the details.
   - Discuss monitoring and metrics. (What sort of things do we want to track? Clicks? Visitors? Site traffic?)
