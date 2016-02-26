
R version 3.1.2 (2014-10-31) -- "Pumpkin Helmet"
Copyright (C) 2014 The R Foundation for Statistical Computing
Platform: x86_64-w64-mingw32/x64 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

[Previously saved workspace restored]


> data <- read.csv("friendCount.txt", stringsAsFactors = F, header = FALSE, sep = " ")
> mydata = data[,1]
> meanData <- paste("Mean: ", mean(mydata), collapse = "")
> medianData <- paste("Median: ", median(mydata), collapse = "")
> sdData <- paste("Std Dev: ", sd(mydata), collapse = "")
> write(meanData, stdout())
Mean:  358.987012987013
> medianData <- paste("Median: ", median(mydata), collapse = "")
> write(medianData, stdout())
Median:  266.5
> write(sdData, stdout())
Std Dev:  371.585298171447
> barplot(mydata,main="friends data")
> 
