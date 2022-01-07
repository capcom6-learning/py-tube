
from flask import abort, redirect, render_template, request, url_for

from core import app

from . import metadata


@app.route('/', methods=['GET'])
def index():
    videos = metadata.select_video()
    return render_template('video-list.html', videos=videos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload-video.html')

@app.route('/history', methods=['GET'])
def history():
    return render_template('history.html')

@app.route('/video', methods=['GET'])
def video():
    id: str = request.args.get('id')
    if not id:
        return redirect(url_for('index'))

    video = metadata.get_video(id)
    if not video:
        return abort(404)

    return render_template('play-video.html', video=video)
