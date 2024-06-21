# myDiscord - Février 2024
(Ajout du README fin Juin 2024)

## <span style="color: red;">ATTENTION :  
Le fichier.env est indispensable pour se connecter.  
Ce fichier contient les identifiants de connexion à la base de donnée.  
Il n'est donc pas stocké sur le repo public</span>

## Table des matière
- [Composition de l'équipe](#Composition de l'équipe)
- [répartition des tâches](#répartition des tâches)
- [Structure du projet](#Structure du projet)
- [Diagramme des classes](#Diagramme des classes)
- [Base de donnée](#Base de donnée)
- [Mode d'emploi](#Mode d'emploi)
- [Conclusion](#Conclusion)



## Composition de l'équipe

Projet réalisé par 3 étudiants en 1ère année de Bachelor IT spécialité Intelligence Artificielle à La Plateforme_ à Marseille :
- Cyril Genisson
- Bruno Coulet
- Lucas savioz


## répartition des tâches

![Illustration](img/equipe.png)


## Structure du projet

![Illustration](img/schema.png)

## Diagramme des classes

![Illustration](img/classes.png)

## Base de donnée

![Illustration](img/tables.png)

## Mode d'emploi:

Lancer le script login.py pour se connecter à un compte.
L'interface graphique pour la créaction de compte et la connexion à un compte existant s'affiche.

![Illustration](img/login.png)

Sélectionner un compte existant, par exemple
- **login :**  
raoul
- **mot de passe :**  
b'$2b$12$c/Nh4OLeJETnPKyW7ubgSOReebGdq7dQernLgqbZIWbm0ZVxDh15u'

L'interface graphique de connexion se ferme, puis l'interface du chat s'affiche à son tour.

![Illustration](img/message_1.png)


L'utilisateur peut  :
- Sélectionner un channel existant, cela affiche les messages du channel sélectionné.
- Créer un channel.
- Ajouter un message.

**Problème :**
Le message est bien ajouté à la base de donnée, mais l'interface graphique ne se reffraichi pas.

## Message audio
Une version alternative permet de gérer les message audio encodé en base 64

## Conclusion

![Illustration](img/conclusion.png)
