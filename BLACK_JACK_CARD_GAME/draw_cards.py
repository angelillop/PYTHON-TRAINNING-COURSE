# Importing clear utility from OS
import os
clear = lambda: os.system('cls')

# Importing Colorama 
from colorama import init,Fore,Back
init(autoreset=True)

#Card Type (# DIAMOND = "\u2666", # CLUB = "\u2663", # HEART = "\u2665", # SPADE = "\u2660" )
D = "\u2666" 
C = "\u2663" 
H = "\u2665" 
S = "\u2660"
 
#Variables
wcu = '' # wild card up
wcd = '' # wild card down


def get_card(hand_card):

    # Giving Color and suit to the card    
    if 'Diamonds' in hand_card:
        ct = D # Card Type
        cc = Fore.RED # Card Color 
        fc = Fore.RED # Frame Color
        bc = Back.WHITE # Back Color
    if 'Hearts' in hand_card:
        ct = H # Card Type
        cc = Fore.RED # Card Color
        fc = Fore.RED # Frame Color
        bc = Back.WHITE # Back Color
    if 'Clubs' in hand_card:
        ct = C # Card Type
        cc = Fore.BLACK # Card Color
        fc = Fore.BLACK # Frame Color
        bc = Back.WHITE # Back Color
    if 'Spades' in hand_card:
        ct = S # Card Type
        cc = Fore.BLACK # Card Color 
        fc = Fore.BLACK # Frame Color
        bc = Back.WHITE # Back Color
        
    # Checking for Aces, Jack, Queen and King
    if 'Ace' in hand_card or 'Jack' in hand_card or 'Queen' in hand_card or 'King' in hand_card:
    
        # Setting upper and down suit
        if 'Ace' in hand_card:
            wcu = 'A' # card rank up
            wcd = 'V' # card rank down
        # Checking Jack
        if 'Jack' in hand_card:
            wcu = 'J' # card rank up
            wcd = '\u017f' # card rank down
        # Checking Queen
        if 'Queen' in hand_card:
            wcu = 'Q' # card rank up
            wcd = '\u038c' # card rank down
        # Checking King
        if 'King' in hand_card:
            wcu = 'K' # card rank up
            wcd = '\u029e' # card rank down  
        
        #Template for Aces, Jack, Queen and King
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + wcu+'    '+fc +'    ║'
        line3 = bc + fc + '║ '+cc + '    '+fc +'    ║'
        line4 = bc + fc + '║ '+cc + '  '+ct+ct+ct+ ' ' + fc +'  ║'
        line5 = bc + fc + '║ '+cc + '  '+ct+ct+ct+ ' ' + fc +'  ║'
        line6 = bc + fc + '║ '+cc + '  '+ct+ct+ct+ ' ' + fc +'  ║'
        line7 = bc + fc + '║ '+cc + '  '+ct+ct+ct+ ' ' + fc +'  ║'
        line8 = bc + fc + '║ '+cc +'      ' +fc + '  ║'
        line9 = bc + fc + '║'+cc + '        '+wcd+fc +'║'
        line10= bc + fc + '╚═════════╝'

    elif 'card hidden' in hand_card:
        bc = Back.WHITE # Back Color
        fc = Fore.BLUE # Frame Color
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║X      X ║'
        line3 = bc + fc + '║ X    X  ║'
        line4 = bc + fc + '║  X  X   ║'
        line5 = bc + fc + '║   XX    ║'
        line6 = bc + fc + '║   XX    ║'
        line7 = bc + fc + '║  X  X   ║'
        line8 = bc + fc + '║ X    X  ║'
        line9 = bc + fc + '║X      X ║'
        line10= bc + fc + '╚═════════╝'
        
    elif 'Two' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc +'2      ' +fc + '  ║'
        line3 = bc + fc + '║         ║'
        line4 = bc + fc + '║ '+cc +'   ' +ct+'  ' +fc + '  ║'
        line5 = bc + fc + '║         ║'
        line6 = bc + fc + '║         ║'
        line7 = bc + fc + '║ '+cc + '   '+ct+ ''+fc +'    ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║'+cc +'        2' +fc + '║'
        line10= bc + fc + '╚═════════╝'
    
    elif 'Three' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + '3    '+fc +'    ║'
        line3 = bc + fc + '║    '+cc + ct + '   ' +fc + ' ║'
        line4 = bc + fc + '║         ║'
        line5 = bc + fc + '║    '+cc + ct +'  '+fc +'  ║'
        line6 = bc + fc + '║         ║'
        line7 = bc + fc + '║    '+cc + ct +'  '+fc +'  ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║  '+cc +'      3' +fc + '║'
        line10= bc + fc + '╚═════════╝'
    
    elif 'Four' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + '4    '+fc +'    ║'
        line3 = bc + fc + '║         ║'
        line4 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line5 = bc + fc + '║         ║'
        line6 = bc + fc + '║         ║'
        line7 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║  '+cc +'      4' +fc + '║'
        line10= bc + fc + '╚═════════╝\n'
    
    elif 'Five' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + '5    '+fc +'    ║'
        line3 = bc + fc + '║  '+cc + ct +'   ' + ct +fc + '  ║'
        line4 = bc + fc + '║         ║'
        line5 = bc + fc + '║    '+cc + ct +'  '+fc +'  ║'
        line6 = bc + fc + '║         ║'
        line7 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║  '+cc +'      5' +fc + '║'
        line10= bc + fc + '╚═════════╝'
    
    elif 'Six' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + '6    '+fc +'    ║'
        line3 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line4 = bc + fc + '║         ║'
        line5 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line6 = bc + fc + '║         ║'
        line7 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║  '+cc +'      6' + fc + '║'
        line10= bc + fc + '╚═════════╝'
    
    elif 'Seven' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + '7    '+fc +'    ║'
        line3 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line4 = bc + fc + '║         ║'
        line5 = bc + fc + '║  '+cc + ct +' '+ ct +' ' + ct + fc + '  ║'
        line6 = bc + fc + '║         ║'
        line7 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║  '+cc +'      7' +fc + '║'
        line10= bc + fc + '╚═════════╝'
    
    elif 'Eight' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + '8    '+fc +'    ║'
        line3 = bc + fc + '║         ║'
        line4 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line5 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line6 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line7 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║  '+cc +'      8' +fc + '║'
        line10= bc + fc + '╚═════════╝'
    
    elif 'Nine' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + '9    '+fc +'    ║'
        line3 = bc + fc + '║         ║'
        line4 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line5 = bc + fc + '║  '+cc + ct +' '+ ct +' ' + ct + fc + '  ║'
        line6 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line7 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║  '+cc +'      9' +fc + '║'
        line10= bc + fc + '╚═════════╝'
    
    
    elif 'Ten' in hand_card:
        line1 = bc + fc + '╔═════════╗'
        line2 = bc + fc + '║'+cc + '10   '+fc +'    ║'
        line3 = bc + fc + '║         ║'
        line4 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line5 = bc + fc + '║  '+cc + ct +' '+ ct +' ' + ct + fc + '  ║'
        line6 = bc + fc + '║  '+cc + ct +' '+ ct +' ' + ct + fc + '  ║'
        line7 = bc + fc + '║  '+cc + ct +'   ' + ct + fc + '  ║'
        line8 = bc + fc + '║         ║'
        line9 = bc + fc + '║  '+cc +'     10' +fc + '║'
        line10= bc + fc + '╚═════════╝'
        
    else:
        print("Enter the correct letter here\n")
        
   #cards_to_print = [line1+'\n'+line2+'\n'+line3+'\n'+line4+'\n'+line5+'\n'+line6+'\n'+line7+'\n'+line8+'\n'+line9+'\n'+line10+'\n']
    card_to_print = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]     
    return (card_to_print)
