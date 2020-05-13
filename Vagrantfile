# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  
  # create ssh key under the name ubuntu
  config.ssh.forward_agent = true

  config.vm.box = "ubuntu/bionic64"


  config.vm.network "private_network", ip: "192.168.33.110"

  
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  config.vm.provision "file", source: "~/.ssh/id_rsa", destination: "~/.ssh/id_rsa_github_deploy_key"
  config.vm.provision "file", source: "./config", destination: "~/config"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get -y update
    sudo apt-get -y install git
    sudo apt-get -y install python3.6 
    sudo apt-get -y install python3-pip 
    sudo apt-get -y install nginx
    sudo apt-get -y install postgresql postgresql-contrib
    sudo apt-get -y install libpq-dev python3-dev
    pip3 install Django
    pip3 install pillow
    pip3 install django-crispy-forms
    pip3 install psycopg2-binary
    pip3 install django-currentuser
    pip3 install django-extensions

    mkdir -p /root/.ssh
    sudo chmod 600 /home/vagrant/.ssh/id_rsa_github_deploy_key
    cp -v /home/vagrant/config /home/vagrant/.ssh/
    cp -v /home/vagrant/config /root/.ssh/

    git clone git@github.com:illinoistech-itm/2020-team05r.git
    sudo chmod 777 2020-team05r/
    sudo chmod 777 2020-team05r/code/Syitech/SyibookExchange/media/
    sudo chmod 777 2020-team05r/code/Syitech/SyibookExchange/media/profile_pics/
    sudo chmod 777 2020-team05r/code/Syitech/SyibookExchange/media/images/

    # create psql server/database.
    sudo -u postgres psql postgres -c "CREATE DATABASE mydb"
    sudo -u postgres psql postgres -c "CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypass'"
    sudo -u postgres psql postgres -c "ALTER ROLE myuser SET client_encoding TO 'utf-8'"
    sudo -u postgres psql postgres -c "ALTER ROLE myuser SET default_transaction_isolation TO 'read committed'"
    sudo -u postgres psql postgres -c "ALTER ROLE myuser SET timezone TO 'UTC'"
    sudo -u postgres psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser"

    python3 2020-team05r/code/Syitech/SyibookExchange/manage.py migrate

    # python3 2020-team05r/code/Syitech/SyibookExchange/manage.py runscript sql_to_psql


    #python3 2020-team05r/code/Syitech/SyibookExchange/manage.py loaddata 2020-team05r/code/Syitech/SyibookExchange/data.json
    
    # Immediately start webserver when everything is done.
    # python3 2020-team05r/code/Syitech/SyibookExchange/manage.py runserver 192.168.33.110:8000

  SHELL
end
