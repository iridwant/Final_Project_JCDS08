# Purwadhika Job Connector Data Science 08 Final Project

## Used Cars Price Prediction & Recommendation

This project was created to pass the Job Connector program on Purwadhika Data Science course. The scope of this project is to create a local web-page to predict prices and give used cars recommendation to user. 

Dataset was taken from Kaggle: [Used Cars Dataset](https://www.kaggle.com/austinreese/craigslist-carstrucks-data).

The model used to predict the price are Random Forest Regressor, and for recommendation I'm using Content-Based Filtering based on price, condition, status, and type. 

I'm using Flask to develop the page, and there's a cars1.csv file used as a database for recommendations.

+ For model, you can check the python notebook Predictions. If you need the joblib file, just uncomment the last line and run it. 
+ For recommendation, you can check the python notebook Recommendations. Again, if you need the joblib file, just uncomment and run the last line.
+ For EDA and data visualization, I've provided the steps in the python notebook EDA.

Thank you.
