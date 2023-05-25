from flask import Flask,render_template,request,make_response
import pyttsx3
from time import sleep
from threading import Thread
from myTraining import pn
app = Flask(__name__)
import pickle

file=open('model.pkl','rb')
model=pickle.load(file)
file.close()

def intro_voice():   
    converter = pyttsx3.init()
    converter.setProperty('rate', 180)
    converter.setProperty('volume', 1.0)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    converter.say("Hello!")
    converter.say("""Welcome to our Heart Disease Prediction website.""")
    #converter.say("I am Amanza, your web assistant.")
    sleep(1)
    converter.runAndWait()

def predicted_voice(text1, text22):
    text1 = text1
    text22 = text22
    converter = pyttsx3.init()
    converter.setProperty('rate', 180)
    converter.setProperty('volume', 1.0)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    converter.say(text1)
    converter.say(text22)
    sleep(1)
    converter.runAndWait()


@app.route('/',methods=['GET','POST'])

def hello_world():
    if request.method=='POST':
        myDict=request.form
        name = str(myDict['name'])
        age=int(myDict['age'])
        anaemia=int(myDict['anaemia'])
        creatinine_phosphokinase=int(myDict['creatinine_phosphokinase'])
        diabetes=int(myDict['diabetes'])
        ejection_fraction=int(myDict['ejection_fraction'])
        high_blood_pressure=int(myDict['high_blood_pressure'])
        platelets=int(myDict['platelets'])
        serum_creatinine=int(myDict['serum_creatinine'])
        serum_sodium=int(myDict['serum_sodium'])
        sex=int(myDict['sex'])
        smoking=int(myDict['smoking'])
        maxhr=int(myDict['maxhr'])
        cp=int(myDict['cp'])
        cholesterol=int(myDict['cholesterol'])
        fh=int(myDict['fh'])
        Medication=int(myDict['Medication'])
        inputFeatures=[age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,cp,cholesterol,maxhr]
        infProb=model.predict_proba([inputFeatures])[0][1]
        pv = round(infProb*100)
        predicted = pn(fh, Medication)
        print(infProb)
        text1 = "Hey" + " " + name
        text2 = "You have the probability of Heart Disease is "
        text22 = "You have the probability of Heart Disease is ", predicted, "percentage"
        text3 = "%"
        print(predicted)
        print(pv)
        
        thr = Thread(target=predicted_voice, args=[text1, text22])
        thr.start()

        return render_template('index.html', text1=text1,org=pv, text2=text2, predict=predicted, text3=text3)

    thr = Thread(target=intro_voice)
    thr.start()

    return make_response(render_template('index.html'))

if __name__ == "__main__":
    app.run(debug=True)