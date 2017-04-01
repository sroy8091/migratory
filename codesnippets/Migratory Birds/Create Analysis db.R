library(dplyr)
total_db  = read.csv(file = '~/R/Migratory Birds/Final Datasets/Total Ebird db 1.csv', row.names = 1, header = TRUE)

#Removing the observations where All.species.reported = 0, i.e, the observer is not sure about the reliability and completeness of the data
consider_data = subset(total_db, All.species.reported == 1)


#For analysis, we are removing the bird count and considering each record to observe only a single bird
consider_data = consider_data %>% select(-bird_count, -species_id)

#Removing fields with effort distance < 0
#Filling the missing values of the Effort.distance field with the median of that particular attribute
consider_data$Effort.distance[is.na(consider_data$Effort.distance) == TRUE] = median(consider_data$Effort.distance, na.rm = TRUE)
consider_data$Duration[is.na(consider_data$Duration) == TRUE] = median(consider_data$Duration, na.rm = TRUE)
consider_data = subset(consider_data, !(Effort.distance < 0))

#Removing Effort.Area since a large percent of it is NA
consider_data = consider_data %>% select(-Project.code, -Sampling.Event.Identifier,-Group.identifier)
consider_data = consider_data %>% select(-Trip.comments.1)

#Since All.species.seen is 1, then remove
consider_data = consider_data %>% select(-All.species.reported)

#Replacing the missing values with the median of the particular attribute
consider_data$Number.of.observers[is.na(consider_data$Number.of.observers)] = median(consider_data$Number.of.observers, na.rm = TRUE)

write.csv(consider_data, file = 'Analysis db 31st March.csv')

#Clustering to be done using k-means clustering where k=370, and each cluster belongs to a particular species recognised by the Species id

analysis_db = read.csv(file = '~/R/Migratory Birds/Analysis db 31st March.csv', header = TRUE, row.names = 1)

cluster_data = analysis_db %>% select(State.Code, City.code, Locality.id, Locality.type, Latitude, Longitude,Obs.month, Obs.year, Observer.id, Protocol.type,Duration,Effort.distance,Number.of.observers)
#Performing k-means clustering where k= 370, nstart = 20
analysis_clus = kmeans(cluster_data, centers = 150)
summary(cluster_data)

#In order to carry on clustering, we convert continuous variables to categorical variables
cluster_data$Obs.year = as.factor(cluster_data$Obs.year)

#Breaking all the months in seasons of size = 3
cluster_data$Obs.month = cut(cluster_data$Obs.month, seq(0,12,3))
cluster_data = cluster_data %>% select(-Latitude, -Longitude)

#Detecting outliers and removing them 
cluster_data = cluster_data %>% filter(Effort.distance < 1000)
cluster_data = cluster_data %>% filter(Number.of.observers<400)

#Dividing the remaining continuous variables into 50 levels each
cluster_data$Duration = cut(cluster_data$Duration, c(0,10,20,30,50,100,250,500, 750,1000, 1500))
cluster_data$Effort.distance = cut(cluster_data$Effort.distance, c(0,10,20,30,40,50,100,150,200,300,500,700,1000))
cluster_data$Number.of.observers = cut(cluster_data$Number.of.observers, c(0,10,20,30,40,50,100,150,200,400))

#Removing observations which have NA values
cluster_data = subset(cluster_data, is.na(Effort.distance) == FALSE)
cluster_data = subset(cluster_data, is.na(Number.of.observers) == FALSE)

analysis_clus = kmeans(cluster_data, centers = 25)
