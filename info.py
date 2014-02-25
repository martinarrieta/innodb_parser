import io

import tablespace
"""

with io.open("./ibdata55", mode='rb') as f:
    pagedata = f.read(PAGE_SIZE)
    
    result = {"0":0,"2":0, "3":0, "5":0, "6":0, "7":0, "8":0, "17855":0}
    
    while pagedata:
        p = Page(pagedata)
        pt = p.gettype()
        
        result[str(pt)] = result[str(pt)] + 1
        
        pagedata = f.read(PAGE_SIZE)
        
    print result
"""


t = tablespace.TableSpace(filename="./ibdata55")

print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
print tablespace.Page(t.getpage()).gettype()
