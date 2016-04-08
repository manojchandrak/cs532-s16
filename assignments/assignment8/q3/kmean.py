#!/usr/local/bin/python

import clusters

blognames,words,data=clusters.readfile('blogmatrix.txt')
print 'Iterations for varying k value '
print "For k=5"
kclust=clusters.kcluster(data, k=5)
print 'Centroid  values for first part are:'
for i in range(0,5):
	for item in kclust[i]:
		print blognames[item]
print

print "For k=10"
kclust=clusters.kcluster(data, k=10)
print 'Centroid  values for second part are:'
for i in range(0,10):
	for item in kclust[i]:
		print blognames[item]
print

print "For k=20"
kclust=clusters.kcluster(data, k=20)
print 'Centroid  values for third part are:'
for i in range(0,20):
	for item in kclust[i]:
		print blognames[item]
print
