# Package nécessaire : 
	
* Django 2.2.1	
* sqlite 3.29.0
* python 3.7.4
* 	




# Importation de la base de données dans l'application web :

	Tout d'abord exécuté la commande suivante :
		
python manage.py shell 
***

sur le shell de l'application web vous devez utilisé la commande suivante :

***
exec(open('import_data.py').read())
Prend quelque temps pour pouvoir importer la base de donnée dans sqlite.db



(serveur us) https://blooming-inlet-34163.herokuapp.com/home_page/ 

(serveur eu) https://blooming-inlet-34166.herokuapp.com/
