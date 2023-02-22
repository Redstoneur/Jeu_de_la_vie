# Jeu_de_la_vie

Le jeu de la vie est un automate cellulaire inventé par John Horton Conway en 1970. Il s'agit d'un jeu de simulation
mathématique dans lequel des cellules évoluent selon des règles simples et produisent des motifs complexes.

## Règles

Le jeu de la vie se déroule sur une grille bidimensionnelle. Chaque cellule peut être soit vivante (1) soit morte (0).
Les cellules évoluent selon les règles suivantes :

1. Si une cellule a exactement trois voisines vivantes, elle devient vivante à la génération suivante.
2. Si une cellule a exactement deux voisines vivantes, elle conserve son état à la génération suivante.
3. Dans tous les autres cas, la cellule meurt ou reste morte à la génération suivante.

## Utilisation

Le jeu de la vie peut être exécuté en utilisant le langage de programmation Python et la bibliothèque Tkinter. Avant de
l'exécuter, assurez-vous d'avoir installé les dépendances en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

Ensuite, vous pouvez lancer le programme en tapant la commande suivante dans un terminal :

```bash
python jeu_de_la_vie.py
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

## Crédits

Le code pour ce jeu de la vie a été écrit en Python par moi-même, avec l'aide de la bibliothèque Tkinter. Les règles du
jeu de la vie ont été inventées par John Horton Conway en 1970.