#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 00:35:04 2018

@author: ericyang
"""

import mysql.connector
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        passwd = 'yy1412850',
        db = 'mysql',
        port = 3306,
        charset = 'utf8'
    )
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `user`;')
    data = cursor.fetchone()
    print(data)
    
    conn.close()

except mysql.connector.Error as e:
    print('Error:%s' % e)