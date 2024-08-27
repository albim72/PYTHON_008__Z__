class FileManager(object):
    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager('test.txt','w','utf-8') as f:
    f.write("to jest pierwsza linia tektu\n")

print(f.closed)

w = open('abc.txt','w',encoding='utf-8')
w.write('52354252343524536524\n')

print(w.closed)

with open('xyz.txt','w',encoding='utf-8') as g:
    g.write("afjdshfaflkflkjaslkjakljakla\n")

print(g.closed)

with FileManager('xyz.txt','r','utf-8') as f:
    print(f.read())

print(f.closed)

