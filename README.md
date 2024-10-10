# Esports-Commentary
Esports commentary powered by machine learning (ML) refers to the automated or AI-assisted analysis and narration of competitive gaming events. Using real-time data from the game, machine learning models provide dynamic, insightful, and engaging commentary, often supplementing or replacing human commentators.

![Alt text](assets/UI.png)


## Running the Project with Docker

To run this project using Docker, follow the steps below:

### Prerequisites

Make sure you have Docker installed on your machine. You can download and install Docker from [here](https://www.docker.com/get-started).

### Step 1: Build the Docker Image

Navigate to the root of your project directory (where the Dockerfile is located) and run the following command to build the Docker image:

```bash
docker build -t esports .
```

This command creates a Docker image named `esports` using the Dockerfile in the current directory (`.`).

### Step 2: Run the Docker Container

Once the Docker image is built, you can run the container with the following command:

```bash
docker run -p 8000:8000 esports
```

### Step 3: Access the Application

Once the container is running, you can access the Django application by navigating to:

```
http://localhost:8000
```

