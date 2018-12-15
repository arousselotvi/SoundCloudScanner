import json
from flask import Flask, render_template,redirect,url_for,request
from queryForm import QueryForm
from search import getResults
from search import myClientId
app = Flask(__name__)
#Secret key to use all the attributes of flask
app.config['SECRET_KEY'] = 'topsecret'
#Main page with the form
@app.route('/',methods=['GET', 'POST'])
def submitQuery():
    form=QueryForm()
    #When the search button is pressed
    if form.validate_on_submit():
        #retrieve the fields values
        myFilteredResults=getResults(form.keyWords.data,form.genre.data,form.label.data)
        messages=json.dumps(myFilteredResults)
        #redirect to results page with the results as parameter
        return redirect(url_for('.displayResults',messages=messages))
    return render_template('searchForm.html',title='Search for sound', form=form)
#Results page
@app.route('/results')
def displayResults():
    results = request.args['messages']
    results=json.loads(results)
    #Create list with link and title to pass it in html
    resultsList=[]
    for track in results:
        resultsList.append([track['permalink_url'], track['title']])
    return render_template('results.html', resultsList=resultsList)
if __name__ == '__main__':
    app.run()
