from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine

from muse_writer.data import session, setup_db, init_db
from muse_writer.models import Project
from muse_writer.forms import ProjectForm


app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


@app.route('/')
def index():
    projects = session.query(Project).order_by('name')
    return render_template('index.html',
                           projects=projects)


@app.route('/project/<int:project_id>')
def editor(project_id):
    project = session.query(Project).filter_by(id=project_id).first()
    return render_template('editor.html',
                           project=project)


@app.route('/project/new', methods=['GET', 'POST'])
def new_project():
    form = ProjectForm(request.form)
    if request.method == 'POST' and form.validate():
        project = Project(name=form.name.data,
                          summary=form.summary.data,
                          date_created=datetime.now())
        session.add(project)
        session.commit()
        return redirect(url_for('index'))

    return render_template('form.html',
                           project=None)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    from os import path

    # db_url = 'sqlite:///%s' % path.join(path.realpath('.'), 'data.db')
    db_url = "mysql+pymysql://muse@localhost/muse"
    engine = setup_db(db_url)
    init_db(engine)

    app.run(debug=True)
