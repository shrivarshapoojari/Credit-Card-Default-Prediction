from flask import Flask , request , jsonify , render_template
 
import pickle
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)
model=pickle.load(open('models/randomforestn.pkl','rb'))
standard_scaler=pickle.load(open('models/scalern.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        credit_limit=int(request.form.get('creditLimit'))
        gender=int(request.form.get('gender'))
        education=int(request.form.get('education'))
        marriage=int(request.form.get('maritalStatus'))
        age=int(request.form.get('age'))
        repay1=int(request.form.get('repaymentStatusSep'))
        repay2=int(request.form.get('repaymentStatusAug'))
        repay3=int(request.form.get('repaymentStatusJul'))
        repay4=int(request.form.get('repaymentStatusJun'))
        repay5=int(request.form.get('repaymentStatusMay'))
        repay6=int(request.form.get('repaymentStatusApr'))
        bill1=int(request.form.get('billAmtSep'))
        bill2=int(request.form.get('billAmtAug'))
        bill3=int(request.form.get('billAmtJul'))
        bill4=int(request.form.get('billAmtJun'))
        bill5=int(request.form.get('billAmtMay'))
        bill6=int(request.form.get('billAmtApr'))
        pay1=int(request.form.get('payAmtSep'))
        pay2=int(request.form.get('payAmtAug'))
        pay3=int(request.form.get('payAmtJul'))
        pay4=int(request.form.get('payAmtJun'))
        pay5=int(request.form.get('payAmtMay'))
        pay6=int(request.form.get('payAmtApr'))
        new_data=[[credit_limit, gender,education, marriage, age, repay1,repay2,repay3,repay4,repay5,repay6, bill1, bill2, bill3, bill4, bill5, bill6, pay1, pay2, pay3, pay4, pay5, pay6]]
        scaled_data = standard_scaler.transform(new_data)
        result=model.predict(scaled_data)
        print(new_data)
        prediction_result = result[0]
        if prediction_result==0 :
            return render_template('nodefault.html')
        
        else:
            return render_template('decreaselimit.html')

    else:
        return render_template('index.html')
    


# if __name__=='main':
#     app.run(debug=True)
