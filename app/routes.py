from flask import Blueprint, render_template, request, flash
from app.transcription_services import get_transcriber
from app.openai_filter import filter_and_categorize
import os

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'app/uploads'

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('index.html')
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html')
        
        if file:
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            
            transcriber = get_transcriber(request.form.get('service', 'speech_recognition'))
            transcription = transcriber.transcribe(filename)
            
            categories_prompt = request.form.get('categories_prompt', '')
            filtered_result = filter_and_categorize(transcription, categories_prompt)
            
            os.remove(filename)  # Clean up the uploaded file
            
            return render_template('result.html', 
                                   transcription=transcription, 
                                   filtered_result=filtered_result)
    
    return render_template('index.html')