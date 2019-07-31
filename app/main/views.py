from flask import render_template, session, redirect, url_for, current_app, send_from_directory
from .. import db
from ..models import User
from . import main
from .forms import NameForm
from werkzeug.utils import secure_filename
from flask import current_app as app
import os


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        file = form.photo.data
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['filename'] = filename
      
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))

    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False), filename=session.get('filename'))

@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']