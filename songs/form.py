from songs import app, connection, render_template, request
from flaskext.wtf import Form, TextField, TextAreaField, Required


class SongForm(Form):
	lyrics = TextAreaField()


@app.route('/form/', methods=['GET', 'POST'])
def form():
	form = SongForm()
	
	return render_template('form.html', form=form)
	
@app.route('/hop/', methods=['GET', 'POST'])
def hop():
	lyrics=request.form['lyrics']
	
	return render_template('hop.html', lyrics=lyrics)