d = read.table('numberdays.txt',col.name=c("number_of_days"))
b = read.table('abovezerocounts.json',col.name=c("memento_counts"))
 plot(b$memento_counts,d$number_of_days,xlab="memento counts",ylab="days")