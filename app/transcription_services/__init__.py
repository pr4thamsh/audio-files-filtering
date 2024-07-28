from .speech_recognition_transcriber import SpeechRecognitionTranscriber
from .deepgram_transcriber import DeepgramTranscriber

def get_transcriber(service: str = "speech_recognition"):
    if service == "speech_recognition":
        return SpeechRecognitionTranscriber()
    elif service == "deepgram":
        return DeepgramTranscriber()
    else:
        raise ValueError(f"Unknown transcription service: {service}")