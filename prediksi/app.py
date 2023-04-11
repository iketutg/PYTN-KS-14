import flask  
import numpy as np
import pickle 

app = flask.Flask(__name__, template_folder='templates')

model_reg = pickle.load(open('model/model_reg_rumah.pkl','rb'))

@app.route('/')
def index():
    return(flask.render_template('main.html'))

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(val) for val in flask.request.form.values()]
    features = [np.array(int_features)]
    y_pred = model_reg.predict(features)
   
    return flask.render_template('main.html',prediction_text=y_pred[0])
    