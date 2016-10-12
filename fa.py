from flask import Flask
from flask import request
from flask import render_template
from clarifai.client import ClarifaiApi


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("pepper_inc.html")

@app.route('/', methods=['POST'])

def fune():
	pic = request.form['picture']
	object1 = request.form['object']
	clarifai_api = ClarifaiApi("gzPcmrpBHcjTmz2I4bu1_QQ9CNRuFAnyH6ZH7bJr", "U6hptJhZaowpSsu53yW4ETcWo4l1Wn7wUI9rt4fv")	
	result = clarifai_api.tag_image_urls(pic)
	result = (result['results'][0]['result']['tag']['classes'])
	print(result)
	if unicode(object1) in result:
		print('yes')
		return "True" 
	
	else:
		print ('false') 
		return "False" 


if __name__ == '__main__':
	app.run()