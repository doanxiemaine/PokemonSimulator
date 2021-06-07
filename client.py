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
            pokemon = game.get_pokemon(player)
            data = game.get_data(pokemon)
            while True:
                print(data)
                game = n.send_pokemon(data)
                if game.player1 == {} or game.player2 == {}:
                    continue
                #print(game.player1, game.player2)
                if game.turn == player:
                    if player == 0:
                        print("Your HP:", game.player1['stats']['hp'], "Opponent's HP:", game.player2['stats']['hp'])
                    else:
                        print("Your HP:", game.player2['stats']['hp'], "Opponent's HP:", game.player1['stats']['hp'])
                    for move in pokemon.moves:
                        move_details = pokemon.moves[move]
                        print(move, ':', move_details)
                    player_move = input("Choose your move")
                    if player_move == "quit":
                        break
                    else:
                        game.play(player, pokemon, player_move)
                        if player == 0:
                            #n.send_pokemon(game.player2)
                            data = game.player2
                        else:
                            #n.send_pokemon(game.player1)
                            data = game.player1
                else:
                    print("wait for player...")

            """if game.get_result() != -1:
                if game.get_result == 0 and player == 0:
                    print("You win!")
                elif game.get_result == 0 and player == 1:
                    print("You lose!")
                elif game.get_result == 1 and player == 0:
                    print("You lose!")
                else:
                    print("You win!")
                break"""

main()