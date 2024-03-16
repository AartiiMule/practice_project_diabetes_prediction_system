from flask import Flask,jsonify,render_template,request

from project_app.utils import Diabetic



app = Flask(__name__)
@app.route("/")
def hello_flask():
    print("Welcome to our world")
    return render_template("index.html") 



@app.route("/predict_charges", methods=["POST", "GET"])
def get_diabetic_pred():
    if request.method == "GET":
        print("We are in a GET Method")
                
        Glucose =       eval(request.args.get("Glucose"))
        BloodPressure = eval(request.args.get("BloodPressure"))
        SkinThickness = eval(request.args.get("SkinThickness"))
        Insulin =       eval(request.args.get("Insulin"))
        BMI =           eval(request.args.get("BMI"))
        DiabetesPedigreeFunction = eval(request.args.get("DiabetesPedigreeFunction"))
        Age =          eval(request.args.get("Age"))

        
        dia_test =  Diabetic(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        charges = dia_test.get_predicted_value()
        
        positive = "Yes,patient is diabetic"
        negative = "No,patient is non diabetic"
    
        if charges == 1:
            return render_template("index.html", prediction=positive)
            
        else:
            return render_template("index.html", prediction=negative)
            
        
        

print("*"*50)
print("__name__-->",__name__)

app.run(host="0.0.0.0", port=5000, debug=False)

