import json;
import requests;
from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__)

@app.route('/search',methods = ['POST'])#,'GET'])
def search():
		if request.method == 'POST':
			print(request.get_json(),"**************************************************************")
			response = requests.post("http://54.205.70.41:5002/create_log",json=request.get_json());
			print("type: "+str(type(response.json())));
			print(response.json(),flush=True);

			response = requests.post("http://18.212.37.111:5003/gett",json=request.get_json());
			for dictt in response.json():
				print("length: "+str(len(dictt['authors'])));
			print("type: "+str(type(response.json())),flush = True);
			print("response getdata: "+str(response.json()),flush = True);
			return jsonify(response.json());	


@app.route('/addnote',methods = ['POST'])#,'GET'])
def add_note():
	response = requests.post("http://3.91.183.79:5004/appendnote",json = request.get_json());
	print("addnote res: "+str(response.json()),flush=True);
	print("addnote res type: "+str(type(response.json())));
	return jsonify(response.json());


@app.route('/shownote',methods = ['POST'])
def show_note():
	print("keyword: "+request.get_json()['keyword']);
	response = requests.post("http://3.91.183.79:5004/shownote",json = request.get_json());
	print("shownote res: "+str(response.json()));
	print("shownote res type: "+str(type(response.json())));
	return jsonify(response.json());
	

if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5001",debug=True);