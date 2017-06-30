from django.shortcuts import HttpResponse
from instapi.models import Members
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Displaying memebers 
# Request type  = GET
#
# Input Url
# 	http://127.0.0.1:8000/instapi/display
#
# OUTPUT
# 	{"success": "true", "data": [{"uid": 1, "firstname": "Tom", "lastname": "Harry", "email": "tom@gmail.com", "role": 1, "phone": 1234567899}, {....}]}


def display(request):

	 queryArr = list(Members.objects.all().values())  #fetching data from DB

	 response = {}
	 response = {'success' : 'true', 'data' : queryArr} #response data to return

	 return HttpResponse(  json.dumps(response), content_type="application/json")
	 

# Adding a member 
# Request type  = POST
#
# Input Url
# 	http://127.0.0.1:8000/instapi/add
#
# Input POST data format
# 	"firstname" : "Amit",
# 	"lastname" : "Singh",
# 	"phone" : 1234567899,
# 	"email" : "amit@gmail.com",
# 	"role" : 2}
#
# OUTPUT
# 	{"success": "true", "data": {"uid": 13, "firstname": "Amit", "lastname": "Singh", "phone": 1234567899, "email": "amit@gmail.com", "role": 2}}

@csrf_exempt
def add(request):

	body_unicode = request.body.decode() # getting payload data into json
	body = json.loads(body_unicode) # converting json into array

	firstname = body["firstname"]
	lastname = body['lastname'] 
	phone = body['phone'] 
	email = body['email'] 
	role = body['role']

	response = {}

	if   firstname and lastname  and phone and email and role:  #checking whether fields are empty or not
		mem = Members.objects.create(firstname=firstname, lastname=lastname, phone=phone, email=email, role=role) #inserting data into DB
		data = {}
		data["uid"] = mem.uid
		data["firstname"] = mem.firstname
		data["lastname"] = mem.lastname
		data["phone"] = mem.phone
		data["email"] = mem.email
		data["role"] = mem.role
		print(data)

		response = {"success" : "true", "data" : data}  #response data to return
	else:
		response = {"success" : "false", "error" : "Data is not valid"}  #response data to return	
	

	return HttpResponse(json.dumps(response), content_type="application/json")


# Updating a member 
# Request type  = PATCH/POST/PUT
#
# Input Url
# 	http://127.0.0.1:8000/instapi/update
#
# Input POST data format
# 	{ uid : 13,
#	"firstname" : "Sam",
# 	"lastname" : "Sahoo"
# 	 }
#
# OUTPUT
# 	{"success": "true", "data": {"uid": 13, "firstname": "Sam", "lastname": "Sahoo"}}

@csrf_exempt
def update(request):
	body_unicode = request.body.decode() # getting payload data into json
	body = json.loads(body_unicode) # converting json into array

	uid = body['uid']

	if uid:   #check only for uid is not empty

		ob = Members.objects.get(uid=uid)

		for key, value in body.items():
			setattr(ob, key, value)
			ob.save()

		response = {"success" : "true" , "data" : body}  #response data to return

	else:
		response = {"success" : "false", "error" : "Data is not valid"}  #response data to return

	return HttpResponse(json.dumps(response), content_type="application/json")


# Deleting a member 
# Request type  = GET
#
# Input Url
# 	http://127.0.0.1:8000/instapi/delete?uid=<uid>
#
# Input Data
# 	uid=1
#
# OUTPUT
# 	{"success" : "true"} 

def delete(request):

	uid = request.GET['uid']

	if uid:  #check only for uid is not empty
		Members.objects.filter(uid=uid).delete() #deleting from DB
		response = {"success" : "true"}  #response data to return
	else:
		response = {"success" : "false", "error" : "Data is not valid"}  #response data to return	


	return HttpResponse(json.dumps(response), content_type="application/json")