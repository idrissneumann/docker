# Python version

Une api restful écrite en Python (Flask) permettant de remplir une TODO List.

Cette api est écrite en plusieurs versions avec différents langages et est inspirée par ce [repo](https://github.com/paulodhiambo/springbootcrud).

Elles a été modifiée afin d'être:
* de fonctionner avec la même base de données PostgreSQL (ce qui permettra d'utiliser la même bdd que les autres versions écrites dans d'autres langages)
* d'être mieux découpée en couche afin de rendre ces différentes couches testables unitairement avec des mocks

## Table des matières

[[_TOC_]]

## Démarrer l'application en local

1. Installer Python 3 et pip3
2. Lancer la commande suivante dans ce répertoire

```shell
pip3 install --no-cache-dir -r requirements.txt
```

3. Démarrez l'application

```shell
python3 -u app.py
```

4. Testez: [rendez-vous ici](../README.md)
