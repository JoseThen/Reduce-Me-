
from flask import Flask, render_template as thing, redirect, request, url_for, abort, flash, session, send_from_directory
from ffmpy import FFmpeg as god
from werkzeug import secure_filename
import os
import subprocess


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'video/'

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mov', 'mp4,' , 'tf', 'wmv', 'avi', 'flv'])


# os.chdir(os.path.join(app.config['UPLOAD_FOLDER']))





@app.route('/')
def index():
    return thing('index.html')


# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():


#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
        

#         stream_file = request.files['file']

#         ff = god(
#             inputs={'pipe:0': None},
#             outputs={'pipe:1': '-f mp4'}
#         )
#         stdout, stderr = ff.run(input_data=stream_file.read('mov'), stdout=subprocess.PIPE)
#         return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
#     '''


   # if request.method == 'POST':
   #    f = request.files['file']
   #    f.save(secure_filename(f.filename))
   #    videoReduce(f.filename)
   #    return 'file uploaded successfully'

# Route that will process the file upload
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # file.save(filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        print 'gotfile'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print 'gotfile2222222222222222222222222222222222222222'
        return peggy(filename)
        # return redirect(url_for("compress", filename = filename))

    print 'Peggy Did not Run Son'
                               

def peggy(filename):
	output_name = changey(filename)
	subprocess.call('ffmpeg -i '+str(filename)+' -b 1000000 '+output_name, cwd=os.path.join(app.config['UPLOAD_FOLDER']), shell=True)
	return redirect(url_for("compress", filename=output_name))
	# subprocess.call('ffmpeg -r 10 -i frame%03d.png -r ntsc '+str(out_movie), shell=True)

def changey(filename):
	file = str(filename)
	splitter = file.split(".")
	rs = splitter[0][::-1]+"."+splitter[1]
	return rs


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



@app.route('/compress/<filename>')
def compress(filename):
    return thing("compress.html", filename = filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/compress/<filename>')
def compress(filename):
    return thing("compress.html", filename = filename)

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def videoReduce(input):
    box = god(inputs={input: None}, outputs={'output.mp4': '-f mp4'})
    box.cmd
    box.run
    return 0



def videoReduce(input):
	box = god(inputs={input: None}, outputs={'output.mp4': '-f mp4'})
	box.cmd
	box.run
	return 0







if __name__ == '__main__':
<<<<<<< HEAD
 	app.run(debug=True, host='0.0.0.0')
 	
 	
=======
     app.run(debug=True, host='0.0.0.0')
>>>>>>> f0ac46f1b9884587536f1a40e670267a4fba2408
