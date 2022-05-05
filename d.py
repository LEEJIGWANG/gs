from flask import Flask,Blueprint, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

#bp = Blueprint('image', __name__, url_prefix='/image')

# HTTP POST방식으로 전송된 이미지를 저장
@app.route('/image', methods=['GET', 'POST'])
def save_image():
    if request.method == 'POSt':
        f = request.files['file']
        f.save('./save/' + secure_filename(f.filename))
    return 'done!'

if __name__ == "__main__":
    		app.run()
