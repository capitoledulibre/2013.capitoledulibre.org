Site du Capitole du Libre
==========================

Le site utilise pelican pour générer les pages HTML à partir de fichiers en rst.

Il suffit d'installer pelican dans un virtualenv en local pour générer le site entier, il n'est pas utile de l'installer sur le serveur.

Installation
-------------

1. créer un dossier virtualenv

::

	virtualenv pelican-sites
	cd pelican-sites
	source bin/activate
	easy_install pelican

2. Cloner le repository

::

	git clone ...
	
3. Générer le site à l'aide de la commande make

::

	make html

4. Ensuite, envoyer les fichiers situés dans "output" sur le serveur
  Vous pouvez vous aider de la commande make ssh_upload
 
