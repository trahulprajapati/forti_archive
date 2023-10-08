
# Setup dev envirorment

### Setup docker env
Clone repo and follow below steps
```commandline
git clone https://github.com/trahulprajapati/forti_archive.git
cd project_home
```
#### Setup docker-compose env
```commandline
docker-compose build
docker-compose up -d
```
Check the status container is up and running
```commandline
docker-compose ps -a
```
#### Run migrations
```commandline
docker-compose run archive python archive_service/manage.py makemigration
docker-compose run archive python archive_service/manage.py migrate
```

#### Setup docker env
Uncomment last line in Dockerfile i.e RUN command and run below steps
```commandline
docker build --tag dkr:latest .
docker run --name dkr -d -p 8000:8000 dkr:latest
```
You can access application via:
```commandline
http://127.0.0.1:8000/
```


### Setup dev env normal (without docker)
Install python3.9.13
Install virtual env package
```commandline
pip install virtualenv
```
Create virtual out of your project home(adjacent to project root directory)
```commandline
python3.11 -m virtualenv archive_service_env
source ./archive_service_env/bin/activate
```
Change directory project home and install requirement.txt file
```commandline
pip install -r requirement.txt
```

#### Run server
uwsgi --ini uwsgi.ini

#### run migrations
```commandline
python archive_service/manage.py makemigrations
python archive_service/manage.py migrate
```
