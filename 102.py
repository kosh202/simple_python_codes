#pessoas = {'nome': 'Raphael', 'sexo': 'M', 'idade': 18}
#pessoas['peso'] = 70
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.values())
#del pessoas['sexo']
#for k, v in pessoas.items():
    #print(f'{k} = {v}')
brasil = []#lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]["sigla"])