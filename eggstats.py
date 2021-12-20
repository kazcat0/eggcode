"""species needs are connected to their needed moisture levels

   aquatic species need to be submerged in the bathtub, average species need no 
   special considerations, and dry species need to be out in the hot sun

   shrimps, crabs, and octopi are aquatic species. birds, echidnas, and platypi 
   are average species. dragons, insects, and reptiles are dry species."""

import random

def speciesSelect():
    species = ["shrimp", "crab", "octopus", 
                "bird", "echidna", "platypi", 
                "dragon", "insect", "reptile"]

    select = species[random.randrange(0,len(species))]

    print(f"Your species is {select}.")

speciesSelect()

#how to save species selection?

#have countdown system for egg warmth