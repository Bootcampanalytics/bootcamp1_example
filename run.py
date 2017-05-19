import json
import pprint
from os.path import join, dirname
import os
from watson_developer_cloud import DocumentConversionV1
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from flask import Flask, render_template, request
from werkzeug import secure_filename
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# Doc conversion
document_conversion = DocumentConversionV1(
  username='9b4798e3-5380-40c4-9d9f-140c34720ee5',
  password='upIn5uG3soR7',
  version='2015-12-15'
)

#Natural language understanding
cred={'user':'f060dfc8-0f2d-4801-a2e1-bde638ec10b6','pass':'rvt40g4afiuF'}
NLU_url='https://gateway.watsonplatform.net/natural-language-understanding/api/v1'


@app.route('/', methods = ['GET', 'POST'])
def serve_page():
	if request.method == 'POST':
		model_id = request.values.get('model_id')
		resp=requests.delete(NLU_url+'/models/'+model_id,auth=HTTPBasicAuth(cred['user'], cred['pass']))
		return render_template('index.htm',model_id="model deleted")
	else:
		resp=requests.get(NLU_url+'/models',auth=HTTPBasicAuth(cred['user'], cred['pass'])).content
		model_id=json.loads(resp.decode('utf8'))['models'][0]['model_id']
		return render_template('index.htm',model_id=model_id)

@app.route('/convert', methods = ['GET', 'POST'])
def convert_file():
	if request.method == 'POST':
		format = request.values.get('format')
		config = {'conversion_target': format}
		f = request.files['file']
		basedir = os.path.abspath(os.path.dirname(__file__))
		f.save(os.path.join(basedir, f.filename))
		with open(os.path.join(basedir, f.filename), 'rb') as document:
			return document_conversion.convert_document(document=document,config=config).content
		return 'there was a problem sending the file'	
	

@app.route('/analzye', methods = ['GET', 'POST'])
def analyze_file():
	config = {'conversion_target': 'NORMALIZED_TEXT'}
	if request.method == 'POST':
		f = request.files['file']
		model_id = request.values.get('model_id')
		basedir = os.path.abspath(os.path.dirname(__file__))
		f.save(os.path.join(basedir, f.filename))
		with open(os.path.join(basedir, f.filename), 'rb') as document:
			clear_text = document_conversion.convert_document(document=document,config=config).content
			input_for_NLU=json.dumps({"text": clear_text,"features":{"entities": {"model": model_id}}})
			ff=requests.post(NLU_url+'/analyze?version=2017-02-27',data=input_for_NLU,auth=HTTPBasicAuth(cred['user'], cred['pass']),headers={'content-type': 'application/json'}).content
			return json.dumps(ff.decode('utf8'),sort_keys=True, indent=4, separators=(',', ': '))
		return 'there was a problem sending the file'	
	
	
		


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=int(port))
