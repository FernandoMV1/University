head(Eurojobs)
rownames(Eurojobs)=Eurojobs$Country
Eurojobs$Country<-NULL

summary(Eurojobs, digits = 2)
Eurojobs |> cor() |> round(2)
library(corrplot)
Eurojobs |> cor() |> corrplot()

# install.packages(FactoMineR)
# install.packages(factoextra)
library(FactoMineR) # pour l'analyse
library(factoextra) # pour plus de graphique

resultat_acp = PCA(Eurojobs)

round(resultat_acp$eig,2) #eigen value (critere de majorité)
fviz_eig(resultat_acp)
round(resultat_acp$var$cos2,2)
sum_cos2_variable <- rowSums(resultat_acp$var$cos2[,c(1,2)]) # somme du cos2 pour les composantes 1 et 2.
round(sort(sum_cos2_variable), 2)

plot.PCA(resultat_acp, choix = "var", axes=c(1,2)) #cercle de corrélation

round(resultat_acp$var$contrib[,1:2],2) #% de représentation des variables dans chaque dimension

#Analyse des individus
sort(round(rowSums(resultat_acp$ind$cos2[, 1:2]), 2))

#carte des individues
plot.PCA(resultat_acp, choix = "ind", axes=c(1,2))

#variable supplémentaire
Eurojobs$UE <- c(TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)
resultat_acp2 <- PCA(Eurojobs, scale.unit = TRUE,
                     quali.sup = 10, graph = FALSE)

################################# Exercices ACP ###########################################
pca_rang <- PCA(rangs[,7:12])
round(pca_rang$eig,2)
#1. Je choisit la dimension 1 et 2
#2. 91.63%
round(pca_rang$var$cos2[,1],2)
#3 Score.on.SCI
#4. 100 - 83.78 = 16,22
sum(pca_rang$var$cos2[2,c(1,2)])
#5. 0.8961436
plot.PCA(pca_rang,choix = "var", axes = c(1,2))
#6.Alumni

row.names(ACPcars) = ACPcars$Type
ACPcars$Type = NULL
pca_cars <- PCA(ACPcars)
plot.PCA(pca_cars,choix = "var",axes = c(1,2))
plot.PCA(pca_cars,choix = "ind",axes = c(1,2))
