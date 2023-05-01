qtd_alunos = 1
notas_alunos = []
questao = 1

while True:

    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    respostas = []
    pontos = 0
    

    for i in range(len(gabarito)):
        resposta = input(f'Informe a resposta para a questao {questao} (A | B | C | D | E): ')

        if resposta == 'A' or resposta == 'B' or resposta == 'C' or resposta == 'D' or resposta == 'E':
            questao += 1
            respostas.append(resposta)
        else:
            print('Resposta Invalida')
        
    for s in range(len(gabarito)):
        if gabarito[s] == respostas[s]:
            pontos += 1 
    
    novo_aluno = input('Outro aluno vai utilizar o sistema? ')
    if novo_aluno == 'SIM' or novo_aluno == 'sim':
        print('Iniciando nova Prova...')
        qtd_alunos += 1
        notas_alunos.append(pontos)
        questao = 1
    else:
        print('Sistema encerrado')
        break

maior_nota = max(notas_alunos)
menor_nota = min(notas_alunos)
total_alunos = qtd_alunos
media_turma = sum(notas_alunos) / total_alunos

print(f'Maior Nota: {maior_nota}\nMenor Nota: {menor_nota}\nTotal de alunos: {total_alunos}\nMedia da turma: {media_turma:.2f}')