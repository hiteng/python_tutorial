


"""
Rock beats scissors
Scissors beats paper
Paper beats rock
"""


def rock_pap_sci():
    player_1 = input("Enter your choice Player 1:")
    player_2 = input("Enter your choice Player 2:")

    if player_1 == "Rock" and player_2 == "Scissors":
        print "Player 1 is the winner"
    elif player_1 == "Rock" and player_2 == "Paper":
        print "Player 2 is the winner"
    elif player_1 == "Scissors" and player_2 == "Rock":
        print "Player 2 is the winner"
    elif player_1 == "Scissors" and player_2 == "Paper":
        print "Player 1 is the winner"
    elif player_1 == "Paper" and player_2 == "Rock":
        print "Player_1 is the winner"
    elif player_1 == "Paper" and player_2 == "Scissors":
        print "Player 2 is the winner"
    else:
        print "Enter valid inputs"

def compare():
    player_1 = raw_input("Enter your choice Player 1:")
    player_2 = raw_input("Enter your choice Player 2:")

    #Make it lower case and use strip to eliminate the outer spaces.

    results = {('Paper','Rock') : True,
               ('Paper','Scissors') : False,
               ('Rock','Paper') : False,
               ('Rock','Scissors') : True,
               ('Scissors','Paper') : True,
               ('Scissors','Rock') : False}
    return results[(player_1, player_2)]
# rock_pap_sci()
#
# def rock_paper_sci(list_arg):
#     player_1 = input("Enter your choice Player 1:")
#     player_2 = input("Enter your choice Player 2:")
#
#     for i in list_arg:
#



if __name__ == '__main__':

    list_str = ["Rock", "Scissors", "Paper"]


#rock_paper_sci()

    print compare()