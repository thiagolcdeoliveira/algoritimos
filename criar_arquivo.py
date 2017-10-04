#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cesar import *

def criar_arquivo_cifrado(text,chave):
	arquivo = open("arquivos/gerados/arquivo_cifrado.txt","w")
	arquivo.write(cesar(text,chave))
	arquivo.close()
	return 0
	
def desifra_arquivo(arquivo_cifrado,chave):
	arquivo_cifrado = open(arquivo_cifrado,"r")
	arquivo_desifrado = open("arquivos/gerados/arquivo_desifrado","w")
	for c in arquivo_cifrado:
		arquivo_desifrado.write(cesar_inverso(c,chave))
	arquivo_cifrado.close()
	arquivo_desifrado.close()
	return 0
	
def main(args):
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
