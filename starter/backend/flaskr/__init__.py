import os
from flask import (
    Flask,
    request,
    abort,
    jsonify
)
from flask.globals import current_app
from sqlalchemy.sql.sqltypes import INTEGER
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import (
    setup_db,
    Question,
    Category
)

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [Question.format() for Question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

 
    # CORS app
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
 
    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, DELETE')
        return response

  
    @app.route('/categories')
    def retrieve_categories():
        # get all categories
        result = Category.query.all()
        categories = {Category.id: Category.type for Category in result}

        return jsonify({
            'success': True,
            'categories': categories
        }), 200



    @app.route('/questions')
    def retrieve_questions():

        # get all questions and categories
        result = Question.query.order_by(Question.id).all()
        categories = Category.query.all()

        # paginate ---> 10 questions per page
        current_q = paginate_questions(request, result)

        if len(current_q) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_q,
            'totalQuestions': len(Question.query.all()),
            'categories': {Category.id: Category.type for Category in categories},
            'currentCategory': None
        }), 200


    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            # delete question based on spacific  id
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            question.delete()

            return jsonify({
                'success': True,
                'deleted': question_id
            }), 200

        except:
            abort(404)


    @app.route('/questions', methods=['POST'])
    def create_question():
        # get data to create new question
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)

        # check if the input empty or not
        if(new_question or new_answer or new_category or new_difficulty) == None:
            abort(422)

        # create question object
        question = Question(question=new_question, answer=new_answer,
                            category=new_category, difficulty=new_difficulty)
        question.insert()

        return jsonify({
            'success': True,
            'questions': question.question,
            'answer':  question.answer,
            'difficulty': question.difficulty,
            'category': question.category
        }), 200


    @app.route('/questions/search', methods=['POST'])
    def search_question():
        # get search term
        body = request.get_json()
        term = body.get('searchTerm', None)
        # find the question
        result = Question.query.filter(
            Question.question.ilike('%' + term + '%')).all()

        if (len(result) == 0):
            abort(404)

        questions = [Question.format() for Question in result]
        return jsonify({
            'success': True,
            'questions': questions,
            'totalQuestions': len(questions),
            'currentCategory': None
        }), 200

 

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def questions_based_on_category(category_id):

            category = Category.query.filter_by(id=category_id).one_or_none()
            
            #check if the catogry exist or not 
            if (category is None):
                abort(404)

            # get question based on category
            result = Question.query.filter(
                Question.category == category_id).all()

            questions = [question.format() for question in result]

            return jsonify({
                'success': True,
                'questions': questions,
                'totalQuestions': len(questions),
                'currentCategory': category_id
            }), 200


   

    @app.route('/quizzes', methods=['POST'])
    def play_game():

        # request data
        body = request.get_json()

        # an array of question id's such as [1, 4, 20, 15]
        previous_questions = body.get('previous_questions')

        # a string of the current category
        quiz_category = body.get('quiz_category')

        # check if JSON empty or not
        if ((previous_questions is None) or (quiz_category is None)):
            abort(400)

        # get questions based on user selection (All or by category)
        # for ALL selection
        if (quiz_category['id'] == 0):
            # get question without the question already in previous question array
            questions = Question.query.filter(
                Question.id.notin_(previous_questions)
            ).all()
        # load questions for given category without the question already in previous question array
        else:
            questions = Question.query.filter_by(
                category=quiz_category['id']).filter(
                Question.id.notin_(previous_questions)
            ).all()

            # if all question already exist in previous question array stop the game.
        if len(questions) == 0:
            return jsonify({
                'success': True
            }), 200
        else:
            # if it's not exist in previous question array, send random question
            random_question = random.choice(questions)
            # Returns: a single new question object
            return jsonify({
                'question': random_question.format()
            })

   
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    # @app.errorhandler(500)
    # def Internal_Server(error):
    #     return jsonify({
    #         "success": False,
    #         "error": 500,
    #         "message": "Internal Server Error"
    #     }), 500

    return app
