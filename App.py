from flask import Flask
from flask import request
from flask import render_template
import cv2
import CardScanner
#import stringComparison

app = Flask(__name__)
#https://stackoverflow.com/questions/46482475/how-handle-a-button-click-on-python-flask/46482985
@app.route('/')
def my_form():
    #app.logger.info(CardScanner.scan())

    #if request.method == "POST":
    #    print("IS a post request")

    return render_template("test.html")

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")
#@app.route('/', methods=['POST'])
#def my_form_post():
#    text1 = request.form['text1']
#    text2 = request.form['text2']
#    plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1,text2)
#    if plagiarismPercent > 50 :
#        return "<h1>Plagiarism Detected !</h1>"
#    else :
#        return "<h1>No Plagiarism Detected !</h1>"

def get_student_num(methods=['POST']):
    return 0

if __name__ == '__main__':
    app.run(debug=True)