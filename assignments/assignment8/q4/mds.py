#!/usr/local/bin/python

import clusters

blognames,words,data=clusters.readfile('blogmatrix.txt')

coords = clusters.scaledown(data)

clusters.draw2d(coords, blognames, jpeg='draw2d.jpg')
