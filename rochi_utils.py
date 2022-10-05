from random import randint


def guess_random_int( user_input ):
    computer_number = randint( 1,10 )

    while True:
        try:
            user_number = int( user_input )
        except ValueError:
            print('Only Integers allowed. You input a non-valid value.')

        else:
            if user_number == computer_number:
                return 'The numbers match! Congrats.'

        user_input = input('Try a number: ')
        print('Good luck! :D')


            
        
