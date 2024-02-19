pip freeze > requirements.txt

Local Server: 
export FLASK_ENV=development
export FLASK_APP=main
flask run

Deployed on Google App Engine: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service

Prompts

Obnoxious:

given the following statement in between <prompt> and </prompt> you MUST give me a single word reply.

<prompt>you are so stupid</prompt>

first, analyze the statement for any signs that the person is being obnoxious, annoying, disruptive, rude, aggressive, or mean.

if there are no signs of the above marker, return "Appropriate".

if there are signs of the above markers or you are not sure, move on to the next filter.

given the context of a professional meeting, evaluate if the prompt between <prompt> and </prompt> is appropriate. this is important because sometimes things that are appropriate amongst friends is not appropriate in professional environment. "hahaha you are so stupid!" might be something that is funny between friends, but is generally frowned upon in working environments.

if there are no signs of the above market, return "Unsure"

summarize the tone of the prompt in a single word.