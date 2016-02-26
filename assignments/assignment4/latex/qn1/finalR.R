data <- read.csv("friendCount.txt", stringsAsFactors = F, header = FALSE, sep = " ")

myData = data[,1]

meanData <- paste("Mean: ", mean(myData), collapse = "")

medianData <- paste("Median: ", median(myData), collapse = "")

sdData <- paste("Std Dev: ", sd(myData), collapse = "")

write(meanData, stdout())
write(medianData, stdout())
write(sdData, stdout())

pos <- (myData == 155)

cols <- c("white", "red") 


barplot(myData, main="Friends of Friends on FaceBook", xlab="Friends sorted in increasing number of friends", ylab="Number of Friends", col=cols[pos + 1], ylim=c(0, 4000))
text(x=match(c(155), myData)+12, y=(max(myData)-20), labels="Nelson", col='red')
arrows(x0=match(c(155), myData)+12, y0=(max(myData) - 80), x1=match(c(155), myData)+12, y1=325, length=0.1, lwd=2.5, col='red')