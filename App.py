from flask import Flask
from flask import request
from flask import render_template
import cv2
import CardScanner
import random
#import stringComparison

app = Flask(__name__)
#https://stackoverflow.com/questions/46482475/how-handle-a-button-click-on-python-flask/46482985
@app.route('/', methods=["GET", "POST"])
def my_form():
    student_num = request.form["student_num"]
    print(student_num)
    return render_template("test.html", message=student_num)

#background process happening without any refreshing
#@app.route('/background_process_test')
#def background_process_test():

#    print("Checking ")
#    print ("Hello")
#    return

# when got, this method is called
# Preform the calculations here, and then return the result :)
#@app.route("/data", methods=["GET", "POST"])
#def data():
    #data = "THIS IS UPDATED"
    #response = make_response(json.dumps(data))
    #response.content_type = "application/json"
#    return str(random.randrange(0, 10))

#@app.route("/msg")
#def update_msg():
#    return render_template("test.html", message="MY MESSAGE")

if __name__ == '__main__':
    app.run(debug=True)