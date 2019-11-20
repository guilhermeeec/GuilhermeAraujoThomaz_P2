def dicionario_data (data):     #A
    ano = int(data[:4])
    mes = int(data[5:7])
    dia = int(data[8:10])
    dicionario = {'ANO':ano, 'MES':mes, 'DIA':dia}

def boolean_ativo (string_ativo):   #B
    if string_ativo[-1] == '/n':
        string_ativo = string_ativo[:-1]
    if string_ativo == 'SIM':
        variavel_booleana = True
    elif string_ativo == 'NAO':
        variavel_booleana = False
    return variavel_booleana

def lista_strings (string):     #C
    lista_palavras = []
    inicio_palavra = 0
    for indice in range (len(string)):
        if string [indice] == ':'
            lista_palavras.append(string[inicio_palavra:indice])
            inicio_palavra = indice + 1
    lista_palavras.append(string[inicio_palavra:])
    return lista_palavras

def listar_arquivo (arquivo):   #D
    arquivo.seek(0)
    lista_linhas = arquivo.readlines()
    return lista_linhas

def main ():    #E
    arquivo = open('cadastro.txt', 'r')
    lista_pacientes = listar_arquivo(arquivo)
    numero_paciente = 0
    dicionario_paciente = {'CPF':0, 'NOME':' ', 'DATA_DE_NASCIMENTO':' ', 'DATA_DO_CADASTRO':' ', 'ATIVO':False}
    lista_dicionarios_pacientes = []
    for paciente in lista_pacientes:
        lista_infos = lista_strings(paciente)
        dicionario_paciente['CPF'] = lista_infos[0]
        dicionario_paciente['NOME'] = lista_infos[1]
        dicionario_paciente['DATA_DE_NASCIMENTO'] = dicionario_datas(lista_infos[2]
        dicionario_paciente['DATA_DO_CADASTRO'] = dicionario_datas(lista_infos[3]
        dicionario_paciente['ATIVO'] = boolean_ativo(lista_infos[4])
        lista_dicionarios_pacientes.append(dicionario_paciente)
        print(lista_dicionarios)
    arquivo.close()
