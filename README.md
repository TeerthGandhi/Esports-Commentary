# Esports-Commentary
Esports commentary powered by machine learning (ML) refers to the automated or AI-assisted analysis and narration of competitive gaming events. Using real-time data from the game, machine learning models provide dynamic, insightful, and engaging commentary, often supplementing or replacing human commentators.

![Alt text](assets/UI.png)


### 1. Create and Activate a Virtual Environment

```bash
pip install virtualenv
```

```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root directory:

```plaintext
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Accessing the Application

```bash
http://127.0.0.1:8000/
```


```markdown
# Docker Setup for Esports Commentary

This README provides instructions for building, running, tagging, and pushing the Docker image for the esports-commentary project.

## Build and Run the Docker Container

1. **Build the Docker image**:

   This will build the Docker image from the `Dockerfile` in the current directory.

   ```bash
   docker build -t esports-commentary .
   ```

2. **Run the Docker container**:

   This will run the Docker container and expose it on port 8000 of your machine.

   ```bash
   docker run -p 8000:8000 esports-commentary
   ```

3. **Build and run the containers using Docker Compose**:

   If you're using Docker Compose, use the following command to build and run all the necessary containers defined in the `docker-compose.yml` file.

   ```bash
   docker-compose up --build
   ```

## Tagging and Pushing the Docker Image to Docker Hub

1. **Tag the Docker image**:

   Tag the image with your Docker Hub username and the desired repository name (`esports-commentary` in this case).

   ```bash
   docker tag esports-commentary shintojoseph1234/esports-commentary:latest
   ```

2. **Push the Docker image to Docker Hub**:

   Push the tagged image to your Docker Hub repository.

   ```bash
   docker push shintojoseph1234/esports-commentary:latest
   ```

```