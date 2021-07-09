## Covid Secure Entrance System
An entrance has the opportunity to become the first line of defence against Covid by enforcement of regulations such as 
quarantine and facemask wearing to keep everyone safe and the building open.

**Please see [`final_report.pdf`](https://github.com/matthew-64/CSBEntranceSystem/blob/main/final_report.pdf) which contains
the full details of the Covid Secure Entrance System.**

### End user experience
![Alt text](./readme_resources/what_user_sees.png?raw=true "Title")


### Performance
![Alt text](./readme_resources/performance.png?raw=true "Title")

### System desing
The entrance system can be divided into four main parts: 
1. a simple GUI that a student can interact with,
2. a database that can store the necessary information on the student
3. a machine learning model that can determine if a 
student is wearing a mask,
4. a flask web server for running the entrance service, responsible for displaying the GIU 
and managing backend tasks

The GUI is responsible for displaying a live video feed to the student beside an NFC card reader. The GUI is built using 
HTML and JavaScript. The WebcamJS library is used to display the live feed from the camera to the student. JavaScript is
used to link the available button and text box (for manual student card entry, used in this prototype) to the flask 
server that is running in the background in order for the server to react to the actions of the student.


Azure SQL databases are used to keep track of who has recently self-reported as testing positive for Covid as well as 
information from a potential contract tracing system based on personal building usage information. Not everyone can wear a 
facemask for medical reasons. As to not discriminate, a database of who is exempt from wearing a facemask also exists. 
Both of these databases are centrally stored on an Azure database server and accessible by any individual entrance 
system.


In order to determine if a student is wearing a facemask, an Azure CustomVision model was trained with a dataset of 644 
faces with a mask and 635 faces with no mask. The person in each image varied on skin colour, hair colour, gender, 
lighting, quality, and background in order to make the model more robust under real-world conditions. The model can be 
used to determine whether a student is wearing a mask. An endpoint is provided which can be used to access this trained 
model and return a response as to the probability of the person wearing and not wearing a mask.


The flask server acts as the backbone that joins the above three parts together. When a student card is entered via the 
NFC reader or manual input (for the prototype), the server starts a series of sequential checks beginning with the 
quickest and least expensive tasks in order to reduce both the time taken for the system to come to a conclusion. the 
system will check that they have not been in close contact with anyone else that has texted positive from. This data 
should come from the contact tracing system. Next, the system will check that they are not a positive case them self.
This data should come from the self-reporting system. If these checks pass, the system will then check if they are 
exempt from wearing a face covering. If they are, the door will open, and they will be granted entry. Otherwise, the
camera will take a picture of their face, send it to the CustomVision machine learning model and open the doors if they 
are wearing a mask. If they are not, they will be asked to put one on and try again.

### Launch the app:  
* Obtain the config.json file from the system adminstrator and put in the base directory
* run `python3 App.py`
* Navigate to http://127.0.0.1:5000/ 
