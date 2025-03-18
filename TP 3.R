rownames(Eurojobs) <- Eurojobs$Country
Eurojobs$Country <- NULL
#KMEANS!!!!!!: On connait le nbre de groupe qu'on veut créer
#Attention: on doit savoir le faire a la main!!
Eurojobs_scaled = scale(Eurojobs)
model <- kmeans(Eurojobs_scaled, centers = 2, nstart = 10)
model
#Qualité de la partition
#compare la variabilité des données à l’intérieur de chaque groupe (within) 
#avec la variabilité entre les différents groupes (between)
#Objectif:Une faible variabilité à l’intérieur de chaque groupe
#         Une grande variabilité entre les groupes
model$withinss
model$betweenss
model$totss #variabilité totale
#pourcentage de variabilité expliqué par la partition (between/total)
model$betweenss/model$totss

#Interpretation de la partition: ajouter la valeur de clusters comme variable
Eurojobs$cluster <- as.factor(model$cluster)
#Representation par un tableau
aggregate(data = Eurojobs, .~ cluster, FUN = mean)
#visualisation graphique
library(ggplot2)
ggplot(data = Eurojobs) + 
  aes(x = Agr, y = Min, colour = cluster, label = rownames(Eurojobs)) +
  geom_point() +
  geom_text(check_overlap=T, nudge_y = 0.1) # affiche les noms

ggplot(data = Eurojobs) + 
  aes(y = Fin, x = cluster, fill = cluster) +
  geom_boxplot() +
  theme(legend.position = "none")

library(FactoMineR)
library(factoextra)
resultat_acp <- PCA(Eurojobs, graph = FALSE, quali.sup = 10)
fviz_pca_ind(resultat_acp, habillage = 10)
#fviz_pca_ind et habillage permet de coloré en fonction du cluster
#contrairement a plot. pca (Eurojobs, choix = "ind")
########################################################################

#CLASSIFICATION HIERARCHIQUE!!!: On ne connait pas le nbre de groupe a l'avance
matrice_distances <- dist(Eurojobs_scaled)
model_complete <- hclust(d = matrice_distances, method = "complete")
barplot(height = model_complete$height)
#Il y a un saut entre la 1ere barre et les suivantes : découpe en 2 groupes
#Il y a un saut entre la 5ème barre et les suivantes : découpe en 6 groupes

plot(model_complete)
rect.hclust(model_complete, k=2, border="red")
rect.hclust(model_complete, k=6, border="blue")

#Algorithme de Ward
model_ward <- hclust(d = (matrice_distances^2)/2, method = "ward.D")
barplot(model_ward$height)
#Après la première barre : 2 classes
#Après la 2ème barre : 3 classes
#Après la 3ème barre : 4 classes
plot(model_ward, hang=-1)
rect.hclust(model_complete, k=3, border="green")
rect.hclust(model_complete, k=4, border="violet")
#Interpretation sur tableau/PCA
Eurojobs$cluster_bis <- cutree(model_ward, k = 3)
aggregate(data = Eurojobs[, - 10], . ~ cluster_bis, FUN = mean)

resultat_acp <- PCA(Eurojobs, graph = FALSE, quali.sup = c(10, 11))
fviz_pca_ind(resultat_acp, habillage = 11)

#ANALYSE DISCRIMINANT LINEAIRE!!!
#construire, sur base des variables quantitatives, des axes qui 
#discriminent au mieux les groupes indiqués par une variable qualitative.

# suppression des variables de la partie classification
Eurojobs$cluster <- NULL
Eurojobs$cluster_bis <- NULL

# creation de la nouvelle variable
Eurojobs$UE <- c(TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)

library(MASS)
resultat_lda <- lda(UE ~ ., data = Eurojobs)
resultat_lda

#description des groupes et interpretation
z <- predict(resultat_lda)$x
round(t(cor(Eurojobs[, -10],z)),2)

#Prediction
# creation de la nouvelle observation
nouveau_pays <- matrix(rep(100/9, times = 9),nrow = 1)
colnames(nouveau_pays) <- colnames(Eurojobs)[1:9]
nouveau_pays <- as.data.frame(nouveau_pays)

# prediction
# creation de la nouvelle observation
nouveau_pays <- matrix(rep(100/9, times = 9),nrow = 1)
colnames(nouveau_pays) <- colnames(Eurojobs)[1:9]
nouveau_pays <- as.data.frame(nouveau_pays)

# prediction
# creation de la nouvelle observation
nouveau_pays <- matrix(rep(100/9, times = 9),nrow = 1)
colnames(nouveau_pays) <- colnames(Eurojobs)[1:9]
nouveau_pays <- as.data.frame(nouveau_pays)

# prediction
nouveau_pays <- matrix(rep(100/9, times = 9),nrow = 1)
colnames(nouveau_pays) <- colnames(Eurojobs)[1:9]
nouveau_pays <- as.data.frame(nouveau_pays)#creation de la nouvelle observation
predict(resultat_lda, newdata = nouveau_pays)

#Qualité de l'analyse
z <- predict(resultat_lda)$x
ldahist(data = z[,1], g = Eurojobs$UE)

#table de validation
# Table de validation 
eurojobs_pred <- predict(resultat_lda, newdata = Eurojobs[,1:9])$class
validation <- table(Eurojobs[,10],eurojobs_pred)
validation
# % des pays bien classés
sum(diag(validation))/nrow(Eurojobs)

