import requests
import json
import os
from flask import Flask, redirect, url_for, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

usr = "csci5409";
pswd = "mongodb";

# client = pymongo.MongoClient("mongodb+srv://" + usr + ":" + pwd + "@firstcluster-obuqd.mongodb.net/test?retryWrites=true&w=majority");
# db = client['assgn3'];
# collection = db['bookdata'];

client = MongoClient("mongodb://csci5409:mongodb@34.205.72.123/assgn3");
db = client['assgn3'];
collection = db['bookdata'];
# collection.insert(book_json);
# client.close();

@app.route("/gett",methods = ['POST'])#, methods=['POST'])
def gett():
	# req_data = request.get_json();
	# collection.insert_one(req_data).inserted_id;
	# return ('',204);
	print("Hello");
	search_data = request.get_json();
	print("request: "+str(search_data));
	response = db_search(search_data);
	#add data in catalogue
	if not len(response) == 0:
		catalogue_add(response);
	else:
		print("No Data for keyword in database",flush=True);
	print("response: "+str(response),flush=True);
	# documents = collection.find({"authors":"Emily Brontë"});
	# response= [];
	# for document in documents:
	# 	document['_id'] = str(document['_id']);
	# 	response.append(document);
	# print("response: "+str(response),flush=True);
	# return "Done";
	return jsonify(response);

def catalogue_add(add_data):
	print("In catalogue add");
	response=[];
	filedata=[];
	floc = "catalogue_data.json"
	if not os.path.exists(floc):
		filedata = [];
		print("File Not Exists",flush=True);
	else:
		with open("catalogue_data.json", mode='r',newline="\n") as file1:
			filedata = json.load(file1);
			file1.close();
	for dictt in add_data:
		filedata.append(dictt);
	print("Dictt:"+str(filedata))
	with open("catalogue_data.json", mode='w',newline="\n") as file1:
		json_article=json.dumps(filedata);
		file1.write(json_article);
		file1.close();

 
def db_search(search_data):
	response= [];
	if search_data['type'] == "title":
		documents = collection.find({"title":search_data["keyword"]});
		#print("type: "+str(type(documents)));
		# for i in documents:
		# 	print("doc",i)
	else:
		documents = collection.find({"authors":search_data["keyword"]});
		# print("len: "+str(documents['authors']));	
	for document in documents:
		print("len: "+str(document['authors']));	
		document['_id'] = str(document['_id']);
		response.append(document);
	# print(response);
	for dictt in response:
		print("length: "+str(len(dictt['authors'])));
	return response;

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5003",debug=True);