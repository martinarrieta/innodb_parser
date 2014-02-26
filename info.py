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


def print_pageinfo(page):
    """docstring for print_pageinfo"""
    if page.get_type() == tablespace.FIL_PAGE_INDEX:
        print "Page id: %s" % page.get_id()
        print "\tnext: %s " % page.get_nextpageid()
        print "\tprev: %s" % page.get_prevpageid()
    else:
        print "Page id: %s" % page.get_id()
        print "\ttype: %s" % page.get_type()
        
        

print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())
print_pageinfo(t.getpage())

print "With get_pages()"

pages = t.getpages(0, 100)

for p in pages:
    print_pageinfo(p)
    
