# Purwadhika Job Connector Data Science 08 Final Project

## Used Cars Price Prediction & Recommendation

This project was created to pass the Job Connector program on Purwadhika Data Science course. The scope of this project is to create a local web-page to predict prices and give used cars recommendation to user. 

<hr>

<h3>Goals</h3>
The goals of this project are: 
1. Help user to predict their used car price for selling purposes.
2. Help user get a recommendation on which car to buy for buying purposes.

<hr>

<h3>Dataset</h3>

Dataset was taken from Kaggle: [Used Cars Dataset](https://www.kaggle.com/austinreese/craigslist-carstrucks-data). The dataset is scraped from Craiglist within the United States, it has 539,759 rows and 25 columns which are:
- id (int64): entry id from craiglist
- url (object): URL listing of craiglist car data
- region (object): craiglist region
- region_url (object): URL for each craiglist region
- price (int64): used cars entry price
- year (float64): used cars entry year
- manufacturer (object): manufacturer of vehicle
- model (object): model of vehicle
- condition (object): condition of vehicle
- cylinders (object): number of cylinders
- fuel (object): type of fuel
- odometer (float64): car mileages
- title_status (object): title status of vehicle
- transmission (object): type of transmission
- vin (object): VIN of car entry
- drive (object): type of wheel drive
- size (object): car sizes
- type (object): type of vehicle
- paint_color (object): paint color of vehicle
- image_url (object): URL for car image
- description (object): seller description of vehicle posted
- county (float64): county of vehicle seller
- state (object): state of vehicle seller
- lat (float64): latitude location of vehicle seller
- long (float64): longitude location of vehicle seller

<hr>
<h3>Model Prediction</h3>

The model used to predict the price are Random Forest Regressor, and for recommendation I'm using Content-Based Filtering based on price, condition, status, and type. 

Random Forest Regressor are chosen because it has the lowest MAE & RMSE score. I've tried others model such as:
- Decision Tree Regressor
- Grid Search Decision Tree Regressor
- XGBoost
- Grid Search XGBoost

<hr>

I'm using Flask to develop the page, and there's a [cars1.csv](https://github.com/iridwant/Final_Project_JCDS08/blob/master/cars1.csv) file used as a database for recommendations.

+ For model, you can check the python notebook [Predictions](https://github.com/iridwant/Final_Project_JCDS08/blob/master/Predictions.ipynb). If you need the joblib file, just uncomment the last line and run it. 
+ For recommendation, you can check the python notebook [Recommendations](https://github.com/iridwant/Final_Project_JCDS08/blob/master/Recommendations.ipynb). Again, if you need the joblib file, just uncomment and run the last line.
+ For EDA and data visualization, I've provided the steps in the python notebook [EDA](https://github.com/iridwant/Final_Project_JCDS08/blob/master/EDA.ipynb).

<hr>
<h3>Model Interfaces</h3>
!
Thank you.
