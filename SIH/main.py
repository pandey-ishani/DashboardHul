import os
import json
from flask import Flask, render_template, request, redirect
from firebase import firebase
import matplotlib.pyplot as plt
from flask_table import Table, Col

app = Flask(__name__)


firebase = firebase.FirebaseApplication('https://fir-project-20449.firebaseio.com/')

result1 = firebase.get('/Returns', None)


ids = list(result1.keys())
dor = list()
wholesaler = list()
region = list()
price = list()

for details in result1.values():
     dor.append(details['Date of Return'])
     wholesaler.append(details['Wholesaler'])
     region.append(details['Region'])
     price.append(details['Money Credited'])

     leng= len(ids)


freq = dict()
for x in region:
	if(x in freq):
		freq[x] +=1
	else:
		freq[x]=1

xaxis=[]
yaxis=[]
for x in freq:
	xaxis.append(x)
	yaxis.append(freq[x])


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index1.html',ID=ids, DOR=dor, WHOLE=wholesaler, REG=region, PRICE=price, leng=leng)

@app.route('/plot', methods=['GET'])
def chart():
	return render_template('linechart.html', xaxis= json.dumps(xaxis), yaxis= json.dumps(yaxis))

	
