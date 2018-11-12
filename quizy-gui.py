#!/usr/bin/python
# coding: utf-8

from Tkinter import *
import random

point = 0

window = Tk()
window.config(background='white')
mot_vide = Label(window, text='', bg='white')
mot_vide.grid(row=0, padx=10, pady=10)

submit = Button(window)	
result = Label(window, text='', bg='white')

def game():
	mot = random.choice(["betterave", "brocoli", "carotte", "chou", "citrouille", "courge", "fenouil", "panais", "poireau", "potiron", "salsifis", "topinambour", "potimarron", "rutabaga", "radis", "champignon"])
	tab_vide = []
	tab_mot = []
	
	for x in mot:
		tab_vide.append('_')
		tab_mot.append(x)

	tiret = str('Mot à deviner : \n' + ' '.join(tab_vide))
	mot_vide.config(text=tiret)
	
	question = Label(window, text='\nEntrez une lettre du mot mystère: ', bg='white')
	question.grid(row=1, padx=10, pady=10)
	
	champ = Entry(window, bg='white')
	champ.focus_set()
	champ.grid(row=2, padx=10, pady=10)
	
	def match():
	
		resp = champ.get()
		champ.delete(0, 'end')
		global point

		if (resp in tab_mot) and (resp not in tab_vide):
			point += 5
			indices = [i for i, x in enumerate(tab_mot) if x == resp]
			for indices in indices:
				tab_vide[indices] = tab_mot[indices]
			if tab_vide == tab_mot:
				question.destroy()
				champ.destroy()
				mot_vide.config(text=str('Mot à deviner : \n\n' + ' '.join(tab_vide)))
				submit.config(text="Continuer", command=game)
				result.config(text=str("Trouvé! Bravo :-)\n" + str(point) + " point(s)\n"), fg="magenta")
			else:
				result.config(text="\nOUI! La lettre '" + resp + "' se trouve dans le mot! ++score = " + str(point) + " point(s)++ :\n", fg='green')
				mot_vide.config(text=str('Mot à deviner : \n' + ' '.join(tab_vide)))
	
		elif (resp in tab_mot) and (resp in tab_vide):
			point -= 1
			result.config(text="Lettre déjà complétée! **Pénalité -1 point** [score = " + str(point) + " point(s)] :\n", fg='orange')
		else:
			point -=5
			result.config(text="\nNON! pas de lettre '" + resp + "' dans ce mot! --score = " + str(point) + " point(s)--...\n", fg='red')
	
	submit.grid(row=3, padx=10, pady=10)
	submit.config(text='Envoyer', command=match, bg='white')
	result.grid(row=4, padx=10, pady=10)
	result.config(text='')

game()

window.mainloop()

