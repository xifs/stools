#encoding=utf-8

import bsddb
db_file = '/home/db/bsddb/main.db'    
out = []

db = bsddb.db.DB()
db.open(db_file,'c',bsddb.db.DB_UNKNOWN,bsddb.db.DB_RDONLY)
out.append(sorted(db.items(),key=lambda (k,v): (v,k)))
db.close()

#格式化输出
for i in databases:
    print i[0]+":",
print

for i in range(len(out[0])):
    for j in range(len(out)):
        #如果输出内容属于电话号码需要反转
        #根据databases中各位置含义来来判断
        if j in [1,2,3,4,5,6]:
            print out[j][i][0].decode('utf16')[::-1],
        else:
            #非ascii字符使用utf16进行解码
            print out[j][i][0].decode('utf16'),
    print
