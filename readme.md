Api Docs.

I have used POSTMAN to run these apis

1.Displaying members 

    Request type  = GET
    
    Input Url
      http://127.0.0.1:8000/instapi/display
    OUTPUT
      {"success": "true", "data": [{"uid": 1, "firstname": "Tom", "lastname": "Harry", "email": "tom@gmail.com", "role": 1, "phone": 1234567899}, {....}]}

2.Adding a member 

    Request type  = POST

    Input Url
      http://127.0.0.1:8000/instapi/add
    Input POST data format
      {
      "firstname" : "Amit",
      "lastname" : "Singh",
      "phone" : 1234567899,
      "email" : "amit@gmail.com",
      "role" : 2
      }
    OUTPUT
      {"success": "true", "data": {"uid": 13, "firstname": "Amit", "lastname": "Singh", "phone": 1234567899, "email": "amit@gmail.com", "role": 2}}

3.Updating a member 

    Request type = PATCH/POST/PUT
    
    Input Url
      http://127.0.0.1:8000/instapi/update
    Input POST data format
      { uid : 13,
        "firstname" : "Sam",
      "lastname" : "Sahoo"
       }

     OUTPUT
      {"success": "true", "data": {"uid": 13, "firstname": "Sam", "lastname": "Sahoo"}}

4.Deleting a member 

    Request type  = GET
    
    Input Url
        http://127.0.0.1:8000/instapi/delete?uid=<uid>
    Input Data
        uid=1
    OUTPUT
        {"success" : "true"}
