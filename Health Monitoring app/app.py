import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model = load("model.save")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[x for x in request.form.values()]]
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if(output==0):
        pred="He/She is perfectly okay"
    elif(output==1):
        pred="He/She is okay, may be a chance of ill"
    else:
        pred="He/She is in ill must consult a doctor"
    
    return render_template('index.html', prediction_text='{}'.format(pred))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
   # For direct API calls trought request

    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)
