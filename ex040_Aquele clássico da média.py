# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Com notas {nota1} e {nota2}, a média é {media}')
if media <= 50:
    print(f'O aluno está \033[1;31mREPROVADO\033[m')
elif 50.1 <= media <= 60.9:
    print(f'O aluno está em \033[1;33mRECUPERAÇÃO\033[m')
elif media <= 70:
    print(f'O aluno está \033[1;32mAPROVADO\033[m')
print('>> FIM DO PROGRAMA <<')
