#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  conn.py
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


import pymysql

conn = pymysql.connect(host='localhost', user='totte', passwd='tummetott', db='replog')

cur = conn.cursor()

cur.execute("SELECT * FROM reparation;")

for r in cur:
    print(r)
cur.close()
conn.close()










def main():
	
	return 0

if __name__ == '__main__':
	main()
