======================================
Édition du site du Capitole du Libre
======================================

Les pages
============

Les pages sont situées dans le dossier ``/src/pages``. 
À la génération du site, elles seront disponible directement à la racine du site, même si elles sont dans des sous-dossiers.

Il est également possible d'utiliser directement des templates en html. C'est le cas pour la page ``programme.html`` qui affiche dynamiquement le programme provenant de Lanyrd.


Ajouter un sponsor
------------------

- créer un fichier pour le sponsor dans ``src/sponsors``
- inclure ce fichier dans la page ``src/pages/sponsors.rst``

::

  .. include:: ../sponsors/kdab.rst


Programme
==========

``programme.html``
----------------------

TODO

Affiche le programme en html à partir d'un fichier json téléchargé depuis le site Lanyrd. Jquery parse le json, et mustache.js s'occupe du template d'affichage dans la page.

Provisoirement, le programme dans son ensemble est affiché à l'aide du plugin pelican ical dans la page ``programme.rst``

Programme détaillé
---------------------

Les pages pour le programme détaillé des conférences et ateliers se trouvent dans les dossier du même nom. Ces fichiers html sont directement interprétés par Jinja (constante TEMPLATE_PAGES du fichier de configuration pelicanconf.py).

Le programme est un fichier json, récupéré depuis lanyrd à l'aide de la commande::

    make update_programm

Celle-ci est également exécutée lors d'un synchronisation avec le serveur.

Le fichier est interprété par jQuery, puis affiché par un template mustache. Les fichiers de template se trouvent dans ``cdltheme-2013/templates``

* schedule_common.html : les div communs
* schedule_mustache.html : les templates mustache utilisés (``summary_tpl`` et ``sessions_tpl``)

Le fichier schedule_lanyrd.js avec la fonction from_lanyrd(day, space) filtre par jour et par salle et permet d'activer les templates mustaches.

