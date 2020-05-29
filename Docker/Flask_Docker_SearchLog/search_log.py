import datetime;
import requests
import json
import os
from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__)

@app.route('/create_log',methods = ['POST'])
def create_log():
		if request.method == 'POST':
			search_data = request.get_json();
			print(search_data,"****************************************");
			search_data = addcurrTime(search_data);
			print("request: "+str(search_data));
			print(type(search_data));
			storedataInJson(search_data);
			calcFreq(search_data);
			d = {'log':"done"};
			print("log obj: "+str(d));
			print("log obj type: "+str(type(d)));
			return jsonify(d);
			# return "done";
			# response = requests.post("http://127.0.0.1:5003/gett",data=request.get_data());
			# print("type: "+str(type(response)));
			# return json.dumps(response.text);

def storedataInJson(search_data):
	floc = "searchLog.json"

	if not os.path.exists(floc):
		logs = [];
		print("Not Exists");
	else:
		with open("searchLog.json", mode='r',newline="\n") as file1:
			logs = json.load(file1);
			file1.close();
			print("Exists");
	logs.append(search_data);
	with open("searchLog.json", mode='w',newline="\n") as file1:
		json_article=json.dumps(logs);
		file1.write(json_article);
		file1.close();

def addcurrTime(search_data):
	cur_time = str(datetime.datetime.now()).split('.')[0];
	search_data["time"] = cur_time;
	return search_data;
		# print("type: "+str(type(logs)));
		# print(logs);

def calcFreq(search_data):
	floc = "keyFreq.json"
	found = False;
	if not os.path.exists(floc):
		logs = [];
		print("Not Exists");
	else:
		with open("keyFreq.json", mode='r',newline="\n") as file1:
			logs = json.load(file1);
			file1.close();
			print("Exists");
			for sin_key in logs:
				if search_data['keyword'] == sin_key['keyword']:
					if search_data['type'] == "title":
						sin_key['title_frequency'] = sin_key['title_frequency']+1;
						sin_key['total'] = sin_key['total']+1;
					else:
						sin_key['author_frequency'] = sin_key['author_frequency']+1;
						sin_key['total'] = sin_key['total']+1;
					found = True;
					break;
	if not found:
		single_keyword = {};
		single_keyword['keyword'] = search_data['keyword'];
		if search_data['type'] == "title":
			single_keyword['title_frequency'] = 1;
			single_keyword['author_frequency'] = 0;
			single_keyword['total'] = 1;
		else:
			single_keyword['author_frequency'] = 1;
			single_keyword['title_frequency'] = 0;
			single_keyword['total'] = 1;
		logs.append(single_keyword);
	with open("keyFreq.json", mode='w',newline="\n") as file1:
		json_article=json.dumps(logs);
		file1.write(json_article);
		file1.close();



if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5002",debug=True);
