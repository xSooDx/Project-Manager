
# Copyright (C) 2015 Saurabh Sood
# This file is licensed under the terms of the GNU General Public License
# version 2.  This program is licensed "as is" without any warranty of any
# kind, whether express or implied.

import sqlite3

def DBstart(a):
	DB= sqlite3.connect(a+"Projects.db")