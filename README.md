# Formation docker

## Table des matières

[[_TOC_]]

## Documentation

Vous pourrez trouver tout les détails nécéssaires (commandes, etc) dans les [slides de la formation](./Formation sur docker.pdf).

La formation est également disponible en vidéo sur YouTube:
* Partie 1: https://youtu.be/z1l3DWGMXek
* Partie 2: https://youtu.be/3WUXtLvoEoE

## Dépôts de sources

* Repo principal : https://gitlab.comwork.io/comwork_training/docker
* Miroir github : https://github.com/idrissneumann/docker.git
* Miroir gitlab : https://gitlab.com/ineumann/docker.git

## Pré-requis

### Dépendances à installer

* Java OpenJDK 11
* Maven >= 3.5
* Python 3
* docker 

### Mettre à jour docker-compose

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

## Cas pratique

0. Tout votre travail devra être pushé sur git avec une branche `main_{votre nom}` et ouvrir une merge request vers la branche `main`

1. Utilisez une image openJDK du docker-hub déjà prête qui vous permettra de démarrer l'app la version java de l'[api todo](./todoapi) que vous aurez préalablement compilé

2. Créer le Dockerfile qui contiendra la création des images des différentes versions de l'[api todo](./todoapi) écrits dans différents langages en traitant les langages dans cet ordre:
  * Version python
  * Version java
  * Version php

Vous devez rendre les applications cloud native. Par exemple l'application java se configure avec un fichier [application.properties](todoapi/java/todo-api/src/main/resources/application.properties), en la transformant en conteneur il faut que chaque élément du fichier de configuration puisse être remplacé ou surchargé par une variable d'environnement.

Exemple: `server.port=5000` doit pouvoir se configurer avec une variable d'environnement `$SERVER_PORT` qu'on pourra ensuite surcharger dans le fichier `docker-compose.yaml`.

3. Dockeriser aussi la partie frontend

4. Ajouter dans le Dockerfile une stage pour lancer les tests unitaires facilement pour la version Python

5. Mettre en place un pipeline CI/CD qui va permettre d'automatiser la création et la livraison des conteneurs sur notre registry https://harbor.comwork.io
