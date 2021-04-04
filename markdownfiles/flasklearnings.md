# Flask Web Stuff

---

Have to use the following import statement to import flask modules

```python
from flask import Flask	

#To reference the current file (in which we are writing this code - app.py) we use
app=Flask(__name__)

#Here we are defining the route that defaults to the homepage
#and we are writing a function home() which returns "Hello World" to the webpage and we can see it on the browser
@app.route('/')
def home():
    return "Hello World"

if __name__=='__main__':
    app.run(debug=True)	#This statement runs the flask app in the debug mode set to True so that we can see errors if they happen directly in our browser
```

Or Alternatively in the command line we can type

```
FLASK_APP=app.py flask run
```

Instead of directly returning a string like "Hello World" we can also return HTML files but for that we need the module render_template from flask. So our import statement will change to `from flask import Flask, render_template` and then our return statement will become `return render_template('index.html')`

To send some data from the back end server to the browser we can pass additional parameter to this render template like this:

```python
name="John"
gender="Male"
return render_template('index.html',name=name,gender=gender)
```

---

Jinja 2 Syntax in the index.html page/template should be written in curly braces like below

`{{ }}` This is for things that have to be printed in strings

`{% %}` This is for if-else statements, for loops, etc

url_for will get the url link according to what we pass as parameters

```html
{% if gender=="Male" %}
<p>Welcome Mr. {{ name }} </p>
{% else %}
<p>Welcome Mrs. {{ name }} </p>
{% endif %}

<link rel="stylesheet" href="{{ url_for('static',filename='css/main.css') }}"> 

{% if tasks|length <1 %} #This is Jinja 2 syntax it filters the length of the items in tasks and if it is less than 1 then something
```

---

To send/receive requests like GET, POST, PUT, DELETE we need a library called requests which is widely used in python `pip3 install requests` and then we can type the below code segment:

```python
from flask import Flask	
import requests	#to send requests to the server

app=Flask(__name__)

@app.route('/')
def home():
    #Here we are storing the response that we get from the server into respones. The URL from where we are requesting information is passed as a parameter to the requests.get() function
    response=requests.get('https://api.chucknorris.io/jokes/random')
    
    #Here we are coverting the respones to a json object using the .json() method of the response object. We can also ues the following .text()
    json_response=response.json()
    
    #Here the chuck norris api sent data back in a json object and the joke that we needed to extra was residing in a field called 'value' so it is being extracted here so that it can be sent as a parameter to the index.html file
    joke=json_response['value']
    
    return render_template("index.html",joke=joke,name="John",gender="Male")

if __name__=='__main__':
    app.run(debug=True)	
```

---

### JSON

Javascript Object Notation is widely used between the client and server or the frontend and the backend because it is easy to read and understand and also interpret in various languages.

Frontend languages are usually - HTML, CSS, JS, NodeJS,etc
Backend languages are usually - PHP, Python, NodeJS, etc
The gap between this is filled by JSON

---

### RESTful APIS

REST - **Representation State Transfer** is an architectural style of creating APIs. It is **Stateless** which means that the State of the client is not saved when it is requesting information from the Server.

The client sends a request to the server to retrieve or modify resources without knowing what state the server is in. The servers send the response to the client without needing to know what was the previous communication with the client.

The information sent by the server will always be independent of who is requesting for the information

---

### Curl command

cURL stands for client URL. It is used in command lines or scripts to transfer data to and from servers.

The below command gets the response from the url specified. If Json is returned it is shown or else if html website is returned then that is shown.

-v is for Verbose i.e, print everything
-k, --insercure is for insecure connection. That is no SSL needed

The following command will display the content of the URL

```
curl -X GET http://127.0.0.1:5000/
curl https://domain.com/
```

The following command will save the output of the curl command into a file

```
curl -o file1 https://www.google.com/
```

To download files we can use -O 
We can also download multiple files. Or download them and rename it.
We can also download the file securely via SSH.

```
curl -O https://www.domain.com/file.zip
curl -O htps://www.domain.com/file.zip -O https://www.domain.com/file2.zip
curl -O archive.zip https://www.domain.com/file.zip

curl -u user sftp://server.domain.com/path/to/file
```

To get header information from a website we can use the -I ( -capital i ) flag

```
curl -I http://domain.com
```

To access an FTP server
To download files via FTP server
To upload files onto a FTP server

```
curl ftp://ftp.domain.com --user username:password
curl ftp://ftp.domain.com/filename.extension --user username:password
curl -T filename.extension ftp://ftp.domain.com/ --user username:password
```

To check the manual we can use the - `man curl`command for help and other command information.

---

### SQLAlchemy

SQLAlchemy is a Python library that provides an object relational mapper (ORM). It maps the databases (tables, etc.) to Python objects, so that they can more easily and natively interact with them.

An ORM provides a set of tools that let you interact with your database models consistently across database engines.

We did the following in our app.py script: 

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'	#/// 3 forward slashes is a relative path and //// 4 forward slashes is an absolute path
db=SQLAlchemy(app)	#this initialises ourdatabase

class Todo(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	content=db.Column(db.String(200), nullable=False)
	completed=db.Column(db.Integer, default=0)
	date_created=db.Column(db.DateTime,default=datetime.utcnow)
	
	def __repr__(self):
		return '<Task %r>'%self.id

@app.route('/',methods=['GET','POST'])
def home():
	if request.method=='POST':
		task_content=request.form['content']
		new_task=Todo(content=task_content)
		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue adding your task'
	else:
		tasks=Todo.query.order_by(Todo.date_created).all()
		return render_template('index.html',tasks=tasks)
	
@app.route('/delete/<int:id>')
def delete(id):
	task_to_delete=Todo.query.get_or_404(id)
	
	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return 'There was an issue deleting your task'

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
	task=Todo.query.get_or_404(id)
	if request.method=='POST':
		task.content=request.form['content']
		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an error updating that task'

	else:
		return render_template('update.html',task=task)
	
if __name__=='__main__':
	app.run(debug=True)
```

Now in the python3 repl or the **interactive python3 shell.** (Better to do it in the virtual environment) We have to run the following commands to set up our database:

```
>> from app import db
>> db.create_all()
```

Then we can exit the interactive python3 shell. 

---

Push to Heroku stuff

