from flask import render_template, url_for, flash, redirect, request
from cvs import app, dropzone
from cvs.forms import RequirementForm, UploadForm
import os

@app.route('/',methods=['GET'])
@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    form = RequirementForm()
    if form.is_submitted:
        pass
    return render_template('dashboard.html',form=form)

@app.route('/upload',methods=['GET','POST'])
def upload():
    form = UploadForm()
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('cvs/resume/', f.filename))
        flash('done')
    return render_template('upload.html',form=form)    