import networkx as nx
from networkx.algorithms import centrality
from operator import itemgetter
import csv

actors = ["1", "3", "83","86","85","6","11","88","106","89","84","5","8","76","77","87","82","96","12","17","80","33","16"]
def read_csv(filename): 
	csv_file = open(filename, 'rb')
	reader = csv.reader(csv_file)
	for row in reader:
		keys = row
		break
	csv_file.close()
	return keys[1:]

def get_matrix(filename): 
	matrix = {}
	csv_file = open(filename, 'rb')
	reader = csv.reader(csv_file)
	n = -1 
	for row in reader: 
		if n==-1:
			for j in row[1:]:
				matrix[j] = {}
			nodes = row[1:]
			n+=1
		break
	for row in reader:
			for i in range(len(nodes)):
				edges = row[1:]
				matrix[nodes[n]][nodes[i]] = edges[i]
			n+=1
	csv_file.close()
	return matrix


def create_graph(filename):
	nodes = read_csv(filename)
	matrix = get_matrix(filename)
	G=nx.DiGraph()
	for i in nodes:
		for j in matrix[i]:
			if int(matrix[i][j]) > 0:
				G.add_edge(i,j,weight=int(matrix[i][j]))
	return G

def analyze(filename):
	nodes = read_csv(filename)
	G = create_graph(filename)
	degree = G.degree()
	betweenness = centrality.betweenness_centrality(G)
	eigen = centrality.eigenvector_centrality_numpy(G,weight='weight')

	actors_degree= []
	actors_betweenness = []
	actors_eigen = [] 

	# in_deg = G.in_degree()
	# out_deg = G.out_degree()

	# a = 0
	# for i in in_deg.keys():
	# 	a+=in_deg[i]

	# print "IN DEGREE "
	# print a/len(in_deg)

	# b = 0
	# for i in out_deg.keys():
	# 	a+=out_deg[i]

	# print "OUT DEGREE "
	# print b/len(out_deg)

	for i in actors:
		if i in degree.keys():
			actors_degree.append((i,degree[i]))
		if i in betweenness.keys():
			actors_betweenness.append((i,betweenness[i]))
		if i in eigen.keys():
			actors_eigen.append((i,eigen[i]))

	actors_degree = sorted(degree.items(), key=itemgetter(1))
	actors_betweenness = sorted(betweenness.items(), key=itemgetter(1))
	actors_eigen = sorted(eigen.items(), key=itemgetter(1))

	actors_degree.reverse()
	actors_betweenness.reverse()
	actors_eigen.reverse()

	print "DEGREE: "
	print actors_degree
	print 
	print "BETWEENNESS" 
	print actors_betweenness
	print 
	print "EIGEN"
	print actors_eigen
	print




def main():
	for i in range (1,12):
		filename = "phase"+str(i)+".csv"
		print 
		print "**************"
		print "Phase ", +i
		print "**************"
		print 
		analyze(filename)

if __name__ == '__main__':
	main()
