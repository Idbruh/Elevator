# Elevator PAD-1461
_____________________________________________________________________________________________________________________________
Dado 2 elevadores (chamados "left" e "right") em um prédio de 3 andares (numerados de 0 a 2), escreva uma função 'elevador' que aceite 3 argumentos (em ordem):

left - O andar atual do elevador esquerdo
right - O andar atual do elevador direito
call - O andar que chamou um elevador
Ele deve retornar o nome do elevador mais próximo do piso chamado ("left" / "right").

No caso em que os dois elevadores estão igualmente distantes do piso chamado, escolha o elevador à direita.

Você pode assumir que as entradas sempre serão números inteiros válidos entre 0-2.

Exemplos:

elevador (0, 1, 0); // => "esquerda"
elevador (0, 1, 1); // => "direita"
elevador (0, 1, 2); // => "direita"
elevador (0, 0, 0); // => "direita"
elevador (0, 2, 1); // => "direita"
