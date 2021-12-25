print('Função Lambda Ou Função Anônima')
print()

import os; os.system('cls')

#A "Função Lambda" (ou "Função Anônima") é uma função simples que não pode ter mais de uma expressão.

#Estrutura da "Função Lambda ('Função Anônima')":

#"lambda argumento (s): expressão".

#Exemplos práticos:

soma = lambda a, b: a + b
resultado = soma(2, 5)
print(f'O resultado da soma é: {resultado}.') #Ou: "print(soma(2, 5))".

multiplicar = lambda a, b, c: (a + b) * c
print(f'\nO resultado da soma entre os dois primeiros valores vezes o terceiro é igual a: {multiplicar(2, 5, 3)}.')

#Outra maneira de declara uma Função Lambda (sem associá-la a uma variável):

print(f'\nO resultado dessa expressão é: {(lambda a, b: a + b)(5, 6)}.')

#Mais um exemplo:

#O valor "x", aqui, corresponderá a 2 (valor passado para a variável "r" como 1ª argumento);
#O valor 2 será operado pela função "function" (2ª argumento da 1ª função);
#O resultado de "function" será: 2 * 2 (resultado == 4).
#Após o fim da operação da função "function", o resultado será o seguinte:
#O primeiro valor passado para a função (2) mais o segundo valor (4) [que será obtido após o término da operação da segunda função].

r = lambda x, function: x + function(x)
res = r(2, lambda x: x * x)
print(f'\nO resultado dessa expressão é: {res}.')
#Essa linha tmabém poderia ser escrita assim: "print(f'\nO resultado dessa função é: {r(2, lambda x: x * x)}.')".

res = r(2, lambda x: x + x)
print(f'\nO resultado dessa expressão é: {res}.')
#Agora foram somados os valores 2 e o valor de "x" resultante de primeira função lambda.
#Resultado final: 6.

res = r(2, lambda x: x + 3)
print(f'\nO resultado dessa expressão é: {res}.')
#Agora foram somados o valores 4 (x) e 3. Resultado final: 7.
