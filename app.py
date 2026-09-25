import assemblyai as aai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
aai.settings.api_key = ASSEMBLYAI_API_KEY

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        language = request.form.get("language")
        file = request.files.get("file")
        if file:
            filename = file.filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Transcribe the audio using AssemblyAI
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(filepath)

            # Return the transcript as JSON
            return jsonify({"transcript": transcript.text})

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
