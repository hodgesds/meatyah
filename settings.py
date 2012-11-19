from server import *
USERNAME = 'dan'
PASSWORD = 'dodge05'
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','vcf','csv','mp3','mp4','mpg','avi','.r','.py'])
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT13\\x8b83'
CSRF_ENABLED = True
tools.config.from_object(__name__)
tools.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
tools.config['Music_Folder'] = '/home/dan/Dropbox/flaskyvids/static/music'
tools.config['Photo_Folder'] = '/home/dan/Dropbox/flaskyvids/static/photos'
tools.config['Thumbs_Folder'] = '/home/dan/Dropbox/flaskyvids/static/thumbs'
tools.config['Video_Folder'] = '/home/dan/Dropbox/flaskyvids/static/videos'
