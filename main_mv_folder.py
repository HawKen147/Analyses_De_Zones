import view.window_mv_files as window_mv_files

#Foncion qui permet de créer la fenêtre pour déplacer les fichiers (appel le fichier view/window_mv_files)
def mv_win():
    app = window_mv_files.main_window()
    app.mainloop()