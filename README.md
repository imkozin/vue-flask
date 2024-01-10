# User State Manager

## Table of Contents
- [Description](#desciption)
- [Technologies Used](#technologies-Used)
- [Features](#features)
- [Configuration](#configuration)
- [Usage](#usage)
- [Possible Improvements](#possible-improvements)
- [Contribute](#contribute)

## Description

User State Managere is a full-stack web application built with Flask for the backend, Vue 2 for the frontend, and styled using BootstrapVue. The application supports two types of user roles: Admin and Standard User. Admins have the ability to edit user details and register new users, while Standard Users can register and manage their profile, including changing the device quantity.

## Technologies Used

- **Backend:** 
  - **Flask:** A Python web framework for building the backend.
  - **ElephantSQL:** Online database used for storing user information.
- **Frontend:** 
  - **Vue 2:** JavaScript framework for building user interfaces.
  - **BootstrapVue:** Bootstrap components for Vue.js for easy and responsive styling.

## Features

- **User Management:** Manage user accounts, ensuring that only authorized individuals have access to your organization's data.
- **User Authentication:** Admin and Standard User roles with different permissions.
- **User Registration:** Standard Users can register with their details.
- **Admin Dashboard:** Admins can manage user details, including editing and registering new users.
- **Profile Management:** Users can manage their profile information and change the device quantity.
- **User Removal:** Remove registered users from website.


## Configuration
### Backend and API
   The backend of the Flask-Vue-App serves as the server-side component responsible for handling HTTP requests, managing the PostgreSQL database, and serving data to the frontend. This section provides details on how to connect to the database, the technologies used, and an overview of the API endpoints.
   - ### PostgreSQL Database
   The backend of this project uses a PostgreSQL relational database to store and manage user and organization data. PostgreSQL is a powerful, open-source relational database system known for its reliability and performance. You can find the database connection information in the app.py file.
   - ### Database Configuration
   To connect to the PostgreSQL database, update the database connection details in the Flask application configuration. The database connection is configured in the app.py file. The application uses the SQLAlchemy library to interact with the database. Here's an example of the database configuration:

    ```
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    import os
    # Load environment variables from .env file
    load_dotenv()

    # create the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # this variable, db, will be used for all SQLAlchemy commands
    db = SQLAlchemy(app)
    ```

Replace DATABASE_URL with your variable name from .env file os.environ.get('*DATABASE_URL*') or you can give a direct link with your PostgreSQL connection details, including the username, password, host, port, and database name e.g. 

    ```
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/your-database-name'
    ``` 
    
### Frontend
The frontend of the Flask-Vue-App is built using the popular JavaScript library Vue. Vue allows for the development of dynamic and responsive user interfaces. This section provides an overview of the frontend architecture, the technologies used, and how to run the frontend application.
   - ### Frontend Architecture
   The frontend of this project follows a component-based architecture, where the user interface is divided into modular components that can be reused and combined to build complex views. Here are some key components used in the frontend:
   - **Navbar:** The navigation bar component displayed at the top of the application. It provides navigation links and user authentication options.
   - **Home:** The start page where users can sign in into existing account using their credentials.
   - **Login and Register:** The login and registration page where users can sign in or create new accounts.
   - **Profile Page:** The profile page which displays different information depending on user role. A Standard users can change their device quantity information and admins can edit user personal information, create or delete users accounts.
   - **PageNotFound:** This page ensures a smooth user experience. If an unauthenticated user attempts to access pages that are intended only for logged-in users, they will be automatically redirected to our "PageNotFound" page.

## Getting Started
### Prerequisites
Before running the project, make sure you have the following prerequisites:

- Python (>=3.7)
- Node.js (>=12)
- npm (Node Package Manager)
- Flask
- Vue

### Installation
To get started, follow these steps:

- Clone the repository:
```
git clone https://github.com/imkozin/vue-flask.git
```
- Navigate to the project directory:
   - cd backend
   - Running the Backend
   - Create a Virtual Environment (Optional): It's recommended to create a virtual environment to isolate your project dependencies. You can do this using the venv module that comes with Python. Open your terminal and run: python -m venv venv

- Install Python dependencies:
```
pip install -r requirements.txt
```

Once the dependencies are installed, you can start the development server by running:
```
python3 app.py
```

- Running the Frontend
To run the frontend of the Flask-Vue-App locally, follow these steps:
   - Make sure you have Node.js installed on your system.
   - Navigate to the frontend directory in your project folder using the terminal.
   - Install the required dependencies by running the following command:
    ```
    npm install
    ```
   - Once the dependencies are installed, you can start the development server by running:
   ```
   npm run serve
   ```
This will launch the development server, and your Vue application will be available in your web browser at http://localhost:8080.

## Usage
- Register a new user as a Standard User.
- Log in as an Admin to access the Admin Dashboard.
- Edit user details or register new users as an Admin.
- Manage your profile and change the device quantity as a Standard User.

## Possible improvements

1. **Structure existing users into departments within organizations:** This improvement can help organize users even further by creating a hierarchical structure within organizations. It could be particularly useful for larger organizations with multiple departments or teams.
2. **Extend functionality by adding a position in the company's hierarchy:** Adding positions or roles for users within organizations can offer more granularity in managing responsibilities and access levels. It allows for better role-based access control.
3. **Add more roles like e.g. head of department:** Introducing different roles, such as heads of departments, can help delegate authority and streamline decision-making processes. It can also enhance the overall management of the organization.
4. **Improve the registration system:** Enhancements like a "Forgot Password" feature and the use of cookies for session management can improve user experience and security. These additions can simplify account recovery and user authentication.

## Contribute
We welcome contributions from the community! Feel free to report issues, suggest enhancements, or submit pull requests to help us improve this application.




