from colorama import init, Fore, Style
init()

qtd_alunos = 1
notas_alunos = []
questao = 1

while True:
   
    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    respostas = []
    pontos = 0
    

    for i in range(len(gabarito)):
        resposta = input(Style.BRIGHT + f'Informe a resposta para a questao {questao} (A | B | C | D | E): ' + Style.RESET_ALL)

        if resposta == 'A' or resposta == 'B' or resposta == 'C' or resposta == 'D' or resposta == 'E':
            questao += 1
            respostas.append(resposta)
        else:
            print(Fore.RED + Style.BRIGHT + 'Resposta Invalida' + Style.RESET_ALL)
        
    for s in range(len(gabarito)):
        if gabarito[s] == respostas[s]:
            pontos += 1 
    
    novo_aluno = input(Style.BRIGHT + 'Outro aluno vai utilizar o sistema? ')
    if novo_aluno == 'SIM' or novo_aluno == 'sim':
        print(Fore.GREEN + 'Iniciando nova Prova...' + Style.RESET_ALL)
        qtd_alunos += 1
        notas_alunos.append(pontos)
        questao = 1
        pontos = 0
    else:
        print(Fore.RED + Style.BRIGHT + 'Sistema encerrado' + Style.RESET_ALL)
        notas_alunos.append(pontos)
        break

maior_nota = max(notas_alunos)
menor_nota = min(notas_alunos)
total_alunos = qtd_alunos
media_turma = (sum(notas_alunos)) / total_alunos

print(Fore.GREEN + Style.BRIGHT + f'Maior Nota: {maior_nota}\nMenor Nota: {menor_nota}\nTotal de alunos: {total_alunos}\nMedia da turma: {media_turma:.2f}' + Style.RESET_ALL)