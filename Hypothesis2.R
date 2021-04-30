# A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch.

# Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.

library(readr)
LabTAT <- read_csv("LabTAT.csv")
View(LabTAT)

attach(LabTAT)

# Normality test

shapiro.test(`Laboratory 1`)
# p-value 0.5508 > 0.05 so p high null fly 
# It follows Normal distribution

shapiro.test(`Laboratory 2`)
# p-value 0.8637 > 0.05 so p high null fly 
# It follows Normal distribution

shapiro.test(`Laboratory 3`)
# p-value 0.4205 > 0.05 so p high null fly 
# It follows Normal distribution

shapiro.test(`Laboratory 4`)
# p-value 0.6619 > 0.05 so p high null fly 
# It follows Normal distribution

install.packages("car")
library(car)
qqPlot(`Laboratory 1`)
qqPlot(`Laboratory 2`)
qqPlot(`Laboratory 3`)
qqPlot(`Laboratory 4`)

# Variance test

var.test(`Laboratory 1`, `Laboratory 2`)
var.test(`Laboratory 2`, `Laboratory 3`)
var.test(`Laboratory 3`, `Laboratory 4`)
var.test(`Laboratory 4`, `Laboratory 1`)

# p-value for all 4 laboratories > 0.05 so p high null fly 
# Equal variances

# ANOVA Test
# Null hypothesis <- Average of all laboratories are same
# ALternative hypothesis <- Atleast 1 laboratories are different

stacked_data <- stack(LabTAT)
View(stacked_data)
attach(stacked_data)
Anova_result <- aov(values~ind, data = stacked_data)
summary(Anova_result)

# p value is less than 0.05
# accept alternative hypothesis
# Hence average of atleast 1 laboratories are different