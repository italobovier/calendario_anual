#Importa Biblioteca
import calendar

try:
    #exibe o calendario do ano atual
    ano = int(input('Informe o ano:'))
              
    #Exibe o calenário do ano atual
    for mes in range(1,12):
        print(calendar.month(ano, mes))
except:
    print('Não foi possível exibir o calendário.')