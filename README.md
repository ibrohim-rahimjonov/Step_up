Online School Platform

An online learning platform built with Django for managing users, groups, teachers, and students — allowing enrollments and course management.

1:**Clone the repository**
git clone https://github.com/YOUR_USERNAME/online_school.git
cd online_school

2.**Create a virtual environment**
pipenv install
pipenv shell

3.**Create an .env file**
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/your_db_name

4.** Apply migration**
python manage.py makemigrations
python manage.py migrate

5.** Run the development server**     
python manage.py runserver

