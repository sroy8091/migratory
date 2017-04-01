ebird_data = read.csv(file = '~/R/Migratory Birds/Total Ebird db 1.csv')
summary(ebird_data)

library(dplyr)

#Found Effort.distance < 0
dist_s = ebird_data %>% filter(Effort.distance < 0)

#Cleaning the above observations
ebird_data = subset(ebird_data, Effort.distance >= 0)

#Filling the missing values
ebird_data$Number.of.observers[is.na(ebird_data$Number.of.observers) == TRUE] = 0

#Removing Effort.Area since 98% of data is NA
ebird_data = ebird_data %>% select(-Effort.area,-X)

ebird_data$Duration[is.na(ebird_data$Duration) == TRUE] = median(ebird_data)

#After the data cleaning stage
ebird_data_new  = read.csv(file = '~/R/Migratory Birds/Final Datasets/Total Ebird db 1.csv', row.names = 1, header = TRUE)

#One parameter for the user, total number of such observations submitted by the user
