import networkx as nx
from networkx.algorithms import centrality
from operator import itemgetter
import csv

def read_csv(filename): 
	csv_file = open(filename, 'rb')
	reader = csv.reader(csv_file)
	for row in reader:
		keys = row
		break
	cases = set()
	crimes = {}


	for row in reader:
		crimes[row[5]] = []
	csv_file.close()

	csv_file = open(filename, 'rb')
	reader = csv.reader(csv_file)
	for row in reader: 
		keys = row
		break 

	for row in reader: 
		crimes[row[5]].append(row[0])

	return crimes

def create_graph(crimes):
	G = nx.Graph()
	for crime in crimes.keys():
		offenders = crimes[crime]
		for i in offenders: 
			for j in offenders:
				if i!=j: 
					if G.has_edge(i, j):
						G[i][j]['weight'] += 1
					else:
          	G.add_edge(i, j, weight=1)
  return G

def main():
	crimes = read_csv("Cooffending.csv")
	graph = create_graph(crimes)
	print len(graph.nodes())

if __name__ == '__main__':
	main()