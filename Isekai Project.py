print("Você morreu enquanto dormia...")
reencarnar = input("Você deseja reencarnar? (sim/nao) ").strip().lower()

if reencarnar == 'sim':
    print("Você pode escolher uma cidade para reencarnar!")

    # Opções de cidade
    print("1 - Wallenstein (Cidade da Princesa da Espada)")
    print("2 - Vgardia (Terra dos Anões)")
    print("3 - Skypia (Habitat do Povo dos Céus)")
    print("4 - Voldgord (Terra dos Demônios)")

    cidade = input("Escolha em qual cidade você quer reencarnar: ").strip()

    if cidade == '1':
        cidade_nome = 'Wallenstein'
        print("Você escolheu Wallenstein, a Cidade da Princesa da Espada! Um ótimo lugar para espadachins talentosos...")
    elif cidade == '2':
        cidade_nome = 'Vgardia'
        print("Você escolheu Vgardia, a Terra dos Anões! Um lugar para pessoas gentis e com talento em ferraria...")
    elif cidade == '3':
        cidade_nome = 'Skypia'
        print("Você escolheu Skypia, o Habitat do Povo dos Céus!!! Espero que você não tenha medo de altura hahahaha!!!")
    elif cidade == '4':
        cidade_nome = 'Voldgord'
        print("Você escolheu Voldgord, a Terra dos Demônios!! O lugar perfeito para pessoas talentosas e com fome de poder!!")
    else:
        print("Resposta inválida.")
        exit()  # Encerra o jogo se a cidade não for válida

elif reencarnar == 'nao':
    print("Você continuará vagando pelo limbo eterno...")
    exit()  # Encerra o jogo se o jogador escolher não reencarnar

else:
    print("Resposta inválida.")
    exit()  # Encerra o jogo se a resposta for inválida

# História continua apenas se o jogador reencarnar corretamente
print("Você escuta um barulho...")
print("Você abre os olhos e vê que está dentro de uma caverna.")

acao = input("Você deseja andar ou ficar parado? ").strip().lower()

if acao == 'andar':
    print("Você anda por alguns minutos e se depara com um dragão que logo sente a sua presença!!!")
elif acao == 'ficar parado':
    print("Você ficou parado e foi morto por um grupo de goblins das cavernas...")
    exit()
else:
    print("Resposta inválida.")
    exit()

nome = input('O dragão olha pra você e pergunta. Qual seu nome meu jovem??')
print(f' Você ---- Meu nome é {nome} Senhor Dragão!!')
print('Dragão ---- Muito prazer!! Eu me chamo Veldanova!!')
destino, idade = input('Vejo que você usa umas roupas estranhas... de onde voce é e quantos anos você tem?').split()
print(f'Dragão ---- {destino} né? Eu não reconheco esse país... {idade}anos? você é apenas um garoto então hahaha')
desejo = input(f'Dragão ---- Mas me diga, agora que você esta em {cidade_nome}, o que você realmente deseja?')