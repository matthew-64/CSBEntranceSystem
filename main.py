from flask import Flask
#from flask import request
from flask import render_template
import cv2
#import stringComparison

app = Flask(__name__)

@app.route('/')
def my_form():
    #return 'test'
    return render_template("index.html") # this should be the name of your html file

#@app.route('/', methods=['POST'])
#def my_form_post():
#    text1 = request.form['text1']
#    text2 = request.form['text2']
#    plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1,text2)
#    if plagiarismPercent > 50 :
#        return "<h1>Plagiarism Detected !</h1>"
#    else :
#        return "<h1>No Plagiarism Detected !</h1>"

#@app.route('/')
#def hello_world():
#    return 'Hello, World!'



if __name__ == '__main__':
    app.run(debug=True)