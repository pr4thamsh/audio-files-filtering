from abc import ABC, abstractmethod

class BaseTranscriber(ABC):
    @abstractmethod
    def transcribe(self, file_path: str) -> str:
        """
        Transcribe the audio file at the given path.
        
        :param file_path: Path to the audio file
        :return: Transcribed text
        """
        pass