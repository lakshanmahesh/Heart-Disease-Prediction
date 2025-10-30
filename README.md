# Heart-Disease-Prediction
This project uses machine learning to predict the likelihood of a person having heart disease based on medical attributes such as age, blood pressure, cholesterol level, and more. The model was trained, evaluated, and saved as a .pickle file for deployment through a simple HTML web interface.
## Data Preprocessing
   - Handled missing values and normalized data.
   - Split dataset into training and testing sets.

## Model Selection

      from sklearn.linear_model import LogisticRegression
      model = LogisticRegression()
      model.fit(X_train, y_train)
   - Used **Logistic Regression** as the base model.

## Model Evaluation

Base model accuracy: 0.8032.
After hyperparameter tuning: 0.8196.

## Model Saving

    import pickle
    with open('model.pickle', 'wb') as file:
        pickle.dump(model, file)

The trained model was saved using pickle for deployment.

## Deployment

Built a simple web interface for real-time predictions using Flask.

Users can input parameters (age, blood pressure, etc.) and get predictions instantly.

## Technologies Used

  Python

  pandas, NumPy — Data manipulation

  scikit-learn — Model training and evaluation

  Flask — Web interface

  pickle — Model serialization

  ### 1. Clone the repository
      git clone https://github.com/yourusername/Heart-Disease-Prediction.git
      cd Heart-Disease-Prediction

  ### 2. Install dependencies
      pip install -r requirements.txt

  ### 3. Run the Flask app
      python app.py 
## Model Accuracy

| Version | Model                                             | Accuracy |
| ------- | ------------------------------------------------- | -------- |
| Initial | Logistic Regression                               | 80.32%   |
| Tuned   | Logistic Regression (after hyperparameter tuning) | 81.96%   |


