from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    prediction = model.predict([url])[0]

    # Map the prediction to a readable format
    if prediction == 'benign':
        result = 'Benign'
    elif prediction == 'malicious':
        result = 'Malicious'
    else:
        result = 'Unknown'  # This should not occur if the model is trained properly

    return render_template('result.html', prediction=result, url=url)

if __name__ == '__main__':
    app.run(debug=True)
