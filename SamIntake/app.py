import os
from flask import Flask, json, request, jsonify
import logging

import errno
import ulid
import time
import mimetypes
import json

from datetime import datetime
from pathlib import Path
from imutils import paths
import shutil

import cv2

###############################
## SAMedia Helper Functions
###############################
def getImagesIn(dirin):
    allImagePaths = sorted(list(paths.list_images(dirin)))
    return allImagePaths

def getImageModifiedTs(pathin):
    modifiedTs = int(os.path.getmtime(pathin))
    return modifiedTs

def getUlid(ts):
    if not ts:
        ts = int(time.time())
    uid = ulid.from_timestamp(ts)
    return uid

def fileNameParts(pathin):
    path = Path(pathin)
    ext = path.suffix
    name = path.stem
    return (name, ext)

def getMimeType(pathin):
    mt = mimetypes.guess_type(pathin)
    return mt

def createDir(dirin):
    try:
        os.makedirs(dirin, 0o777, True)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
            
def copyNoMeta(src, tgt):
    cpy_result = shutil.copy(src, tgt)
    return cpy_result
    
def copyWithMeta(src, tgt):
    cpy_result = shutil.copy2(src, tgt)
    return cpy_result
    
def moveFile(src, tgt_dir):
    new_fp = shutil.move(src, tgt_dir)
    return new_fp

########################################
## End SAMedia Helper Functions
########################################

# Initalize Log file
def setLogfile(log_level=logging.INFO):
    logfile = "/data/logs/SAMIntakeLogs.log" #os.environ.get('LOGFILE')
    print(logfile)
    logging.basicConfig(filename=logfile, format='%(asctime)s  * %(message)s', encoding='utf-8', level=log_level)
    logging.info("Logging has been activated")

# Begin Intake Process
def intakeSAMStep01(directory, filename):
    logging.info("Begin intake for {}{}".format(directory, filename))
    fp = directory + filename
    result = getImageModifiedTs(fp)
    return result



# Define app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():    
    return "HERE WE ARE"

@app.route('/newsam', methods=['POST'])
def newSAMedia():
    content = request.json
    tdirectory = content['directory']
    filename = content['filename']
    
    # replace directory path with proper data path
    directory = tdirectory.replace('/home/samadmin/samlocal/imgproc/SAMData', '/data')

    logging.info("The file {} was uploaded to the {} directory".format(filename, directory))
    
    # begin image intake process
    result = intakeSAMStep01(directory, filename)

    return str(result)


if __name__ == '__main__':
    setLogfile()

    app.run(debug=True, host='0.0.0.0')