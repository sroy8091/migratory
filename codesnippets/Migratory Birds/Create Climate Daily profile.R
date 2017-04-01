#Clearing the workspace
rm(list = ls())

library(dplyr)
db_500 = read.csv(file = '~/R/Migratory Birds/Final Datasets/500_max_min_avg.csv', header = FALSE)
colnames(db_500) = c('day.no','grid.no', 'daily.max','daily.min','daily.average')

#Similarly for other pressure levels
#Renaming the column names
db_850 = read.csv(file = '~/R/Migratory Birds/Final Datasets/850_min_max_avg.csv', header = FALSE)
colnames(db_850) = c('day.no','grid.no', 'daily.max','daily.min','daily.average')

db_950 = read.csv(file = '~/R/Migratory Birds/Final Datasets/950_min_max_avg.csv', header = FALSE)
colnames(db_950) = c('day.no','grid.no', 'daily.max','daily.min','daily.average')

#Loading the utility files regarding the calendar daily data
calendar_data = read.csv(file = '~/R/Migratory Birds/Final Datasets/Calendar_1951_to_2014.csv', header = TRUE, row.names = 1)

#in order to join , we mutate the day.no attribute of db_500 to 4-times its value. The folow with the merge
db_500 = db_500 %>% mutate(index = day.no * 4)
db_850 = db_850 %>% mutate(index = day.no * 4)
db_950 = db_950 %>% mutate(index = day.no * 4)

#Adding the attributes of the Calendar utility files to th  clmate profile data
db_500 = merge(db_500, calendar_data, all.x = TRUE)
db_500 = db_500 %>% select(-month_name, -quarter,-index)

db_850 = merge(db_850, calendar_data, all.x = TRUE)
db_850 = db_850 %>% select(-month_name, -quarter,-index)

db_950 = merge(db_950, calendar_data, all.x = TRUE)
db_950 = db_950 %>% select(-month_name, -quarter,-index)

write.csv(db_500, file = '~/R/Migratory Birds/Final Datasets/500_max_min_avg.csv')
write.csv(db_850, file = '~/R/Migratory Birds/Final Datasets/850_min_max_avg.csv')
write.csv(db_950, file = '~/R/Migratory Birds/Final Datasets/950_min_max_avg.csv')

#Climate profiling code is done only on the surface air temporature, based on utility files

#The above code across the dbs is better represented when we write a function related type
