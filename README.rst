==========================
Site du Capitole du Libre
==========================

Le site utilise pelican pour générer les pages HTML à partir de fichiers en rst.

Il suffit d'installer pelican dans un virtualenv en local pour générer le site entier, il n'est pas utile de l'installer sur le serveur.

Installation
=============

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
	pelican-themes -s cdltheme-2012

Générer le site
----------------

Générer le site à l'aide de la commande make

::

	make html

Mettre en ligne le site
-------------------------

Pour envoyer les fichiers situés dans "output" sur le serveur, vous pouvez 
vous aider de la commande 

::

	make ssh_upload
 
Les paramètres de connexion sont dans le fichier Makefile, il faut une clé 
ssh pour se connecter au serveur bien sûr :-)

Édition
=========

Architecture des pages
------------------------

Les fichiers source se trouvent dans le dossier ``src``, les fichiers 
générés dans le dossier ``output``.

Les pages classiques sont dans le dossier ``src/pages``, mais sont générées 
à la racine du dossier ``output``.

Les actualités (billets de blog) sont dans le dossier ``src/blog`` et 
générées dans le dossier ``output/blog``.

Format ``rst``
---------------

Les pages source sont au format `restructured text 
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_

L'essentiel à savoir est qu'il faut mettre un titre principal à toute page:

\=================
\Titre de la page
\=================

et que les liens sont notés \`nom du lien <url>`_
