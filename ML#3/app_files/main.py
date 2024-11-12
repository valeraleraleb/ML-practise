import flask
from flask import render_template
import pickle
import sklearn
import pandas as pd
import catboost
from catboost import CatBoostRegressor

app = flask.Flask(__name__, template_folder= 'templates')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    
    if flask.request.method == 'POST':
        with open ('model_Depth.pkl', 'rb') as f:
            loaded_model_depth = pickle.load(f)
        
        with open ('model_Width.pkl', 'rb') as f:
            loaded_model_width = pickle.load(f)

        form_a = float(flask.request.form['IW'])
        form_b = float(flask.request.form['IF'])
        form_c = float(flask.request.form['VW'])
        form_d = float(flask.request.form['FP'])

        exp = pd.DataFrame(
            {'IW': [form_a],
             'IF': [form_b],
             'VW': [form_c],
             'FP': [form_d]} #, index=[0]
            )
        y_pred = loaded_model_depth.predict(exp)
        z_pred = loaded_model_width.predict(exp)

        return render_template('main.html', result_depth = y_pred, result_width = z_pred)

if __name__ == '__main__':
    app.run()