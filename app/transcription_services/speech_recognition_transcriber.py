import speech_recognition as sr
from .base_transcriber import BaseTranscriber

class SpeechRecognitionTranscriber(BaseTranscriber):
    def transcribe(self, file_path: str) -> str:
        recognizer = sr.Recognizer()
        
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Speech Recognition could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results from Speech Recognition service; {e}"