import os
from flask import Flask,request,jsonify
from werkzeug.utils import secure_filename
app = Flask('app')

app.config["UPLOAD_FOLDER"] = "archivos"
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg', 'gif','pdf','txt','doc','docx'])


def extesiones(file):
  file = file.split('.')
  if file[1] in ALLOWED_EXTENSIONS:
    return True
  return False


@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/user/archivos', methods=['POST'])
def guardaArchivo():
  file = request.file["uploadFile"]
  filename = secure_filename(file.filename)
  if file and extesiones(filename):
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return jsonify({"message":"Subido correctamente"})
  return jsonify({"message":"No subido"})

app.run(host='0.0.0.0', port=8080)
