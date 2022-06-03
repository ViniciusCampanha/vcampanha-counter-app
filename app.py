import os
import sys

from flask import Flask

from django.shortcuts import render

app = Flask(__name__)

@app.route("/", methods=[ 'GET' ])
def index():
   return "Hello"

@app.route('/flipacoin', methods=[ 'GET' ])
def flipacoin():
    return choice(['Cara', 'Coroa'])

# Create your views here.
def counterView(request):
   if request.method == "POST" and 'count' in request.POST:
      try:
         request.session['count'] +=1
      except:
         request.session['count'] = 0
   elif request.method == 'POST' and 'reset' in request.POST:
      request.session['count'] = 0
      return render(request,'counter.html')


if __name__ == '__main__':

    current_module = os.path.dirname(os.path.curdir)
    sys.path.append(current_module)

    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'development'   
    

    app.run(host='0.0.0.0',port='8080')