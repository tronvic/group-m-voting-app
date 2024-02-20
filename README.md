# VOTING APPLICATION GROUP M

## Installing and Running The Project
1. clone/download the code
2. Change directory into the folder `cd group-m-voting-app `
3. Create a virtual environment  `python -m venv env`
4. Start a Virtual Environment In Windows `env\Scripts\activate `
5. Install the requirements `pip install -r requirements.txt`
6. Make Migrations / Instanciate our database `python manage.py makemigrations`
7. Run the migrations to create the tables `python manage.py migrate`
8. Create a Super User/Admin `python manage.py createsuperuser` then follow the commands
9. Start Server  `python manage.py runserver 8090`


## How The Project Works
A user can be registered inside the Admin Page .
  - on your browser open localhsost:8090/admin
  - Under Users click add a user then fill in your details

A candidate can be added using the same procedure but this time inside the Admin Panel Click `Add Candidate `

Now open localhsost:8090 to login then you can vote 
