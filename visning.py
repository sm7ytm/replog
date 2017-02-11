#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  visning.py
#  
#  Copyright 2017 Magnus Jönsson <magnus@debian>
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

from conn import config


try:
	
	import pymysql

	cnx = pymysql.connect(**config)
	cnx.autocommit(True)
	cur = cnx.cursor()
except pymysql.err.OperationalError:
	sys.exit("Invalid input: Wrong username/password")



sqlquery = ("SELECT * FROM reparation")


cur.execute(sqlquery)
for maskin_id,felkod,maskintyp,felbeskrivning,koll_komp,bytt_komp,resultat in cur:
	print(maskin_id,felkod,maskintyp,felbeskrivning,koll_komp,bytt_komp,resultat)
	



def main():
	
	return 0

if __name__ == '__main__':
	main()

