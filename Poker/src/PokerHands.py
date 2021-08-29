
'''
Phoebe Schulman
Cps 109. Assignment 1. Poker hands.
Oct 12 - Oct 13, 2019
'''

def evaluate(hand):
    ''' 
    Takes in a string representing 5 cards.
    Identifies and returns what kind of poker hand is represented by the 10-character string hand. 
    '''
    flush, matches = False, False # matches means 4 kind, full house, 3 kind, 2 kind (1 pair or 2)
    startPosition = 0 # ranks goes up by even
    ranks = 0 # counts matches of ranks in a sequence # 4 kind means 6 matching, full house means 4 matching, 3 kind means 3 matching, 2 kind means 2 or 1 matching

    #============================ # flush: all 5 suits the same
    if hand[1] == hand[3] == hand[5] == hand[7] == hand[9]: # suits in odd positions #regardless of case
        flush = True
        return 'flush'
    
    #============================# same rank: 4 kind, full house, 3 kind, 2 kind  #nested loops check all 10 groupings of two cards in the hand, counting how many of these groupings have the same rank for both cards
    if flush == False :

        for startPosition in range (startPosition, len(hand)-2, 2): # for-for rank # from startPosition to end of evens in hand. go by 2
            for currentPosition in range (startPosition+2, len(hand)-1, 2): #first card and current card must be dif to start
    
                if hand[startPosition].upper() == hand[currentPosition].upper(): #accepts any case
                    ranks+=1
       
        if ranks <= 6 and ranks >= 1 and ranks != 5: #hand was 4 kind, full house, 3 kind, 2 kind
            matches == True

        # output the kind
        if ranks == 6 : # 4 kind
            return 'four of a kind'
        elif ranks == 4 : # full house
            return 'full house'
        elif ranks == 3 :# 3 kind
            return 'three of a kind'
        elif ranks == 2 or ranks == 1: # 2 kind #2 or 1 pairs
            return 'pair'

    #============================ # high #if not flush or matches
    if matches == False:
        highest, high = '23456789TJQKA', ''

        for char in highest: #for. each char in order of lowest to highest rank
            if char in hand.upper(): #if the char is in the hand, high card = that char #regardless of case
                high = char.upper()

        output = high +' high'
        return output
#end EVALUATE func------------------------------------

def test():
    ''' 
    Tries all 6 types of hands with a string representing 5 cards.
    Prints out the returned output from the EVALUATE function.
    '''
    
    hand = 'Qs7s2s4s5s'
    print(hand, '\n' + evaluate(hand)) #flush
    hand = '7h8hKsTs8s'
    print(hand, '\n' + evaluate(hand)) #pair
    hand = '2h4d2d4s4c'
    print(hand, '\n' + evaluate(hand)) #full house
    hand = 'KsKhKc8sKd'
    print(hand, '\n' + evaluate(hand)) #four of a kind
    hand = '3s9hTh9s9d'
    print(hand, '\n' + evaluate(hand)) #three of a kind
    hand = '2s8hThQs9d'
    print(hand, '\n' + evaluate(hand)) #Q high
#end TEST func------------------------------------

#MAIN------------------------------------------
'''
Uses the TEST function to try given values.
Allows user to input a hand. 
Outputs the hand with the EVALUATE function.
'''
test() # calls function to test hands

hand = ''
while hand != 'quit': #accept input
    hand = input('Enter a valid poker hand or "quit" to exit: ')
    if hand == 'quit': # exit with quit
       break
    
    hand = hand[0].upper() + hand[1].lower() + hand[2].upper() + hand[3].lower() + hand[4].upper() + hand[5].lower() + hand[6].upper() + hand[7].lower() + hand[8].upper() + hand[9].lower()
    print(hand, '\n' + evaluate(hand)) #accepts any case and outputs it in correct format #alternates upper and lower case. ranks = upper, suits = lower
#end program------------------------------------------



