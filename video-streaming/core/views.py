import os
from flask import send_file
from core import app
from config import basedir

@app.route('/video')
def video():
    return send_file(os.path.join(basedir, 'videos', 'SampleVideo_1280x720_30mb.mp4'))