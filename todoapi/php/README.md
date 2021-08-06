# PHP version

Une api restful écrite en PHP (Lumen) permettant de remplir une TODO List.

## Table des matières

[[_TOC_]]

## Installer les dépendances php nécéssaires

Installer: composer, pdo-pgsql

Sous mac:

```shell
brew install composer
```

## Démarrer l'application en local

```shell
export PATH=/opt/homebrew/Cellar/php/8.0.9/bin/:$PATH # pour mac OS bigsur
composer install
php -S 0.0.0.0:5000 -t public
```
