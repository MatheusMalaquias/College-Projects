#I added a delay to show the options people will choose to help them read the history and choose the better option.
import time
print('WELCOME TO THE ADVENTURE WORLD!!')
time.sleep(2)
print('Here we will embark in a great adventure where you will define the end to the history and to start you can choose one of these places to start your adventure:')
print('The places you can start is in the FOREST or in the BEACH. ')
time.sleep(5)
print('Write your answer!')
#Forest part
time.sleep(3)
game_start = input('What is the place do you would like to start? ')
time.sleep(3)
if game_start.lower() == 'forest':
    print("You went to the forest with a tour group that like to climb mountains and appreciate the natural landscape but before to start the climbing you realize that you forget your security tools and these are the options you have WAIT IN THE CAR, VENTURE IN THE FOREST or SEARCH TOOLS")
    time.sleep(3)
    print('Write your answer!')
    time.sleep(3)
    first_choose_forest = input('What is your choose? ')
    time.sleep(3)
    if first_choose_forest.lower() == 'wait in the car':
        print("You are sleeping in the car when you hear something outside that made you fear and try to find something to recognize the sound and have these options you have is TURN ON THE CAR HEADLIGHTS or LEAVE THE CAR TO FIND SOMETHING")
        time.sleep(3)
        print('Write your answer!')
        time.sleep(3)
        second_choose_forest = input('What is your choose? ')
        time.sleep(3)
        if second_choose_forest.lower() == 'turn on the car headlights':
            print('You are focuos looking everything around you trying recognize some different thing when you see a tiger and start to drive to escape and leave the forest.')
        if second_choose_forest.lower() == 'leave the car to find something':
            print('You are walking close to the car when you look a tiger looking to you and you start to run to escape it until become safe.')

    if first_choose_forest.lower() == 'venture in the forest':
        print("You are walking and don't noticed the nightfall is coming and these are the options you have is MAKE A CAMP IN THE FOREST or BACK TO THE GROUP")
        time.sleep(3)
        print('Write your answer!')
        time.sleep(3)
        third_choose_forest = input('What is your choose? ')
        time.sleep(3)
        if third_choose_forest.lower() == 'make a camp in the forest':
            print('You make a camp in the forest to rest and wake up willing to find everyone and back at home in the next day.')
        if third_choose_forest.lower() == 'back to the group':
            print('You back to the group meat everyone and prepare to back at home after a long day in the forest.')

    if first_choose_forest.lower() == 'search tools':
        print("You are searching your securuty tools in the car's bags and can't find until you see a poisonous spider ans these are the options you have is KILL THE SPIDER or LEAVE THE CAR")
        time.sleep(3)
        print('Write your answer!')
        time.sleep(3)
        fourth_choose_forest = input('What is your answer? ')
        time.sleep(3)
        if fourth_choose_forest.lower() == 'kill the spider':
            print('You kill the spider got the security tools, climb the mountain and appreciate the natural landscape with the group.')
        if fourth_choose_forest.lower() == 'leave the car':
            print('You leave the car and take the necessary to walk through the forest and back at home.')
time.sleep(3)


#Beach part
if game_start.lower() == 'beach':
    print("You went to the beach with a tour group that like to surf but when you arrive there you se that is able use a boat to go to the island and these are the options you have is GO TO SURF, GO TO THE ISLAND or GO TO SWIM")
    time.sleep(3)
    print('Write your answer!')
    time.sleep(3)
    first_choose_beach = input('What is your choose? ')
    time.sleep(3)
    if first_choose_beach.lower() == 'go to surf':
        print("You are surfing when you are surpresed to a shark and these are the options you have is ESCAPE or FIGHT TO SURVIVER")
        time.sleep(3)
        print('Write your answer!')
        time.sleep(3)
        second_choose_beach = input('What is your choose? ')
        time.sleep(3)
        if second_choose_beach.lower() == 'escape':
            print("You won't try some hard thing and escape to the shark to a island when you find food and suplements to pass the rest of your life there.")
        if second_choose_beach.lower() == 'fight to surviver':
            print("You tried fight with the shark and gain but now you're so tired and the sea ​​current carries you to an island full of trees when you pass the rest of your days.")

    if first_choose_beach.lower() == 'go to the island':
        print("You are browsing to the island when suddenly the gasoline runs out and these are the options you have is LEAVE THE BOAT or USE THE ALCOHOLIC DRINK")
        time.sleep(3)
        print('Write your answer!')
        time.sleep(3)
        third_choose_beach = input('What is your choose? ')
        time.sleep(3)
        if third_choose_beach.lower() == 'leave the boat':
            print('You left the boat and will swim until the beach to take your things and back at home.')
        if third_choose_beach.lower() == 'use the alcoholic drink':
            print('You put alcoholic drink in the boat and arrive in the island and can enjoy everything there.')

    if first_choose_beach.lower() == 'go to swim':
        print('You are swim with the fishes when you see something shining in the seabed and these are the options you have is TRY TAKE ALONE or FORGET IT AND KEEP SWIMMING')
        time.sleep(3)
        print('Write your answer!')
        time.sleep(3)
        fouth_choose_beach = input('What is your choose? ')
        time.sleep(3)
        if fouth_choose_beach.lower() == 'try take alone':
            print('You tried take the object alone and saw that is a piece of gold that you take sell and become rich.')
        if fouth_choose_beach.lower() == 'forget it and keep swimming':
            print("You don't pay attention to the object and keep swimming with the fishes.")
time.sleep(3)
print('Congrats!! You finish the game!!')