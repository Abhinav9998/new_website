#print(__name__) #__name__ variable has the name __main__ since it is invoked by app.py
from flask import Flask
app = Flask(__name__)
#the variable __name__ is altready defined

@app.route("/")# route is part of the domain name after url
def hello_world():
    return "<p>Hello everyone!</p>"

if __name__== '__main__' : #name variable has the value main
   app.run(host='0.0.0.0', debug=True)
#debug=True means everytime we make some change the output will be updated