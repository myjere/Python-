def rlecode(inputfilename, rledone):
    f = open(inputfilename,'rb')
    w = open(rledone,'wb')
    last = None
    count = 0
    t = f.read(1)
    while t:
        if last is None:
            last = t
            count = 1
        else:
            if t == last and count<255:
                count += 1
            else:
                w.write(int.to_bytes(count,1,byteorder = 'big'))
                w.write(last)
                last = t
                count = 1
        t = f.read(1)
    w.write(int.to_bytes(count,1, byteorder = 'big'))
    w.write(last)

def rledecode(inputfilename,outputfilename):
    w = open(outputfilename,'wb')
    f = open(inputfilename,'rb')
    count = f.read(1)
    byte = f.read(1)
    while count and byte:
        w.write(int.from_bytes(count,byteorder='big')*byte)
        count = f.read(1)
        byte = f.read(1)

if __name__ == '__main__':
    #rlecode(input("输入待压缩文件：\n"),input("输入压缩后文件：\n"))
    rledecode(input("输入待解压文件：\n"),input("输入解压后文件：\n"))