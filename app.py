from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        audio_only = request.form.get('audio') == 'on'
        resolution = request.form.get('resolution', 'best')

        if not url:
            flash("Please enter a YouTube URL", "error")
            return redirect(url_for('index'))

        try:
            ydl_opts = {
                'format': resolution if not audio_only else 'bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
                'noplaylist': True,
                'quiet': True,
                'nocheckcertificate': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info_dict)
                final_filename = os.path.basename(filename)

            return redirect(url_for('download_file', filename=final_filename))

        except Exception as e:
            flash(f"Error: {str(e)}", "error")
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
