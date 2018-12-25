import os
from datetime import datetime

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import send_from_directory
from flask import session
import werkzeug
from werkzeug import secure_filename

from trim_face_image import TrimFace

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)
# limit upload file size : 2MB
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


def is_allowed_file(filename):
    return '.' in filename and filename.split('.')[-1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        try:
            img_file = request.files['img_file']
            if img_file and is_allowed_file(img_file.filename):
                trim_face = TrimFace()
                filename = datetime.now().strftime("%Y%m%d_%H%M%S") + secure_filename(img_file.filename)
                img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                if trim_face(os.path.join(app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['UPLOAD_FOLDER'],"trim_" + filename)):
                    # img_url = '/uploads/trim_' + filename
                    img_url = os.path.join(app.config['UPLOAD_FOLDER'],"trim_" + filename)
                    name = trim_face.classify_face(img_url)
                    return render_template('index.html', img_url=img_url,name=name)
                else:
                    return render_template('index.html', file_error='no face')
            else:
                return render_template('index.html', file_error='filetype error')
        except Exception as e:
            print(e)
            return render_template('index.html', file_error=e)
    else:
        return redirect(url_for('index'))

@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    return render_template('index.html', file_error='file size over')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
