Site du Capitole du Libre
==========================

Le site utilise pelican pour générer les pages HTML à partir de fichiers en rst.

Il suffit d'installer pelican dans un virtualenv en local pour générer le site entier, il n'est pas utile de l'installer sur le serveur.

Installation
-------------

1. créer un dossier virtualenv

::

	virtualenv pelican-sites

2. installer pelican

::

	cd pelican-sites
	source bin/activate
	easy_install pelican

3. cloner le repository

::

	git clone ...

4. lier le thème dans système de fichiers

::

	cd cdl2012
	pelican-theme -s cdltheme-2012

Générer le site
----------------

Générer le site à l'aide de la commande make

::

	make html

Mettre en ligne le site
-------------------------

Pour envoyer les fichiers situés dans "output" sur le serveur, vous pouvez vous aider de la commande 

::

	make ssh_upload
 
