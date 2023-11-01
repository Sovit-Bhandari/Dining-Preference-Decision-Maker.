'''Full Name = Sovit Bhandari
   U-number = U83561265
   Brief discription = This code identify the food choice of group of people and provide them with the list of restaurant 
   where they can go. Note: anything other than yes "is a no" for this code '''

#Providing the input for the user with automatic lower case input
veg = input('Is anyone in your party a vegetarian?').lower()
vegan = input('Is anyone in your party a vegan?').lower()
glutenfree = input('Is anyone in your party gluten free?').lower()

#providing the conditions 
if vegan == 'yes':
    Restaurant = "Farmacy Vegan Kitchen"
elif glutenfree == 'yes':
    Restaurant = "Wood Fired Pizza Wine Bar\nFarmacy Vegan Kitchen"
elif veg == 'yes':
    Restaurant ="Wood Fired Pizza Wine Bar\nVillaggio's Ristorante Italiano\nFarmacy Vegan Kitchen"   
else:
    Restaurant = "Council Oak Steaks and Seafood\nWood Fired Pizza Wine Bar\nVillaggio's Ristorante Italiano\nFarmacy Vegan Kitchen"
print(f'Here are your restaurant choices:\n{Restaurant}')