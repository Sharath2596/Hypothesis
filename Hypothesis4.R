# TeleCall uses 4 centers around the globe to process customer order forms. They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  The manager wants to check whether the defective %  varies by centre. Please analyze the data at 5% significance level and help the manager draw appropriate inferences

library(readr)
COM <- read_csv("Costomer+OrderForm.csv")
View(COM)

attach(COM)

table(Phillippines, Indonesia, Malta, India)

# Chi square test ###
# Null hypothesis <- All are same
# Alternative Hypothesis <- at least one are different

test <- chisq.test(table(Phillippines, Indonesia, Malta, India))
test
test <- chisq.test(table(Phillippines, Malta))
test

# P value is 1 so p high null fly 
# We accept null hypothesis