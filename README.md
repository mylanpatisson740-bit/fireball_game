# Fireball Game

Petit jeu 2D en Python avec **pygame** : tu contrôles un arbre qui lance des boules de feu sur une momie qui te poursuit.

## Installation

Il faut Python 3 et pygame :

```
pip install pygame
```

## Lancer le jeu

Depuis le dossier du projet :

```
python main.py
```

## Commandes

| Touche  | Action                              |
|---------|-------------------------------------|
| Flèches | Se déplacer                         |
| Espace  | Lancer une boule de feu             |
| R       | Rejouer (sur l'écran Game Over)     |

## Règles

- Chaque boule de feu enlève 20 points de vie au monstre.
- Un monstre vaincu rapporte **100 points**, puis un nouveau monstre apparaît.
- Si le monstre te touche, tu perds de la vie petit à petit. À 0, c'est **Game Over**.

## Fichiers

| Fichier            | Rôle                                      |
|--------------------|-------------------------------------------|
| `main.py`          | Le jeu                                    |
| `arbre.png`        | Sprite du joueur                          |
| `mommy.png`        | Sprite du monstre                         |
| `bdf.png`          | Sprite de la boule de feu                 |
| `fond.jpg`         | Image de fond                             |
| `Fonction.py`, `verif_matrice.py` | Exercices Python (pas liés au jeu) |
