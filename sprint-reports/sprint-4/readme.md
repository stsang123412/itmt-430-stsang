# Sprint-04 Report

## Team Number 05

- Stephan Tsang : Developer
- Randy Mai :  Jr. Developer
- Zayaan Haider : UI/UX Developer
- Mohmedamir Arther : IT Infrastructure & Operations
- Mohammed Wasfi : Project Manager

### UI/UX Artifacts

- Added correct images and post descriptions to posts
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/Post-descriptions.png)
- Added profile picture base code(not completed yet, but base code is in place)
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/git_commit_1.png)
- List all tasks that you have completed along with the artifacts proving they are complete (GitHub commit URL and Project Management artifact screenshot)
- There was no user story or admin story in our sprint 3 report, so here are the new stories
- User story
  - Unlogged-in home page ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/user_story_1.png)
  - Login Page ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/user_story_2.png)
  - Login page ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/user_story_3.png)
  - Creating a post as a user named alex ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/user_story_4.png)

- Admin story
  - administration home page ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/admin_story_1.png)
  - Users list ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/admin_story_2.png)
  - Editing user information, note the hashed password ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/admin_story_3.png)
  - Posts list ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/admin_story_4.png)
  - Post editing page, note image selection ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/admin_story_5.png)


### Infrastructure

**Tasks completed since sprint 3:**

- Build and run discrete server to run the app on a private ip address
- Write instructions for automating, creating, and running the discrete server in the install.md file
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/github_commit_4.png "github_commit_4")
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/trello_artifact.png "trello")
- Diagram of the discrete server with the private IP address
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/diagram_tcp.png "diagram_tcp")

### Developer

* Configured the Vagrantfile so that access to the server can be done through the vagrant env:  
https://github.com/illinoistech-itm/2020-team05r/commit/f24756f64bc380b5a2da362adc8248f50dbb8b8b
```
Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 3000, host: 3000
```
* Updated the installation folder readme.md with instructions about the vagrantfile and how to access the server via vagrant:  
https://github.com/illinoistech-itm/2020-team05r/commit/f9e7b68e32d11aef4c99aef352f88632e48601ce

* Updated ``/installation/install-script.sh ``  
https://github.com/illinoistech-itm/2020-team05r/commit/c2335579392c1fd40d104b5943dcef4ac80b2ac6  
![picture1-steve](https://github.com/illinoistech-itm/2020-team05r/blob/stephan2/diagrams/images/stsang-sprint4/1-install.shupdate.png "picture1-dev-artifact")

* .gitignore was created to ignore ``.pyc`` cache files  
https://github.com/illinoistech-itm/2020-team05r/blob/master/.gitignore
```
# gitignore these files

# links
# https://www.atlassian.com/git/tutorials/saving-changes/gitignore#ignoring-a-previously-committed
# https://help.github.com/en/github/using-git/ignoring-files
# https://git-scm.com/docs/gitignore

# Pycache + .pyc files
__pycache__/
*.pyc
*.DS_Store
```
### Junior Developer

Assisted everyone in their roles.

- Figured out a way to migrate sqlite3 to psql.

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint4/django_to_psql.png "artifact 1 for Jr. Dev")
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint4/pip_install_psycopg2_binary.png "artifact 2 for Jr. Dev")

- Created 15 test users and 15 test posts

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint4/post.png "artifact 3 for Jr. Dev")
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint4/user.png "artifact 4 for Jr. Dev")

- Due to lack of time it was required to make a temporary fix to the CSS (when runing web server using Ubuntu) by removing the link and hard code it in the HTML. Because of this the logo for the website is missing.

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint4/emergency_fix.png "artifact 5 for Jr. Dev")



### Project Manager

![pm text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/stsang-sprint4/2-sprint4-projManager.png "PM-pic1")

* Organized Meetings with all the team members to discuss how to proceed with the meeting:

![pm text](https://github.com/illinoistech-itm/2020-team05r/blob/stephan2/diagrams/images/stsang-sprint4/3-slack-discussions.png "pm-3")
