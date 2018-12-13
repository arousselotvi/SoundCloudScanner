from flask import Flask, render_template,redirect
from queryForm import QueryForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'topsecret'
@app.route('/',methods=['GET', 'POST'])
def submitQuery():
    form=QueryForm()
    if form.validate_on_submit():
        print(form.keyWords.data)
        print(form.genre.data)
        print(form.label.data)
        return redirect('/')
    return render_template('searchForm.html',title='Search for sound', form=form)

if __name__ == '__main__':
    app.run()
