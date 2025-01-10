### Early Child API
The Early Child API is designed to support the educational development of young children by providing age-appropriate resources. This platform offers curated content for parents, teachers, and caregivers to enhance children's language development, math skills, creativity, and STEM education.

## Features
User Management: Manage user profiles with roles such as teacher, parent, or caregiver.
Child Profiles: Create and manage child profiles, including personal details like name and age.
Educational Modules:
Language Development (Phonetics Module)
Math Learning (Math Module)
STEM Education (STEM Module)
Resource Management: Access and manage resources such as videos, articles, and interactive games.

## Technologies Used
Backend Framework: Django and Django REST Framework
Database: SQLite (default, can be configured to PostgreSQL, MySQL, etc.)
Language: Python
Other Tools: Git, Virtual Environment, and Pip


# Prerequisites
Before setting up the project, ensure you have the following installed:

Python 3.9+: Download and install Python
Git: Download and install Git
Virtual Environment (venv): Included with Python installations.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/agathaikemeh/early_child_api.git

## Navigate into the project directory:
cd early_child_api

# Set up a virtual enviroment
python -m venv venv

# Activate the virtual enviroment
venv\Scripts\activate

## Run Migrations
python manage.py migrate

## Start the development server
python manage.py runserver


### Usage
Endpoints
User Management:

GET /users/: Retrieve user details.
POST /users/: Create a new user.
PUT /users/<id>/: Update user details.
Child Profiles:

GET /child_profiles/: Retrieve all child profiles.
POST /child_profiles/: Create a child profile.
PUT /child_profiles/<id>/: Update a child profile.
Modules & Resources:

GET /modules/: Retrieve all modules.
POST /resources/: Add resources to modules.
Refer to the full API documentation for detailed endpoint usage.

## Testing
Run Unit Tests
Execute all tests:

python manage.py test
## Commit and Push to GitHub
Finally, commit all the changes and push them to your GitHub repository.
git add .

# Commit Changes
git commit -m "Initial Django setup with virtual environment"

# push to github
git push origin master

## Contributing
I welcome contributions! To contribute:

Fork the repository.
Create a new branch for your feature:

git checkout -b feature-name
Commit your changes and push them to your forked repository.
Create a pull request to the main repository.

## Contact
For questions or support, reach out to:

Name: Ikemeh Agatha
Email: ikemehagatha@gmial.com
GitHub: https://github.com/agathaikemeh