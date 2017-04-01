species_data_envis = read.csv(file = '~/R/Migratory Birds/tabulated_species.csv', header = TRUE)
species_data_datazone = read.csv(file = '~/R/Migratory Birds/species_20170316_2521.csv', header = TRUE)

#Joining the data based on Scientific name
merged_species_data = merge(species_data_datazone, species_data_envis, all.y = TRUE)
write.csv(merged_species_data, file = 'Merged dataset Envis 31st March.csv')
