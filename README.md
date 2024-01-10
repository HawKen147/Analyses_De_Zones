# Application Analayse de Zones
## Objectifs de l'application
- Facilité la création de fichiers
- Gagner du temps lors de la vérification si il manque des dossiers / fichiers
- Limite les erreurs de manipulation
- Création du fichier excel de maniere simple et rapide

## Version actuel V0.5
La version V0.5 est une version minimaliste qui replit presque tout les objectifs. Le visuel est terminé mais reste à être confirmé par les utilisateurs.
### V0.5
La v0.5 permet de créer les dossiers qui permettront de stocker les videos d'eesaies de zones 
```
CAM_XX
  |-rampe
  |-courir
  |-marche
  |-incomplet.txt
```
Le dossier "CAM_XX" contient les dossiers rampe, courir, marche et le fichier incomplet.txt.
Il y a autant de dossier CAM_XX que de camera. Il suffit de le creer depuis l'application.
- Le dossier rampe contient les vidéos des essaies de zones en rampant
- Le dossier marche contient les vidéos des essaies de zones en marchant
- Le dossier courir contient les vidéos des essaies de zones en courant
- Le dossier incomplet.txt contient toutes les vidéos manquantes dans les differents dossiers
 - DM -> Debut Marché, DC -> Début Courir, DR -> Début Rampé, MC -> Milieux Courir, MM -> Milieux MArché, MR -> Milieux Rampé, FC -> Fin Courir, FM -> Fin Marché, FR -> Fin Rampé.
** Chaque nom de vidéos doit avoir un nom générique et le format .asf: ** NomDuSite_THXX-aaaa-mm-jj_00h00min00s000ms_DM.asf
** Avec la version 0.5, on ne peut pas encore créer de fichier excel. **
## Prochaines Mises à jours
- Ajouter la vérification des fichiers en double (si les deux fichiers on le meme nom, ils ne peuvent pas etre dans le même dossier, mais cela crée une erreur)
- Création du fichier excel avec toutes les informations utiles
- Incoporer les analyses de vie a l'interface graphique. 
### Rendu de l'application (front-end)
![Screenshot de l'application](https://www.aht.li/3826115/Capture_decran_2024-01-10_134231.png)
