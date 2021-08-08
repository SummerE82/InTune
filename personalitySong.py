from flask import Flask, render_template, url_for, request
from quizQuestions import Questions
app = Flask(__name__)

@app.route("/")
def Quiz_start(): 
    return render_template('quizStart.html')

@app.route("/Quiz")
def QuizForm():
    questions = Questions()
    return render_template('quizForm.html', q = questions.question_prompt)
@app.route('/Personality', methods=['GET','POST'])
def QuizAnswers():
    questions = Questions() 
    #for values in questions.question_prompt[1].items():
    answer = request.form['Favorite Social Setting']
            #print(answer)
    return render_template('personality.html',a = answer)
       

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")