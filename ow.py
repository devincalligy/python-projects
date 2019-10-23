def intro():
    print(
    """
             ____________   _________________________  __      __  _________________________   ___ ___  
             \_____  \   \ /   /\_   _____/\______   \/  \    /  \/  _  \__    ___/\_   ___ \ /   |   \ 
              /   |   \   Y   /  |    __)_  |       _/\   \/\/   /  /_\  \|    |   /    \  \//    ~    \        
             /    |    \     /   |        \ |    |   \ \        /    |    \    |   \     \___\    Y    /
             \_______  /\___/   /_______  / |____|_  /  \__/\  /\____|__  /____|    \______  /\___|_  / 
                     \/                 \/         \/        \/         \/                 \/       \/  
                    _________  ________   ____ __________________________________________  _________           
                    \_   ___ \ \_____  \ |    |   \      \__    ___/\_   _____/\______   \/   _____/           
                    /    \  \/  /   |   \|    |   /   |   \|    |    |    __)_  |       _/\_____  \            
                    \     \____/    |    \    |  /    |    \    |    |        \ |    |   \/        \           
                     \______  /\_______  /______/\____|__  /____|   /_______  / |____|_  /_______  /           
                            \/         \/                \/                 \/         \/        \/            
                                                   by:kaiserguwop
                                                 ow_herocounterv1.0
    """)
    print("hi, im a simple script provides overwatch hero counters.\n")
    
def intro_options():
    print("here are your options:\n")
    print("[1] i can print a list of all heroes or print them by class.")
    print("[2] you can type in a name and i'll tell you the counters.")
    print("[3] you can gtfo and close this.\n")
    print("type option number below to continue.\n")
    response_input()
    
def response_input():
    input_response = input(prompt)
    if input_response == 'yes' or 'no' or '1' or '2' or '3':
        input_reponse == True
        print("Okay, let me do that for you.")
    else:
        input_reponse == False
        print("i'm sorry, that's not a choice.")
    
    
def try_again(): 
    print("i'm sorry, that's not an option. Would you like to try again?\n")
    print('type yes or no below\n')
    
def list_print():
    print("would you like to see a list of heroes and their class?\n")
    print("type yes or no below\n")
    response_input()
    
def print_list():
    print("here are tanks heroes\n", tanks)
    print("here are damage heroes\n", damage)
    print("here are support heroes\n", support)
 
 
tanks = ['d.va','orisa','reinhardt','roadhog','sigma','winston','wrecking ball','zarya']
damage = ['ashe','bastion','doomfist','genji','hanzo','junkrat','mccree','mei','pharah','reaper','soldier:76','sombra','symmetra','torbjorn','tracer','widowmaker']
support = ['ana','baptiste','brigitte','lucio','mercy','moira','zenyatta']
prompt = ('~~~ ')





intro()
intro_options()
#list_print()
