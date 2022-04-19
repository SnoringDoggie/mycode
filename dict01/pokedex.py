pokedex={"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}

pokedex["Pikachu"] = "Electric"
#pokedex.keys() is a list of keys
#.join can be used to join elements in a list together

x = pokedex 
x = ",".join(x)
print(x)

choice= input("Name a Generation 1 starter Pokemon:\n>")

#print(pokedex[choice])
print(pokedex.get(choice, "Sorry, we don't have any record of that Pokemon!"))







