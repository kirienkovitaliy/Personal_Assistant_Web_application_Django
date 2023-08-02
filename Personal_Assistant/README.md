# Personal Assistant Web Application

![logo_Readme.jpg](static%2Flogo_Readme.jpg)

https://personal-assistant-vekd.fly.dev/

Personal Assistant is a web application built on Django that provides users with a centralized platform to manage
contacts, notes, cloud storage, and daily news summaries. The application incorporates authentication mechanisms to
ensure user privacy and data security.

## Features

- _Contact Book_: Users can store contact details, including names, addresses, phone numbers, emails, and birthdays, in the
contact book.

- _Upcoming Birthdays_: The application displays a list of contacts whose birthdays are within a specified number of days
from the current date.

- _Contact Validation_: During the creation or editing of a contact, the application validates the phone number and email
input, notifying users of any incorrect entries.

- _Search Contacts_: Users can perform contact searches within the contact book.

- _Edit and Delete Contacts_: The application allows users to edit and delete contact records.

- _Notes_: Users can create and manage notes with text information.

- _Tagging Notes_: Users can add tags (keywords) to describe the subject of each note, facilitating search and sorting.

- _Search and Sort Notes_: The application enables users to search for notes using tags and sort them based on keywords.

- _Cloud Storage_: Users can upload files to the cloud storage service via the web interface.

- _File Categorization_: The application categorizes uploaded files into specific categories (e.g., images, documents,
videos) and offers users the ability to filter files by category.

- _Daily News Summaries_: Users can choose a topic of interest (e.g., finance, sports, politics, weather) and select
relevant news sources. The application collects information (headlines, currency exchange rates, sports event results,
etc.) from the selected sources and displays it on the results page.

## Getting Started

- Clone the project repository from
GitHub: https://github.com/kirienkovitaliy/Personal_Assistant_Web_application_Django.git

- Install PostgreSQL and create a database for the project.

- Set up a virtual environment and install the project dependencies using the following commands:

~~~
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
~~~

- Configure the database settings and other critical information as environment variables. Do not commit sensitive data to
the repository.

- Run database migrations to create necessary tables:

~~~
python manage.py migrate
~~~

- Create a superuser for the application to access the admin interface:

~~~
python manage.py createsuperuser
~~~

- Start the Django development server:

~~~
python manage.py runserver
~~~

- Access the application via the web browser at http://localhost:8000/ and log in using the superuser credentials.

## Project Structure

The project follows the standard Django directory structure. The key directories and files are:

- Personal_Assistant/: Contains the Django project configuration files (asgi.py, settings.py, urls.py, wsgi.py, etc.).
- app/: Contains the Django app with the main functionality of the Personal Assistant application.
- templates/: Stores HTML templates for rendering the views.
- static/: Holds static files such as CSS, JavaScript, and images.
- media/: Stores uploaded user files.
- manage.py: The Django project management script.
- docker-compose.yml: The Docker Compose configuration file for deploying the application.

## Contributors

- Vitalii Kiriienko - <u>kirienkovitaliy1989@gmail.com</u>
- Constantine Zagorodnyi - <u>constantine2903@gmail.com</u>
- Egor Shanin - <u>egorshanin21@gmail.com</u>
- Denys Kotsiuba - <u>denis.kotsiuba@gmail.com</u>

## License

This project is licensed under the <u>MIT License</u>.

## Contact

If you have any questions or feedback, please email us at <u>kirienkovitaliy1989@gmail.com</u>.
