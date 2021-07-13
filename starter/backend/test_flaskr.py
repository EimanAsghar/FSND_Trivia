#from _typeshed import Self
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://postgres:1998@{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()



    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_paginated_questions(self):

        # retrive response and load data
        res = self.client().get('/questions')

        data = json.loads(res.data)

        # test if contaion 10 or less questions in page
        self.assertTrue(len(data['questions']) <= 10)
        # test if the following data are return
        self.assertTrue(data['totalQuestions'])

    def test_requesting_beyond_valid_page(self):

        # send requesr with unavilable page
        res = self.client().get('/questions?page=1000')
        
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    #Delete a different question in each attempt
    def test_delete_question(self):
        res = self.client().delete('/questions/9')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        # check if the return id equla to 8
        self.assertEqual(data['deleted'], 9)
        # find the question by id to check if it's deleted or not
        self.assertEqual(Question.query.filter(Question.id == 9).one_or_none(), None)

    def test_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        
        data = json.loads(res.data)
        # check if the return values equal to these.
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    def test_create_new_question(self):
        res = self.client().post('/questions', json={
            'question': 'Who is the most famous artist ever?',
            'answer':  'Pablo Picasso',
            'difficulty': '3',
            'category': '2'
        })
        
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['questions']))

    # def test_question_creation_not_allowed(self):
        
    #     res = self.client().post('/questions/45', json={})
        
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

    def test_question_search(self):
        res = self.client().post("/questions/search",
                                 json={"searchTerm": "title"})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data["questions"]), 2)

    def test_question_search_does_not_exist(self):
        res = self.client().post("/questions/search",
                                 json={"searchTerm": "book"})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    def test_exist_category(self):
        res = self.client().get('/categories/6/questions')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['totalQuestions'], 2)

    # def test_not_exist_category(self):
    #     res = self.client().get('/categories/100/questions')

    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'not found')

    def test_play_game_with_correct_request(self):
        res = response = self.client().post('/quizzes', json={
            'previous_questions': [16, 17],
            'quiz_category': {
                'type': 'Art',
                'id': 2
            }
        })


        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['question']['category'], 2)
        self.assertNotEqual(data['question']['id'], 16)
        self.assertNotEqual(data['question']['id'], 17)


    def test_play_game_without_correct_request(self):
        res = response = self.client().post('/quizzes', json={})


        data = json.loads(response.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
