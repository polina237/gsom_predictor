from flask import Flask, request

app=Flask(__name__)

MODEL_PATH="for_models/model_catboost.pkl"
SCALER_X_PATH="for_models/scaler_x_catboost.pkl"
SCALER_Y_PATH="for_models/scaler_y_catboost.pkl"


@app.route("/predict_price", methods=['GET'])
def predict():
    args=request.args
    rooms=args.get('rooms', default=-1, type=int)
    area=args.get('area', default=-1, type=float)
    renovation=args.get('renovation', default=-1,type=int)
    response="rooms:{}, area:{}, renovation:{}".format(rooms, area, renovation)
    return response


if __name__=='__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')