from flask import Flask, request, jsonify


app = Flask(__name__)


from sklearn.externals import joblib
pipeline = joblib.load('models/pipeline.pickle')
targets = joblib.load('models/targets.pickle')
def predict(text):
 idx = pipeline.predict([text])[0]
 return targets[idx]



@app.route('/')
def index():
 text = request.args.get('text')
 result = {'prediction' : predict(text)}
 return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')        
    # app.run(debug=True)