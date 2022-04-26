import joblib
from flask import Flask, render_template, request

app = Flask(__name__)
pipeline = joblib.load('./HousePrice.pkl')

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction1', methods=['POST','GET'])
def pred():
    a = []
    if request.method=='POST':
        bedrooms=request.form['bd']
        bathrooms=request.form['br']
        yr_built=request.form['hb']
        yr_renovated=request.form['hr']
        total_sqft=request.form['tf']
        a.extend([bedrooms,bathrooms,yr_built,yr_renovated,total_sqft])
        pred = pipeline.predict([a])
        return render_template('prediction.html', msg="done", op=pred)


if __name__ =='__main__':
    app.secret_key="megha"
    app.run(debug=True)