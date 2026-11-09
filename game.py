import time
import os
import sys
#declaring names as variables. 
player_name = "jimbob"
npc1 = "Unknown Voice"
npc2 = "Annoyed Man"
npc3 = "Unknown Prisoner"
god = "god"

#location 
place = "interrogation"

# progression variables
key = False
distraction = "no"


def wait(sec):
    time.sleep(sec)

##dialauge function. easier for my lazy butt to type
def says(speaker, text):
    print(speaker+ ": " + text)
    wait(1.5)

while place == "interrogation":
    says(npc1,"Why hello")
    wait(2)
    player_name = input(npc1+": Now tell me, what's your name? ")
    if player_name[0].isupper() == False:
        player_name = player_name[0].upper() + player_name[1:]
    wait(1)
    if player_name == "Kill me":
        says(npc1, "Fine then.")
        place = "end"
    else:
        says(npc1, "Ahh yes. Hello, " + player_name + "!")
        says(npc1, "My name is Carol.")
        npc1 = "Carol"
        says(npc1, "Nice to meet you.")
        wait(3)
        says(npc1, "...")
        wait(1)
        while place == "interrogation":
            says(npc1, "Now tell me, do you know why you're here?")
            response = str(input("How do you respond?(y/n): " )).strip().lower()
            if response == "y" or response == "yes":
                says(npc1, "Well then. That makes this easier.") 
                says(npc1, "I guess I'll send you straight to processing.")   
                print("You feel rough hands grab your shoulders. And you feel a rough sack come over your head. As consciousness fades you hear something.")
                wait(2)
                says(npc2, "You know this is breach of protocol C!")
                says(npc1, "Ahh fooy to your protocol, they said knew why they were here, but we both know they are clueless as a pheasant.")
                place = "processing"
            elif response ==  "n" or response == "no":
                says(npc1, "Well too damn bad.")
                says(npc1, "Go find an open cell.")
                print("The door on the far end of the room swings open with a slow, eerie creak that speaks to the maintenance budget of this place.")
                wait(3)
                place = "reception"
            else: 
                says(god, "Boy, you know that's not an answer. Try again")

while place == "processing":
    wait(1)
    print(player_name + " wakes up in another strange room, full of strewn papers and a very unhappy looking man.")
    wait(2)
    says(npc2, "Ah yes, up up. Let's get moving, I have better things to do here.")
    wait(1)
    says(npc2, "Get to your cell.")
    says(npc2, "I took care of the paper work while you were napping.")
    print(player_name+ " enters the hall." )
    print("There are four cells, two on the left and two on the right.")
    place = "hall"

while place == "reception":
    print(player_name + " walks through the door into a room with a desk just ahead. Behind the desk sits a man who looks none too happy.")
    wait(1)
    print("A long hall off to one side goes to the cells, and an open door to what looks like a street on the other.")
    says(npc2, "Damn her")
    says(npc2, "Oh whatever, come over here.")
    choice = int(input("Make a break (1) or Approach the unhappy man?(2) (1 or 2): "))
    if choice == 1: 
        print("Ahh hell nah. " + player_name + "thinks.")
        print('Get me outta here.')
        wait(1)
        print(player_name + " runs as fast as they can towards the open door much to the indifference of the annoyed man.")
        says(npc2, "*sigh* What do I care at this point.")
        print("Poor " + player_name + " didn't even know what hit them.")
        wait(.5)
        print("As you run through the open door a figure falls on top of you.")
        wait(1)
        print("The end")
        wait(.3)
        print("Poor chap never stood a chance.")
        wait(2)
        # print("Ending " end_count " of 3")
        place = "end"
    elif choice == 2 :
        print(player_name + " approaches the man. His annoyance is evidenced by his glare.")
        wait(1)
        says(npc2, "get on with it, then")
        says(npc2, "Head down the hall and find a cell. It's fine, most don't bite...")
        wait(1)
        says(npc2, "too hard.")
        wait(2)
        print(player_name+ " enters the hall." )
        print("There are four cells, two on the left and two on the right.")
        place = "hall"
    else:
        says(god, "Dawg it's 1 or 2 how do you mess that up?")

while place == "hall":
    
    wait(.5)
    answer = int(input("Which cell will you check out?(1, 2, 3, or 4): "))
    if answer == 1:
        if key == True:
            print("There sits an old man. His single gold tooth gleams in the dull light.")
            print("He says not a word, just offers an open palm.")
            answer = input("Give him the key?(y/n): ")
            if answer == "y" or "Y" or "Yes" or "yes":
                print("He silently opens the cell and runs out into the first room.")
                print("You hear yelling and maybe a few airborn objects.")
                distraction = "yes"
        else: 
            print("The closest cell on the right has a strange old man with a single crooked gold tooth. He just sits there and grins with a madness in his eye.")
            print("Best not engage with him.")
    elif answer == 2:
        enter_cell = input("This cell is empty. Do you enter?(y/n): ")
        if enter_cell == "y" or "Y" or "Yes" or "yes":
            if key == False:
                print("As you enter the cell, the door closes behind you.")
                wait(2)
                print("No matter what you do, claw as you might, there is no way out. You are trapped.")
                wait(2)
                print("The end")
                wait(5)
                # print("Ending " end_count " of 3")
                place = "end"
            if key == True:
                print("As you enter the cell, the door closes behind you.")
                wait(1)
                choice = input("Do you wait?(y/n): ")
                if choice == "y" or "Y" or "Yes" or "yes":
                    wait(1)
                    print("You wait for hours. Until dusk has far set.")
                    wait(1)
                    print("You run out the open door from before.")
                    wait(1)
                    print("Lucky you.")
                    print("not a soul")
                    wait(1)
                    print("You run")
                    wait(1)
                    print("as far and fast as you can.") 
                    wait(1)
                    print("maybe then they wont find you.")
                    print("The end")
                    wait(.3)
                    print("Good Luck, Raven")
                    wait(5)
                    # print("Ending " end_count " of 3")
                    place = "end"
                else:
                    print("As you walk out the door you just unlocked, your luck fails you.")
                    wait(3)
                    says(npc1, "Oh hello there!")
                    says(npc1, "Out of your cage are we?")
                    says(npc1, "What a shame, it seems you knew after all.")
                    says(npc1, "Well...")
                    says(npc1, "Can't have that can we.")
                    wait(2)
                    print("The end")
                    wait(.3)
                    print("Poor chap never stood a chance.")
                    wait(5)
                    # print("Ending " end_count " of 3")
                    place = "end"
                    
        else: 
            print("Fine then, be that way. Go wander the hall.")
            print("You'll be back >:|")
    elif answer == 3:
        print("Theres a big hole in the back of this cell. You can hear the faint sound of wind coming from it.")
        enter_cell = input("This cell is empty. Do you enter?(y/n): ").strip().lower()
        if enter_cell == "y" or enter_cell == "yes":
            print("You look through the crack and see the outside world.")
            wait(.8)
            print("It looks tight, but you think you could fit.")
            wait(.5)
            enter_crack = int(input("Enter the crack (1) or return to the hall (2) (1 or 2)?: "))
            if enter_crack == 1:
                if distraction == "yes":
                    print("You run")
                    wait(1)
                    print("as far and fast as you can.") 
                    wait(1)
                    print("maybe then they wont find you.")
                    print("The end")
                    wait(.3)
                    print("Good Luck, Raven")
                    wait(5)
                    # print("Ending " end_count " of 3")
                    place = "end"
                else:
                    print("As" + player_name+ "gets out of the crack,  a figure falls on top of them.")
                    wait(1)
                    print("The end")
                    wait(.3)
                    print("Poor chap never stood a chance.")
                    wait(5)
                    # print("Ending " end_count " of 3")
                    place = "end"
            print("boy")
        else:
            print("Fine then, be that way. Go wander the hall.")
            wait(1)
            print("You'll be back. I know you are curious.")
    elif answer == 4:
        print("As you approach, you see a prisoner in the cell.") 
        wait(1)
        print("He smiles at you.")
        wait(1)
        says(npc3, "Why hello there.")
        says(npc3, "And do you know why you are here?")
        take_key = input("Do you?(y/n): ").strip().lower()
        if take_key == "y" or take_key == "yes":
            says(npc3, "HAHA! well then. This should be fun.")
            print("The prisoner reaches a fist through the bars.")
            wait(1)
            print("He opens it, and in his hand lies a key.")
            wait(1)
            choice = input("Do you dare take it?(y/n): ").strip().lower()
            if choice == "y" or choice == "yes":
                key = True
                print("As you take the key you feel a weight in your bones.")
                wait(2)
                print("You leave as he cackles with glee.")
                wait(1)
                says(npc3, "Good luck, Raven!")
            else:
                print("As you shrink away, he scowls.")
                wait(.2)
                says(npc3, "Well, I'll be here.")
        else:
            says(npc3, "Well, too bad. Come back later if you figure it out")
            says(npc3, "fool")



while place == "end": 
    os.system('cls' if os.name == 'nt' else 'clear')
    os.execl(sys.executable, sys.executable, *sys.argv)
    