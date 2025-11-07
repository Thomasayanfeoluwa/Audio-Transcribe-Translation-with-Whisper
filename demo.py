# import openai
import assemblyai as aai
import os
from dotenv import load_dotenv


load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")

aai.settings.api_key = ASSEMBLYAI_API_KEY

audio_file_path = "Recording.m4a"

with open(audio_file_path, "rb") as audio_file:

    transcript = aai.Transcriber().transcribe(audio_file)

print(transcript.text)