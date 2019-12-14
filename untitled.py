import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('nba.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    if output == 1:
        out = 'Tim 1 Menang'
    else:
        out = 'Tim 2 Menang'

    return render_template('index.html', prediction_text='{}'.format(out))

if __name__ == "__main__":
    app.run(debug=True)