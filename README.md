# Project-Planner-Tool
Welcome to the Project Planne Tool, a powerful suite of APIs built using Django Rest Framework.


## Introduction
The Project Planner Tool is a web application built using Django and the Django REST framework. It serves as a comprehensive tool for managing team projects, user accounts, teams, and project boards along with their tasks. The tool provides a RESTful API for seamless integration and efficient project management.


## Features
1. User Management: Create, update, and delete user accounts.

2. Team Management: Form teams, assign administrators, and manage team members.

3. Project Board: Create project boards with tasks, assign tasks to team members, and track task status.
   
4. RESTful API: Provides endpoints for all features, enabling easy integration and automation.


## API Reference
The API endpoints are as follows:

1. Users
GET /users/: Retrieve a list of all users.
GET /users/<int:pk>/: Retrieve details of a specific user.

2. Teams
GET /teams/: Retrieve a list of all teams.
GET /teams/<int:pk>/: Retrieve details of a specific team.

3. ProjectBoard 
GET /project/: Retrieve a list of all project boards.
GET /project/<int:pk>/: Retrieve details of a specific project board.
For more detailed information, refer to the API Documentation.


## Usage
User Management: Use the API to create, update, and delete user accounts. Authenticate users for secure access.

Team Management: Form teams, set administrators, and add team members. Manage team-related operations through API calls.

Project Boards: Create project boards, add tasks, assign tasks to team members, and track task progress.

API Integration: Integrate the provided RESTful API with external tools, applications, or scripts for seamless project management.


## Installation

Install project dependencies mentioned in requirements.txt:
pip install -r requirements.txt

Start the development server using the following command:
python manage.py runserver

Open the URL: http://127.0.0.1:8000

1. To access admin : http://127.0.0.1:8000/admin
2. To access user : http://127.0.0.1:8000/user/
3. To access Team : http://127.0.0.1:8000/Team/
4. To access Project : http://127.0.0.1:8000/Project/

