from flask import Flask, render_template, request, url_for
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

cars = pd.read_csv('cars1.csv',index_col=0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predictions():
    if request.method == 'POST':
        data = request.form
        col_order = ['year', 'manufacturer', 'condition', 'cylinders', 'fuel', 'odometer', 
        'title_status', 'transmission', 'drive', 'type', 'paint_color']
        features = pd.DataFrame([data],columns=col_order)
        x = model.predict(features)
        data = data.to_dict()
        data.update(price=x[0])
        print(data)
        return(render_template('predictResult.html',data=data))
    else:
        return render_template('predict.html')

@app.route('/recommendation', methods=['GET','POST'])
def recommendations():
    if request.method == 'POST':
        data = request.form
        carFilter = cars.loc[(cars['price'] <= int(data['price'])) & (cars['type'] == data['type'])].sort_values(
            by=['price','condition_rank','status_rank'], ascending=False).index[0]
        
        simCars     = list(enumerate(simscore[carFilter]))
        sortCars    = sorted(simCars, key=lambda x:x[1], reverse=True)

        carData     = []
        for i in sortCars[:6]:
            carData.append(cars.iloc[i[0]])
        carData = pd.DataFrame(carData)
        
        carRecommendation = carData[carData['price'] <= int(data['price'])].sort_values('price', ascending=False)

        return render_template('recommendationResult.html', carRecommendation = carRecommendation, data=data)
    else:
        return render_template('recommendation.html')

if __name__ == '__main__':
    model = joblib.load('model')
    simscore = joblib.load('score')

    app.run(debug = True)
