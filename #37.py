#a=3
#b=5
#print('Os valores sao \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'raphael'
cores={'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretobranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretobranco'], nome, cores['limpa']))