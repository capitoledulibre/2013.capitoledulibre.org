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



``programme.html``
----------------------

Affiche le programme en html à partir d'un fichier json téléchargé depuis le site Lanyrd. Jquery parse le json, et mustache.js s'occupe du template d'affichage dans la page.

