pip freeze > requirements.txt

Local Server: 
export FLASK_ENV=development
export FLASK_APP=main
flask run

Deployed on Google App Engine: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service