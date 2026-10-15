
from flask import Flask, render_template, request, send_file
from pytubefix import YouTube
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url", "").strip()

    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        path = stream.download(filename="audio.mp4")

        return send_file(
            path,
            as_attachment=True,
            download_name="audio.mp4"
        )

    except Exception as e:
        return f"Download failed: {e}", 400

if __name__ == "__main__":
    app.run(debug=True)
