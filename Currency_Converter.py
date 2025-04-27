#------import os------
import os   
#------import time-----
from time import sleep  
#----the ascii dollar----
dollar="""
||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
||(100)==================| MONACODE RESERVE NOTE |===============(100)||
||\\$//        ~         '------========--------'                \\$//||
||<< /        /$\              // ____ \\                         \ >>||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
||<<|        \\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
"""
#----clear terminal function----
def clear_terminal():   
    os.system('cls' if os.name=='nt' else 'clear')
#----display exchange rates function----
def display_exchange_rates():   
    print('Welcom to "Mona Daud Currency Converter":')
    for currency in exchange_rates:
        print(f'{currency}: {exchange_rates[currency]}')

#----exchange rates dict----
exchange_rates={                     
    '':dollar,
    'USD':1.0,
    'KSA':3.70,
    'EUR':0.85,
    'RMB':6.5,
}                 
#-----the main exchange function-----
def exchange():   
    clear_terminal()
    display_exchange_rates()
    from_currency=input('\nChoose a currency to convert from: ').upper()
    while True:
        amount=float(input('Enter the amount: '))
        if input(f'\nyou entered {amount} {from_currency}. Confirm? (Y/N) ').upper()=='Y':
            sleep(1)
            break
    clear_terminal()
    display_exchange_rates()
    convert_to_currency=input('\nChoose a currency to convert to: ').upper()
    sleep(1)
    print('Analyzing your request... Please wait.')
    sleep(2)
    print(f'Checking for {convert_to_currency}’s best rates available.....Please wait')
    sleep(2)
    print(f'Getting a discount price for {from_currency}.....Please wait')
    sleep(2)
    if from_currency not in exchange_rates or convert_to_currency not in exchange_rates:
        print('invalid currency')
        sleep(3)
        
    clear_terminal()
    new_rate=exchange_rates[convert_to_currency]/exchange_rates[from_currency]
    print(f'Preparing the deal from {from_currency} to {convert_to_currency}....Please wait')
    sleep(2)
    print(f'Exchange Rate: 1 {from_currency} = {round(new_rate,2)} {convert_to_currency}')
    sleep(2)
    print(f"\n{amount} {from_currency} is equal to {round(new_rate*amount,2)} {convert_to_currency}")

    if input("Do you accept this transaction? (Y/N): ").upper()=='Y':
        clear_terminal()
        print('Currency converted successfully')
        
    else:
        print('Transaction Canceled.')
    if input('Do you want to perfrom another conversion? (Y/N): ').upper()=='Y':
        exchange()
    else:
        print('Thank you for useing\n"Mona Daud Currency Converter"')
exchange()