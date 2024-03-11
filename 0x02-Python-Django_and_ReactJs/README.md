# Backend(django and Frontend(React) connection project

## Introduction
Welcome, developers!

This project is all about how to connect a Django backend framework to a React frontend library. The goal is to create a simple data entry application in the backend and retrieve data in the frontend using the Axios library.

## Why React with Django?
- Popularity: Both React and Django are widely used and supported frameworks in their respective domains.
- Optimization: React's Single Page Application (SPA) optimization complements Django's powerful features.
- Community Support: Both frameworks boast large communities, providing immediate assistance whenever needed.

## Benefits of Separation
By handling both Django and React separately, we achieve:

- Cleaner Interface: Clear separation between front-end and back-end logic and functions.
- Independent Deployment: Easy deployment of either part without affecting the other.
- Team Independence: Separate teams can work on front-end and back-end without dependencies.
- Scalability: Facilitates scalability for multiple client applications (web, mobile) consuming the same API.

## Backend Development
The work is divided into two parts:

`Back-end:` Creating APIs using Django-Rest.
`Front-end:` Interacting with the API using React JS.

#### Setting Up Django
Ensure Django is installed.
Create a virtual environment using pipenv.
Install required packages:
    - `pipenv install djangorestframework`
    - `pipenv install django-cors-headers`

#### Backend Components
* models.py: Define database models for employee and department.
* serializer.py: Convert complex data to native Python types for JSON rendering.
* views.py: Implement GET and POST methods for retrieving and saving data.
* urls.py: Define API endpoints.

#### Configuration Changes
* Update settings.py:
    Add rest_framework, corsheaders to INSTALLED_APPS.
    Include corsheaders.middleware.CorsMiddleware in MIDDLEWARE.
    Configure REST_FRAMEWORK permissions.
    Set CORS_ORIGIN_ALLOW_ALL = True for CORS handling.

#### Running Django
Make migrations: `python manage.py makemigrations`
Apply migrations: `python manage.py migrate`
Create superuser: `python manage.py createsuperuser`
Run server: `python manage.py runserver`


## Frontend Development
The process of setting up the frontend:

Create a React app: `npx create-react-app frontend`
Install Axios: cd `frontend` && `npm install axios`

#### Fetching Data
Axios is used to connect to the backend and fetch data.

```javascript
// App.js outline
import React from 'react';
import axios from 'axios';

class App extends React.Component {
    componentDidMount() {
        // Fetch data using Axios
    }

    render() {
        return (
            <div>
                <div>
                    <div>
                        <h1>Kotech plc</h1>
                    </div>
                </div>
            </div>
        );
    }
}

export default App;

#### Retrieving and Rendering Data
Axios within componentDidMount is used to retrieve data from the server and render it in the UI.

#### Running the Application
Ensure both backend and frontend servers are running, and then enter data in the backend to reflect changes in the React frontend.

## Conclusion
With React and Django working seamlessly together, one can successfully build a basic data entry application. Happy coding!