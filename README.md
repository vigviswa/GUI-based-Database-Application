# CS6360 Programming Assignment

Technologies and Tools Used:

1) Python
2) Flask
3) sqlalchemy
4) wtforms
5) pandas
6) Google cloud platform
7) Mysql

Setup:

Download the zip provided on eLearning to get all the files involved in the project.
Also, the same files can be obtained from my GitHub repository : https://github.com/vigviswa/GUI-based-Database-Application
The repository is named: GUI Based Database Application

After downloading, go to the directory where the file is downloaded and setup the environment and packages by using the command:

'pip install -r requirements.txt'

Also to note that the environment variables used in the project are:

SECRET_KEY=cs6360;
MYSQL_HOST=35.225.127.97;
MYSQL_USER=contacts-user;
MYSQL_PASSWORD=cs6360;
MYSQL_DB=dev_contacts

I have created the Key and User credentials using google cloud to connect my native app to a mysql engine

The app can be run locally on the machine or can be accessed anywhere using the deployed app created through google cloud

App URL: 'https://cs6360-vxv190028-contacts.appspot.com/'

Process:

Run the main.py to deploy the Flask app on a local server. The app is configured to run at port 5000.

The Add Contact Link can be seen on the menu bar, is used to add a new contact to the app. 

The Homepage lists all the contacts currently listed in the application, ordered according to their time of creation.

The Edit Contact is not explicitly listed. The contact listing is itself a hyperlink, which redirects the user to edit the current contact.

The Search Contact functionality can be achieved through the Search Bar provided on the Homepage. The Search results can be seen by clicking on the Search Button and lists the editable contacts which match the search.

The Delete Contact function is integrated with the edit contact and the button to delete contact can be listed when you click on the contact to edit it.

About the App:

The App can work as a general purpose contact listing application such as 'https://contacts.google.com/'

Hence, I haven't populated the Database with data provided on the contacts.csv. However, If required, during demo, I can use the MYSQL Workbench to populate the Application with contacts as required.

Kindly Try out the app by adding/deleting/editing created contacts.

In the Edit contact page, If the date/address/phone field has only one row listed and you were to delete it, Kindly add a new row, by clicking the '+' and then delete the original row.

Feel free to contact me if any issue arises during running the app.
