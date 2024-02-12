# Kibhoret
- An automated Material Flow Management System

## Title and Description
This repository contains a Material Flow Management System developed using Django for the backend and React with Vite for the frontend. The system integrates the powerful features of Django for robust backend operations and the lightning-fast development experience provided by Vite for frontend development. 
This web app enables users to efficiently track trucks with material payload as they enter a company premise. It captures various stages of material handling process in a company and the flow of materials in real-time.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Features](#features)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Installation
To install the Automated Material Flow Management System;
#### back-end
1. Clone the repository: `git clone https://github.com/kibuchijw/portfolio-project`
2. Navigate to the backend directory: `cd Kibhoret-backend`
3. Install dependencies: `pipenv install`
4. Activate virtual env: `pipenv shell`
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`

#### front-end
1. On a new window, navigate the front-end directory: `cd kibhoret-frontend`
2. install dependencies: `npm install`
3. Build the front-end assets: `npm run build`
4. Start front end: `npm run dev`

## Usage
1. Access the web application in your browser by navigating to `http://localhost:8000`.
2. Register an account or log in (if you already have one)
3. Access the front-end by navigating to `http://localhost:5173/`
4. Navigate through the different dashboards to manage material flow:
   - **Gate Entry**: Record trucks' general information as they enter the premises.
   - **Weighbridge In**: Record weight data of trucks at the weighbridge.
   - **Quality Control**: Record quality parameters and sampling information.
   - **Offloading**: Manage material offloading process.
   - **Weighbridge Out**: Record final weight of trucks at the weighbridge.




## Configuration
The Automated Material Flow Management System can be configured by modifying the settings in the `config.py` file. Additionally, environment variables can be set for sensitive information such as database credentials and secret keys.

## Features
- Streamlined material flow management process.
- Real-time tracking of trucks and materials.
- User-friendly dashboards for data entry and monitoring.
- Integration with Django's authentication system for user management.
- Customizable configurations to suit different company needs.

## Contributing
Contributions are welcome! If you'd like to contribute to the Automated Material Flow Management System, please follow these guidelines:
- Fork the repository.
- Create a new branch: `git checkout -b feature-new-feature`.
- Make your changes and commit them: `git commit -m 'Add new feature'`.
- Push to the branch: `git push origin feature-new-feature`.
- Submit a pull request detailing your changes.

## Credits
The Automated Material Flow Management System was created by [Your Name]. Special thanks to the Django community for providing excellent documentation and resources.

## License
This project is licensed under the [MIT License](LICENSE).