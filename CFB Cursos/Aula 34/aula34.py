import os; os.system('cls')

print('Módulos Externos / Funções Em Arquivos Externos')
print()

import canal; from canal import jogador

#É possívem mudar o nome do módulo importado. Para fazer isso, é preciso usar, após o nome do módulo, um "as" e então digitar o novo nome.
#Exemplo: "import canal as cn".

canal.canal_nome()
print(canal.jogador['nome'])
print(jogador['pontos'])

#Como saber tudo o que compõem um módulo:

resultado = dir(canal)
print(resultado)
