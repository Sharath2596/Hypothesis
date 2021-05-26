# Fantaloons Sales managers commented that % of males versus females walking in to the store differ based on day of the week. Analyze the data and determine whether there is evidence at 5 % significance level to support this hypothesis

library(readr)
Faltoons <- read_csv("Faltoons.csv")
View(Faltoons)

attach(Faltoons)

table(Weekdays, Weekend)

# 2 proportion test ###

ptest <-prop.table(table(Weekend))
ptest
ptest2 <- prop.table(table(Weekdays))
ptest2
chisq.test(table(Weekdays, Weekend))
prop.test(table(Weekdays, Weekend))

# P value is 1 so p high null fly 
# We accept null hypothesis
# Hence proportion of males vs females in weekdays = proportion of males vs females in weekdends
