import os
import time
from whisper_cpp_python import Whisper

class STT:
    def __init__(self, config):
        self.model = Whisper(model_path=config["WHISPER_MODEL_PATH"])

    def recognize(self, audioPath):
        try:
            outFile = f"out-{time.strftime('%M_%S')}.wav"
            os.system(f"ffmpeg -loglevel quiet -i {audioPath} -ar 16000 -ac 1 -f wav {outFile}")
            result = self.model.transcribe(open(outFile, "rb"), language="ru")
            os.remove(audioPath)
            os.remove(outFile)
            return result["text"]
        except Exception as e:
            exit(e)