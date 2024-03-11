

# Financial Status Prediction

This Streamlit web application is designed to predict financial status based on user input. The underlying model has been trained on financial survey data and can provide predictions for different financial status levels.

## Usage

1. **Run the Application:**
   - Make sure you have Streamlit installed. If not, install it using `pip install streamlit`.
   - Open a terminal and navigate to the directory containing your script.
   - Run the application with the command: `streamlit run  .py`.

2. **Input Your Information:**
   - After running the application, you will be prompted to input various financial indicators.
   - Select or input values for:
      - Financial Wellbeing Score
      - Handling Unexpected Expenses
      - Belief in Financial Future
      - Belief in Achieving Life Goals
      - Perceived Financial Situation
      - Giving Gifts Impact on Finances
      - Confidence in Saving Habits
      - Estimated Home Value
      - Retirement Account Ownership
      - SNAP Benefits Received
      - Financial Hardship Concerns
      - Food Security
      - Confidence in Raising $2,000 in 30 Days
      - Health Insurance Coverage
      - Retirement Savings Account
      - Defined-Benefit Pension Ownership
      - Education Levels

3. **View Prediction:**
   - The application will then use the trained model to predict your financial status.
   - The prediction will be displayed on the web page.

## Technical Details

### Data Preprocessing and Feature Selection
The script `data_preprocessing.py` demonstrates the steps taken to prepare the dataset for training the model. It includes:
- Handling missing values
- Removing outliers
- Scaling numerical features
- Selecting relevant features using ANOVA F-statistic

### Model Training and Evaluation
The script `model_training.py` covers the training of the Decision Tree model and its evaluation using accuracy and a classification report.

### Streamlit Application
The main application script `streamlit_fhs.py` uses Streamlit to create a user-friendly interface for entering information and displaying predictions.

## Files
- `financial.ipynb`: Data preprocessing steps and model
- `streamlit_fhs.py`: Streamlit web application for predicting financial status.
- `NFWBS_PUF_2016_data.csv`: Dataset used for training the model.
- `fhs__model_dt.pkl`: Pre-trained Decision Tree model.

Feel free to explore, modify, and enhance the application to suit your needs!
