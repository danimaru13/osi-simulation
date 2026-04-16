# Simulation du modèle OSI en Python

## Description

Ce projet a été réalisé dans le cadre du cours de Programmation pour la Cybersécurité.

Il s'agit d'une simulation du modèle OSI (Open Systems Interconnection) permettant d’illustrer le processus de communication réseau à travers ses 7 couches.

Le programme montre comment un message est transformé lors de son envoi (encapsulation) et comment il est reconstruit à la réception (décapsulation).

## Fonctionnement

Le programme fonctionne en deux grandes étapes :

### 1. Encapsulation (envoi)

Le message passe successivement par les 7 couches du modèle OSI :

- Application  
- Présentation  
- Session  
- Transport  
- Réseau  
- Liaison  
- Physique  

Chaque couche ajoute une information au message sous forme de balises (ex : <IP>, <TCP>, etc.).

À la fin, le message est converti en binaire pour simuler la transmission physique.

### 2. Décapsulation (réception)

Le processus inverse est appliqué :

- chaque couche enlève les informations qu’elle a ajoutées  
- le message est progressivement reconstruit  
- on retrouve le message initial  

## Lancer le programme

Assurez-vous d’avoir Python installé, puis exécutez :

Simulation_OSI.py

## Démonstration
Vidéo de démonstration du fonctionnement du programme :
[Voir la vidéo](./osi-simulation-demo.mp4)

