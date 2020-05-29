import json;
import requests;
from flask import Flask, redirect, url_for, request, render_template, jsonify
app = Flask(__name__)

@app.route('/client',methods = ['GET'])#,'GET'])
def home():
	return render_template('client.html',dataflag=False,dataNotes=False);
	# if request.method == 'POST':
	# 		ttype = request.form['type'];
	# 		#author = request.form['author'];
	# 		keyword = request.form['keyword'];
	# 		d = {'type':ttype,'keyword':keyword};

	# 		response = requests.post("http://3.87.202.58:5001/search",data=json.dumps(d));
	# 		response = requests.post("http://127.0.0.1:5000/add_note",data=json.dumps(response.text));

@app.route('/getdata',methods = ['POST'])#,'GET'])
def get_data():
	if request.method == 'POST':
		ttype = request.form['type'];
		#author = request.form['author'];
		keyword = request.form['keyword'];
		d = {'type':ttype,'keyword':keyword};

		response = requests.post("http://3.87.202.58:5001/search",json=d);
		print("getdata res: "+str(response.json()),flush=True);
		print("type getdata: "+str(type(response.json())));
		for dictt in response.json():
			print("length: "+str(len(dictt['authors'])));
		#response = requests.post("http://127.0.0.1:5000/add_note",data=json.dumps(json.loads(response.text)));
		return render_template('client.html',data = response.json(),key = keyword,dataflag=True);

@app.route('/addnote',methods = ['POST'])#,'GET'])
def add_note():
	print("key: "+str(request.form['keyword']));
	note = request.form['note'];
	keyword = request.form['keyword'];
	d = {'keyword':keyword,'note':note};

	print("req: "+str(d));
	response = requests.post("http://3.87.202.58:5001/addnote",json = d);
	print("addnote res: "+str(response.json()),flush=True);
	print("type addnote: "+str(type(response.json())));
	return render_template('client.html',msg = response.json());	#aa haji jovanu baki

@app.route('/shownote',methods = ['POST'])
def show_note():
	print("key: "+str(request.form['keyword']),flush=True);
	keyword = request.form['keyword'];
	d = {'keyword':keyword};

	response = requests.post("http://3.87.202.58:5001/shownote",json = d);
	print("shownote res: "+str(response.json()),flush=True);
	print("type shownote: "+str(type(response.json())));
	return render_template('client.html',notedata = response.json(),dataNotes=True);

if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5000",debug=True);