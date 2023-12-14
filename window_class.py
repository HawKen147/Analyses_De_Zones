import tkinter
import os
import fonctions
import tkinter.messagebox
import customtkinter

#Corriger le code pour qu'il ne fasse pas d'erreur lorsque le fichier dans le dossier des vidéos a déplacer lorsque celui ci ne convient pas au format

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

width = 825
height = 500

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Move Folder")
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
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Essaies Zones")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Analyse de vie")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))


        #Main : Essaies Zones
        self.intro_label = customtkinter.CTkLabel(self, width=350, anchor='center', text="Pour commencer, choisissez si vous voulez créer les fichiers afin de mettre les vidéos des cameras dedans. \n Ensuite, assurez vous que le dossier fournis soit vide pour créer les dossiers des caméras. \n Enfin donnez le chemin des vidéos pour quelles soient deplacés dans les dossiers crée précédement. \n Le nom des vidéos doivent êtres comme suis : 'Nom_THXX-aaaa-mm-jj_10h44min02s083ms_DM.asf'. \n THXX avec XX le numero de la camera (00 à <99) ")
        self.creation_dossiers_label = customtkinter.CTkLabel(self, anchor='center', text="Arborescence des dossiers créer :\n CAM_XX \n         |_rampe \n        |_courir \n           |_marche \n                    |_incomplet.txt")
        self.nb_camera_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Nombre de dossier à créer")
        checked = customtkinter.IntVar()
        self.verification_checkbox = customtkinter.CTkCheckBox(self, variable=checked, onvalue=True, offvalue=False, text="Cocher pour voir les fichiers manquants", command=self.valider_button_event)
        self.chemin_dossier_label = customtkinter.CTkLabel(self, anchor='center', text="Entrer le chemin pour créer / stocker les vidéos")
        self.chemin_video_label = customtkinter.CTkLabel(self, anchor='center', text="Entrer le chemin pour récupérer les vidéos de surveillance")
        self.chemin_dossier_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Chemin pour stocker les vidéos")
        self.chemin_video_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Chemin pour récupérer les vidéos")
        self.valider_button = customtkinter.CTkButton(self, anchor='center', text="Valider", command=self.main_button_event)
    
        #position of the main_frame_widgets
        self.intro_label.grid(row=0, column=1, pady=(50,0), padx=5, sticky="nswe")
        self.creation_dossiers_label.grid(row=1,column=1, sticky="nsew")
        self.nb_camera_entry.grid(row=2, column=1, pady=(0,5))
        self.verification_checkbox.grid(row=3, column=1)
        self.chemin_dossier_label.grid(row=4, column=1, pady=(5,0), sticky="nsew")
        self.chemin_dossier_entry.grid(row=5, column=1, pady=(0,5))
        self.chemin_video_label.grid(row=6, column=1, pady=(5,0), sticky="nsew")
        self.chemin_video_entry.grid(row=7, column=1, pady=(0,5))
        self.valider_button.grid(row=8,column=1, pady=5)

        #definition initial state       
        self.valider_button.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.bind_all("<KeyPress>", self.functions_calls)

    def check_path(self, path):
        if ((os.path.exists(path) or path == '')):
            return True
        else :
            return False
        
    """def modify_entrys(self):
         nb_camera = self.nb_camera_entry.get()
         if nb_camera.isdigit():
        """

    def get_entrys(self):
        nb_camera = self.nb_camera_entry.get()
        chemin_stocker = self.chemin_dossier_entry.get()
        chemin_get_videos = self.chemin_video_entry.get()
        check_folders_checkbox = self.verification_checkbox.get()
        #print(check_folders_checkbox)
        if check_folders_checkbox:
            return True
        elif nb_camera.isdigit() and os.path.exists(chemin_stocker) and len(os.listdir(chemin_stocker)) == 0 and chemin_get_videos == '' and not check_folders_checkbox :          # Verifier si nb_camera est bien un entier, si le chemin rensigner est existant et si le chemin renseigner est vide, si il n'y a rien d'entré dans lentré des videos surveillances et si la checkbox est bien décocher.
            return True
        elif nb_camera == '' and os.path.exists(chemin_stocker) and len(os.listdir(chemin_stocker)) > 0 and  os.path.exists(chemin_get_videos) and len(os.listdir(chemin_get_videos)) > 0 and not check_folders_checkbox :   #verifie si le nb de camera est null, si le chemin stocker existe et n'est pas vide, si le chemin pour les videos existe bien et n'est pas vide, si la checkbox n'est pas coché.
            return True
        
            
    def valider_button_event(self):
        bool = self.get_entrys()
        if bool :
            self.valider_button.configure(state="normal")
        else :
            self.valider_button.configure(state="disabled")
        #print(f"nb_cam = {nb_camera}, chemin stocker = {chemin_stocker}, chemin_get_videos {chemin_get_videos}")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")   
        
    def main_button_event(self):
        nb_camera = self.nb_camera_entry.get()
        chemin_stocker = self.chemin_dossier_entry.get()
        chemin_get_videos = self.chemin_video_entry.get()
        if self.verification_checkbox.get():
            #appel la fonction pour verifier tous les fichiers
            print("check les fichiers manquants")
        elif nb_camera != '' and chemin_stocker!= '':
            #appel la fonction pour créer les dossiers
            fonctions.creer_dossier(nb_camera, chemin_stocker)
        elif chemin_stocker!= '' and chemin_get_videos != '':
            #appel la fonction pour déplacer les videos des cameras
            fonctions.get_video_cam_files(chemin_get_videos, chemin_stocker)
    
    def functions_calls(self, event):
       # self.check_path(self.chemin_dossier_entry.get())
       self.valider_button_event()
    
    #def afficher_taille_frame(self, event=None):
    #    largeur_sidebar_frame = self.sidebar_frame.winfo_width()
    #    hauteur_sidebar_frame = self.sidebar_frame.winfo_height()
    #    heuteur_main_frame = self.main_frame.winfo_height()
    #    largeur_main_frame = self.main_frame.winfo_width()
    #    width = self.winfo_width()
    #    height = self.winfo_height() 
    #    print(f"Largeur window : {width} pixels")
    #    print(f"Hauteur window : {height} pixels")
    #    print(f"Largeur du frame {largeur_sidebar_frame} pixels")
    #    print(f"Hauteur du frame {hauteur_sidebar_frame} pixels")
    #    print(f"Largeur du frame {largeur_main_frame} pixels")
    #    print(f"Hauteur du frame {heuteur_main_frame} pixels")
        
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
