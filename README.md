# FastAPI Task Manager
FastAPI Task Manager is a web application designed to help users manage their tasks efficiently. Built with FastAPI, it offers a robust and high-performance backend for task management.

## Features
User Authentication: Secure user registration and login functionalities.
Task Management: Create, read, update, and delete tasks.
Task Prioritization: Assign priorities to tasks to manage them effectively.
Status Tracking: Update and monitor the status of each task.

## Technologies Used
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+
PostgreSQL: A powerful, open-source object-relational database system.
Docker: A platform to develop, ship, and run applications inside containers.
Docker Compose: A tool for defining and running multi-container Docker applications.
Kafka: Sending email after registration

## Installation and Setup
Clone the Repository:

```bash
git clone https://github.com/woodoo2x2/FastAPI_task_manager.git
cd FastAPI_task_manager
```
## Set Up Environment Variables:

Rename the `.env_need_to_change` file to `.env` and update the environment variables as needed.

## Build and Run with Docker Compose:

Ensure you have Docker and Docker Compose installed. Then, run:

```bash
docker-compose up --build
```
This command will build the Docker images and start the services defined in the docker-compose.yml file.

## Access the Application:

Once the services are up and running, the FastAPI application will be accessible at http://localhost:8000.

## API Documentation:

FastAPI provides interactive API documentation. You can access it at:

Swagger UI: `http://localhost:8000/docs`
ReDoc: `http://localhost:8000/redoc`
## Running Tests
To run the test suite, use the provided Docker Compose configuration:

```bash
docker-compose -f docker-compose.test.yml up --build
```
This will execute the tests defined in the tests directory.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.
