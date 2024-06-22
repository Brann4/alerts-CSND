## Creating new Django project

1. Run virtualenv env
2. We need to activate the virtual enviroment
   cd env\Script\  
3. Then we put *activate*

So now we created a file call **requirements.txt**.In this file we control all the libreries version control.

# Now we create install all the libraries with
pip install -r requirements.txt

# Then we create a Django project with
django-admin startproject core .

# For run the server we need
python manage.py runserver  

# To setup the env variables we need to add a pip library in requirement.txt
django-environ==0.11.2

