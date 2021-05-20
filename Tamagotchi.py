# author: Léna SIMONIN 

#L'image de faim du tamagotchi mort ne marche pas + le malade reste constamment en false mais un label marque lorsqu'il est malade.
from tkinter import *
import time
from tkinter.ttk import Progressbar
import tkinter.simpledialog
import tkinter.messagebox
import _thread


#------------------------------------------------------------------------LES ATTRIBUTS-----------------------------

faim = 100  		# /100
soif = 100			# /100
energie = 100 		# /100
amusement = 100		# /100
jour = 0
malade = False
vivant = True

# Constante--------------------------------------------
Nom_Tama = "n/a"
duree_jour = 5 #en seconde
maladepourcent = 10
faim_update = 1000 #en ms
soif_update = 1000
amusement_update = 1000
energie_update = 1000

# ce que fais lorsque l'on appuie sur le boutons correspondant
faim_ajout = 25
amusement_ajout = 10
soif_ajout = 25
energie_ajout = 50 


gameStarted = False
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------LES SOUS-PROGRAMME-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def startGame(event):
	start()








#------------------------------------------------------------------------DEBUT DU JEU---------------------------------------

def start():
	global gameStarted, faim, amusement, soif, vivant, energie, malade, jour

	if gameStarted == False:
		gameStarted = True
		faim = 100
		energie = 100
		amusement = 100
		soif = 100
		jour = 0
		Malade = False
		vivant = True
		DebutLabel.config(text="le jeu commence")
		update()












#-------------------------------------------------------- LES UPDATES(jours / affichage progress bar/label qui indique)---------------------------------------------------------------------------------
def update():

	updateJour()
	update_affichage()
	update_attribut()



def update_affichage():
	global jour, amusement, faim, energie, soif, malade, vivant

	if faim <= 60:
		catPic.config(image = tamaFaim)
		imageLabel.config(text ="a faim")
	elif malade == True:
		catPic.config(image = tamaMalade)
		imageLabel.config(text= "est malade")
	elif amusement <=70:
		catPic.config(image = tamaEnnuie)
		imageLabel.config(text = "s'ennuie")
	
	elif energie <=50:
		catPic.config(image = tamaFatigue)
		imageLabel.config(text = "A besoin de dormir")
	elif soif <=50:
		catPic.config(image = tamaSoif)
		imageLabel.config(text = "à Soif")
	elif vivant==False:
		catPic.config(image = tamaMort)
	else:
		catPic.config(image = tamaNormal) 
		imageLabel.config(text = " n'as besoin de rien")
		
	progressBar()
	faim_lab.config(text="Faim : "+str(faim))
	amusement_lab.config(text="Amusement : "+str(amusement))
	energie_lab.config(text="Energie : "+str(energie))
	soif_lab.config(text="Soif : "+str(soif))


	jour_Label.config(text="jour: "+ str(jour) )

	catPic.after(100, update_affichage)

def updateJour():
	global jour 
	
	if vivant == True:
		jour += 1
		jour_Label.after(duree_jour * 1000, updateJour)
	
	
def updateLabel(turns,ici):

	global jour

	if vivant == True:
		ehohlab.config(text=ici)
		time.sleep(turns)
		ehohlab.config(text=" ")




def update_attribut():
	updateFaim()
	updateAmusement()
	updateEnergie()
	updateSoif()
	updateMalade()
	
	schrodinger()
	if vivant == True:
		mon_jeux.after(1000,update_attribut)
	


#-----------------------------------------------------------------------UPDATE BESOIN DU TAMA -----------------------------------------------------------------------

def updateFaim():
	global faim
	
	faim -= 5
	
	
def updateSoif():
	global soif 
	
	soif -= 3
	

	
def updateAmusement():
	global amusement 
	
	amusement -= 2


def updateEnergie():
	global energie 
	
	energie -= 5

		
def updateMalade():
	global malade, amusement
	
	if amusement <= 50:
		malade = True







# est-il toujours vivant ?

def schrodinger():                             
	global faim, amusement, energie, soif, vivant

	if faim <=0 or energie <=0 or soif <= 0:
		catPic.config(image = tamaMort)
		imageLabel.config(text ="IL EST MORT BG")
		_thread.start_new_thread(updateLabel, (4, Nom_Tama + "est mort :( "))
		DebutLabel.config( text=" FIN DU JEUX :'( ")
		vivant = False
		fin_de_partie()
		if tkinter.messagebox.askyesno("Rejouer?", "veux tu rejouer ?"):
			start()



def fin_de_partie():
	global vivant, gameStarted
	gameStarted = False
	
	
	
#---------------------------------------------------------------------------bar de progression -----------------------------------------------------------------------------


def progressBar():
	global faim, amusement, energie, soif

	Bar_faim["value"] = faim
	Bar_amusement["value"] = amusement
	Bar_energie["value"] = energie
	Bar_soif["value"] = soif

	if vivant == True:
		Bar_faim.after(100,progressBar)
		
		
		
		
#-----------------------------------------------------------------------------Lié au Bouton--------------------------------------------------------------


	
	

def nourrir():
	global faim, malade
	
	if faim <= 75:
		if malade ==True:
			_thread.start_new_thread(updateLabel, (3,Nom_Tama + " est trop malade pour manger."))
		else:
			faim += faim_ajout
	else:
		_thread.start_new_thread(updateLabel, (3,Nom_Tama + " a deja assez manger"))

def boire():
	global soif, malade
	
	if soif <= 75:
		if malade ==True:
			_thread.start_new_thread(updateLabel, (3,Nom_Tama + " est trop malade pour manger."))
		else:
			soif += soif_ajout
	else:
		_thread.start_new_thread(updateLabel, (3,Nom_Tama + " a deja assez manger"))
		
def jouer():
	global amusement, malade
	
	if amusement <= 90:
		if malade == True:
			_thread.start_new_thread(updateLabel, (3,Nom_Tama + " est trop malade pour jouer soigner le !"))
		else :
			amusement += amusement_ajout
	else:
		_thread.start_new_thread(updateLabel, (3,Nom_Tama + "  n'as pas besoin de jouer"))
		
def dormir():
	global energie, malade
	
	if energie < 50:
		if malade == True:
			_thread.start_new_thread(updateLabel, (3,Nom_Tama + " est trop malade pour dormir paisiblement, soigner le !"))
		else:
			energie += energie_ajout
	else:
		_thread.start_new_thread(updateLabel, (3,Nom_Tama + " ne peux pas dormir, soigner le !"))
		
def soigner():
	global soigner, malade
	
	if malade == True:
		malade = False
	else:
		_thread.start_new_thread(updateLabel, (3,Nom_Tama + " n'est pas malade !"))
			
			
	
#------------------------------------------------------------------ SECONDE FENETRE AVEC LES REGLES -------------------------------------------------
def regles():
    tkinter.messagebox.showinfo( Nom_Tama,
		"Le nom de ton animal est:" + Nom_Tama + "\n, Les regles du jeux : \n\n" +
		"1. Il ne faut pas laisser les barres de vie tel que la Faim, Soif et l'energie de " + Nom_Tama + " atteindre 0.\n" +
		"2. Lorsque " + Nom_Tama + " ne joue pas assez et  atteint moins 50 en amusement, il tombe malade\n" +
		"3. Quand " + Nom_Tama + " est malade il faut le soigner en appuyant sur le bouton soigner,\n"
         +"on ne peux pas le faire manger/boire/jouer/dormir lorsqu'il est malade\n"
         "4.Un jour dure 5 secondes\n")

# initialisation de l'application  --------------------------
mon_jeux = Tk()
mon_jeux.title("Tamagotchi")    # change le titre de la fenetre


#commence le sous programme startGame quand la bare espace est pressé    
mon_jeux.bind("<space>", startGame)


# Label au dessus----------------------------
DebutLabel = Label(mon_jeux, text="Appuyer sur Espace pour commencer le jeux.")
DebutLabel.grid(row=0, column=0, columnspan=5)

#-------------------------------------------------------------------BAR ATTRIBUT----------------------------------

Bar_faim =Progressbar(mon_jeux, orient="horizontal", mode="determinate", length="100", variable="faim")
Bar_faim.grid(row=2, column=0)
faim_lab =Label(mon_jeux, text="Faim : "+str(faim))
faim_lab.grid(row=1, column=0)


malade_lab = Label(mon_jeux, text="Malade : "+str(malade))
malade_lab.grid(row=3, column=2)

Bar_amusement = Progressbar(mon_jeux, orient="horizontal", mode="determinate", length="100", variable="amusement")
Bar_amusement.grid(row=5, column=0)
amusement_lab =Label(mon_jeux, text="Amusement : "+str(amusement))
amusement_lab.grid(row=4, column=0)


Bar_energie = Progressbar(mon_jeux, orient="horizontal", mode="determinate", length="100", variable="energie")
Bar_energie.grid(row=2, column=4)
energie_lab =Label(mon_jeux, text="Energie : "+str(energie))
energie_lab.grid(row=1, column=4)

Bar_soif = Progressbar(mon_jeux, orient="horizontal", mode="determinate", length="100", variable="soif")
Bar_soif.grid(row=5, column=4)
soif_lab =Label(mon_jeux, text="Soif : "+str(soif))
soif_lab.grid(row=4, column=4)




progressBar() 

# --------------------------------------------------------------LABELS------------------------------------------------

ehohlab =Label(mon_jeux, text="")          
ehohlab.grid(row=7, column=0, columnspan=5)
imageLabel =Label(mon_jeux, text="") # Phrase en dessous de l'image
imageLabel.grid(row= 5,column=0, columnspan=5)


#image-------------------------------------------------------------         Photos  au centre du jeux ------------------------------------------
#images provenant des Sticker facebook Meow Town
tamaNormal = PhotoImage(file = "tama_normal.png") 
tamaFaim = PhotoImage(file = "tama_Faim.png")
tamaMalade = PhotoImage(file = "tama_malade.png")
tamaMort = PhotoImage(file = "tama_Mort.png")
tamaEnnuie = PhotoImage(file ="tama_ennuie.png")
tamaFatigue = PhotoImage(file ="tama_Fatigue.png")
tamaSoif = PhotoImage(file ="tama_Soif.png")

# positionnement de l'image au centre
catPic = tkinter.Label(mon_jeux, image=tamaNormal)
catPic.grid(row=6, column=0, columnspan=5)


#------------------------------------------------------------------------LABEL JOUR ( sous la photo)------------------------------------------------

jour_Label = Label(mon_jeux, text="Jour: "+ str(jour))
jour_Label.grid(row=8, column=2)

#-----------------------------------------------------------------------------Bouton----------------------------------- ------------------------
btnNourrir = Button(mon_jeux, text= "Nourrir", command=nourrir, fg="pink", activebackground="black", bg="grey")
btnNourrir.grid(row=9,column=0)

btnBoire = Button(mon_jeux, text= "Boire", command=boire, fg="pink", activebackground="black", bg="grey")
btnBoire.grid(row=9,column=1)

btnJouer = Button(mon_jeux, text= "Jouer", command=jouer, fg="pink", activebackground="black", bg="grey")
btnJouer.grid(row=9,column=2)

btnDormir = Button(mon_jeux, text= "Dormir", command=dormir, fg="pink", activebackground="black", bg="grey")
btnDormir.grid(row=9,column=3)

btnSoigner = Button(mon_jeux, text= "Soigner", command=soigner, fg="pink", activebackground="black", bg="grey")
btnSoigner.grid(row=9,column=4)

#---------------------------------------------------------------------------------------premiere fenetre----------------------------------------------------------
Nom_Tama = tkinter.simpledialog.askstring("Nom", "Donnez un nom a votre animal", initialvalue = "Tama")  # idée= ajouter une liste radiobutton pour choisir le nom du tama'
if not Nom_Tama:
	Nom_Tama = "pouly"
else:
	Nom_Tama = Nom_Tama.upper()
regles()



mon_jeux.mainloop()
