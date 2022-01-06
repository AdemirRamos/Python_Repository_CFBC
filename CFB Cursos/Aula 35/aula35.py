import os; os.system('cls')

print('Trabalhando Com Datas Em Python - Funções Em Arquivos Externos')
print()

import datetime

data = datetime.datetime.now()
print(data) #Data corrente.
print(f'\n{data.day} / {data.month} / {data.year}.')

nascimento = datetime.datetime(1978, 3, 7) #Criando uma data.

print(f'\n{nascimento.strftime("%A")}.') #Modificando a formatação da data. | Dia da semana.

#Legenda:

#a%: dia da semana (resumido);
#A%: dia da semana (completo);
#W%: número do dia da semana - domingo é o primeiro dia da semana e o seu número é o 0 (zero);
#%d: dia do mês;
#%b: mês do ano (resumido);
#%B: mês do ano (completo);
#%m: número do mês;
#%y: ano (dois digitos);
#%Y: ano (quatro digitos);
#%H: hora (dois digitos - de 0 a 23hrs);
#%I: hora (dois digitos - de 0 a 12hrs);
#%p: AM / PM
#%M: minutos;
#%S: segundos;
#%f: microssegundos;
#%j: dia do ano (de 0 até 365);
#W: agora é número do ano?
