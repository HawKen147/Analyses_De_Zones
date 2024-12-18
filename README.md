# Application Analyse de Zones
## Objectifs de l'application
- Faciliter la création de dossier
- Gagner du temps lors de la vérification si il manque des dossiers / fichiers
- Limite les erreurs de manipulation
- Création du fichier excel de manière simple et rapide

## Version actuel V1.0
La version V1.0 est la première version fini du script.
Le script permet de déplacer les clips vidéos contenue dans le coffre fort de Genetec, dans des dossiers créés depuis l'application. Cela permet de gagner du temps et d'éviter les erreurs lorsque l'on extrait les clips de test. Le script vérifie la bonne extension du clip et si le clip n'existe pas déja. Si ces conditions sont respectés, alors le clip est déplacé dans le bon dossier.
### V1.0
La V1.0 permet de créer les dossiers qui permettront de stocker les vidéos d'essaies de zones. Il suffit de renseigner le dossier dans lequel on souhaite stocker les vidéos. Le dossier doit être vide sinon cela ne marche pas.

Ci dessous l'arborescence des dossiers créés pour chaque caméra
```
CAM_XX
  |-rampe
  |-courir
  |-marche
  |-incomplet.txt
```
Le dossier "CAM_XX" contient les dossiers rampe, courir, marche et le fichier incomplet.txt.
Il y a autant de dossier CAM_XX que de caméra. Il suffit de les créer depuis l'application.
- Le dossier rampe contient les vidéos des essaies de zones en rampant
- Le dossier marche contient les vidéos des essaies de zones en marchant
- Le dossier courir contient les vidéos des essaies de zones en courant
- Le fichier incomplet.txt contient toutes les vidéos manquantes dans les différents dossiers
 - DM -> Debut Marché, DC -> Début Courir, DR -> Début Rampé, MC -> Milieux Courir, MM -> Milieux MArché, MR -> Milieux Rampé, FC -> Fin Courir, FM -> Fin Marché, FR -> Fin Rampé.
- Les fichiers en double ne sont pas déplacés et sont affichés dans la fenêtre erreur lors de la fin de l'éxecution du programme.

**Avec la version 1.0, pas besoin de nom générique, A partir du moment ou dans le nom de fichier figure bien "TH" et si le passage est au fond (F), milieux (M) ou debut (D) de zone avec le style de passage (Ramper (R), Marcher (M), Courir (C)). Exemple : NomDuSite_THxx_HeureDuPassage_DM, THxxHeureDuPassageDM**

La V1.0 permet aussi la création d'un fichier Excel ! Le fichier excel permet d'afficher rapidement les clips vidéos présent dans les dossiers. Le fichier excel est créé et stocké dans le dossier excel du projet. 
Une fois les dossiers créés, il faudra renseigner le chemin où sont stockés les vidéos des passages. Une fois cela réalisé, le bouton pour générer l'excel deviendra cliquable.

## Prochaines Mises à jours
- Incorporer les analyses de vie à l'interface graphique
- Gestion de la fenêtre, éviter quelle ne s'ouvre qu'au même endroit (même après l'avoir déplacé)

### Rendu de l'application (front-end)
# Thème claire 
![Screenshot de l'application thème claire 1](https://www.aht.li/3849489/Capture_decran_2024-05-13_123516.png)
![Screenshot de l'application thème claire 2](https://www.aht.li/3849490/Capture_decran_2024-05-13_123537.png)
# Thème sombre 
![Screenshot de l'application thème Sombre 1](https://www.aht.li/3849491/Capture_decran_2024-05-13_123622.png)
![Screenshot de l'application thème Sombre 2](https://www.aht.li/3849493/Capture_decran_2024-05-13_123600.png)
