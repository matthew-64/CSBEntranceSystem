from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import cv2
import CardScanner
import random
import InfectedChecker
import CloseContactChecker
import MaskExemption
import Camera
import MaskClassifier
#import stringComparison

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def my_form():
    return render_template("test.html")
    #print(request.form["blah"])
    student_num = "-1"
    #student_num = request.form["student_num"]
    try:
        student_num = request.form.get["student_num"]
    except(Exception):
        print("ILL USE -1 THIS TIME...")
    if student_num == "-1":
        return render_template("test.html", message="hello")

    print("Checking for positive test result")
    if InfectedChecker.isInfected(student_num):
        return render_template("test.html", message="Sorry you have had a positive test recently. Entry denied.")

    if CloseContactChecker.isContact(student_num):
        return render_template("test.html", message="You have been in close contact with a positive case. Entry denied.")

    if not MaskExemption.hasMaskExemption(student_num):
        Camera.take_picture()
        if not MaskClassifier.is_wearing_mask():
            return render_template("test.html",
                                   message="Please wear a mask and try again.")
    #print("Checking for close contact")

    #print("Check for mask exemption")

    #print("Check if wearing mask")
    #student_num = request.form["student_num"]
    #print(student_num)
    return render_template("test.html", message="Doors opening. Please enter.")

@app.route('/scan', methods = ['POST'])
def signup():
    student_num = request.form['student_number']

    print("Checking for positive test result")
    if InfectedChecker.isInfected(student_num):
        return render_template("test.html", message="Sorry you have had a positive test recently. Entry denied.")

    print("Checking for close contact")
    if CloseContactChecker.isContact(student_num):
        return render_template("test.html", message="You have been in close contact with a positive case. Entry denied.")

    if not MaskExemption.hasMaskExemption(student_num):
        Camera.take_picture()
        if not MaskClassifier.is_wearing_mask():
            return render_template("test.html",
                                   message="Please wear a mask and try again.")
    return render_template("test.html", message="Welcome. Doors opening.")
    #return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)