#!/user/bin/env python
# -*- coding: utf-8 -*-

from utilsdm import delimiters, handleFiles, copyFileToServer
import shutil
from flask import Flask, request

LOCALPATH = 'C:\sdm\data\datafile'

app = Flask(__name__)

@app.route('/copyFile/<string:file>')
def copyFile(file):
    try:
        copyFileToServer(file)
    except:
        return 'Path not found!!!'
    return 'File Copied Succesfully!!!'

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
