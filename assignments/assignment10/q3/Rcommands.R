d = read.table('dif2.json',col.name=c("mementos"))
plot(d$mementos,xlab="Number of URI's",ylab="Difference between Old and New Mementos",xlim=c(0,1000),ylim=c(-2,50),type="l")