import os

def renommer_fichiers(dossier):
  """
  Fonction pour renommer les fichiers d'un dossier en remplaçant le premier "-" par "_".

  Args:
    dossier: Le chemin du dossier à traiter.

  Returns:
    None.
  """

  for fichier in os.listdir(dossier):
    nom_fichier = os.path.basename(fichier)
    nouveau_nom = nom_fichier.replace("-", "_", 1)

    if nom_fichier != nouveau_nom:
      os.rename(os.path.join(dossier, fichier), os.path.join(dossier, nouveau_nom))

# Remplacer "C:\Mon\Dossier" par le chemin du dossier que vous souhaitez traiter
dossier = "C:\\Users\\pierry.benoit\\Documents\\SPIE\\AVELIN\\video_importé"

renommer_fichiers(dossier)

print("Fichiers renommés avec succès!")
