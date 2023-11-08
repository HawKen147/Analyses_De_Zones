import customtkinter as ctk
from fonctions import *

#definit le mode qui sera affiché dans la fenetre
ctk.set_appearance_mode("Light")

#fonction qui permet d'appeler d'autres fonctions selon l'evenement 
def appel_fonctions(e):
    cache_bouton_valider(e)
    affiche_bouton_creation_dossier(e)

#Verifie si les chemins données existent et si elles existent, appel la fonction recupere les videos du fichiers 
def valider():
    if entry_chemin_dossier.get() and entry_chemin_video.get() :
        val_entry_chemin_dossier = entry_chemin_dossier.get()
        val_entry_chemin_video = entry_chemin_video.get()
        #appel la fonction pour bouger les fichiers d'un dossier a un autre dossier
        get_video_cam_files(val_entry_chemin_video,val_entry_chemin_dossier)

def affiche_bouton_creation_dossier(e):
    val_nb_camera = entry_nb_camera.get()
    chemin_dossiers = entry_chemin_dossier_nb_camera.get()
    res_chemin_dossier = verifie_chemin_dossiers(chemin_dossiers)
    print(res_chemin_dossier, val_nb_camera, chemin_dossiers)
    if res_chemin_dossier == False and  verifie_str_is_int(val_nb_camera) and int(val_nb_camera) > 0:
        button_valide_creation_cam.grid(pady=5, row=8)


#Cache le Widget en fonction de si la chekcboxe est coché ou non
def gestion_case_cocher():
    if (checked.get() == 1):
        affiche_cache_widget(1)
    else :
        affiche_cache_widget(2)

#Verifie si les dossiers fournis existent, si il existent
#affiche le bouton valide
def cache_bouton_valider(e):
    print("vous avez pressez une touche")
    chemin_dossiers = entry_chemin_dossier.get()
    chemin_videos = entry_chemin_video.get()
    res_chemin_dossier = verifie_chemin_dossiers(chemin_dossiers)
    res_chemin_video = verifie_chemin_dossiers(chemin_videos)
    if res_chemin_dossier and res_chemin_video :
            resultat_label.grid_forget()
            bouton_valider.grid(pady=5, row=11)
    if res_chemin_video == False :
        resultat_label.grid(pady=5, row=11)
        resultat_label.configure(text=f" Le chemin \"{chemin_videos} \" vers les videos n'existe pas ou est vide")
        bouton_valider.grid_forget()
    elif res_chemin_dossier == False:
        resultat_label.grid(pady=5, row=11)
        resultat_label.configure(text=f" Le chemin \"{chemin_dossiers} \" vers les dossiers n'existe pas ou est vide")
        bouton_valider.grid_forget()

#appel les fonctions cache widget ou affiche widget selon ce que l'on veut faire
def affiche_cache_widget(bool_affiche):
    match bool_affiche:
        #affiche ce qu'il y a quand on coche la checkboxe
        case 1:
            cache_widget_entre_dossier()
            affiche_widget_nb_camera()
        case 2:
            cache_widget_nb_camera()
            affiche_widget_entre_dossier()
        case _ :
            cache_widget_nb_camera()
            affiche_widget_entre_dossier()

#cache le widget de la camera
def cache_widget_nb_camera():
    entry_nb_camera.delete(0, 200) #supprime l'entré quand on décoche la checkboxe (les 200 premiers caracteres entrés dans l'entry)
    label_nb_camera.grid_forget()
    entry_nb_camera.grid_forget()
    entry_chemin_dossier_nb_camera.grid_forget()
    button_valide_creation_cam.grid_forget()

#cache le widget / label dossier
def cache_widget_entre_dossier():
    label_dossier_video.grid_forget()
    entry_chemin_dossier.grid_forget()
    label_chemin_video.grid_forget()
    entry_chemin_video.grid_forget()

def affiche_widget_nb_camera():
    label_nb_camera.grid(pady=5, row=4)
    entry_nb_camera.grid(pady=5, row=5)
    label_dossier_video.grid(pady=5, row=6)
    entry_chemin_dossier_nb_camera.grid(pady=5, row=7)


def affiche_widget_entre_dossier():
    label_dossier_video.grid(pady=5, row=7)
    entry_chemin_dossier.grid(pady=5, row=8)    
    label_chemin_video.grid(pady=5,row=9)
    entry_chemin_video.grid(pady=5, row=10)

# Crée une fenêtre principale
fenetre = ctk.CTk()
fenetre.title("Entrée de données")
fenetre.minsize(800, 600)

#creer un label 
label_presentation = ctk.CTkLabel(fenetre,text="Pour commencer, veuilliez choisir si vous voulez créer les fichiers afin de mettre les vidéos des cameras dedans. \n Ensuite, assurez vous que le dossier fournis soit vide pour créer les dossiers des caméras. \n Enfin donnez le chemin des vidéos pour quelles soient deplacés dans les dossiers crée précédement. \n Le nom des vidéos doivent êtres comme suis : 'Nom_THXX-aaaa-mm-jj_10h44min02s083ms_DM.asf'. \n THXX avec XX le numero de la camera (00 à <99) ")
label_presentation.grid(row=1, pady=30)


label_creation_dossiers = ctk.CTkLabel(fenetre,text="Cocher la case si vous souhaitez creer les dossiers (voir exemple ci dessous) \n CAM_XX \n         |_rampe \n        |_courir \n            |_marche \n                     |_incomplet.txt")
label_creation_dossiers.grid(row=2)

# Crée une variable Tkinter pour stocker l'état de la case à cocher
checked = ctk.IntVar()

# Crée la case à cocher
case_checkbox = ctk.CTkCheckBox (fenetre, text="Cocher la case si vous souhaitez creer les dossiers", variable=checked, onvalue=1, offvalue=0, command=gestion_case_cocher)
case_checkbox.grid(row=3)

#label + champs entré pour le nombre de camera à créer
#Ils sont afficher si la checkbox est coché ou pas
label_nb_camera = ctk.CTkLabel(fenetre, text=("Veuillez saisir le nombre de camera pour creer le meme nombre de dossier qui correspond au nombre de camera"))
entry_nb_camera = ctk.CTkEntry(fenetre, width=50)
#entry pour le chemin pour creer les dossiers
entry_chemin_dossier_nb_camera = ctk.CTkEntry(fenetre, width=400)

button_valide_creation_cam = ctk.CTkButton(fenetre, text=("Creer dossiers camera"), command=lambda : creer_dossier(entry_nb_camera.get(), entry_chemin_dossier_nb_camera.get() ))

# Crée les étiquettes (labels) pour les champs d'entrée (Entrys)
label_dossier_video = ctk.CTkLabel(fenetre,  text="Chemin vers les dossiers pour stocker les videos (ou creer les dossiers qui vont stocker les videos)")
label_dossier_video.grid(pady=5, row=7)
entry_chemin_dossier = ctk.CTkEntry(fenetre, width=400)
entry_chemin_dossier.grid(pady=5, row=8)




label_chemin_video = ctk.CTkLabel(fenetre, text="Chemin vers les dossiers pour récuperer les videos")
label_chemin_video.grid(pady=5,row=9)
entry_chemin_video = ctk.CTkEntry(fenetre, width=400)
entry_chemin_video.grid(pady=5, row=10)

#Affiche ce que l'utilsateur a rentré
resultat_label = ctk.CTkLabel(fenetre, text="")


# Crée un bouton pour valider les données
bouton_valider = ctk.CTkButton(fenetre, text="Valider", command=valider)

fenetre.bind_all("<KeyPress>", appel_fonctions)


#permet de creer les "grilles" dans la fenetres
fenetre.grid_columnconfigure(0, weight=1)

# Lance la boucle principale
fenetre.mainloop()
