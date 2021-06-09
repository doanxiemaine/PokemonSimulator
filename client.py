import pygame
from network import Network
from Combat import Combat


def main():
    run = True
    n = Network()
    player = int(n.getP())
    print("you are player ", player)
    while run:
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break
        if not game.connected():
            print("Waiting for player.....")
        else:
            if game.get_turn() == -1:
                n.send("init")
            if game.get_result() != -1:
                if game.get_result() == 0 and player == 0:
                    print("You win!")
                elif game.get_result() == 0 and player == 1:
                    print("You lose!")
                elif game.get_result() == 1 and player == 0:
                    print("You lose!")
                else:
                    print("You win!")
                break
            if game.turn == player:
                if player == 0:
                    print("Your HP:", game.player1['stats']['hp'], "Opponent's HP:", game.player2['stats']['hp'])
                else:
                    print("Your HP:", game.player2['stats']['hp'], "Opponent's HP:", game.player1['stats']['hp'])
                game.get_move(player)
                player_move = input("Choose your move")
                if player_move == "quit":
                    n.send("surrender")
                else:
                    n.send(player_move)
            else:
                print("wait for player...")



main()