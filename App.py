from flask import Flask
from flask import request
from flask import render_template
from database import CloseContactChecker, InfectedChecker
from utils import Camera
from machineLearning import MaskClassifier, MaskExemption

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def my_form():
    return render_template("test.html")


@app.route('/scan', methods = ['POST'])
def signup():
    try:
        student_num = request.form.get["student_num"]
    except(Exception):
        return render_template("test.html",
                               message="")
    print("Checking for close contact")
    if CloseContactChecker.isContact(student_num):
        return render_template("test.html", message="You have been in close contact with a positive case. Entry denied.")

    print("Checking for positive test result")
    if InfectedChecker.isInfected(student_num):
        return render_template("test.html", message="Sorry you have had a positive test recently. Entry denied.")


    if not MaskExemption.hasMaskExemption(student_num):
        Camera.take_picture()
        if not MaskClassifier.is_wearing_mask():
            return render_template("test.html",
                                   message="Please wear a mask and try again.")
    return render_template("test.html", message="Welcome. Doors opening.")


if __name__ == '__main__':
    app.run(debug=True)