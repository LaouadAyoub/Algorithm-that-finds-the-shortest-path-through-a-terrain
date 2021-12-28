# Université de Lille, Sciences et technologies
# Master 2 génie industriel, Industrie 4.0
# TP3 Applications Industrielles des Sciences des Données (AISD)
# Réalisé par : Laouad Ayoub
import matplotlib.colors as mcolors
import numpy as np
from matplotlib import pyplot as plt


# On cherche un chemin traversant verticalement Terrain
def trouver_chemin(terrain):
    # Creer des variables pour hauteur, largeur
    h, l = terrain.shape
    # Creer 2 matrices nulles de la meme taille que Field: Energie_cumulee et Indices
    E = np.zeros((h, l))
    INDICE = np.zeros((h, l), dtype=np.int32)
    # Remplir ces deux matrices de facon bottom-up en prog dyn.
    # La matrice E présente le cumul de la matrice terrain plus le minimum des energies des trois cases supérieur
    # La première ligne de la matrice d'energie est la même que la première ligne de la matrice terrain
    E[0, :] = terrain[0, :]
    for i in range(1, h):
        for j in range(0, l):
            # pour la première colonne on enlève j-1 car on prend on compte que deux cases supérieur
            if j == 0:
                m = min(E[i - 1, j], E[i - 1, j + 1])
                E[i, j] = terrain[i, j] + m
                INDICE[i, j] = np.argmin((E[i - 1, j], E[i - 1, j + 1]))
            elif j == (l - 1):
                # Le même cas pour la dernière case ou on a pas la case j+1
                m = min(E[i - 1, j - 1], E[i - 1, j])
                E[i, j] = terrain[i, j] + m
                INDICE[i, j] = np.argmin((E[i - 1, j - 1], E[i - 1, j])) + j - 1
            else:
                # pour le reste on prend la valeur de l'énergie correspond à la valeur du terrain dans cette case plus le minimum des trois énergies supérieur ce qui nous donne un cumul des énergies.
                m = min(E[i - 1, j - 1], E[i - 1, j], E[i - 1, j + 1])
                E[i, j] = terrain[i, j] + m
                # la matrice indice stocke l'indice du minimum des trois cases supérieur donc le chemin le plus facile à prendre
                INDICE[i, j] = np.argmin((E[i - 1, j - 1], E[i - 1, j], E[i - 1, j + 1])) + j - 1

    liste_indices = []
    # On commence par l'indice final qui est l'argument de la valeur minimal du cumul d'énergie car c'est la ou on a le chemin le plus pratique
    indice_final = np.argmin(E[-1, :])
    liste_indices.append(indice_final)
    # On parcours les ligne de la matrice ligne
    for c in range(h - 1, 0, -1):
        # Creer une liste qui, en partant de la derniere ligne, va indiquer les indices horizontaux successifs
        # l'indice du la case optimale est la matrice indice de la ligne superieur de la colonne du dernier indices stocké dans liste indices
        I = INDICE[c, liste_indices[-1]]
        liste_indices.append(I)

    print(f"le chemin : {liste_indices}")
    print(f"Terrain = \n{terrain}")
    print(f"Energie = \n{E}")
    print(f"Indice = \n{INDICE}")

    # On inverse la liste pour avoir les indices en partant du début: utiliser la fonction reverse().
    # vu qu'on commence par le dernièr indice, on doit inverser la liste
    liste_indices.reverse()
    return liste_indices


# Pour creer un terrain aleatoire avec des valeurs entre 0 et 9 pour une taille donnee.
def creer_terrain(h, l):  # h = hauteur, l = largeur
    return np.random.randint(low=0, high=9, size=(h, l))


# Pour afficher le resultat
def affichage(Terrain):
    # On affiche le terrain en noir et blanc
    # j'ai changé de couleur pour que ça fait zone vert = zone sécurisé et zone rouge = zone dangereuse
    plt.imshow(Terrain, cmap='RdYlGn_r')
    plt.colorbar()

    # A partir de la liste, on trace les indices successifs
    Liste_indices = trouver_chemin(Terrain)

    # Si la liste n'est pas vide, on la rajoute a l'affichage
    if Liste_indices != []:
        plt.plot(Liste_indices, range(Terrain.shape[0]), color='blue')
    plt.show()
    return


def main():
    T = creer_terrain(10, 20)
    affichage(T)


if __name__ == '__main__':
    main()
