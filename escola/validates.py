import re
from validate_docbr import CPF


def cpf_invalido(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido



def nome_invalido(nome):
 return not nome.isalpha()


def celular_invalido(celular):
   #99 99999-9999
   modelo = '[0-9]{2} 9[0-9]{4}-[0-9]{4}'
   resposta = re.findall(modelo, celular)
   return not resposta
















