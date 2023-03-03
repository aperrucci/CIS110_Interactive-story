print (f"Hello, Lets create an interactive story together. ")
print (f"To get started, lets answer a few questions.")
print (f"After typing your answer, be sure to press the enter key.")
input (f"Press the enter key to continue...")
keepPlaying='yes'
while keepPlaying=='yes':

    #5 Questions
    cat_name = input("What is your cat's name? ")
    while len(cat_name) == 0:
        cat_name = input(f"Please enter your cats name:  ")
    cat_gender = input("What is your cat's gender? ")
    while len(cat_gender) == 0:
            cat_gender = input(f"Is your cat a boy or a girl:  ")
    cat_color = input("What color is your cat? ")
    while len(cat_color) == 0:
            cat_color = input (f"What color is your cat?  ")
    location = input("Where do you and your cat live? ")
    while len(location) == 0:
            location = input (f"Where do you and your cat live?  ")
    cat_who = input (f'Are you your cats mom or dad?  ')
    while len(cat_who) == 0:
            cat_who = (f'Are you your cats mom or dad?  ')


    # Story Starts


    print(f"\nThere once was an adorable {cat_color} kitty named {cat_name}")
    print(f"{cat_name} is a little {cat_gender} kitty that lives in {location} with {cat_who} ")
    print(f"One day when {cat_name} woke up for the day the front door was open")
    print(f"{cat_name} was curious about the outside")


    explore = input(f"\nShould {cat_name} go outside and explore?  Type yes or no:  ")
    while explore.lower() != "yes" and explore.lower() != "no":
            explore = input("Please type yes or no:  ")

    if explore == "yes":
            print(f"\n{cat_name} walks out the front door and down the front steps. ")
            print(f'{cat_name} feels the warm sunshine and sits in the soft grass looking around')
            print(f'{cat_name} see the bees flying and hears the birds chirping in the tree')
            print(f'{cat_name} is a curious {cat_gender}')
            print(f'{cat_name} sees the tree where the birds live ')
            tree = input (f'\nSould {cat_name} climb the tree to see the birds?  ')
            while tree.lower() != 'yes' and tree.lower() != 'no':
                tree = input ('Please type yes or no:  ')


    if explore == 'yes' and tree == 'yes':  
        print (f'\n{cat_name} climbs the tree and encounters the birds in their nest')
        print (f'the birds are afraid of {cat_name} at first')
        print (f'the birds realize {cat_name} is the cute kitty that watches them from the kitchen window')
        print (f'they know {cat_name} is friendly and they chirp and chatter to each other')
        print (f'When {cat_name} {cat_who} arrives home from work and sees {cat_name} in the tree, {cat_who} gets {cat_name} out of the tree and brings {cat_name} inside.')
        print (f'\nTHE END!')


    if explore == 'yes' and tree == 'no' :
        print (f'\nThe {cat_color} {cat_gender} decides to play in the grass')
        print (f'After playing with the leaves in the grass {cat_name} falls asleep.')
        print (f'When {cat_name} {cat_who} arrives home from work and sees {cat_name} sleeping in the grass {cat_who} scoops {cat_name} up and brings {cat_name} inside.')
        print(f'{cat_name} is a good {cat_gender}')
        print (f'\nTHE END!')

    if explore == 'no':
        print(f'\n{cat_name} decides to stay inside.')
        nap = input(f"\nShould {cat_name} take a nap?  Type yes or no:  ")
        while nap.lower() != "yes" and nap.lower() != "no":
            nap = input("Please type yes or no:  ")

    if explore == 'no' and nap == 'yes':
        print(f'\n{cat_name} went to the cat napper and took a long nap and waited for {cat_who} to come home')
        print (f'When {cat_name} {cat_who} arrives home from work and sees {cat_name} sleeping peacefully {cat_who} smiles and gives {cat_name} some pets and kisses.')
        print(f'{cat_name} is a good {cat_gender}')
        print (f'\nTHE END!')

    if explore == 'no' and nap == 'no':
        print(f'{cat_name} ate some kibble and played with some toys waiting for {cat_who} to come home')
        print(f'When {cat_who} gets home from work {cat_name} gets some kisses and pets and is happy')
        print(f'{cat_name} is a good {cat_gender}')
        print (f'\nTHE END!')

    keepPlaying = input(f'\nDo you want to play again? Enter yes or no:  ')
    while keepPlaying.lower() != 'yes' and keepPlaying.lower() != 'no':
            keepPlaying = input(f'Please type yes or no:  ')
        