# QR Genrator API

## **Prerequisites**
Before you begin, make sure you have the following prerequisites installed on your system:

- #### **Docker**

## **Getting Started**
Clone this repository to your local machine:
```
git clone https://github.com/your-username/your-repo.git
```

Navigate to the project directory:
```
cd your-repo
```

## **Building the Docker Image**
Build the Docker image using the provided Dockerfile and docker-compose.yml file:
```
docker-compose build
```

## **Running the Flask Application**
1. Start the Flask application inside a Docker container:
```
docker-compose up -d
```

>The -d flag runs the container in the background.

2. Access the application in your web browser by navigating to http://localhost:5000.

## **Stopping the Application**
To stop the running container, use the following command:
```
docker-compose down
```


