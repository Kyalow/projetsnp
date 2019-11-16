# Package nécessaire principalement : 
	
* Django 2.2.1	
* sqlite 3.29.0
* python 3.7.4

Regarder le fichier requirements.txt s'il vous manque un package pour faire fonctionner l'application web. 



# Importation de la base de données dans l'application web :

	Tout d'abord exécuté la commande suivante :
		python manage.py shell 
***

sur le shell de l'application web vous devez utilisé la commande suivante :

***
		exec(open('import_data.py').read())
Prend quelque temps pour pouvoir importer la base de donnée dans sqlite.db

*** 

## Lancer le serveur local de l'application web 

#### Dans votre terminal :
		
		python manage.py runserver

Récupérer l'adresse présente dans le terminal (127.0.0.1:8000/), mettre ensuite sur votre navigateur internet l'adresse suivante avec home_page ou sans rien (donne accès à la page d'accueille)

## Accès au serveur web déployer à l'aide de heroku 

* (serveur us) 
		https://blooming-inlet-34163.herokuapp.com/
		https://blooming-inlet-34163.herokuapp.com/home_page

* (serveur eu) 
		https://blooming-inlet-34166.herokuapp.com/
		https://blooming-inlet-34166.herokuapp.com/home_page
