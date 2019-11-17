### Tester sur la version 18.04 et 16.04 LTS ubuntu

# Package nécessaire principalement : 
Le fichier environment.yml contient l'environnement conda pour installer cet environnement vous devez faire la commande suivant sur votre terminal :

		conda env create --file=environment.yml

le nom de l'environnement crée sera "djangoenv", si le nom est déjà utilisé ouvrir le fichier et modifier la première ligne correspondant à "name:djangoenv" par le nom que vous voulez.

Si vous ne voulez pas passez par l'installation de l'environnement conda par environment.yml alors vous pouvez installer ces packages qui sont dépendants.

* Django 2.2.1	
* sqlite 3.29.0
* python 3.7.4
* conda install -c anaconda libpq
* conda install -c anaconda psycopg2
* pip install django-heroku
* conda install -c conda-forge jquery
* conda install -c conda-forge django-jquery
* pip install gunicorn==20.0.0

Regarder le fichier requirements.txt s'il vous manque un package pour faire fonctionner l'application web. 


# Migration de la base donnée dans sqlite.db :

		python manage.py makemigrations

		python manage.py migrate


# Importation de la base de données dans l'application web (dans sqlite.db):

	Tout d'abord exécuté la commande suivante :
		python manage.py shell 
***

sur le shell de l'application web vous devez utilisé la commande suivante :

***
		exec(open('import_data.py').read())
Prend quelque temps pour pouvoir importer la base de donnée dans sqlite.db (ici la base de donnée à déjà été ajoutée)

*** 

## Lancer le serveur local de l'application web 

#### Dans votre terminal :
		
		python manage.py runserver

Récupérer l'adresse présente dans le terminal (127.0.0.1:8000/), mettre ensuite sur votre navigateur internet l'adresse suivante avec home_page ou sans rien (donne accès à la page d'accueille).

## Accès au serveur web déployer à l'aide de heroku 

Pour accéder à l'application web voici les liens ci-dessous, choisir le serveur de préférence, le site prend un quelque seconde pour de lancer (le temps que le serveur s'active).

* (serveur us) 
		https://blooming-inlet-34163.herokuapp.com/
		https://blooming-inlet-34163.herokuapp.com/home_page

* (serveur eu) 
		https://blooming-inlet-34166.herokuapp.com/
		https://blooming-inlet-34166.herokuapp.com/home_page



# Crédit ©:

Application web crée par HAMMAMI Yousri 


#### Lien accès au git :

https://github.com/Kyalow/projetsnp
