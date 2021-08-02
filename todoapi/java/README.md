# Java version

Une api restful écrite en Java (Springboot) permettant de remplir une TODO List.

Cette api est écrite en plusieurs versions avec différents langages et est inspirée par ce [repo](https://github.com/paulodhiambo/flaskcrudapi).

Elles a été modifiée afin d'être:
* de fonctionner avec la même base de données PostgreSQL (ce qui permettra d'utiliser la même bdd que les autres versions écrites dans d'autres langages)
* de fonctionner avec maven au lieu de gradle

## Table des matières

[[_TOC_]]
## Démarrer l'application en local

1. Installer Java OpenJDK 11 et maven >= 3.5
2. Lancer la commande suivante dans ce répertoire

```shell
mvn clean install
```

3. Démarrez l'application

```shell
java -jar todo-api/target/todo-api-0.0.1-SNAPSHOT.jar
```

4. Testez: [rendez-vous ici](../README.md)
