iba_data2 = read.csv(file = '~/R/Migratory Birds/IBA_details7.csv')
library(dplyr)

#Removing X. field, Extra
iba_data2 = iba_data2 %>% select(-X., -Extra)

iba_col = colnames(iba_data2)
type_index = seq(1,length(iba_col))
habitat_type = cbind(type_index, iba_col)
habitat_fr = as.data.frame(habitat_type)

write.csv(habitat_fr, file = 'habitat type.csv')
