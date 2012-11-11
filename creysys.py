#! /usr/bin/python
# encoding=utf-8
import os,sys
import MySQLdb
import md5
import hashlib
#import codecs

#reload(sys)
#sys.setdefaultencoding('utf-8') 

#print "wo"
#import sys
try:
#    str = 'good morning'
#    key=md5.new()
#    key.update(str)
#    uid =  key.hexdigest()
#    print uid
#    c= uid[0:8]
#    print c
#    print key.hexdigest()
#    print hashlib.md5(str).hexdigest().upper()
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='recommander',charset='utf8',port=3306)
    cur=conn.cursor()
    fp = open('./appchina/app_packagename_all.txt')
    values=[]
#    while True:
    for i in range(2):
        line = fp.readline()
        if line:
	    parts = line.strip().split()
#	    print parts
#	    c = str(parts[1]).decode("utf-8")
#	    b = unicode(parts[1],'gbk')
#	    print b
#	    a = b.encode('utf-8')
#	    print a
#	    print parts
	    print parts[1]
	    key=md5.new()
	    key.update(parts[0])
	    
	    allid = key.hexdigest()	
	    aid = allid[0:8]	
	    parts.insert(0,long(aid,16))	
	    values.append(parts)
	else:
	    break
#    value=[long(c,16),'hi rollen']
    fp.close()
    cur.executemany('insert into application values(%s,%s,%s)',values)


#    count=cur.execute('select * from application')
#    result_set=cur.fetchall()
#    print result_set
    #print 'ID:%d Info %s' % result_set
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
 
##try:
##    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',port=3306)
##    cur=conn.cursor()
##     
##    #cur.execute('create database if not exists saturn')
##    conn.select_db('saturn')
##    #cur.execute('create table users(id int,info varchar(100))')
##     
##    value=[1,'hi rollen']
##    cur.execute('insert into users values(%s,%s)',value)
##     
##    values=[]
##    for i in range(20):
##        values.append((i,'hi rollen'+str(i)))
##         
##    cur.executemany('insert into users values(%s,%s)',values)
## 
##    cur.execute('update users set info="I am rollen" where id=3')
## 
##    conn.commit()
##    cur.close()
##    conn.close()
## 
##except MySQLdb.Error,e:
##     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
