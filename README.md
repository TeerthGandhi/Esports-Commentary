# Esports-Commentary
Esports commentary powered by machine learning (ML) refers to the automated or AI-assisted analysis and narration of competitive gaming events. Using real-time data from the game, machine learning models provide dynamic, insightful, and engaging commentary, often supplementing or replacing human commentators.

![Alt text](assets/UI.png)


## 1. Create and Activate a Virtual Environment

To keep the project dependencies isolated, create a virtual environment. You can use `venv` or `virtualenv` for this purpose.

### Using `virtualenv` (recommended)

Install `virtualenv` if you don't have it:

```bash
pip install virtualenv
```

Now, create and activate the virtual environment:

```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Using Python's built-in `venv` (alternative method)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## 2. Install Dependencies

Once the virtual environment is activated, install the project dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 3. Set Up Environment Variables

Create a `.env` file in the project root directory and add the required environment variables. For example:

```plaintext
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 4. Apply Database Migrations

Before running the project, apply the migrations to set up the database schema:

```bash
python manage.py migrate
```

## 5. Run the Development Server

Now that everything is set up, you can run the Django development server on `localhost`:

```bash
python manage.py runserver
```

The server will start on `http://127.0.0.1:8000/` or `http://localhost:8000/`.

## 6. Accessing the Application

Once the server is running, open your browser and navigate to:

```bash
http://127.0.0.1:8000/
```

