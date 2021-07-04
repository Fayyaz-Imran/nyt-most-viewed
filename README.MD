#New York Times Most Viewed Articles

This Flask-based web app is designed to query most viewed articles API calls from [NYT Developers API website](https://developer.nytimes.com/) and display it in a list as a webpage.
It can be run locally or deployed on any cloud platform such as [Heroku](https://www.heroku.com). A live demo of this app can be accessed on link below:

Live Demo: https://nyt-most-viewed.herokuapp.com/

Click on each list to reveal more details about each articles data such as url, published date, authors, abstract, etc.

##LOCAL DEPLOYMENT GUIDE

- Clone the repository or download ZIP to your local machine
- Created on Python version 3.7.8, if possible use the same Python version
- It is recommended to run the script in a virtual environment (virtualenv)
- Activate virtual environment before running the code (. env/Scripts/activate)
- Install all dependency from requirements.txt (pip install -r 'requirements.txt')
- Edit the settings.ini file API_KEY value to your own NYT API Dev keys. Failure to edit this will fail the API call.
- Run the python script at 'wsgi.py' on terminal (python wsgi.py)
- Open the designated Flask url: http://127.0.0.1:5000/ 


Created by Fayyaz Imran