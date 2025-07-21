library(dismo)
library(reshape2)

climate_prec <- read.csv("climate_prec_ecotypes.csv")
climate_max_temp <- read.csv("climate_max_temp_ecotypes.csv")
climate_min_temp <- read.csv("climate_min_temp_ecotypes.csv")

climate_prec <- as.matrix(climate_prec[, -1])  # Exclude the site column
climate_max_temp <- as.matrix(climate_max_temp[, -1])
climate_min_temp <- as.matrix(climate_min_temp[, -1])

bio_clim_vars <- biovars(prec=climate_prec, tmin=climate_min_temp, tmax=climate_max_temp)

write.csv(bio_clim_vars, "bio_clim_vars_ecotypes.csv", row.names=FALSE)
