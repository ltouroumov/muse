from wtforms import Form, StringField, validators


class ProjectForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    summary = StringField('Summary')
