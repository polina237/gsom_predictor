from flask import Flask, request

app=Flask(__name__)

MODEL_PATH="Final_task/model_forest.pkl"
SCALER_X_PATH="Final_task/scaler_x_forest.pkl"
SCALER_Y_PATH="Final_task/scaler_y_forest.pkl"

@app.route("/predict_price", methods=['GET'])
def predict():
    args=request.args
    amount = args.get('amount', default=-1, type=int)
    rooms=args.get('rooms', default=-1, type=int)
    area=args.get('area', default=-1, type=float)
    renovation=args.get('renovation', default=-1,type=int)
    response="amount:{},rooms:{}, area:{}, renovation:{}".format(amount,rooms, area, renovation)
    return response

if __name__=='__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')