from egzP9btesty import runtests

def DFS(G, R, A, RES):

	def DFSVisit(v, G, R):

		visited[v] = True

		RES.append(v)

		for i in range(len(G[v])):
			if visited[G[v][i]] == False and A[v][G[v][i]] == True:
				DFSVisit(G[v][i], G, R)

		

			
	visited = [False] * len(G)

	for i in range(len(visited)):
		if visited[i] == False:
			DFSVisit(i, G, R)


def dyrektor( G, R ):

	
	A = [ [ True for j in range(len(G))] for i in range(len(G)) ]

	for i in range(len(R)):
		for j in range(len(R[i])):
			A[i][R[i][j]] = False

	RES = []

	DFS(G, R, A, RES)

	return RES[::-1]

G = [
[1, 0, 2],
[2, 0],
[1, 0]
]
R = [
[0],
[],
[]
]

print(dyrektor(G, R))

#runtests(dyrektor, all_tests=True)
