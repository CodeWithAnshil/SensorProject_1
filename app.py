import os, sys
from flask import request, jsonify, render_template, Flask, send_file
from src.exception import CustomException
from  src.logger import logging as lg
from src.pipline.predict_pipeline import PredictionPipeline
from src.pipline.train_pipeline import TrainingPipeline


app = Flask(__name__)

@app.route("/about")
@app.route("/predict-page")
@app.route("/")
def home():
  return render_template('upload_file.html')


@app.route("/train")
def train_route():
  try:
    trian_pipeline = TrainingPipeline()
    trian_pipeline.run_pipeline()

    return "Training Complete"
  except Exception as e:
    raise CustomException(e, sys)
  
@app.route('/predict', methods=['POST','GET'])
def upload():
  try:

    if request.method =='POST':
      prediction_pipeline  = PredictionPipeline(request)  

      prediction_file_detail = prediction_pipeline.run_pipeline()

      lg.info("Prediction complete. Downloading prediction file.")
      return send_file(prediction_file_detail.prediction_file_path, download_name=prediction_file_detail.prediction_file_name,as_attachment=True)
    else:
      return render_template('upload_file.html')
  except Exception as e:
    raise CustomException(e, sys)

if __name__ =="__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)

