from flask import Blueprint, current_app, render_template, send_from_directory, request
from zipfile import ZipFile
import os
from werkzeug.utils import secure_filename
import shutil

from .FileManage import FileManage
from .Exception import NotIsDirException

browse_file_blueprint = Blueprint('browsefile', __name__, url_prefix='/browsefile')

@browse_file_blueprint.route('/list/', defaults={"path": ""})
@browse_file_blueprint.route('/list/<path:path>')
def file_list(path):
    abs_path = ""
    if len(path) == 0:
        abs_path = current_app.config["ROOT_PATH"]
    else:
        abs_path = current_app.config["ROOT_PATH"] + "/" + path
    node_list = None
    try:
        node_list = FileManage.get_list(abs_path)
    except Exception as e:
        print (str(e))
    if node_list == None:
        return f"访问路径失败: {path}"
    tmp_path_list = []
    tmp_str = ""
    for f in path.split('/'):
        tmp_str += ('/'+f)
        tmp_path_list.append({"file":f, "path":tmp_str})
    return render_template("filelist.html", node_list=node_list, root_path="/browsefile/list", path_list=tmp_path_list)

@browse_file_blueprint.route('/download/<path:path>')
def file_download(path):
    abs_path = current_app.config["ROOT_PATH"] + "/" + path
    try:
        return send_from_directory(directory=os.path.dirname(abs_path), path=os.path.basename(abs_path), as_attachment=True)
    except IOError:
        return "下载不了哇！" + str(path)

@browse_file_blueprint.route('/upload', methods = ['POST'])
def file_upload():
    path = request.form.get('path')
    print (request.form.get('path'))
    abs_path = current_app.config["ROOT_PATH"] + "/" + path
    for f in request.files.getlist('file1'):
        print (f"f.filename: {f.filename}")
        if f.filename == "":
            continue
        elif f:
            f.save(os.path.join(abs_path, secure_filename(f.filename)))
    return "1"

@browse_file_blueprint.route('/delete/<path:path>')
def file_delete(path):
    print(f"Delete: {path}")
    abs_path = current_app.config["ROOT_PATH"] + "/" + path
    FileManage.delele(abs_path)
    return path

@browse_file_blueprint.route('/createfolder/<path:path>')
def folder_create(path):
    print(f"folder_create: {path}")
    abs_path = current_app.config["ROOT_PATH"] + "/" + path
    FileManage.folder_create(abs_path)
    return path
