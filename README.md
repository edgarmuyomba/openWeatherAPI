# OpenWeatherAPI Clone using Django Rest Framework

This project is a clone of the OpenWeatherAPI implemented using Django Rest Framework. It allows users to retrieve current weather information, weather every 3 hours for 3 days, and weather every hour for 4 days for a specified location. The project also includes a subscription-based system with discount and premium options to access extended weather data.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Subscription](#subscription)
- [Contributing](#contributing)
- [License](#license)

## Features

- Retrieve current weather for a location.
- Get weather every 3 hours for the next 3 days.
- Access weather every hour for the next 4 days (available to premium subscribers).
- Subscription-based system with discount and premium options.
- RESTful API design using Django Rest Framework.
- [Add more features here...]

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-project.git
   ```
2. Create and activate a virtual environment
    ```bash
    python -m venv env
    source venv/bin/activate  # On Windows: env\Scripts\activate
    ```
3. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
4. Setup your database
    ```bash
    python manage.py migrate
    ```
5. Run the development server
    ```bash
    python manage.py runserver
    ```

## Usage
To use this API, you can make requests to the provided endpoints using a tool like curl or through a tool like Postman. Below are the available endpoints and their functionalities.

## Endpoints
GET /data/weather/?location={location}
Get the current weather for the specified location.

GET /data/daily/?location={location}
Get weather every 3 hours for the next 3 days for the specified location.

GET /data/hourly/?location={location}
Get weather every hour for the next 4 days for the specified location (premium feature).

## Authentication
Authentication is required to access certain features. You can use token-based authentication. Include the generated token in the headers of your requests
```bash
Authorization: Token your_token_here
```
You can get a token through the django admin portal or after creating an account,
visit the url:
POST /data/auth/
make sure the include a json attachment of the username and password of your account

## Subscription
To access premium features (such as 4-day weather forecasts), users need to subscribe. Subscription options include discount and premium plans. A user can be added to the discount and premium groups through the admin portal.

## Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name
Make your changes and commit them: git commit -m "Add some feature"
Push to the branch: git push origin feature/your-feature-name
Open a pull request
