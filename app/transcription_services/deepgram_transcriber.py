import os
from dotenv import load_dotenv
from deepgram import DeepgramClient, PrerecordedOptions, FileSource
from .base_transcriber import BaseTranscriber

load_dotenv()

class DeepgramTranscriber(BaseTranscriber):
    def __init__(self):
        self.DEEPGRAM_API_KEY = os.getenv("DG_API_KEY")
        self.client = DeepgramClient(self.DEEPGRAM_API_KEY)

    def transcribe(self, file_path: str) -> str:
        with open(file_path, 'rb') as file:
            buffer_data = file.read()

            try:
                payload: FileSource = {
                    "buffer": buffer_data,
                }

                options = PrerecordedOptions(
                    model="nova-2",
                    smart_format=True,
                )

                response = self.client.listen.rest.v("1").transcribe_file(payload, options)

                return response['results']['channels'][0]['alternatives'][0]['transcript']

            except Exception as e:
                return f"Error during transcription: {str(e)}"