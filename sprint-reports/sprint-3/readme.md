# Sprint-03 Written Report

## Team Number 05

- Stephan Tsang : Project Manager
- Randy Mai :  Developer
- Zayaan Haider : Jr. Developer
- Mohmedamir Arther : UI/UX Developer
- Mohammed Wasfi : IT Infrastructure & Operations

### UI/UX Artifacts

Users are able to create Posts or their book selling listing and are able to display it on the home page of the site. UI structure for forms as well as the paths structure for the site have also been fixed. Navigation bar now displays Sign up and Login when a user is not logged in and displays logout and profile when signed in.

Artifacts:
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/sprint-report-3-images/artifact.png "artifact")
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/sprint-report-3-images/artifact_2.png "artifact")


### Infrastructure

Place links and or screenshots to minimum of **5** artifacts here. Artifacts are defined as GitHub commit URL and Project Management Tool Kanban board images (Trello or JIRA).

### Developer

Fixed the issue where signing in automatically signs the user out and head straight to the admin login page. Assist UI/UX developer with code. Made the navigation bar change depending on whether or not the user signed in and also linked the post button so that main area change from product lift to post form.

Artifacts:
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/sprint-report-3-images/rmai_git_com.png "artifact")

### Junior Developer
![Commit History](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/sprint-report-3-images/zayaan_commit_history.png)
Installed PostgreSQL and started to play around with it. Updated install.sh script to install PostgreSQL. Added some tutorials for next developer to operate PostgreSQL as the migration from sqlite3 to PostgreSQL

PostgreSQL:![Command Line example](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/sprint-report-3-images/zayaan_commit_history.png)  

Place screen shot to image of a minimum of 5 GitHub issues/bugs reported and assigned

### Project Manager

  [Commit History](https://github.com/illinoistech-itm/2020-team05r/blob/stephan/diagrams/images/sprint-report-3-images/PM-4-stephan-commit-history.png)

1. Place images of the full User & Admin and/or anonymous story here with annotations of the functioning and the non-functioning portions as necessary (can reuse the artifact created by UI/UX)

  **New Landing Page**  
  ![PM1-homelanding-page](https://github.com/illinoistech-itm/2020-team05r/blob/stephan/diagrams/images/sprint-report-3-images/PM-1-landing-home-page.png "artifact1")  
  **New Posts Page**  
  ![PM2-POST-page](https://github.com/illinoistech-itm/2020-team05r/blob/stephan/diagrams/images/sprint-report-3-images/PM-2-POST-PAGE.png "artifact2")  
  **New Register Layout**  
  ![PM-3-newRegisterForm](https://github.com/illinoistech-itm/2020-team05r/blob/stephan/diagrams/images/sprint-report-3-images/PM-3-newRegisterForm.png "artifact3")

2. Include a file  ```install.md``` in the root of the team GitHub Repo detailing all instructions to build and run the functioning parts of your site  

  * Link: https://github.com/illinoistech-itm/2020-team05r/tree/master/installation

3. Verify that all defined minimum goals were met and explain goals that were reached beyond what was defined.  Also explain reasons behind goals that were not met.
  * **UI/UX:** We updated the design of our site. Layout looks more modern, user-friendly, and easier to understand.
  * **Infrastructure:**  

  * **Developers:**
    * Users are now able to create posts.
    * Users logged in can create posts.
    * Users __not__ logged in __cannot__ create posts.
    * The devs reformatted the structure of the site.  
      * In sprint 2, the first thing you'd see was the login page.   
      * In sprint 3, the first thing users will see is the unauthenticated homepage.

## Atomic Goals for Sprint-04

  - UI/UX Goals
    1. Automatically set the seller's username when creating posts instead of having a drop down of all usernames.  
    2. Provide posts creation for only authenticated users. In other words, Different UI for Unauthenticated (non-logged in) Users.
    3. Further improve the UI (color, font style and size, etc.)

  - IT Infrastructure Goals



  - Developer Goals
    1. Continue to assist UI/UX developer.
    2. Work on PostgreSQL with IT infrastructure.

  - Junior Developer Goals
    1. Create compatible database in PostgreSQL
    2. Migrate data from sql lite to PostgreSQL
    3. Make the master-slave connection from PostgreSQL(research into how to do this)
