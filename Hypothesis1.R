# Hypothesis testing
# A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions

library(readr)
Cutlets <- read_csv("Cutlets.csv")
View(Cutlets)

attach(Cutlets)

# Normality test

shapiro.test(`Unit A`)

# p-value 0.32 > 0.05 so p high null fly 
# It follows Normal distribution

shapiro.test(`Unit B`)

# p-value 0.5225 > 0.05 so p high null fly 
# It follows Normal distribution

install.packages("car")
library(car)

qqPlot(`Unit A`)
qqPlot(`Unit B`)

# Variance test

var.test(`Unit A`, `Unit B`)

# p-value 0.3136 > 0.05 so p high null fly 
# Equal variances


## 2 sample t test ####


t.test(`Unit A`,`Unit B`, alternative = "two.sided", conf.level = 0.95, correct = TRUE)
# alternative = "two sided means we are checking for equal and unequal
# Null hypothesis -> equal means
# Alternative hypothesis -> unequal hypothesis

# p-value 0.4723 > 0.05 so p high null fly 
# Accept null hypothesis
# Hence Average of Unit A = Average of Unit B
# There is similarity between Unit A and Unit B

t.test(`Unit A`,`Unit B`, alternative = "greater", var.equal = T)

# Null hypothesis -> (Unit A - Unit B)<0
# Alternative hypothesis -> greater means true difference > 0
# p-value 0.2361 > 0.05 so p high null fly 
# Accept null hypothesis
# There is similarity between Unit A and Unit B


