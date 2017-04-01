#Clearing the workspace
rm(list = ls())

ebird_data = read.csv(file = '~/R/Migratory Birds/Ebird-db-30th-March-csv.csv')

#Seeing the summary of the data 

summary(ebird_data)
str(ebird_data)

#Checking sanity of value entered in the fields
print('Unique months')
print(unique(ebird_data$Obs.month))

#Adding the bird count and species recognition id by sampling
bird_cnt_range = 1:200
species_cnt_range = 1:340
set.seed(42)
bird_count  = sample(bird_cnt_range, size = nrow(ebird_data), replace = TRUE)
species_id = sample(species_cnt_range, size = nrow(ebird_data), replace = TRUE)

#Adding the column values to the table : bird_count, species_id
ebird_data_mod = cbind(ebird_data, bird_count, species_id)
ebird_data_mod$species_id = as.factor(ebird_data_mod$species_id)

write.csv(ebird_data_mod, file = "Total Ebird db 1.csv")


library(dplyr)

#Toying with the landslide data over all India from 2001 to 2012
slide_data = read.csv(file = '~/R/Migratory Birds/landslide.csv', header = TRUE, row.names = 1)

#To compare the rate of change of data, we normalize the values
#Performing Min-max normalisation
slide_data_norm = slide_data %>% mutate(lives_list_norm = (Lives.Lost..in.Nos.. - min(Lives.Lost..in.Nos..))/(max(Lives.Lost..in.Nos..)- min(Lives.Lost..in.Nos..)), house_dameged_norm = (House.damaged..in.Nos.. - min(House.damaged..in.Nos..))/(max(House.damaged..in.Nos..)- min(House.damaged..in.Nos..)), cattle_lost_norm = (Cattle.Lost..in.Nos.. - min(Cattle.Lost..in.Nos..))/(max(Cattle.Lost..in.Nos..)- min(Cattle.Lost..in.Nos..)), crops_affected_norm = (Cropped.areas.affected..in.lakh.ha. - min(Cropped.areas.affected..in.lakh.ha.))/(max(Cropped.areas.affected..in.lakh.ha.)- min(Cropped.areas.affected..in.lakh.ha.)))


#Lives lost in numbers, cattle lost in numbers, house damaged in numbers and Cropped areas affected in lakh hectares
#Making scree plots

#Code template made
title_graph = 'Trend of landslide impact from 2001 to 2011 over India'
plot(slide_data_norm$lives_list_norm, xlab = 'Year', ylab = 'No. of people dead in landslides', type = 'b', col = 'red')
axis(side = 1, at= 1:11,labels = rownames(slide_data))
title(title_graph)

lines(slide_data_norm$house_dameged_norm, type="b",lty=2, col="blue")
lines(slide_data_norm$cattle_lost_norm, type="b",col="green",lty=2)
lines(slide_data_norm$crops_affected_norm, type="b",col="black",lty=2)

legend( x="topleft", 
        legend=c("Lives Lost","House damaged","Cattle lost","Crops affected"),
        col=c("red","blue","green","black"), lwd=c(2,2,10,2), lty=c(1,1,1,1), cex=0.6)



