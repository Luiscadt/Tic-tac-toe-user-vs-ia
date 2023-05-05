## Tic Tac Toe Game in Python

This is a simple Tic Tac Toe game programmed in Python. The game can be played between a human player and the computer. The game has a 3x3 board, and the first player to get three in a row wins the game.

The game begins by asking the user to select a symbol to play with, either X or O. The computer then takes the other symbol. The player takes the first turn, and then the computer takes its turn.

The board is displayed on the console after each move, and the game continues until either the player or the computer wins, or there is a tie.

The game has been developed using Python and utilizes the following libraries: `time`, `random` and `os`.

To run the game, simply execute the Python script in a Python environment.

Enjoy!

## Juego del Tres en Raya en Python

Este es un pequeño proyecto de Python que implementa el juego del Tres en Raya. Se trata de un juego para dos jugadores, en el que cada uno de ellos va marcando su ficha en el tablero de juego con el objetivo de conseguir colocar tres fichas consecutivas en línea, ya sea de forma horizontal, vertical o diagonal. El juego se desarrolla en una consola de Python.

## Cómo jugar

Antes de comenzar a jugar, el programa le pedirá al usuario que seleccione si quiere jugar con la ficha 'X' o con la ficha 'O'. A continuación, se irán alternando los turnos entre el jugador y el ordenador, hasta que uno de los dos consiga colocar tres fichas consecutivas en línea o hasta que se llene el tablero de juego sin que se haya producido un ganador, lo que se consideraría un empate.

## Funciones del programa

El programa consta de varias funciones que se encargan de gestionar diferentes aspectos del juego:

- `inicio_juego()`: esta función se encarga de pedir al usuario que seleccione la ficha con la que quiere jugar y devuelve las fichas del jugador y del ordenador.
- `tablero()`: esta función dibuja el tablero de juego en la consola de Python.
- `empate(matriz)`: esta función comprueba si se ha producido un empate, es decir, si el tablero está lleno sin que se haya producido un ganador.
- `victoria(matriz)`: esta función comprueba si se ha producido una victoria, es decir, si algún jugador ha conseguido colocar tres fichas consecutivas en línea.
- `movmiento_jugador()`: esta función gestiona el movimiento del jugador.
- `movmiento_ordenador()`: esta función gestiona el movimiento del ordenador.

## Desarrollo del juego

El juego comienza pidiéndole al usuario que seleccione la ficha con la que quiere jugar. A continuación, se irán alternando los turnos entre el jugador y el ordenador. En cada turno, el programa dibujará el tablero de juego y le pedirá al jugador que seleccione una casilla en la que colocar su ficha.

Una vez que el jugador haya realizado su movimiento, el ordenador realizará el suyo, intentando colocar su ficha en una casilla que le permita ganar o que le impida perder en el siguiente turno. Si no existe ninguna casilla que le permita ganar o le impida perder, el ordenador seleccionará una casilla aleatoria.

El juego termina cuando uno de los dos jugadores consigue colocar tres fichas consecutivas en línea o cuando el tablero está lleno sin que se haya producido un ganador. En el primer caso, se mostrará un mensaje de felicitación al jugador ganador y se reiniciará el juego. En el segundo caso, se mostrará un mensaje de empate y se reiniciará el juego.

¡Diviértete jugando al Tres en Raya en Python!
