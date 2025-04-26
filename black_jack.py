import random
import os
#-----clear terminal function-------
def clear_terminal():
    os.system('cls'if os.name=='nt' else 'clear')
#-----deal card function-----
def deal_card():
    '''return a random number'''
    return random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10,10,])
#-----calculate cards function------
def calculate_cards(cards):
    '''reurn the sum of the list card'''
    #is there a black jack
    if sum(cards)==21 and len(cards)==2:
        return 0
    #----is there A in the cards and the sum over than 21-----
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#------compare function-------
def compare(user_cards,com_cards):
    '''
    the function is comparimg the listes of cards and
    return the resoult
    '''
    
    resoult={
        'user_over':'You lose you are over 21 ',
        'computer_over':'You won computer over 21 ',
        'user_21':'You won with black jack',
        'computer_21':'You lose computer won with black jack',
        'user_win':'You won your score is over than computer ',
        'computer_win':'You lose computer score is over than your',
        'draw':'Draw',

    }
    if user_cards>21:
        return resoult['user_over']
    elif com_cards>21:
        return resoult['computer_over']
    elif user_cards==0:
        return resoult['user_21']
    elif com_cards==0:
        return resoult['user_over']
    elif user_cards>com_cards:
        return resoult['user_win']
    elif user_cards<com_cards:
        return resoult['computer_win']
    else:
        return resoult['draw']
#-----game function------
def game(): 
    clear_terminal()
    user_cards=[deal_card() for _ in range(2)]
    comp_cards=[deal_card() for _ in range(2)]
    game_contiue=True
    #-----user deal_card loop----
    while game_contiue:
        clear_terminal()
        print(f'Your cards are {user_cards} and your score is {sum(user_cards)}')
        print(f'Coputer first card is {comp_cards[0]}')
        user_score=calculate_cards(user_cards)
        computer_score=calculate_cards(comp_cards)
        if user_score==0 or computer_score==0 or user_score>21 or computer_score>21:
            game_contiue=False
        else:
            if input('Get anthor cade? (y/n) ').lower()=='y':
                user_cards.append(deal_card())
            else:
                game_contiue=False
    #-----computer deal_card loop------
    while computer_score!=0 and computer_score<17 and user_score<21 and user_score!=0:
        comp_cards.append(deal_card())
        computer_score=calculate_cards(comp_cards)
    #----display resoult----
    clear_terminal()
    print(f'Your cards are {user_cards} and your score is {sum(user_cards)}')
    print(f'Computer cards are {comp_cards} with score {sum(comp_cards)}')
    print(compare(user_score,computer_score))
#----start the game-----
input('\nWlcome to Blackjack Game\n\nPress Enter to start')
game()