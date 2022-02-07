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
				self.check_input_node = 1
				self.input_node = input_node
				self.node_visited = np.full((len(node)), 0)
			else:
				self.check_input_node = 0
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
	
	
	def initialisation (self):

		if self.check_input_node == 1:
			i = self.node.index(self.input_node)
			self.current_matrix = np.full( (self.size_matrix, self.size_matrix+1),"nan" )
			
			for line in range(self.size_matrix):
				for row in range(self.size_matrix):
					if line == 0 and row == i:
						self.current_matrix[0][i] = 0
						self.node_visited[i] = 1
						self.current_matrix[0][self.size_matrix] = int(i)
					else:
						self.current_matrix[line][row] = float('inf')
			output = self.current_matrix
		else:
			output = "Warning : Le sommet initiale n'est pas sur la liste"
		
		return output
	

# Test 
matrix = np.array([
	[0., 5., 2., 6., 0., 0., 0.],
	[0., 0., 2., 0., 5., 0., 0.],
	[0., 0., 0., 3., 9., 6., 0.],
	[0., 0., 0., 0., 0., 1., 0.],
	[0., 0., 0., 0., 0., 0., 2.],
	[0., 0., 0., 0., 1., 0., 6.],
	[0., 0., 0., 0., 0., 0., 0.]
	])

node = ("A","B","C","D","E","F","G")
D = Dijkstra(matrix, node, 'A')
#D.desc()
print(D.initialisation() )
