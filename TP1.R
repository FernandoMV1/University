(exp(28) + cos(0.5))/3
log(4)
log(4, base = 4)
log10(4)
a = c(0,3,4.5,2,10,11,10,4,0.66)
mean(a)
sd(a)
a[4]
which(a==4)
b = c(1,2,3,4,5)
c = c(5,4,3,2,1)
cor(b,c)
mean(Eurojobs$Agr)
median(Eurojobs$Agr)
#mean > median, il y a des valeurs élevés qui influencent la moyenne
var(Eurojobs$Man)
quantile(Eurojobs$Man,0.6)
cor(Eurojobs$SI, Eurojobs$SPS)
cor(Eurojobs$SPS, Eurojobs$SI)
#la corrélation est symetriquedonc les valeurs sont les memes
median(rangs$Score.on.Alumni)
quantile(rangs$Score.on.SCI,0.3)
cor(rangs$Score.on.Alumni, rangs$Score.on.Award)
lapply(rangs[7:13],var)
#Pipes shortcut Ctrl + Shift + M --> |> 
"ggplot2" |> install.packages()
ggplot2 |> library()

ggplot(data = pokemon2) + 
  aes(y = HP) +
  geom_boxplot() +
  labs(title = "Boxplot de la variable HP",
       x = NULL,
       y = "HP")

ggplot(data = pokemon2)+ 
  aes(x = Attack, y = Defense, colour = Legendary)+
  geom_point()

ggplot(data=pokemon2)+
  aes(group = Generation, y = Total)+
  geom_boxplot()

pokemon_legendary <- subset(pokemon2, Legendary == "True")
ggplot(pokemon_legendary)+
  aes(x = Total, y = HP, label = Name)+
  geom_text(check_overlap = T, nudge_y = 4)+
  geom_point()+
  labs(title = "Pokemon légendaires",
       x = "Total",
       y = "HP")

plot(x = mpg$displ, y = mpg$hwy, type = "p", 
     main = "Efficacité vs Cylindrée", 
     xlab = "Cylindre", 
     ylab = "Efficacité",
     xlim = c(2,4),
     ylim= c(20,30))



