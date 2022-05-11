from flask import Flask, request

app=Flask(__name__)

MODEL_PATH="mlmodels/model.pkl"
SCALER_X_PATH="mlmodels/scaler_x.pkl"
SCALER_Y_PATH="mlmodels/scaler_y.pkl"


@app.route("/predict_price", methods=['GET'])
def predict():
    args=request.args
    open_plan=args.get('open_plan', default=-1, type=int)
    rooms=args.get('rooms', default=-1, type=int)
    area=args.get('area', default=-1, type=float)
    renovation=args.get('renovation', default=-1,type=int)
    response="open_plan:{}, rooms:{}, area:{}, renovation:{}".format(open_plan, rooms, area, renovation)
    return response


if __name__=='__main__':
    app.run(debug=True, port=544, host='0.0.0.0')


