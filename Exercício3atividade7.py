notas = {}
nome = input("Informe o nome do aluno: ")
media = float(input("Informe a média do aluno : "))
if media >= 7.0:
        situacao = "Aprovado"
elif media >=5.0:
        situacao = "Recuperação"
elif media <5:
        situacao = "Reprovado"
notas[nome] = {
        "Média": media,
        "Situação": situacao
}
print("Dados dos alunos: ") 
for nome, dados in notas.items(): 
        print(f"Aluno: {nome}") 
        print(f"Média: {dados['Média']}") 
        print(f"Situação: {dados['Situação']}") 
        print() 