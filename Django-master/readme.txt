Django ::

* Getting Started: <br>
	django-admin startproject website
	
* Running in server
	python manage.py runserver
	
* Creating new app, actually new indevidual functionality
	python manage.py startapp music
	
* any variable int a class in models.py is going to be a column in db.sqlite3 database
	table name is going to be the class name
	and we can access all those data by 
	all_album = Album.objects.all()   //here Album is class name or object name

	after writing code we need to go to the console and command
	
	python manage.py makemigrations music		//music is the app name where the models.py is in
	python manage.py migrate
	
* Adding admin
	python manage.py createsuperuser
	
	
* Writing Python code inside HTML
	{%   %}		//inside this
	
* Writingn variable
	{  }		//inside this
	
* Running the python shell
	python manage.py shell