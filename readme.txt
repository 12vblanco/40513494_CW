BarBench Table Reservation App
==============================

Introduction
------------
BarBench is a table system application built into a fictional pub website as part of the Advanced Web Technologies module.

Installation
------------
To install the app: 
1. Clone the repository: https://github.com/12vblanco/assignment.git
2. Project directory: cd assignment
3. Install dependencies: pip install -r requirements.txt

Running the Application
-----------------------
To run the application:
1. Activate the virtual environment: source env/bin/activate
2. Start the Flask app: flask --app assignment run --host=0.0.0.0 --port 5000

Deployed URL
------------
The application and website can be seen at:
http://webtech-2324-07.napier.ac.uk/

Admin Login 
-----------
Username: Admin
Password: password
This credentials are hardcoded for demonstration purposes

Bugs
----
The deployed version of the site contains some known bugs that have been corrected in the repository but not deployed.

1. The name in the booking form is limited to 12 characters and the reservation would not work  if the name contains more. There is no error message or validation advising the user of this.
2. The custom error pages for 404 and 500 error do not work in the deployed site. The routes have been changed in the repository and they would work in case or redeployment.

**This would need to be deployed in the code in order to improve the user experience and further improve the app but they were discovered last minute and only corrected in the development environment.
