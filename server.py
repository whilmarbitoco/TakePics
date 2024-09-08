
from flask import Flask, render_template, request, redirect
import base64, time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/up', methods=['POST'])
def upload():
    image = request.form.get('image_data')
    image = image.replace("data:image/jpeg;base64,", "")
    decoded_img = base64.b64decode(image)

    with open("uploads/"+ str(time.time()) + ".jpg", 'wb') as f:
        f.write(decoded_img)

    return redirect("/")

if __name__ == "__main__":
    app.run()