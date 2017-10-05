#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bla.py
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
import unittest

def cesar(texto, casas):
	
	return "".join([chr(ord(letra) + casas %126) for letra in texto]) 
	
def cesar_inverso(texto,casas):	
    return "".join([chr(ord(letra) - casas %126) for letra in texto]) 

class Test(unittest.TestCase):

    def test_cifrar(self):
        self.assertEqual(cesar("texto",3), 'wh{wr')
        self.assertEqual(cesar("texto",4), 'xi|xs')

    def test_desifrar(self):
        self.assertEqual(cesar_inverso("wh{wr",3), 'texto')
        self.assertEqual(cesar_inverso("xi|xs",4), 'texto')
        
    

def main(args):

	return 0

if __name__ == '__main__':
    import sys
    unittest.main()
    sys.exit(main(sys.argv))
