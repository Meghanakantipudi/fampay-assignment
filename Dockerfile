FROM centos
RUN yum install -y python38 &&\
yum install -y python3-pip &&\
pip3 install django &&\
yum install -y vim &&\
yum install wget &&\
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm && rpm -ivh mysql-community-release-el7-5.noarch.rpm &&\
yum install -y mysql-server &&\
pip3 install google-api-python-client

