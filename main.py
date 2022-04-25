import random
when = ['A millenia ago', 'In another life', 'While stealing a body', 'After jumping to a new body','After cleaning the grime from the crime scene']
name = ['Bright Kelidescope,', 'Mayhem Muriel,','Werewolf Ken,', 'Black Ivy,', 'Soul Winter,']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['home', 'insane','seminar', 'school', '']
happened = ['felt resolute about finding the killer.','checked on their pet Sphinx.', 'found a secret key.', 'solved a mystery of the shapeshifter.', 'left for Paris.']
print(random.choice(when) + ', ' + random.choice(name) + ' who lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))