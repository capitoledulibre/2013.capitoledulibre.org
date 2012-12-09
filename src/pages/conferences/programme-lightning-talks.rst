======================================
Conférences éclair, samedi 24 novembre
======================================

.. contents:: Liste des conférences
    :depth: 1
    :backlinks: none

.. _conf-firewall:

Réaliser votre firewall, sans aucune connaissance d'iptables, *Frédéric Zulian*
-------------------------------------------------------------------------------

Iptables est un peu aride à configurer en mode console. Beaucoup de
personnes se tournent donc vers des applications intermédiaires
générant des rêgles iptables de manière plus conviviale. Au travers de
cette présentation, nous vous proposons de découvrir différentes
applications graphiques permettant de genérer la configuration d'un
firewall. Elles sont souvent simples d'utilisation et ne demandent pas
d'avoir une connaissance approfondie d'Iptables.

Ces applications traduisent la syntaxe des régles Iptables en «
langage » utilisé par le commun des mortels.  Voici quelques exemples:
fwbuilder, modules iptables de webmin, kmyfirewall, gufw.

.. include:: ../../intervenants/frederic-zulian.rst

.. class:: confhour

Mini-conférence de 14h à 14h20.

La `vidéo de la conférence 'Réaliser votre firewall, sans aucune
connaissance d'iptables'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/zulian-firewall-sans-connaitre-iptables.mp4>`_
est disponible (45 Mo)

.. _conf-po4a:

po4a, outil de traduction pour la documentation, *Denis Barbier*
----------------------------------------------------------------

Depuis 1995, les logiciels libres du projet GNU sont capables grâce à
GNU gettext d'afficher leurs messages dans la langue de
l'utilisateur. De nombreux projets s'en sont inspirés pour gérer des
traductions dans des contextes non prévus initialement par gettext. En
particulier, KDE et GNOME l'utilisent pour traduire leur documentation
en format XML. Le programme `po4a <http://po4a.alioth.debian.org/>`_
repose sur le même principe, mais accepte de nombreux autres formats
d'entrée (pages de manuel groff, Texinfo, LaTeX, POD, HTML, Markdown,
AsciiDoc). La conférence donnera une présentation rapide de la gestion
de traduction de documentation avec des outils basés sur gettext,
ainsi que des exemples pratiques avec po4a.

.. include:: ../../intervenants/denis-barbier.rst

.. class:: confhour

Mini-conférence de 14h20 à 14h20.

La `vidéo de la conférence 'po4a, outil de traduction pour la
documentation'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/barbier-po4a.mp4>`_
est disponible (68 Mo). Les `slides de la conférence 'po4a, outil de
traduction pour la documentation'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/slides/barbier-po4a.pdf>`_
sont également disponibles.

.. _conf-scapy:

Scapy : Easy Packet Handling, *Etienne Maynier*
-----------------------------------------------

Scapy est un framework open-source de création et gestion de paquets
réseau. Ecrit en python, il permet de manipuler des paquets très
simplement et très rapidement.

.. include:: ../../intervenants/etienne-maynier.rst

.. class:: confhour

Mini-conférence de 14h40 à 15h.

La `vidéo de la conférence 'Scapy : Easy Packet Handling'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/maynier-scapy.mp4>`_
est disponible (71 Mo). Les `slides de la conférence 'Scapy : Easy
Packet Handling'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/slides/maynier-scapy.pdf>`_
sont également disponibles.

.. _conf-otb:

OTB:  Librairie de traitement d'images spatiales, *Manuel Grizonnet, CNES*
--------------------------------------------------------------------------

La multiplication des capteurs et des satellites d’une part et
l’amélioration des produits issus de la télédétection d’autre part se
traduisent par des applications de plus en plus nombreuses dans les
divers domaines de l’observation de la Terre. Depuis plus de 7ans le
CNES développe l'OTB, une bibliothèque open source d'algorithmes de
traitement d'images dédiée aux données de télédétection.

L'OTB a pour vocation de démocratiser l'utilisation des données
d'observation de la Terre et de rendre notamment accessible aux
utilisateurs des méthodes récentes d'analyse et de traitements de ces
images. La librairie participe à la valorisation des données satellite
et fédère maintenant autour d'elle une large communauté d'utilisateurs
et de contributeurs.

Cette mini-conférence présentera brièvement le logiciel et sa
philosophie:

- Le contexte générale du traitement d'images des données de télédétection et les enjeux pour le suivi de l'environnement
- Présentation et illustration de la librairie
- Comment à l'avenir des outils open source comme l'OTB peuvent permettre d'aider à une meilleure gouvernance des territoires et à l'amélioration du dialogue avec les populations

.. include:: ../../intervenants/manuel-grizonnet.rst

.. class:: confhour

Mini-conférence de 15h à 15h20.

La `vidéo de la conférence 'OTB: Librairie de traitement d'images
spatiales'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/grizonnet-otb.mp4>`_
est disponible (65 Mo). Les `slides la conférence 'OTB: Librairie de
traitement d'images spatiales'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/slides/grizonnet-otb.pdf>`_
sont également disponibles.

.. _conf-diogene:

Diogène, logiciel libre de Biométrie et Génétique sous Linux, *Philippe Baradat*
--------------------------------------------------------------------------------------

Le logiciel DIOGENE (licence GPL) a été conçu et développé en Fortran
90 et en C sous Linux pour répondre aux besoins d'étudiants et de
chercheurs dans les domaines de la Biométrie générale et de la
Génétique des plantes annuelles ou pérennes.  Il peut être téléchargé
depuis le site http://amap.cirad.fr. Ses caractéristiques principales
sont les suivantes :

- Possibilité de traiter simultanément un très grand nombre de variables (jusqu'à 9999) ;
- Utilisation de modèles non-orthogonaux (permettant de traiter des fichiers ayant beaucoup de donnée manquantes) ;
- Présence d'un analyseur syntaxique autorisant la définition de nouveaux caractères à partir de formules algébriques ;
- Calcul standardisé par rééchantillonnage des intervalles de confiance de paramètres estimés (corrélations par exemple) ;
- Structure modulaire permettant de traiter des modèles complexes par assemblage de modules de base ;
- Fonctionnement multilingue (Français, Anglais, Espagnol, Portugais et italien). Ajout facile de nouvelles langues.

Ce logiciel est interfacé avec Gnuplot (sorties graphiques 2-D ou
3-D). En revanche, une interface utilisateur graphique reste à créer.

.. include:: ../../intervenants/philippe-baradat.rst

.. class:: confhour

Mini-conférence de 15h20 à 15h40.

La `vidéo de la conférence 'Diogène, logiciel libre de Biométrie et
Génétique sous Linux'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/baradat-diogene.mp4>`_
est disponible (64 Mo). Les `slides de la conférence 'Diogène,
logiciel libre de Biométrie et Génétique sous Linux'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/slides/baradat-diogene1.pdf>`_
sont également disponibles.

.. _conf-orekit:

Orekit, l'innovation libre comme pari industriel, *Sébastien Dinot*
-------------------------------------------------------------------

`Orekit <https://www.orekit.org/forge/projects/orekit/wiki/Overview>`_
est une bibliothèque de mécanique spatiale développée et diffusée par
`CS <http://www.c-s.fr>`_ sous licence Apache. Preuve de sa qualité,
Orekit est désormais exploitée en opération et en simulation par le
CNES, l'ESA et un nombre croissant d'industriels. Outre sa licence
permissive, Orekit se démarque par l'ouverture de son comité de
pilotage à d'autres entités qui orientent, avec CS, le développement
du projet.

La question se pose donc. Quelle mouche peut bien avoir piqué une
société disposant d'un savoir-faire pointu dans un domaine extrêmement
technique pour qu'elle décide de diffuser sous une licence libre
permissive (i.e. très avantageuse pour ses clients et ses concurrents)
un composant logiciel innovant et implantant l'état de l'art en ce
domaine. Pourquoi avoir fait le choix rarissime pour un industriel d'une
gouvernance collégiale ?

Nous verrons que la démarche de CS n'a rien d'idéologique mais découle
au contraire de sa compréhension du marché et d'une stratégie mûrement
réfléchie. Et nous verrons que cette stratégie est d'ores et déjà
gagnante...

.. include:: ../../intervenants/sebastien-dinot.rst

.. class:: confhour

Mini-conférence de 15h40 à 16h.

La `vidéo de la conférence 'Orekit, l'innovation libre comme pari
industriel'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/dinot-orekit.mp4>`_
est disponible (67 Mo). Les `slides de la conférence 'Orekit,
l'innovation libre comme pari industriel'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/slides/dinot-orekit.pdf>`_
sont également disponibles.

.. _conf-opensource:

L'Open Source et les éditeurs de logiciel: avantage compétitif agressif ou développement durable?, *Gaël Blondelle, Obéo*
-------------------------------------------------------------------------------------------------------------------------

Les valeurs sociétales de partage dont la communauté Open Source se
prévaut ne sont pas réellement celles sur lesquelles se développent
les "startup open source" les plus connues.

Certaines de ces entreprises adoptent l'Open Source comme une approche
leur permettant d'intégrer un marché en se faisant une place à côté
d'acteurs en situation de monopole ou d'oligopole ; D'autres, comme un
outil marketing spécifique leur permettant d'acquérir une visibilité
mondiale.

Cette mini-conférence décrira, en se basant sur des exemples:
  - comment ces startups se développent, et mettent en œuvre leur
    business model,
  - comment elles font le lien entre les demandes de fond
    d'investissement et les contraintes de l'Open Source
  - comment elles utilisent l'Open Source pour bousculer les acteurs
    établis du secteur
  - en quoi ces startups ressemblent ou diffèrent des éditeurs
    logiciels propriétaires

.. include:: ../../intervenants/gael-blondelle.rst

.. class:: confhour

Mini-conférence de 16h à 16h20.

La `vidéo de la conférence 'L'Open Source et les éditeurs de logiciel:
avantage compétitif agressif ou développement durable?'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/blondelle-open-source-editeurs-logiciels.mp4>`_
est disponible (74 Mo)

.. _conf-software-defined-network:

Quand le Software prend le contrôle des réseaux et que l’Open Hardware est une solution pour aller plus loin, *Marc Bruyère*
----------------------------------------------------------------------------------------------------------------------------

SDN ou Software Defined Network un nouveau paradigme pour les réseaux
LAN WAN Optique ou Wireless.  Qu’est ce que cela cache, permet et
permettra ?

Présentation d’OpenFlow le protocole du Software Defined Network.

Comment débuter et appréhender OpenFlow avec le contrôleur Open Source
Floodlight, en regardant comment piloter autant les équipement
compatible OpenFlow qu’Open vSwitch.

Comment pouvons nous imaginer aller plus loin que l’OpenFlow 1.x et
avoir des Switch qui pourrons implémenter des fonctionnalités avancées
comme crypter , encapsuler par exemple qui demandent beaucoup de
ressources hardware. Pourquoi la plateforme Open Hardware NetFPGA est
une solution.

.. include:: ../../intervenants/marc-bruyere.rst

.. class:: confhour

Mini-conférence de 16h20 à 16h40.

La `vidéo de la conférence 'Quand le Software prend le contrôle des
réseaux et que l’Open Hardware est une solution pour aller plus loin'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/bruyere-reseaux-open-hardware.mp4>`_
est disponible (82 Mo)

.. _conf-mozilla:

C'est quoi Mozilla ?, *Clarista, Théo Chevalier*
------------------------------------------------

Mozilla est le premier navigateur en Europe. Mais il y a quoi au juste
derrière Mozilla ? C'est une fondation, mais d'où vient l'argent? Quid
de la concurrence de Chrome ? Cette conférence essaiera de répondre à
toutes vos questions sur Firefox et sur les autres projets de Mozilla.

.. include:: ../../intervenants/theo-chevalier.rst

.. class:: clearfix

|

.. include:: ../../intervenants/clarista.rst

.. class:: confhour

Mini-conférence de 16h40 à 17h.

La `vidéo de la conférence 'C'est quoi Mozilla'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/clarista-chevalier-c-est-quoi-mozilla.mp4>`_
est disponible (92 Mo)

.. _conf-gcompris:

Le logiciel éducatif GCompris fait le plein de nouveautés, *Bruno Coudoin*
--------------------------------------------------------------------------

GCompris est un logiciel éducatif qui propose des activités variées
aux enfants de 2 à 10 ans. Au fil des ans GCompris s'est imposé comme
la véritable référence du domaine sur GNU/Linux et au delà sur les
systèmes d'exploitation non libres. Bien qu'il soit déjà très abouti
avec plus d'une centaine d'activités, chaque année amène son lot de
nouveautés.  L'objet de cette présentation est de parcourir les
nouvelles activités d'éveil musical et scientifique développée dans le
cadre du "Google Summer Of Code 2012".

.. include:: ../../intervenants/bruno-coudoin.rst

.. class:: confhour

Mini-conférence de 17h30 à 17h50.

La `vidéo de la conférence 'Le logiciel éducatif GCompris fait le
plein de nouveautés'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/coudoin-gcompris-nouveautes.mp4>`_
est disponible (81 Mo)

.. _conf-videoenpoche:

Vidéo en Poche : présentation et état des lieux, *Rodolphe Village*
-------------------------------------------------------------------

C'est une initiative (démarrage en septembre 2010) des Cinémas Utopia
cherchant à apporter une réponse aux questions posées par notre époque
sur les échanges culturels et la rémunération de la création. À l'aide
d'un logiciel développé par Objectif Libre sous licence GPLv3, Les
salles membres du réseau Vidéo en Poche proposent la vente sur le
support amovible type clé USB ou carte mémoire des spectateurs des
films au format ouvert Matroska et sans DRM.

.. include:: ../../intervenants/rodolphe-village.rst

.. class:: confhour

Mini-conférence de 17h50 à 18h10.

La `vidéo de la conférence 'Vidéo en Poche : présentation et état des
lieux'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/village-video-en-poche.mp4>`_
est disponible (88 Mo)

.. _conf-cinemalibre:

Vers un système de projection libre pour le cinéma numérique, *Nicolas Bertrand*
--------------------------------------------------------------------------------

La conversion des salles de cinéma françaises et européennes vers le
cinéma numérique est en cours, et d'ici 2014 il n'y aura pratiquement
plus de tirage en bobine 35 mm. Le matériel pour la projection
numérique dans les salles est standardisé et amène de nouvelles
contraintes de coût, de technologie et de sécurité.

Pour continuer à produire, distribuer et diffuser des films, le cinéma
Art et Essai doit pouvoir s'approprier le cinéma numérique, et adapter
la technologie à la création et non le contraire. Le cinéma numérique
actuel impose un modèle qui n'a pas été pensé pour le cinéma Art et
Essai. Le modèle du logiciel libre peut fournir une solution adaptée
à ce problème. Nous travaillons sur un système de création, diffusion
et projection de copies numériques. Ce système sera ouvert et peu
coûteux. Au delà du côté technique, le but est de permettre l'accès à
toute œuvre aux salles obscures.

.. include:: ../../intervenants/nicolas-bertrand.rst

.. class:: confhour

Mini-conférence de 18h10 à 18h30.

La `vidéo de la conférence 'Vers un système de projection libre pour
le cinéma numérique'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/bertrand-projection-libre-cinema.mp4>`_
est disponible (70 Mo). Les `slides de la conférence 'Vers un système
de projection libre pour le cinéma numérique'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/slides/bertrand-cinema-numerique.pdf>`_
sont également disponibles.

.. _conf-contribuer-mozilla:

Comment contribuer à Mozilla, *Clarista, Théo Chevalier*
--------------------------------------------------------

Mozilla est le premier navigateur en Europe. Mais il y a quoi au juste
derrière Mozilla ? C'est une fondation, mais d'où vient l'argent? Quid
de la concurrence de Chrome ? Cette conférence essaiera de répondre à
toutes vos questions sur Firefox et sur les autres projets de Mozilla.
Par ailleurs, pourquoi contribuer à Mozilla ? Nous montrerons que
contribuer, c'est gratifiant, à la fois pour soi et pour les
autres. Et il y en a pour tous les goûts ! Pour les techniques, comme
pour les non techniques. Nous reviendrons en particulier sur la
communauté francophone, la façon dont elle se structure. Et sur le
programme Reps, qui est une vraie opportunité pour gagner en
visibilité, et pour voyager !

.. include:: ../../intervenants/theo-chevalier.rst

.. class:: clearfix

|

.. include:: ../../intervenants/clarista.rst

.. class:: confhour

Mini-conférence de 18h30 à 18h50.

La `vidéo de la conférence 'Comment contribuer à Mozilla'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/clarista-chevalier-contribuer-a-mozilla.mp4>`_
est disponible (62 Mo)

.. _conf-roman-cc-zero:

Comment mettre mon roman dans le domaine public a fait de moi un auteur, *Pouhiou*
----------------------------------------------------------------------------------

Je ne suis pas venu au libre par le logiciel, mais par la
création. Auteur geek, je me suis lancé un défi quotidien : bloguer
une série de 8 romans-feuilleton. Un épisode par jour, 4 jours par
semaine. Très vite, l'urgence de devoir publier une nouvelle création
chaque soir m'a mis face aux mécanismes du processus créatif. Cette
réalisation m'a poussé à l'évidence : mon oeuvre appartient au domaine
public. C'est en mettant #Smartarded (mon premier roman) sous licence
CC0 que je me suis fait reconnaître en tant qu'auteur. Avec à la clé
une édition chez Framasoft.

Le plus étonnant, c'est que la majeure partie des artistes que je
côtoie pensent comme moi. Ils sentent bien que leurs créations ont
leur place dans les biens communs. Ce qui les empêche de sauter le pas
?  Quelques peurs. Basées sur de l'ignorance et de fausses
conceptions. C'est le prochain défi de la communauté du Libre que
d'accompagner ces artistes dans la libération de leurs
ouvrages. D'initier une changement dans les mentalités pour que la
culture partagée devienne la norme, non l'exception.

.. include:: ../../intervenants/pouhiou.rst

.. class:: confhour

Mini-conférence de 18h50 à 19h10.

La `vidéo de la conférence 'Comment mettre mon roman dans le domaine
public a fait de moi un auteur'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/pouhiou-roman-domaine-public.mp4>`_
est disponible (92 Mo)

.. _conf-framazic:

"Framazic, et si on changeait la musique ?", *Framartin*
---------------------------------------------------------------

Avez-vous déjà téléchargé illégalement de la musique sur Internet ?
Feriez-vous partie de cette bande de vilains pirates qui pillent les
gentils artistes ? Savez-vous qu'à chaque visite sur The Pirate Bay,
un musicien meurt dans le monde ? Telles sont les questions qui
reviennent sans cesse dans les débats autour du partage d'œuvres
culturelles sur Internet.

Alors que même la Hadopi a reconnu dans un rapport que ceux qui
téléchargent illégalement sont ceux qui achètent le plus de musique,
ne serait-il pas temps de repenser ces pratiques ? Et si justement la
musique libre était un exemple qui montre que le téléchargement ne
fait pas que tuer des bébés phoques, mais fait naître aussi des
vocations, tout en défendant un modèle de société ? Et si le problème
ne venait pas de mélomanes irresponsables, mais des personnes qui les
désignent comme tel ? Et si l'industrie du divertissement utilisait ce
prétexte pour dissimuler un vrai problème de modèle économique dépassé
?  Face à de telles questions, il a paru important au sein de
Framasoft d'apporter des éléments au débat grâce à Framazic. Un projet
dédié à la promotion de la musique libre, essayant montrer aux
mélomanes comme aux musiciens que l'ouverture aux licences libres ne
signifie pas la fin du monde.

.. include:: ../../intervenants/framartin.rst

.. class:: confhour

Mini-conférence de 19h10 à 19h30.

La `vidéo de la conférence 'Framazic, et si on changeait la musique ?'
<http://www.toulibre.org/pub/2012-11-24-capitole-du-libre/videos/framartin-si-on-changeait-la-musique.mp4>`_
est disponible (102 Mo)
