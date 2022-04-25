import random
when = ['A millenia ago', 'In another life', 'While stealing a body', 'After jumping to a new body','After cleaning the grime from the crime scene']
name = ['Bright Kelidescope,', 'Mayhem Muriel,','Werewolf Ken,', 'Black Ivy,', 'Soul Winter,']
residence = ['the land of the Winter Queen','in the catacombs under Paris', 'at thet top of the belltower', 'the cemetary', 'England']
went = ['home', 'insane','to meet other superheroes', 'to the home of their arch nemisis', 'the secret library room']
happened = ['felt resolute about finding the killer.','checked on their pet Sphinx.', 'found a secret key.', 'solved the mystery of the shapeshifter.', 'left the planet.']
print(random.choice(when) + ', ' + random.choice(name) + ' who lived ' + random.choice(residence) + ', went ' + random.choice(went) + ' and ' + random.choice(happened))