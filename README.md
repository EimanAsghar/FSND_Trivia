# Full-Stack web developer Nanodegree - Trivia API 
# Frontend 


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
