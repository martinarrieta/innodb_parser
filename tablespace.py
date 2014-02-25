import io

PAGE_SIZE=16*1024

# This is a checksum of the page
SIZE_FIL_PAGE_SPACE             = 4
SIZE_FIL_PAGE_OFFSET            = 4
SIZE_FIL_PAGE_PREV              = 4
SIZE_FIL_PAGE_NEXT              = 4
SIZE_FIL_PAGE_LSN               = 8
SIZE_FIL_PAGE_TYPE              = 2
SIZE_FIL_PAGE_FILE_FLUSH_LSN    = 8
SIZE_FIL_PAGE_ARCH_LOG_NO       = 4


OFFSET_FIL_PAGE_SPACE           = 0
OFFSET_FIL_PAGE_OFFSET          = OFFSET_FIL_PAGE_SPACE + SIZE_FIL_PAGE_SPACE
OFFSET_FIL_PAGE_PREV            = OFFSET_FIL_PAGE_OFFSET + SIZE_FIL_PAGE_OFFSET 
OFFSET_FIL_PAGE_NEXT            = OFFSET_FIL_PAGE_PREV + SIZE_FIL_PAGE_PREV
OFFSET_FIL_PAGE_LSN             = OFFSET_FIL_PAGE_NEXT + SIZE_FIL_PAGE_NEXT
OFFSET_FIL_PAGE_TYPE            = OFFSET_FIL_PAGE_LSN + SIZE_FIL_PAGE_LSN
OFFSET_FIL_PAGE_FILE_FLUSH_LSN  = OFFSET_FIL_PAGE_TYPE + SIZE_FIL_PAGE_TYPE
OFFSET_FIL_PAGE_ARCH_LOG_NO     = OFFSET_FIL_PAGE_FILE_FLUSH_LSN + SIZE_FIL_PAGE_FILE_FLUSH_LSN

# File page types (values of FIL_PAGE_TYPE) */
#define FIL_PAGE_INDEX          17855   /* B-tree node */
#define FIL_PAGE_UNDO_LOG           2   /* Undo log page */
#define FIL_PAGE_INODE              3   /* Index node */
#define FIL_PAGE_IBUF_FREE_LIST     4   /* Insert buffer free list */

#define FIL_PAGE_TYPE_ALLOCATED 0       /*!< Freshly allocated page */
#define FIL_PAGE_IBUF_BITMAP    5       /*!< Insert buffer bitmap */
#define FIL_PAGE_TYPE_SYS       6       /*!< System page */
#define FIL_PAGE_TYPE_TRX_SYS   7       /*!< Transaction system data */
#define FIL_PAGE_TYPE_FSP_HDR   8       /*!< File space header */
#define FIL_PAGE_TYPE_XDES      9       /*!< Extent descriptor page */
#define FIL_PAGE_TYPE_BLOB      10      /*!< Uncompressed BLOB page */
#define FIL_PAGE_TYPE_ZBLOB     11      /*!< First compressed BLOB page */
#define FIL_PAGE_TYPE_ZBLOB2    12      /*!< Subsequent compressed BLOB page */


FIL_PAGE_INDEX                  = 17855  # B-tree node
FIL_PAGE_UNDO_LOG               = 2      # Undo log page
FIL_PAGE_INODE                  = 3      # Index node
FIL_PAGE_IBUF_FREE_LIST         = 4      # Insert buffer free list

FIL_PAGE_TYPE_ALLOCATED         = 0      # Freshly allocated page
FIL_PAGE_IBUF_BITMAP            = 5      # Insert buffer bitmap
FIL_PAGE_TYPE_SYS               = 6      # System page
FIL_PAGE_TYPE_TRX_SYS           = 7      # Transaction system data
FIL_PAGE_TYPE_FSP_HDR           = 8      # File space header
FIL_PAGE_TYPE_XDES              = 9      # Extent descriptor page
FIL_PAGE_TYPE_BLOB              = 10     # Uncompressed BLOB page
FIL_PAGE_TYPE_ZBLOB             = 11     # First compressed BLOB page
FIL_PAGE_TYPE_ZBLOB2            = 12     # Subsequent compressed BLOB page






def data2hex( dataarray ):
    hexstr = ''.join( [ "%02X" % ord( x ) for x in dataarray ] )
    return hexstr

def data2int( data ):
    """docstring for data2int"""
    return int(data2hex(data),16)

class TableSpace():
    """docstring for TableSpace"""
    def __init__(self, filename):
        self.filename = filename
        
        try:
            self.file = open(filename, 'rb')
        except IOERror:
            print "Error to open the file %s" % self.filename
            
        
        
    def getpage(self, number=0):
        """docstring for getpage"""
        if number > 0:
            self.file.seek(PAGE_SIZE * number)
            
        return self.file.read(PAGE_SIZE)

class Page():
    """docstring for Page"""
    def __init__(self, data):
        self.data = data
        
    def getheader(self):
        """docstring for getheader"""
        return self.data.read(32)
    
    def gettype(self):
        
        return data2int(self.data[OFFSET_FIL_PAGE_TYPE:OFFSET_FIL_PAGE_TYPE + SIZE_FIL_PAGE_TYPE])
        
