# Full-Stack web developer Nanodegree - Trivia API 
# Frontend 

### Getting Setup

### Installing Dependencies

1. **Installing Node and NPM**<br>
This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

2. **Installing project dependencies**<br>
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:
```bash
npm install
```
>_tip_: **npm i** is shorthand for **npm install**

# Required Tasks

### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
# Backend 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

### API Referance 
## Geting Started
- Base URL: this app run only rub locally and is not hosted as a base URL.
- Authentication: Trivia app soes not require authentication or API key.
## Error Handling
- Error are returnes as JSON objects in the following format:
```bash
{
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }
```
- The API will return these error types when request fail: 
   - 400: Bad Request
   - 404: Not found
   - 422: unprocessable
   - 500: Internal Server Error
## Endpoints 
### GET /categories
- General: Return a list of categories.
- Sample: curl http://localhost:5000/categories
```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}

```
### GET /questions
- General: Return a list of questions, result are paginated in group of 10.
- Sample: curl http://localhost:5000/questions?page=1
```bash


```
### DELETE /questions/<int:question_id>
- General: Deletes a specified question using the id of the question
- Sample: curl -X DELETE http://localhost:5000/questions/20
```bash
{
  "deleted": 20
}

```
### POST /questions
- General: Sends a post request in order to add a new question
- Sample: 
```bash
{
    'question':  'Heres a new question string',
    'answer':  'Heres a new answer string',
    'difficulty': 1,
    'category': 3,
}
```
### POST /questions/search
- General: Sends a post request in order to search for a specific question by search term
- Sample: 
```bash


```
### GET /categories/<int:category_id>/questions
- General: Fetches questions for a cateogry specified by id request argument 
- Sample: 
```bash
{
    'questions': [
        {
            'id': 1,
            'question': 'This is a question',
            'answer': 'This is an answer', 
            'difficulty': 5,
            'category': 4
        },
    ],
    'totalQuestions': 100,
    'currentCategory': 'History'
}

```
### POST /quizzes
- General: Sends a post request in order to get the next question, returns a single new question object
- Sample: 
```bash
{
    'question': {
        'id': 1,
        'question': 'This is a question',
        'answer': 'This is an answer', 
        'difficulty': 5,
        'category': 4
    }
}

```
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
