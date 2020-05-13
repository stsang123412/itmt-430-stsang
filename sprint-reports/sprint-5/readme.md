# Sprint-05 Written Report

## Team Number 05

Mohmedamir Arther - Project Manager  
Mohammed Wasfi - UI/UX Developer  
Randy Mai - IT Operations/Infrastructure  
Stephan Tsang - Jr Developer  
Zayaan Haider - Developer  

### UI/UX Artifacts

- Improved UI for the pages

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/frontpage.jpg "Front Page UI")

- Corrected UI for the navigation bar

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/navbar.jpg "Front Page UI")

- Removed name from post form so now it automatically assigns it to logged in user

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/removename.jpg "Name Removal")

- Inlcuded a placeholder for content info

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/placeholder.jpg "Placeholder")

### Infrastructure

- Improve the autmoation process by editing the Vagrantfile, so that when the user `vagrant up` several things happen automatically
  1. Install all libraries and dependencies used in the project.
  2. Clone team repo into the ubuntu server
     - Assuming id_rsa file is in the `~/.ssh` diectory and that the id_rsa.pub key is set up in github setting
     - ![artifact 1](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint5/git_in_ubuntu.png "Cloned team repo in ubuntu")
  3. Create and migrate over to Postgres database
     - ![artifact 2](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint5/psql_db.png "psql db")
  4. Dump the data from db.sqlite3 to a JSON file which will be loaded into the Postgres database.
     - Ran the command `python manage.py dumpdata > data.json` before hand to create data.json file. So this part will not be included in the automation process.
     - ![artifact 3](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint5/loaddata.png "Load previous db data to psql")
- Sort newsfeed from most recent post to oldest post
  - ![artifact 4](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint5/date_time_field.png "Added date time to sql")
  - ![artifact 5](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/rmai_sprint5/post_order.png "Changed order of post from recent to oldest")

### Developer

- search bar sort created ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/sbar1.png)
- actual search code ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/sbarcode.png)
- project management artifact ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/trelo1.png)

- this is Randy's automation code in the vagrantfile that automates the entire environment and clones the repo in to the dev environment ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/scripts2.png)
  ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/scripts4.png)

- this is our original install script that installed all of the dependencies ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/scripts1.png)

-this is the updated version of the install script that can run with the new automation ![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/zhaider_sprint4/scripts4.png)

- a normal user of the site can only see other posts, and create and edit their own posts.

### Junior Developer
![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/stephan3/diagrams/images/sprint5-stephan/sp5-A.png "sp5-A")

Code below should be used to import the data from the data.json file
```
python3 manage.py shell
  from django.contrib.contenttypes.models import ContentType
  ContentType.objects.all().delete()
  quit()
python3 manage.py loaddata data.json
```
- Show from the code the firewall ports opened on each discrete vm
```
ALLOWED_HOSTS = ['192.168.33.10', 'localhost', '127.0.0.1','192.168.33.110']
```

### Project Manager

- We assume that the user will have pulled our project from github and has access to the github repo before following the install.md file

- Assigned tasks to everyone:

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/trello_sp5.png "trello artifact sp5")
- Made plans to meet for discussion, planning, resolution to problems, etc: 

- Made plans to meet for discussion, planning, resolution to problems, etc:

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/slack_sp5.png "slack artifact sp5")

![alt text](https://github.com/illinoistech-itm/2020-team05r/blob/master/diagrams/images/slack_sp6.png "slack artifact sp6")
