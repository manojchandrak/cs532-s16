import clusters
import sys

blognames,words,data=clusters.readfile('blogmatrix.txt')
clust = clusters.hcluster(data)

# print ASCII dendrogram
clusters.printclust(clust, labels=blognames)
sys.stdout = open('ascii.txt', 'w')

# save JPEG dendrogram
clusters.drawdendrogram(clust, blognames, jpeg='dendogram.jpg')