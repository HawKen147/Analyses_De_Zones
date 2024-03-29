import tkinter
from tkinter import filedialog
import os
import fonctions
import tkinter.messagebox
import customtkinter
import webbrowser
import windows_err

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

width = 825
height = 500

class main_window(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Aventure en Stockage")
        self.minsize(825,500)
        self.geometry(f"{width}x{height}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="On part où ?", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Essaies Zones")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Analyse de vie")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Mode d'apparence :", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Echelle de l'interface :", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))


        #Main : Essaies Zones
        self.intro_label = customtkinter.CTkLabel(self, width=350, anchor='center', text="Assurez vous que le dossier soit vide avant de créer les dossiers pour stocker les passages. \n Choisissez le nombre de dossier (ou camera) que vous voulez créer. \n Pour plus d'informations vous pouvez aller voir la doc ici : ")
        self.lien2_label = customtkinter.CTkLabel(self, width=350, anchor='center', text="https://github.com/HawKen147/Analyses_De_Zones", cursor="hand2", text_color="blue")
        self.creation_dossiers_label = customtkinter.CTkLabel(self, anchor='center', text="L'arborescence des dossiers créés ressemblera a cela :\n CAM_XX \n         |_rampe \n        |_courir \n           |_marche \n                    |_incomplet.txt")
        self.nb_camera_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Nombre de dossier à créer")
        self.recuperer_repertoire_button = customtkinter.CTkButton(self, height=15, width=30, text="...", command=self.cherche_dir)
        self.chemin_dossier_label = customtkinter.CTkLabel(self, anchor='center', text="Entrer le chemin pour créer les dossiers ou seront stockés les vidéos")
        self.chemin_dossier_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Chemin pour stocker les vidéos")
        self.valider_button = customtkinter.CTkButton(self, anchor='center', text="Valider", command=self.main_button_event)
        self.lien2_label.bind("<Button-1>", self.callback)
    
        #position of the main_frame_widgets
        self.intro_label.grid(row=0, column=1, pady=(50,0), padx=5, sticky="nswe")
        self.lien2_label.grid(row=1, column=1, pady=(0,0), sticky="nsew" )
        self.creation_dossiers_label.grid(row=2,column=1, sticky="nsew")
        self.nb_camera_entry.grid(row=3, column=1, pady=(0,5))
        self.chemin_dossier_label.grid(row=4, column=1, pady=(5,0), sticky="nsew")
        self.chemin_dossier_entry.grid(row=5, column=1)
        self.recuperer_repertoire_button.grid(row=5, column=1, padx=(300,0))
        self.valider_button.grid(row=8,column=1, pady=5)

        #definition initial state       
        self.valider_button.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.bind_all("<KeyPress>", self.functions_calls)

    #ouvre la page internet via l'hyperlink
    def callback(self, event):
        webbrowser.open_new(event.widget.cget("text"))

    #Verifie si le chemin donnée existe
    def check_path(self, path):
        if ((os.path.exists(path) or path == '')):
            return True
        else :
            return False
        
    #Change l'apparence de la fenetre
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    #Change l'echelle de l'interface utilisateur
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    #Récupère les clics sur les boutons dans la sidebar
    def sidebar_button_event(self):
        print("sidebar_button click")   
        

    #Lorsque le bouton Valider est cliqué, on récupere les paramètre entrés dans l'interface
    #On crée le nombre de dossier demander par l'utilisateur et on affiche si tout c'est bien passé ou si il y a des erreurs
    def main_button_event(self):
        nb_camera = self.nb_camera_entry.get()
        chemin_stocker = self.chemin_dossier_entry.get()
        if nb_camera != '' and chemin_stocker!= '':
            #appel la fonction pour créer les dossiers
            if (fonctions.creer_dossier(nb_camera, chemin_stocker)):
                windows_err.window_err(no_err='no_err')
            else :
                windows_err.window_err(simple_err = 'simple_err')

    #Fonction qui appel la fonction qui gere le bouton validé    
    def functions_calls(self, event):
       self.valider_button_event()

    #Change the button state (normal or disabled)
    def valider_button_event(self):
        bool = self.get_entrys()            #Get if the checkbox is checked
        if bool :
            self.valider_button.configure(state="normal")
        else :
            self.valider_button.configure(state="disabled")

    #Récupère l'entré pour le nmobre de caméra, le chemin pour stocker
    def get_entrys(self):
        nb_camera = self.nb_camera_entry.get()
        chemin_stocker = self.chemin_dossier_entry.get()
        if nb_camera.isdigit() and os.path.exists(chemin_stocker) and len(os.listdir(chemin_stocker)) == 0 :          # Verifier si nb_camera est bien un entier, si le chemin renseigner est existant et si le chemin renseigné est vide, si il n'y a rien d'entré dans l'entré des videos surveillances et si la checkbox est bien décocher.
            return True
        
   #ferme la fenetre correspondante
    def close_window(self):
        if hasattr(self, 'err_window') and self.err_window:
            self.err_window.destroy()

    #Lorsqu'une fenetre est créee, l'ouvre au milieu de la fenetre parente
    def window_center(self,window_width, window_height):
        # Obtient les dimensions de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculer les coordonnées pour centrer la fenêtre
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        return x,y
    #Bouton "..." qui ouvre le gestionnaire de fichier et recupere le dossier que l'utilisateur a choisit pour stocker les vidéos
    def cherche_dir(self): 
        chemin_dossier = filedialog.askdirectory()
        chemin_dossier = chemin_dossier.replace('/','\\')
        print(chemin_dossier)
        self.chemin_dossier_entry.insert(0, chemin_dossier)

