import whisper
import os

# Load Whisper model once
model = whisper.load_model("base")


def transcribe_audio(file_path):
    """
    Transcribes an existing audio file using Whisper.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("Audio file not found.")

    result = model.transcribe(file_path)
    return result["text"]