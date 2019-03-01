import random
from firebase import firebase
firebase = firebase.FirebaseApplication("https://fir-project-20449.firebaseio.com/", None)
result= firebase.post('/', {'ID': 4})
print(result)