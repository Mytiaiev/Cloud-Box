# CLOUD BOX
This application is supposed upload and download files for users after registration

# How to run a project
Run `sudo docker-compose up --build`
Run migrations by `sudo docker exec -it cloud python manage.py migrate`
Run to create admin user `docker exec -it cloud python manage.py createsuperuser` 
Open http://localhost:8000/admin/ in browser and auth with user created
Connect to DB 'sudo docker-compose exec db psql --username=admin --dbname=cloud'