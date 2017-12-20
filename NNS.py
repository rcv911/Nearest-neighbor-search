from numpy import *
from matplotlib.pyplot import *

x=loadtxt('cluster_test.txt')
N=x.shape[0]
M=zeros((N,N))

# critical distance 
dc=7


for i in range(N):
	for j in range(i+1, N):
		M[j, i] = M[i, j] = (sum((x[i, :]-x[j, :])**2))**0.5

print('matrix of distances is ready')

l1=[]
l2=[]
l3=[]
res=[]
Q=range(N)

# we need change 0 in diagonal matrix then we can found min value of matrix
maxi=M.max()
for i in range(N):
	M[i,i]=maxi

# NNS algorithm
fv=True

while fv:
	minim = M[Q[0], Q[1]]
	iz = Q[0]
	jz = Q[1]
	for i in Q:
		for j in Q:
			if M[i, j] < minim:
				iz = i
				jz = j
				minim = M[i, j]

	l1 = []
	l2 = [iz, jz]
	l3 = []

	f = True
	while f:
		for el in l2:
			for i in Q:
				if M[el, i] < dc:
					if (i not in l1) and (i not in l2) and (i not in l3):
						l3.append(i)
		if not l3:
			f = False
		l1.extend(l2)
		l2 = l3
		l3 = []
	res.append(l1)
	Q = [el for el in Q if el not in l1]
	if not Q:
		fv = False
	x2 = x.take(l1,0)
	plot(x2[:,0], x2[:,1], '.')

grid()
show()

# savefig('NNS_cluster.png')
