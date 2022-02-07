import numpy as np

class Dijkstra():

	def __init__ (self, matrix, node, input_node):

		if (len(matrix) == len(node)):
			self.check = 1
			self.matrix = matrix
			self.size_matrix = len(matrix)
			self.node = node
			self.size_edge = 0			
			if input_node in node:
				self.input_node = input_node
				self.node_visited = np.full((len(node), len(node)), 0)
			else:
				print ("WARNING : Le sommet d'entree n'est pas sur la liste des sommets !!!!\n")
		else:
			self.check = 0
			self.check_text = "WARNING : Merci de verifier les inputs !!!!"
			print("\nWARNING : Taille matrice d'adjacence != Taille des sommets\n")

	def desc (self):
		if self.check == 1:
			
			for line in range(self.size_matrix):
				print( "Les voisins de {} : ".format(self.node[line]) , end=' ')
				for row in range(self.size_matrix):
					if self.matrix[line][row] != 0:
						print ("({},{}): w={} ".format(self.node[line], self.node[row], self.matrix[line][row] ), end=' ' )
						self.size_edge += 1
				print('') 
			print('\nNombre de Sommets = {}'.format(self.size_matrix) )
			print("Nombre d'aretes = {}".format(self.size_edge) )
			
		else:
			print(self.check_text)




