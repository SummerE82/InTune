#from flask_wtf import FlaskForm 
from flask import request

class Questions():
    question_prompt = {
        'Favorite Color':['pink', 'blue', 'green', 'black'], 
        'Favorite Social Setting':['Alone', 'With Friends', 'With Family', 'At Work'],
        'Favorite animal':['A Bird', 'A Dog', 'A Whale', 'A Lion'],
        'Favorite Meal Time':['Breakfast', 'Lunch', 'Dinner', 'I just like to snack']
    }
    