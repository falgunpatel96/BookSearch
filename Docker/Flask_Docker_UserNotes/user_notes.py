import datetime;
import requests
import json
import os
from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__)

@app.route('/appendnote',methods = ['POST'])
def append_note():
		if request.method == 'POST':
			print("In Append",flush=True);
			search_data = request.get_json();
			print("request: "+str(search_data),flush=True);
			print(type(search_data),flush=True);
			obj = storedataInNote(search_data);
			return jsonify(obj);
			

def storedataInNote(search_data):
	print("In inner",flush=True);
	floc = "notes.json"
	foundNote = False;
	if not os.path.exists(floc):
		notes = [];
		print("Not Exists",flush=True);
	else:
		with open("notes.json", mode='r',newline="\n") as file1:
			notes = json.load(file1);
			file1.close();
			print("notes file Exists",flush=True);
			for sin_key in notes:
				if search_data['keyword'] == sin_key['keyword']:
					print("keyword: "+sin_key['keyword'],flush=True);
					print("type: "+str(type(search_data['note'])),flush=True);
					print("data: "+str(search_data['note']),flush=True);
					print("type123: "+str(type(sin_key['notes'])),flush=True);
					sin_key['notes'].append(search_data['note']);
					# print("Note: "+str(newNote),flush=True);
					# sin_key['notes'] = newNote;
					foundNote = True;
					break;
	if not foundNote:
		single_keyword = {};
		sinkey_notes = [];
		sinkey_notes.append(search_data['note']);
		single_keyword['keyword'] = search_data['keyword'];
		single_keyword['notes'] = sinkey_notes;
		notes.append(single_keyword);
		print("new note:"+str(notes),flush=True);

	with open("notes.json", mode='w',newline="\n") as file1:
		json_article=json.dumps(notes);
		file1.write(json_article);
		file1.close();
	d = {'added':"done"};
	print("addnote obj: "+str(d),flush=True);
	print("addnote obj type: "+str(type(d)),flush=True);
	return d;

@app.route('/shownote',methods = ['POST'])
def show_note():
	print("Hello",flush=True);
	search_data = request.get_json();
	print("key: "+search_data['keyword'],flush=True);
	floc = "notes.json"
	foundNote = False;
	matched_note = [];
	if not os.path.exists(floc):
		notes = [];
		print("Not Exists",flush=True);
	else:
		with open("notes.json", mode='r',newline="\n") as file1:
			notes = json.load(file1);
			file1.close();
			print("notes file Exists");
			for sin_key in notes:
				if search_data['keyword'] == sin_key['keyword']:
					matched_note = sin_key['notes'];
					foundNote = True;
					break;
	if not foundNote:
		matched_note.append("No previous note added");
	print("shownote obj: "+str(matched_note),flush=True);
	print("addnote obj type: "+str(type(matched_note)),flush=True);
	return jsonify(matched_note);


if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5004",debug=True);
