from flask import Flask

UPLOAD_FOLDER = 'C:/Users/ADMIN/Desktop/Projectst/dea/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from flask import Flask, render_template, request, redirect, flash, url_for
import main
from main import getPrediction
import urllib.request
from app import app
from werkzeug.utils import secure_filename
#from main import getPrediction
import os
import random
@app.route('/')
def homie():
    print("Hellooo")
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_file():
    preds=random.randint(0,9)
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')

            
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            getPrediction(filename)
            label= getPrediction(filename)
            print("Executeeeed/n\n")
            print(label)
            label=label
            pred=label.max()
            index=label.argmax()
            arr=['Safe driving', 
                'Texting - right', 
                'Talking on the phone - right', 
                'Texting - left', 
                'Talking on the phone - left', 
                'Operating the radio', 
                'Drinking', 
                'Reaching behind', 
                'Hair and makeup', 
                'Talking to passenger']
            result="Predicted as: "+ arr[preds]
            return result
            


if __name__ == "__main__":
    app.run(host='127.0.0.1', threaded=True)