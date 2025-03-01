# Jeu_de_la_vie

---

![License](https://img.shields.io/github/license/Redstoneur/Jeu_de_la_vie)
![Top Language](https://img.shields.io/github/languages/top/Redstoneur/Jeu_de_la_vie)
![Python Version](https://img.shields.io/badge/python-3.8-blue)
![Size](https://img.shields.io/github/repo-size/Redstoneur/Jeu_de_la_vie)
![Contributors](https://img.shields.io/github/contributors/Redstoneur/Jeu_de_la_vie)
![Last Commit](https://img.shields.io/github/last-commit/Redstoneur/Jeu_de_la_vie)
![Issues](https://img.shields.io/github/issues/Redstoneur/Jeu_de_la_vie)
![Pull Requests](https://img.shields.io/github/issues-pr/Redstoneur/Jeu_de_la_vie)

---

![Forks](https://img.shields.io/github/forks/Redstoneur/Jeu_de_la_vie)
![Stars](https://img.shields.io/github/stars/Redstoneur/Jeu_de_la_vie)
![Watchers](https://img.shields.io/github/watchers/Redstoneur/Jeu_de_la_vie)

---

![Latest Release](https://img.shields.io/github/v/release/Redstoneur/Jeu_de_la_vie)
![Release Date](https://img.shields.io/github/release-date/Redstoneur/Jeu_de_la_vie)
[![Build Status](https://github.com/Redstoneur/Jeu_de_la_vie/actions/workflows/build.yml/badge.svg)](https://github.com/Redstoneur/Jeu_de_la_vie/actions/workflows/build.yml)
---

Le jeu de la vie est un automate cellulaire inventé par John Horton Conway en 1970. Il s'agit d'un jeu de simulation
mathématique dans lequel des cellules évoluent selon des règles simples et produisent des motifs complexes.

## Règles

Le jeu de la vie se déroule sur une grille bidimensionnelle. Chaques cellules peuvent être soit vivante (1) soit morte
(0). Les cellules évoluent selon les règles suivantes :

1. Si une cellule a exactement trois voisines vivantes, elle devient vivante à la génération suivante.
2. Si une cellule a exactement deux voisines vivantes, elle conserve son état à la génération suivante.
3. Dans tous les autres cas, la cellule meurt ou reste morte à la génération suivante.

## Utilisation

Le jeu de la vie peut être exécuté en utilisant le langage de programmation Python et la bibliothèque Tkinter.

La version python minimale requise pour exécuter le programme est la version `3.8`.

Avant de l'exécuter, assurez-vous d'avoir installé les dépendances en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

Ensuite, vous pouvez lancer le programme en tapant la commande suivante dans un terminal :

```bash
python ./src/main/python/main.py
```

Le programme affichera une grille initiale de cellules. Vous pouvez cliquer sur les cellules pour les faire vivre ou
mourir. Vous pouvez également sélectionner des modèles prédéfinis à partir du menu déroulant "Patterns". Vous pouvez
ajuster la vitesse de l'évolution en sélectionnant une option de vitesse à partir du menu déroulant "Speed". Enfin, vous
pouvez mettre en pause ou reprendre l'évolution en cliquant sur le bouton "Pause/Resume".

## Exemples de modèles prédéfinis

Le jeu de la vie comprend plusieurs modèles prédéfinis que vous pouvez sélectionner à partir du menu déroulant "
Patterns". Voici quelques exemples :

Glider : Un petit vaisseau qui se déplace diagonalement sur la grille.
Blinker : Un oscillateur qui alterne entre deux positions à chaque génération.
Lightweight spaceship : Un vaisseau plus grand qui se déplace horizontalement et verticalement sur la grille.

## Personnalisation

Vous pouvez personnaliser le jeu de la vie en modifiant les paramètres du programme. Par exemple, vous pouvez ajuster la
taille de la grille, la vitesse de l'évolution, ou la liste des modèles prédéfinis. Le code est entièrement modifiable
et peut être adapté à vos besoins.

## Téléchargement

Vous pouvez télécharger la dernière version du programme au format `.exe` à partir de la [dernière release](https://github.com/Redstoneur/Jeu_de_la_vie/releases/latest).

## Crédits

Le code pour ce jeu de la vie a été écrit en Python par moi-même, avec l'aide de la bibliothèque Tkinter. Les règles du
jeu de la vie ont été inventées par John Horton Conway en 1970.