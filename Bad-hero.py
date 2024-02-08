import secrets
from random import randint
from os import system
from time import sleep

vida = 180
vidaBoss = 230
curaOver = 1
defesaOver = 2
ataqueOverplayer = 0

bossname = ['um Colossus', 'um troll da internet', 'uma valquiria', 'um mago', 'um elfo', 'O cr7', 'um anão gigante', 'um ladrão', 'A Sentinela do Criador (do jogo)', 'o Ursinho poh (pós academia)', 'Sua sombra', '"você"', 'lampada da pixar', 'Sua Aluscinação', 'O ancara messi', 'um mendigo de bazooka', 'O cachorro caramelo', 'O scorpion' , 'Barack Obama', 'bolsonaro', 'putin', 'semi-deus grego enfraquecido', 'jogador de rpg', 'cthulu', 'herobrine', '???', 'AQSAKJDHAGFGHJDLODEF' ]

bossname = secrets.choice(bossname)
nome = input('Escolha um nome para seu herói: ')
tutorial = input('deseja fazer o tutorial? s/n')

if tutorial == 's':
  print('''
  
┌┬┐┬ ┬┌┬┐┌─┐┬─┐┬┌─┐┬  
 │ │ │ │ │ │├┬┘│├─┤│  
 ┴ └─┘ ┴ └─┘┴└─┴┴ ┴┴─┘

digite 1 para curar
função cura: cura custa 1 rodada e cura entre 1 e 20 de vida

digite 2 para atacar
função ataque: ataque custa 1 rodada e tira entre 5 e 20 de vida

digite 3 para defender
função defesa: defesa custa 1 rodada, e tem 50%  de chance de sucesso (é mais doq imagina) e devolve metade do dano que você tomaria para o adversario e você não toma nenhum dano

digite 4 para master attack
função master attack: master attack demora 5 rodadas para ficar pronto e quando usado tira 20 a 40 de vida do adversario e gasta 1 rodada

nota: se você digitar algum comando inexistente tomara 0.1 de dano e perdera uma rodada
 ''')
  
  input('aperte enter para continuar')
system('clear')
input(f'''
{"-="*40}
 ______     ______     _____        __  __     ______     ______     ______    
/\  == \   /\  __ \   /\  __-.     /\ \_\ \   /\  ___\   /\  == \   /\  __ \   
\ \  __<   \ \  __ \  \ \ \/\ \    \ \  __ \  \ \  __\   \ \  __<   \ \ \/\ \  
 \ \_____\  \ \_\ \_\  \ \____-     \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_/\/_/   \/____/      \/_/\/_/   \/_____/   \/_/ /_/   \/_____/ 

{"-="*40}

Era uma vez um jovem guerreiro chamado {nome}, que viveu em uma aldeia pacífica no topo de uma montanha. {nome} era um habilidoso lutador e um homem corajoso, mas ele se sentia inquieto com a monotonia da vida em sua aldeia.

Um dia, um rumor chegou à aldeia: um chefão malvado estava aterrorizando as aldeias vizinhas e ameaçando destruir todo o reino. {nome}, ansioso por aventura, decidiu que era hora de agir e ofereceu-se para ajudar.

Assim, {nome} começou sua jornada perigosa, percorrendo florestas escuras e montanhas rochosas, enfrentando monstros e superando obstáculos. Ele não tinha certeza se era forte o suficiente para derrotar o chefão, mas sua determinação nunca vacilou.

Finalmente, {nome} chegou ao covil do chefão, era {bossname}. Ele entrou no castelo e, apesar de estar exausto e ferido, enfrentou {bossname} com coragem e...

press enter to continue
''')
system('clear')
dificuldade = input('''escolha a dificuldade
[1] easy
[2] average
[3] Hard
[4] I wanna die
''')
if dificuldade == '1':
  vidaBoss -= 70
  vida += 20
  curaOver -= 1
  defesaOver -= 2
elif dificuldade == '2':
  vidaBoss -= 30
  vida -= 30
elif dificuldade == '3':
  vidaBoss += 20
  vida -= 30
elif dificuldade == '4':
  vidaBoss -= 30
  vida += 20
  curaOver += 29
  defesaOver += 19
ponto = ''
for i in range(5):
  ponto += '.'
  print(ponto)
  sleep(0.5)
  system('clear')
print('sistema pronto')
sleep(1)

while vidaBoss > 0:
  ataqueOverplayer = ataqueOverplayer + 1
  defesa = False
  danoBoss = randint(1, 20)
  system('clear')
  escolha = input(f'''
{bossname}: {vidaBoss:.2f}
{nome}: {vida:.2f}\n
menu de batalha!!! escolha sua ação
[1] Cura
[2] Ataque
[3] defesa
{"[4] master attack" if ataqueOverplayer >= 5 else ""}

Sua ação: ''')
  
  if(escolha == "1"):
    system('clear')
    cura = randint(1, 20)
    vida += cura
    print(f"Você curou {cura} de vida")
    sleep(1)
  elif(escolha == "2"):
    system('clear')
    dano = randint(5, 20)
    vidaBoss -= dano
    print(f"Você deu {dano} de dano")
    sleep(1)
  elif(escolha == "3"):
    if 1 == randint(1, 2):
      defesa = True
    else:
        system('clear')
        print('você falhou em defender')
        sleep(1)
  elif escolha == "4" and ataqueOverplayer >= 5:
    ataqueOverplayer = 0
    dano = randint(20, 40)
    vidaBoss -= dano
    system('clear')
    print('Você carregou o poder e...')
    sleep(1)
    system('clear')
    print('POW!! você deu', dano)
    sleep(1)
  else:
    system('clear')
    print("Função não encontrada, seu imbecil, -0.1 de vida")
    vida -= 0.1
    sleep(1.5)

  system('clear')
  print("Rodada do boss")
  if 3 > randint(0, 10) and defesaOver > 0 and escolha == "2":
    defesaOver -= 1
    vidaBoss = vidaBoss + dano
    vida = vida - 10
    print('boss defendeu perfeitamente e conseguiu te contra atacar com um soco -10 de vida!!!')
  else:
    if(vidaBoss <= 40 and curaOver > 0):
      vidaBoss += 30
      curaOver -= 1
      print("boss riu da sua cara e bebeu uma poção, +30 de vida")
    else:
      if defesa:
        vidaBoss -= danoBoss / 2
        print(f"voce defendeu o ataque e deu {danoBoss /2}")
      else:
        vida -= danoBoss
        print('boss te atacou, você tomou', danoBoss, 'de dano')

  if vida <= 0:
    break
    
  sleep(2.5)

if vida<=0:
  print('''  
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
                                                     ''')
else:
  print('''
:::   :::  ::::::::  :::    :::      :::       ::: ::::::::::: ::::    ::: 
:+:   :+: :+:    :+: :+:    :+:      :+:       :+:     :+:     :+:+:   :+: 
 +:+ +:+  +:+    +:+ +:+    +:+      +:+       +:+     +:+     :+:+:+  +:+ 
  +#++:   +#+    +:+ +#+    +:+      +#+  +:+  +#+     +#+     +#+ +:+ +#+ 
   +#+    +#+    +#+ +#+    +#+      +#+ +#+#+ +#+     +#+     +#+  +#+#+# 
   #+#    #+#    #+# #+#    #+#       #+#+# #+#+#      #+#     #+#   #+#+# 
   ###     ########   ########         ###   ###   ########### ###    #### 
   ''')
