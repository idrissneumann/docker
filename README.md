# Formation docker

## Table des matières

[[_TOC_]]

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

1. Créer le Dockerfile qui contiendra la création des images des différentes versions de l'[api todo](./todoapi) écrits dans différents langages en traitant les langages dans cet ordre:
  * Version bash
  * Version python
  * Version java
  * Version php

2. Dockeriser aussi la partie frontend

3. Ajouter dans le Dockerfile une stage pour lancer les tests unitaires facilement pour la version Python

5. Mettre en place un pipeline CI/CD qui va permettre d'automatiser la création et la livraison des conteneurs sur notre registry https://harbor.comwork.io
