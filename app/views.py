import os
import logging
from flask import render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
		return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def upload_song():
    if request.method == 'POST':
    	logging.debug('if request.method == 'POST': is TRUE')
        file = request.files['file']
        if file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', filename=filename)
    return render_template('index.html')
 
@app.route('/uploads/<filename>')
def uploaded_song(filename):
	return send_from_directory(app.config ['UPLOAD_FOLDER'],filename, as_attachment=True)