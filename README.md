# Application Analyse de Zones
## Objectifs de l'application
- Faciliter la création de dossiers
- Gagner du temps lors de la vérification si il manque des dossiers / fichiers
- Limite les erreurs de manipulation
- Création du fichier excel de manière simple et rapide

## Version actuel V0.6
La version V0.6 est une version minimaliste qui remplit presque tous les objectifs. Le visuel est (presque) terminé.
### V0.6
La v0.6 permet de créer les dossiers qui permettront de stocker les videos d'essaies de zones 
```
CAM_XX
  |-rampe
  |-courir
  |-marche
  |-incomplet.txt
```
Le dossier "CAM_XX" contient les dossiers rampe, courir, marche et le fichier incomplet.txt.
Il y a autant de dossier CAM_XX que de camera. Il suffit de les créer depuis l'application.
- Le dossier rampe contient les vidéos des essaies de zones en rampant
- Le dossier marche contient les vidéos des essaies de zones en marchant
- Le dossier courir contient les vidéos des essaies de zones en courant
- Le dossier incomplet.txt contient toutes les vidéos manquantes dans les différents dossiers
 - DM -> Debut Marché, DC -> Début Courir, DR -> Début Rampé, MC -> Milieux Courir, MM -> Milieux MArché, MR -> Milieux Rampé, FC -> Fin Courir, FM -> Fin Marché, FR -> Fin Rampé.
- Les fichiers en double ne sont pas déplacés et sont affichés dans la fenêtre erreur lors de la fin de l'éxecution du programme.

**Avec la version 0.6, pas besoin de nom générique, A partir du moment ou dans le nom de fichier figure bien "TH" et si le passage est au fond (F), milieux (M) ou debut (D) de zone avec le style de passage (Ramper (R), Marcher (M), Courir (C)). Exemple : NomDuSite_THxx_HeureDuPassage_DM, THxxHeureDuPassageDM**

**Avec la version 0.6, on ne peut pas encore créer de fichier excel !**
## Prochaines Mises à jours
- Refaire l'interface utilisateur pour que ce soit plus simple
- Création du fichier excel avec toutes les informations utiles
- Incorporer les analyses de vie a l'interface graphique
### Rendu de l'application (front-end)
![Screenshot de l'application](https://www.aht.li/3826115/Capture_decran_2024-01-10_134231.png)
