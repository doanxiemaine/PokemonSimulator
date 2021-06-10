# PokemonSimulator 0.1.21
=========================

A Net-centric programming course project.

This is an effort of making an online multiplayer Pokémon copy using TCP programming, written in Python 3.
Shoutout to Tech with Tim (@techwithtim) for the amazing guide videos on Network and Socket Programming.

PokeCat Reference: https://github.com/techwithtim/Pictonary-Livestream
PokeBat Reference: https://www.techwithtim.net/tutorials/python-online-game-tutorial/

# Installation
-------------

If you want to try the game, its recommended to download and try the main branch. There might be breaking bugs since the game is not fully complete.

**Windows Source**

To get started, you will need to install library by:
```cmd
git clone https://github.com/doanxiemaine/PokemonSimulator.git
cd PokemonSimulator
python -m pip install -U -r requirements.txt
```

# PokeCat

PokeCat is a world with a simple UI written in pygame, created for players to connect to a world and walk around, farm some Pokémon.
To see how it work, checkout `reference.txt` in server folder.

**Instruction**
---------------

Firstly, you need to start up the server. Run:
```cmd
cd server
python request_handler.py
```
Remember to change your server's IP address in request_handler.py.

After the server is up, start the game with:
```cmd
cd client
python start_game.py
```
Currently, you can only connect to the game under the following names:
* *test1*
* *test2*

Controls
--------

* *Arrow Keys* - Movement
* *=* - Auto play - Player will be moved automatically each second
* *ESC* - Quit the game

# PokeBat

PokeBat is a simple turn-based pokemon battle game by command line.
2 players connect to the server and start the battle.

Currently, only 2 pre-made players with 1 pokemon in their collection. Who connects to the server first will make the first move.
Refer to the pokemon database in pokemon_data.json.

**Instruction**
---------------

Firstly, you need to start up the server. Run:
```cmd
python server.py
```

After the server is up, start the game with:
```cmd
python client.py
```
When there are 2 players connected, the game will start.

Controls
--------

When the game start, player who has the turn will type in the pokemon's move.