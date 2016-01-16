#!/user/bin/env python
# -*- coding: utf-8 -*-

from utilsdm import delimiters, handleFiles, allowed_file
import shutil, os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

LOCALPATH = '../Uploads/'
#LOCALPATH = 'C:\sdm\data\datafile'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = LOCALPATH

@app.route('/copyFile', methods=['GET','POST'])
def copyFile():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route("/uploaded_file")
def uploaded_file():
    return 'File Uploaded'

@app.route("/handleFile", methods=['GET'])
def handleFile():
    try:
        f = request.args.get('file')
        d = delimiters(request.args.get('delimiter'))
        fields = request.args.get('fields')
        handleFiles(f, d, fields.split(','))
    except:
        return 'Could not copy files!!!'
    return 'Handle Files!!!'

@app.route("/")
def hello():
    return 'Is Alive!!!!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    #app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
