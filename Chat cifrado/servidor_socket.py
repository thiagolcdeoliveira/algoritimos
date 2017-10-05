#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cliente_socket.py
#  
#  Copyright 2017 Unknown <thiago@thiago-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#serv_sock.py
import socket
from cesar import *
import os
from cliente_socket import *
def servidor_socket(): 
	HOST = ''
	PORT = 57000
	chave =4
	print("aqui")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	print("dpois")
	mensagem_desifrada = []
	mensagem_cifrada = []
	texto=raw_input("Digite o texto:")
	host=raw_input("Digite o Host:")
	for c in texto:
	    mensagem_cifrada.append(cesar(c,chave))
	    enviar_mensagem(texto, host)
	while True:
		s.listen(1)
		 
		conn, addr = s.accept()
		

		while 1:
			 dados = conn.recv(1024)
			 if not dados:
				 break
			 print("DADOS Recebidos: %s" %dados)
			 for i in dados:
				 mensagem_desifrada.append(cesar_inverso(i,4))
			 print("DADOS Recebidos Desifrados: %s" %"".join(arq_desifrado))
			 texto=raw_input("Digite o texto:")
			 host=raw_input("Digite o Host:")
			 for c in texto:
				 mensagem_cifrada.append(cesar(c,chave))
			 enviar_mensagem(texto, host)
 
	#conn.close()
def main(args):
	servidor_socket()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
