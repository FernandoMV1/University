#Charger les packages

library(ggplot2) # Pour la visualisation
library(FactoMineR) # Pour l'ACP
library(factoextra) # Pour la visualisation de l'ACP
library(cluster) # Pour le clustering
library(dplyr) # Pour la manipulation des données
library(MASS) #Pour LDA
library(pander) #Visualisation 

#Importer les données
mcdo <- read.csv("~/Bac 2 - Projet ASM/mcdo.csv")

### Question 0 ###

summary(mcdo)

#Utiliser les noms des produits comme nom pour chaque observation :
rownames(mcdo) <- mcdo$Item
mcdo$Item <- NULL
#a. Valeur max Total.Fat
max_fat <- max(mcdo$Total.Fat, na.rm = TRUE)
max_fat
#Produit associé a max Total.Fat
product_max_fat <- rownames(mcdo)[which(mcdo$Total.Fat == max_fat)]
product_max_fat

#Moyenne Total.Fat
mean_fat <- mean(mcdo$Total.Fat, na.rm = TRUE)
mean_fat
#La valeur max est beaucoup plus grande que la moyenne

#b. Relation Quantity et Carbohydrates
cor_qte_car <- cor(mcdo$Quantity,mcdo$Carbohydrates)
cor_qte_car

cor_graph <- ggplot(data = mcdo) +
  aes(x = Quantity, y = Carbohydrates) +
  geom_point() +
  labs(title = "Relation entre Quantity et Carbohydrates",
       x = "Quantity",
       y = "Carbohydrates")
cor_graph

cor_test <- cor.test(mcdo$Quantity, mcdo$Carbohydrates)
pander(cor_test)

#Nous voyons que la quantité a une corrélation positive avec les glucides
#Ce qui veut dire que plus on a de quantité plus il y a de glucides dans les produits
#Nous voyons aussi que cette corrélation est statistiquement significative (p-valeur ***)
#Cependant la corrélation est faible. En effet on voy sur le graphique qu'il y a une concentration des observation a gauche
#Nous voyons aussi plusieurs outliers qui affectent l'analyse
#Avec IA, nous ferons l'analyse sans outliers avec la méthode Interquantile Range

# Calculer les quartiles
Q1 <- quantile(mcdo$Carbohydrates, 0.25)
Q3 <- quantile(mcdo$Carbohydrates, 0.75)
IQR <- Q3 - Q1

# Définir les seuils
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Filtrer les données sans outliers
mcdo_clean <- mcdo[mcdo$Carbohydrates >= lower_bound & mcdo$Carbohydrates <= upper_bound, ]

#Recalculer la corrélation et refaire la visualisation
cor_qte_car_clean <- cor(mcdo_clean$Quantity,mcdo_clean$Carbohydrates)
cor_qte_car_clean

cor_graph_clean <- ggplot(data = mcdo_clean) +
  aes(x = Quantity, y = Carbohydrates) +
  geom_point() +
  labs(title = "Relation entre Quantity et Carbohydrates",
       x = "Quantity",
       y = "Carbohydrates")
cor_graph_clean

cor_test_clean <- cor.test(mcdo$Quantity, mcdo$Carbohydrates)
pander(cor_test_clean)

#Nous observons que la corrélation reste statistiquement significative mais
#elle devient encore plus faible
#Nous pouvons conclure que la quantité n'est pas la variable qui est la plus
#corrélée a la quantité de glucides

### Question 1 ###

#On fait un vecteur avec les variables de l'acp et on crée une sous base de données
var_acp <- c("Calories", "Total.Fat", "Saturated.Fat", "Cholesterol",
              "Carbohydrates", "Dietary.Fiber", "Sugars", "Protein", "Quantity")
mcdo_acp <- mcdo[,var_acp]

#ACP
res_acp <- PCA(mcdo_acp, scale.unit = TRUE, ncp = 9)

#a. critere de Kaiser
kaiser <- res_acp$eig |> round(2)
kaiser
#On conserve les valeurs > 1
#Dans ce cas on conserve les 2 premieres composantes principales

#b. Les 3 premieres composantes expliquent 88,36%.
#Verifions les contributions des variables
cos2_variables <- rowSums(res_acp$var$cos2[,1:3])
sort(cos2_variables)
#Le cholesterol est la variable la moins bien représentée par les 3 premieres
#composantes avec 80% de représentation

#c. 
cos2_variables <- rowSums(res_acp$var$cos2[,1:2])
sort(cos2_variables)
top6_var <- c("Calories", "Sugars", "Carbohydrates", "Total.Fat", "Saturated.Fat", "Quantity")
graph_var <- fviz_pca_var(res_acp, axes = c(1,2), select.var = list(name = top6_var)) #le dernier argument (select.var = list(name = top6_var) est avec l'aide de IA
#la composante 1 explique 61,5% de la variance totale.
#les variables fortement corréles a cette composante (axe horizontale) sont:
#Quantity, Total.Fat, Calories, Saturated.Fat
#Dim 1 semble représenté les aliments qui sont plus riches en graisses et en énergie (plus caloriques)

#d.
mcdo_acp$Category <- mcdo$Category
graph_ind <- fviz_pca_ind(res_acp, axes = c(1,2), habillage = as.factor(mcdo_acp$Category), label = "none")
graph_ind
#Nous voyons que les aliments de la catégorie Beef & Pork sont en bas au centre et sont distribués de maniere horizontale
#Comme on avait dit, la composante 1 (horizontale) représente les aliments riches en graisses et caloriques
#Nous pouvons déduire que les aliments de la catégorie Beef & Pork sont riches en graisses et caloriques

