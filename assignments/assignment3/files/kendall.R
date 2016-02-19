tfidf<- c(0.00741,0.008,0.01324,0.01393,0.01621,0.01828,0.01838,0.02105,0.02243,0.02915)
pagerank<-c(0.2,0.3,0.3,0.5,0.7,0.7,0.7,0.7,0.8,0.8)
cor.test(tfidf, pagerank, method = "kendall", alternative = "greater")