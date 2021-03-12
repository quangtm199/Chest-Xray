from flask import Flask, render_template,request
import os

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='static'

@app.route("/", methods=['POST','GET'])
def home():
    if request.method == "GET":
       return render_template("index.html")
    else:
        image_file=request['file']
        path_to_save=os.path.join(app.config['UPLOAD_FOLDER'],image_file)
        image_file.save(path_to_save)

        return "Day la home"
if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)