# Path_finder

This is an academic project tht i realized during the 2nd year of my master's degree, within the practical work of industrial applications to data science.

this algorithm is programmed in python using the libraries : Matplotlib and Numpy 

It looks for the shortest path crossing vertically terrain, the more the area is in red the more time is needed to cross it.

# Working principle :

- we create a matrix Terrain
- we create 2 null matrices of the same size as Terrain (E and Indices) : 
- we fill these two matrices in a bottom-up way
E (cumulative energy) : Presents the cumulative energy of the terrain matrix plus the minimum of the energies of the three upper cells.
Indices : Indices matrix stores the index of the minimum of the three upper cells so the easiest path to take

After having filled these two matrices :

- We start with the final index which is the argument of the minimal value of the energy accumulation because it is where we have the most convenient path.
  - We create a list that, starting from the last row, will indicate the successive horizontal indices (The index of the optimal cell is the index matrix of the upper row, and of the column of the last index stored in the index list)
  - we reverse the list to get the indices from the beginning: use the reverse() function (Since we start with the last index, we must reverse the list ;) )

- Finally, We display the terraub with the function Plt.imshow(), I chose the red and green color so that it makes green zone = fast area, red zone = slow area
- We display the path stored in the list "Liste_indices" in blue 

![Path_finder_results](https://user-images.githubusercontent.com/96794946/147682172-1fb7adec-b935-47f8-86fe-27a87fffa9eb.png)
