from flask import Flask, render_template, request, send_from_directory
from pytube import YouTube
from pydub import AudioSegment
import os, shutil

app = Flask(__name__)

# declare current file for download
current_file = ""

# Index/Homepage Endpoint
@app.route('/')
def index():
    return render_template('index.html')

# Download Endpoint
@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    file_format = request.form['file_format']

    if file_format == 'mp3':
        filename = download_mp3(url)
    else:
        filename = download_mp4(url)


    if filename:
        print(filename)
        return send_from_directory("./files", filename, as_attachment=True, mimetype='audio/mp3')
    else:
        return "Error downloading the video."

# Download and convert function for YT videos (audio)
def download_mp3(url):
    global current_file 

    clean_dir("./files")
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()

        out_file = video.download(output_path="./files")
        base, _ = os.path.splitext(out_file)
        current_file = str(base) + '.mp3'

        # Convert to MP3 using pydub
        audio = AudioSegment.from_file(out_file)
        audio.export(current_file, format="mp3")

        # Remove the original MP4 file
        os.remove(out_file)

        print(current_file)
        return os.path.basename(current_file)
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Download and convert function for YT videos (video)
def download_mp4(url):
    global current_file 

    clean_dir("./files")
    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').desc().first() # Get highest resolution stream with audio

        out_file = video.download(output_path="./files")

        print(out_file)
        return os.path.basename(out_file)
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Delete files being temporarily stored in ./files before
def clean_dir(directory_path):
    try:
        shutil.rmtree(directory_path) # del whole dir
        os.makedirs(directory_path) # create dir again

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0") # Remove host if you only want to hsot locally