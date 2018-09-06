import random
from draw_cards import get_card

def request_cards(requested_cards):

    # Making a string for each line to print
    line1_to_print =''
    line2_to_print =''
    line3_to_print =''
    line4_to_print =''
    line5_to_print =''
    line6_to_print =''
    line7_to_print =''
    line8_to_print =''
    line9_to_print =''
    line10_to_print=''
    
    card_line_number = 0
    for cards_in_hand in requested_cards:
        card_per_line = get_card(cards_in_hand)
        line1_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line2_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line3_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line4_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line5_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line6_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line7_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line8_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line9_to_print += card_per_line[card_line_number]
        card_line_number += 1
        line10_to_print += card_per_line[card_line_number]
        card_line_number = 0
        
    cards_to_print = line1_to_print+'\n'+line2_to_print+'\n'+line3_to_print+'\n'+line4_to_print+'\n'+line5_to_print+'\n'+line6_to_print+'\n'+line7_to_print+'\n'+line8_to_print+'\n'+line9_to_print+'\n'+line10_to_print+'\n'
    print(cards_to_print)
        
