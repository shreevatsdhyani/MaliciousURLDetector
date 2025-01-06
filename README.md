

---

# Malicious & Spam Links Detector by Delhi Police

This project is a web application that detects whether a given URL is benign or malicious. It uses a machine learning model to classify URLs into these two categories. The project is designed with a user-friendly interface and integrates the branding of the Delhi Police.

## Features

- **URL Classification**: Classifies URLs as either benign or malicious.
- **User Interface**: A simple web interface where users can input a URL and get the classification result.
- **Styled Results Page**: The result page features a background with the Delhi Police logo and a styled prediction box.
- **Interactive UI**: Includes a "Go Back" button on the result page for easy navigation.

## Project Structure

```
.
├── app.py                 # The Flask application code
├── malicious_phish.csv    # The dataset used for training the model (Couldn't upload due to size restrictions)
├── model.pkl              # The trained machine learning model (Couldn't upload due to size restrictions)
├── templates
│   ├── index.html         # The home page where users can input a URL
│   └── result.html        # The results page showing the prediction
├── static
│   ├── style.css          # CSS file for additional styling
│   └── dpimg.jpg          # Delhi Police logo image
└── README.md              # Project documentation
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/malicious-link-detector.git
   cd malicious-link-detector
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:

   ```bash
   python app.py
   ```

6. **Open the browser**:
   - Go to `http://127.0.0.1:5000` to access the application.

## Dataset

The dataset used is `malicious_phish.csv`, which contains more than 600,000 URLs labeled as `benign` or `malicious`. The dataset is used to train the machine learning model.

## Machine Learning Model

- **Model**: RandomForestClassifier
- **Features**: The model uses a `TF-IDF` vectorizer to convert URLs into numerical features before classification.
- **Training**: The model is trained on the dataset, and the trained model is saved as `model.pkl`.

## Usage

1. **Input a URL**: On the home page (`index.html`), enter the URL you want to classify.
2. **View Results**: The result page (`result.html`) will display the prediction (`benign` or `malicious`), along with a "Go Back" button for easy navigation.

## Styling

- **Background**: The result page has a black background with a transparent image of the Delhi Police logo behind the prediction box.
- **Prediction Box**: A centered box that shows the prediction with a "Go Back" button in red for returning to the home page.

## Issues and Troubleshooting

- **Always Predicting 'benign' or 'unknown'**: This issue can occur due to model overfitting or imbalance in the dataset. Ensure the dataset is balanced and the model is trained properly.
- **TemplateNotFound Error**: Ensure that the `index.html` and `result.html` templates are correctly placed in the `templates` directory.


