from tkinter import filedialog
from functools import partial
import windows_err as werr
import tkinter.messagebox
import customtkinter
import create_excel
import webbrowser
import fonctions
import tkinter
import main
import os

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
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

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
        self.sidebar_button_2.configure(state="disabled")
        self.sidebar_label_create_excel = customtkinter.CTkLabel(self.sidebar_frame, text="Génèrer Excel")
        self.sidebar_label_create_excel.grid(row=5, column=0, padx=20, pady=(10,0))
        self.sidebar_button_create_excel = customtkinter.CTkButton(self.sidebar_frame, command=self.create_excel, text="Créer Excel")
        self.sidebar_button_create_excel.grid(row=6, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Mode d'apparence :", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Echelle de l'interface :", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))


        #Main : Essaies Zones
        self.intro_label = customtkinter.CTkLabel(self, width=350, anchor='center', text="Ici, nous allons maintenant déplacer les videos de surveillances dans les dossiers qui ont été crée précedement. \n Pour se faire il faut renseigner le chemin des dossiers créer précedement et le dossier ou les videos sont stocker \n pour être déplacer dans les bons dossiers.  \n Pour plus d'informations vous pouvez consulter la doc en cliquant sur le lien ci dessous.")
        self.lien2_label = customtkinter.CTkLabel(self, width=350, anchor='center', text="https://github.com/HawKen147/Analyses_De_Zones", cursor="hand2", text_color="blue")
        checked = customtkinter.IntVar()
        self.verification_checkbox = customtkinter.CTkCheckBox(self, variable=checked, onvalue=True, offvalue=False, text="Cocher pour voir les fichiers manquants", command=self.valider_button_event)
        self.chemin_video_label = customtkinter.CTkLabel(self, anchor='center', text="Entrer le chemin pour récupérer les vidéos de surveillance")
        self.chemin_video_recuperer_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Chemin pour récuperer les vidéos")
        variable_recup_dir = "recuperer_repertoire_videos_recuperer_button"
        variable_stock_dir = "recuperer_repertoire_videos_stocker_button"
        self.recuperer_repertoire_videos_recuperer_button = customtkinter.CTkButton(self, anchor='center', height=15, width=30, text="...", command=partial(self.cherche_dir, variable_recup_dir))
        self.chemin_dossier_label = customtkinter.CTkLabel(self, anchor='center', text="Entrer le chemin pour stocker les vidéos de surveillance")
        self.chemin_video_stocker_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Chemin pour stocker les vidéos")
        self.recuperer_repertoire_videos_stocker_button = customtkinter.CTkButton(self, anchor='center', height=15, width=30, text="...", command=partial(self.cherche_dir, variable_stock_dir))
        self.retour_creation_dossier = customtkinter.CTkLabel(self, text="Besoin de créer les dossiers ?", cursor="hand2", text_color="blue")
        self.lien2_label.bind("<Button-1>", self.callback)
        self.valider_button = customtkinter.CTkButton(self, anchor='center', text="Valider", command=self.main_button_event)
    
        #position of the main_frame_widgets
        self.intro_label.grid(row=0, column=1, pady=(50,0), padx=5, sticky="nswe")
        self.lien2_label.grid(row=1, column=1, pady=(0,0), sticky="nsew")
        self.verification_checkbox.grid(row=2, column=1, pady=(20,0), padx=(width / 4, 0), sticky="nsew")
        self.chemin_video_label.grid(row=3, column=1, pady=(5,0), sticky="nsew")
        self.chemin_video_recuperer_entry.grid(row=4, column=1)
        self.recuperer_repertoire_videos_recuperer_button.grid(row=4, column=1, padx=(300,0))
        self.chemin_dossier_label.grid(row=5, column=1, pady=(5,0), padx=5, sticky="nsew")
        self.chemin_video_stocker_entry.grid(row=6, column=1)
        self.recuperer_repertoire_videos_stocker_button.grid(row=6, column=1, padx=(300, 0))
        self.retour_creation_dossier.grid(row=7, column=1)
        self.valider_button.grid(row=8,column=1, pady=(0,15))

        #definition initial state       
        self.valider_button.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.bind_all("<KeyPress>", self.functions_calls)
        self.bind_all("<ButtonPress-1>", self.functions_calls)
        self.retour_creation_dossier.bind("<ButtonPress-1>", self.back_to_main)
        self.sidebar_button_create_excel.configure(state="disabled")
        
    
    #ouvre la page internet via l'hyperlink
    def callback(self, event):
        webbrowser.open_new(event.widget.cget("text"))
        
    #Check if the given path exits
    def check_path(self, path):
        if ((os.path.exists(path) or path == '')):
            return True
        else :
            return False
    
    #Get the entrys for the number of cameras, path to get the videos, path to stock the videos and the checkbox state
    def get_entrys(self):
        chemin_get_videos = self.chemin_video_recuperer_entry.get()
        chemin_stocker = self.chemin_video_stocker_entry.get()
        check_folders_checkbox = self.verification_checkbox.get()
        if check_folders_checkbox and os.path.exists(chemin_stocker):
            return True
        elif os.path.exists(chemin_stocker) and len(os.listdir(chemin_stocker)) == 0 and chemin_get_videos == '' and not check_folders_checkbox :          # Verifier si nb_camera est bien un entier, si le chemin renseigner est existant et si le chemin renseigné est vide, si il n'y a rien d'entré dans l'entré des videos surveillances et si la checkbox est bien décocher.
            return True
        elif os.path.exists(chemin_stocker) and len(os.listdir(chemin_stocker)) > 0 and  os.path.exists(chemin_get_videos) and not check_folders_checkbox :   #verifie si le nb de camera est null, si le chemin stocker existe et n'est pas vide, si le chemin pour les videos existe bien et n'est pas vide, si la checkbox n'est pas coché.
            return True
        
    #Change the button state (normal or disabled)
    def valider_button_event(self):
        bool = self.get_entrys()            #Get if the checkbox is checked
        if bool :
            self.valider_button.configure(state="normal")
        else :
            self.valider_button.configure(state="disabled")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")   
        
    def main_button_event(self):
        chemin_stocker = self.chemin_video_stocker_entry.get()
        chemin_get_videos = self.chemin_video_recuperer_entry.get()
        if self.verification_checkbox.get() and chemin_stocker != "":
            #appel la fonction pour verifier tous les fichiers
            dict_check = fonctions.check_folders(chemin_stocker)
            werr.window_err.win_err(self, dict_check=dict_check)
        elif chemin_stocker != '' and chemin_get_videos != '':
            list_video_err, list_bad_extensions, list_video_err_double = fonctions.get_video_cam_files(chemin_get_videos, chemin_stocker)  #appel la fonction pour déplacer les videos des cameras
            if (list_video_err or list_bad_extensions or list_video_err_double):
                werr.window_err.win_err(self, list_video_err=list_video_err, list_bad_extensions=list_bad_extensions, list_video_err_double=list_video_err_double)
            else :
                werr.window_err.win_err(self, no_err = 'no_err')
    
    #fonction qui appel la fonction qui gere le bouton validé
    def functions_calls(self, event):
       self.valider_button_event()
       self.excel_button()

   
   #ferme la fenetre correspondante
    def close_window(self):
        if hasattr(self, 'err_window') and self.err_window:
            self.err_window.destroy()

    def window_center(self,window_width, window_height):
        # Obtient les dimensions de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculer les coordonnées pour centrer la fenêtre
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        return x,y

    def cherche_dir(self, nom_button): 
        chemin_dossier = filedialog.askdirectory()
        chemin_dossier = chemin_dossier.replace('/','\\')
        if nom_button == "recuperer_repertoire_videos_recuperer_button" :
            self.chemin_video_recuperer_entry.delete(0, customtkinter.END)
            self.chemin_video_recuperer_entry.insert(0, chemin_dossier)
        elif nom_button == "recuperer_repertoire_videos_stocker_button" :
            self.chemin_video_stocker_entry.delete(0, customtkinter.END)
            self.chemin_video_stocker_entry.insert(0, chemin_dossier)
        
    #Fonction qui appel la fonction de la création du fichier excel
    #Si il y a une erreur, alors appel la fonction pour ouvrir la fenêtre d'erreur et affiche les erreurs
    def create_excel(self):
        erreurs = create_excel.main_excel()
        print(erreurs)

        
    #cette fonction crée la fenetre no err
    def call_window_no_err(self):
        werr.window_err.win_err(self.sidebar_frame, no_err = 'no_err')

    #Gestion du bouton de la création du fichier excel (bouton sidebar "excel")
    def excel_button(self): 
        chemin_stockage_video = self.chemin_video_stocker_entry.get()
        if os.path.exists(chemin_stockage_video):
            self.sidebar_button_create_excel.configure(state="normal")
        else : 
            self.sidebar_button_create_excel.configure(state="disabled")
    
    #lorsque le lien "les dossiers sont déja créer ?" est cliqué, ,on change de fenetre pour aller sur la fenetre suivante pour déplacer les videos
    #La fonction peut aussi etre appelé lorsque les dossiers ont finis d'être crées
    def back_to_main(self, event):
        self.destroy()
        main.main_win()

    def test(self):
        print("je suis cliqué")