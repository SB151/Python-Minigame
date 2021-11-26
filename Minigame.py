# Minigame: Mara the Vile

# Names: player & boss mara
name=input('Player, what is your name? ').title()
print(f'\tWelcome, {name}...prepare yourself for the worst.')
print('\nA shadow approaches from behind, it\'s Mara the vile! Get ready!')


health=15
mara=15
# Player Initiative

initiative=input('It\'s your turn, do you punch Mara or use magic? Type \'punch\' or \'magic\' ').title()

#for rounds in range(3):
while health >= 1:
    # use random library to simulate behaviors for mara
    # use random library to determine damage values in the game
    import random
    critical=random.randint(1,20)
    punch=random.randint(1,4)
    magic=random.randint(1,6)
    if critical==20:
        punch=random.randint(5,8)
        magic=random.randint(7,14)
    else:
        punch=random.randint(1,4)
        magic=random.randint(1,6)
    if health <=0:
        break
    if initiative=='Punch':
        print(f'\tYou deal {punch} damage to Mara!')
        mara-=punch
        print(f'\tMara has {mara} hit points remaining')
        if mara <=0:
             break
        else:
            tentacle=random.randint(1,6)
            health-=tentacle
            print(f'\nMara attacks you dealing {tentacle} damage !')
            print(f'\tYou have {health} hit points remaining')
            initiative=input('Do you punch Mara or use magic? Type \'punch\' or \'magic\' ').title()
            if health <=0:
                break
    elif initiative=='Magic':
        print(f'\tYou deal {magic} damage to Mara!')
        mara-=magic
        print(f'\tMara has {mara} hit points remaining')
        if mara <=0:
            break
        else:
            tentacle=random.randint(1,6)
            health-=tentacle
            print(f'\nMara attacks you dealing {tentacle} damage !')
            print(f'\tYou have {health} hit points remaining')
            if health <=0:
                break
            initiative=input('Do you punch Mara or use magic? Type \'punch\' or \'magic\' ').title()
        #elif initiative != 'Punch' or 'Magic':
            #while initiative != 'Punch' or 'Magic':
    else:
        initiative=input('Invalid entry. Do you punch Mara or use magic? Type \'punch\' or \'magic\' ').title()
        
    #print(f'\tMara has {mara} hit points remaining')
# Mara Initiative
#while mara 
    #if mara <=0:
       #break
    #else:
        #tentacle=random.randint(1,6)
        #health-=tentacle
        #print(f'\nMara attacks you dealing {tentacle} damage !')
       #print(f'\tYou have {health} hit points remaining')
    
    #initiative=input('Do you punch Mara or use magic? Type \'punch\' or \'magic\' ').title() 
if health <=0:
    print('\n You have lost!')
else:
    print('\n Mara flees, vowing revenge!')

    
    
