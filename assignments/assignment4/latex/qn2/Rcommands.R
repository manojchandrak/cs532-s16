data <- read.csv("orderedfollowers.txt", stringsAsFactors = F, header = FALSE, sep = ",")
mydata = data[,1]
meanData <- paste("Mean: ", mean(mydata), collapse = "")
medianOut <- paste("Median: ", median(mydata), collapse = "")
sdData <- paste("Std Dev: ", sd(mydata), collapse = "")
write(meanData, stdout())
write(medianOut, stdout())
write(sdData, stdout())

barplot(mydata, main="Followers  of Followers on Twitter", xlab="Followers sorted in increasing order of their followers", ylab="Number of Followers ",ylim=c(0,100))
 arrows(x0=match(c(34), mydata)+3, y0=80, x1=match(c(34), mydata)+3, y1=34, length=0.1, lwd=2.5, col='red')
 text(x=match(c(34), mydata)+3, y=90, labels="Manoj_chandra11", col='red')