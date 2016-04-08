import clusters
import sys

blognames,words,data=clusters.readfile('blogmatrixnew.txt')
clust = clusters.hcluster(data)


clusters.printclust(clust, labels=blognames)
# sys.stdout = open('ascii.txt', 'w')


clusters.drawdendrogram(clust, blognames, jpeg='dendogram.jpg')