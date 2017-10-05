#!/usr/bin/env python
# -*- coding: utf-8 -*-

from criar_arquivo import *
from cliente_socket import *
def main(args):
	chave=4
	#try:
	arg_caminho=args[1]
	arg_host=args[2]
	#arg_cifrado=arg[3]
	if arg_caminho == "novo":
		texto=raw_input("Digite o texto:")
		criar_arquivo_cifrado(texto,chave)
		#arg_caminho="arquivos/gerados/arquivo_cifrado.txt"
	else:
		cifra_arquivo(arg_caminho,chave)	
	#if arg_cifrado != "s":
	#	cesar(arg_caminho,chave)
	caminho="arquivos/gerados/arquivo_cifrado.txt"
	enviar_arquivo(caminho,arg_host)
	#except:
	#	print("Parametros errados: main.py [caminho do arquivo ou a palavra novo] [host]")
	return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
