import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request, render_template
from train import model

app = Flask(__name__)
@app.route("/")
def index():
     return render_template('index.html')

@app.route("/output",methods=["POST","GET"])
def output():
    if request.method=="POST":
        #age
        age=int(request.form['age'])
        #gender male=1 female=0
        gender=request.form['gender']
        if gender.lower()=='male':
            gender=1
        elif gender.lower()=='female':
            gender=0
        #chestpain asy = 0 ata = 1 nap = 2 ta = 3 
        chestpain=request.form['chestpain']
        if chestpain=='asy':
            chestpain=0
        elif chestpain=='ata':
            chestpain=1
        elif chestpain=='nap':
            chestpain=2
        else:
            chestpain=3
        #restingbp 
        restingbp=int(request.form['restingbp'])
        #cholesterol
        cholesterol=int(request.form['cholesterol'])
        #fastingbs 1 at >=120 0-->otherwise
        fastingbs=int(request.form['fastingbs'])
        if fastingbs >=120:
            fastingbs=1
        else:
            fastingbs=0
        #restingecg lvh=0 normal = 1 st= 2
        restingecg=request.form['restingecg']
        if restingecg=='lvh':
            restingecg=0
        elif restingecg=='normal':
            restingecg=1
        else:
            restingecg=2
        #maxhr
        maxhr=int(request.form['maxhr'])
        #exerciseangina
        exerciseangina=request.form['exerciseangina']
        if exerciseangina.lower()=='yes':
            exerciseangina=1
        else:
            exerciseangina=0
        #oldpeak :float step 0.01
        oldpeak=float(request.form['oldpeak'])
        #st_slope: up = 2 flat = 1 down=0
        st_slope=request.form['st_slope']
        if st_slope=='down':
            st_slope=0
        elif st_slope=='flat':
            st_slope=1
        else:
            st_slope=2

        df_dict={'age':age,'sex':gender,'chest_pain':chestpain,'resting_bp':restingbp,'cholesterol':cholesterol,'fasting_bs':fastingbs,'resting_ecg':restingecg,'max_hr':maxhr,'exercise_angina':exerciseangina,'oldpeak':oldpeak,'st_slope':st_slope}
        x_predict=pd.DataFrame(df_dict,index=[0])
        heart_disease = model.predict(x_predict)

        return render_template('output.html',age=age,gender=gender,chestpain=chestpain,restingbp=restingbp,cholesterol=cholesterol,fastingbs=fastingbs,restingecg=restingecg,maxhr=maxhr,exerciseangina=exerciseangina,oldpeak=oldpeak,st_slope=st_slope, heart_disease=bool(heart_disease[0]))


if __name__ == '__main__':        

    app.run(debug=True)
