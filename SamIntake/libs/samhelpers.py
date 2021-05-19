import os
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