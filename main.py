#!/usr/bin/env python
# -*- coding: utf-8 -*-

from criar_arquivo import *
from cliente_socket import *
def main(args):
	
	if len(args) != 2:
		texto=raw_input("Digite o texto:")
		criar_arquivo_cifrado(texto,4)
		caminho="arquivos/gerados/arquivo_cifrado.txt"
	else:
		caminho=args[1]

	enviar_arquivo(caminho)
	
	return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
