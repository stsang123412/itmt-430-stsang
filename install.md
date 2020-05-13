# Instructions
## Using Vagrant and Ubuntu server

0. Have vagrant installed and run 
```
vagrant plugin install vagrant-vbguest
```
1. Run the following command in the terminal and press enter three times. This will accept the default save location and not create a password.

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

2. Navigate into the .ssh directory in the root directory and copy and paste ssh key from the id_rsa.pub file into Github.

3. Back to the terminal, in the project root directory, run the command:
    - The Vagrantfile has the script to install all libraries and dependencies needed and automatically clone the Github repo.

```
vagrant up
```

4. Then run:

```
vagrant ssh
```

5. The terminal should now be logged into the ubuntu server. Navigate to SyibookExchange directory by typing in the command:

```
cd code/Syitech/SyibookExchange/
```
6. Run the following commands to convert sqlite3 to psql

```
python3 manage.py shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
quit()
```

7. Run the command to transfer db to psql

```
python3 manage.py loaddata data.json
```

8. Run the command to start the server
    
```
python3 manage.py runserver 192.168.33.110:8000
```

9. Head back to the local machine, start a broswer, and run the IP address 192.168.33.110:8000
    
## Without vagrant
1. Run the `~/installation/install.sh` file
    -   This will install all libraries and dependecies used in this project
2. Navigate to SyibookExchange directory by typing in the command:
```
cd ~/2020-team05r/code/Syitech/SyibookExchange/
```
3. Run the following commands to migrate Django's stock database to psql
```
python3 manage.py migrate
python3 manage.py shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
quit()
python3 manage.py loaddata data.json
```
4. To start the server on `localhost:8000` or `127.0.0.1:8000`, run
```
python3 manage.py runserver
```
---
## Quick troubleshooting solutions
### With Vagrant
- During the vagrant up, if there is a permission issue with the git cloning process, make sure that the ssh key from the `~/.ssh/id_rsa.pub` is in the github repo setting -> Deploy keys. And also, make sure that the id_rsa file (not the .pub file) is the private key that came with the .pub when it was created. If unsure just run the first two steps from the "Using vagrant" instruction again.

### Without Vagrant
- Make sure the Postgres app is installed on the computer. During the set up, the installer will ask which port to run psql on. The Default is `5432`, but for any reason that you must change this, head to the `setting.py` files in the `~/2020-team05r/code/syitech/SyibookExchange/SyibookExchange/` directory. In that file, add the port number you are using for psql within the single quotes under DATABASES. Then in the terminal/Powershell create a mydb database. Afterward do steps 2 - 4 from the "Without Vagrant" instructions.



