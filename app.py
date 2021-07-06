
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn


app = Flask(__name__, template_folder='templates')

model = pickle.load(open('titanicdatasetDecisionTree.pkl', 'rb'))

@app.route('/', methods= ['Get'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods= ['POST'])
def predict():
      if request.method == 'POST':
          Ticket_class = int(request.form['Ticket_class'])
          Gender = request.form['Gender']
          if(Gender == 'Male'):
              Gender = 1
          else:
              Gender = 0
          Age = int(request.form['Age'])
          SibSp = int(request.form['SibSp'])
          Parch = int(request.form['Parch'])
          Fare = float(request.form['Fare'])
          prediction= model.predict([[Ticket_class, Gender, Age, SibSp, Parch, Fare]])
          output = (prediction)
          if output==0:
              return render_template('index.html', prediction_text="Sorry! Passenger is not survived")
          else:
              return render_template('index.html', prediction_text= "Good News! Passenger is survived")

      else:
        return render_template('index.html')


if __name__ ==  "__main__":
    app.run(debug = True)
