from flask import Flask, request, render_template, redirect,url_for
import joblib
import pickle
import numpy as np

app = Flask(__name__)
lr_model = joblib.load('lung_cancer_model.pkl') # Loading the trained model

#Mapping for yes/no inputs to binary values
yes_no_map = {'yes': 1, 'no': 0}

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html') # Loading the home page

# @app.route('/predict',methods=['GET'])
# def predict():
#     return render_template('predict.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        # Collect data from form
        age = int(request.form['age'])
        gender = 1 if request.form['gender'] == 'male' else 0  # Male=1, Female=0
        smoking = yes_no_map[request.form['smoking']]
        yellow_fingers = yes_no_map[request.form['yellow_fingers']]
        anxiety = yes_no_map[request.form['anxiety']]
        peer_pressure = yes_no_map[request.form['peer_pressure']]
        chronic_disease = yes_no_map[request.form['chronic_disease']]
        fatigue = yes_no_map[request.form['fatigue']]
        allergy = yes_no_map[request.form['allergy']]
        wheezing = yes_no_map[request.form['wheezing']]
        alcohol_consumption = yes_no_map[request.form['alcohol_consumption']]
        coughing = yes_no_map[request.form['coughing']]
        shortness_of_breath = yes_no_map[request.form['shortness_of_breath']]
        swallowing_difficulty = yes_no_map[request.form['swallowing_difficulty']]
        chest_pain = yes_no_map[request.form['chest_pain']]

        # Prepare the data for prediction
        input_features = np.array([[age, gender, smoking, yellow_fingers, anxiety, peer_pressure,
                                    chronic_disease, fatigue, allergy, wheezing, alcohol_consumption,
                                    coughing, shortness_of_breath, swallowing_difficulty, chest_pain]])

        # Get prediction from the model (0 for low risk, 1 for medium, 2 for high risk)
        prediction = lr_model.predict(input_features)[0]

        # Map prediction to risk levels
        risk_levels = {0: 'low', 1:'high'}
        risk_level = risk_levels.get(prediction, 'unknown')

        # Redirect to result page with the predicted risk level
        return redirect(url_for('result', risk_level=risk_level))

    return render_template('predict.html')  # Render the prediction form
@app.route("/result")
def result():
       # Get the risk level from the query parameter
    risk_level = request.args.get('risk_level', 'unknown')

    # Render the result page with the risk level
    return render_template('result.html', risk_level=risk_level)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
