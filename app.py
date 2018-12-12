import requests
import urllib2
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/superman")
def superman():
    return render_template('superman.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/recipesideas")
def recipesideas():
    return render_template('recipesideas.html')

@app.route("/instagramsuggestions")
def instagramsuggestions():
    return render_template('instagramsuggestions.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

#@app.route("/bbcfood", methods=['GET', 'POST'])
#def bbcfood():
#	return render_template('bbcfood.html')


required = urllib2.Request('http://www.food2fork.com/api/search?key=5b7660d0e7091a482b64648127a8c732&q=chicken%20breast&page=2', headers={'User-Agent' : "Magic Browser"})
response = urllib2.urlopen(required)
html = response.read()

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://www.food2fork.com/api/search?key=5b7660d0e7091a482b64648127a8c732&q={}&page=2".format("chicken"))

# Print the status code of the response.
print(response.status_code)


if __name__ == '__main__':
    app.run(debug=True)

