# import the libraries
from flask import Flask,request
import pandas as pd
import pickle

app = Flask(__name__)

## collecting the model which we have created earlier
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/', methods=['GET'])
def default():
    return 'Welcome All'

@app.route('/predict', methods = ['GET'])
def bank_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return " THE PREDICTED OUTCOME IS : " + str(prediction)

@app.route('/predict_file', methods=['POST'])
def bank_note_prediction():
    df_test = pd.read_csv(request.files.get('testfile'))
    prediction = classifier.predict(df_test)
    return " THE PREDICTED VALUES FOR THE TEST FILE ARE : " + str(list(prediction))


if __name__ == "__main__":
    app.run(debug=True)
