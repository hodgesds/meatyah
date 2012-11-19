import csv, mmap, os, subprocess, tempfile
from flask import *
from server import *
from flask.ext.wtf import Form, SelectField, IntegerField, TextField, BooleanField
from flask.ext.wtf import Required
from functools import wraps
from flask import request, session, g, redirect, url_for
from pic_functions import *
# When you flash a message make sure it is one of the following:
# info, success, error or alert
###################################
# Forms
###################################

###################################
# Login/Logout
###################################
@tools.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != tools.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != tools.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in',"success")
            return redirect(url_for("home"))
    return render_template('login.html', error=error)
    
@tools.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out','info')
    return redirect('/')
        
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@tools.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('base.html')


@tools.route('/music', methods=['GET', 'POST'])
@login_required
def music():
    if request.method == "POST":
        # Get form data
        return render_template('music.html')
    else:
        mp3 = os.listdir(tools.config['Music_Folder'])
        return render_template('music.html',songs=mp3)

@tools.route('/movies', methods=['GET', 'POST'])
@login_required
def movies():
    if request.method == "POST":
        # Get form data
        return render_template('movies.html')
    else:
        vidlist = os.listdir(tools.config['Video_Folder'])
        return render_template('movies.html',videos=vidlist)

@tools.route('/pics', methods=['GET', 'POST'])
@login_required
def pics():
    if request.method == "POST":
        # Get form data
        return render_template('pics.html')
    else:
        piclist = os.listdir(tools.config['Photo_Folder'])
        return render_template('pics.html',photos=piclist)


@tools.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == "POST":
        # Get form data
        ufile = request.files['ufile']
        ufolder = request.form['ufolder']
        print ufile.filename,ufile.content_type,ufolder
        if 'pics' in ufolder:
            ufile.save(str(tools.config['Photo_Folder']+"/"+ufile.filename))
            pic_resizer()
        if 'music' in ufolder:
            ufile.save(str(tools.config['Music_Folder']+"/"+ufile.filename))
        if 'movies' in ufolder:
            ufile.save(str(tools.config['Video_Folder']+"/"+ufile.filename))
        flash(str(ufile.filename+" uploaded successfully"),'success')
        return render_template('upload.html')
    return render_template('upload.html')


@tools.route('/uploads/<path:filename>')
@login_required
def download_file(filename):
    return send_from_directory(tools.config['UPLOAD_FOLDER'],filename, as_attachment=True)


@tools.route('/test')
@login_required
def dfile():
    #return send_file(mp3,as_attachment=True)
    return Response(stream_with_context(open(mp3,'r')))
    

