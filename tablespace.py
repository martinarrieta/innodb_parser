import io

PAGE_SIZE=16*1024


SIZE_FIL_PAGE_DATA              = 38

SIZE_PAGE_N_DIR_SLOTS           = 2

PAGE_STRUCTURE={ 
    "FIL_PAGE_SPACE"            :{"offset":0,  "size":4},
    "FIL_PAGE_OFFSET"           :{"offset":4,  "size":4},
    "FIL_PAGE_PREV"             :{"offset":8,  "size":4},
    "FIL_PAGE_NEXT"             :{"offset":12, "size":4},
    "FIL_PAGE_LSN"              :{"offset":16, "size":8},
    "FIL_PAGE_TYPE"             :{"offset":24, "size":2},
    "FIL_PAGE_FILE_FLUSH_LSN"   :{"offset":26, "size":8},
    "FIL_PAGE_ARCH_LOG_NO"      :{"offset":34, "size":4},
}

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

    def getpage(self, offset=0):
        """docstring for getpage"""
        
        return Page(self.getpagesraw(offset=offset, limit=1)[0])
    
    def getpagesraw(self, offset=0, limit=1):
        """docstring for getpageraw"""
        if offset > 0:
            self.file.seek(PAGE_SIZE * number)
        
        values = []
        for x in range(0, limit):
            chunk = self.file.read(PAGE_SIZE)
            if chunk:
               values.append(chunk)
            else:
                break
         
        return values

    def getpages(self, offset=0, limit=10):
        """docstring for getpages"""
        values = self.getpagesraw(offset, limit)
        
        pages = []
        for v in values:
            pages.append(Page(v))
        
        return pages

class Page():
    """docstring for Page"""
    def __init__(self, data):
        self.data = data
        
    def get_header(self):
        """docstring for getheader"""
        return self.data.read(38)
    
    def get_id(self):
        """docstring for get_id"""
        attr = PAGE_STRUCTURE["FIL_PAGE_SPACE"]
        return self.get_attribute(attr)

    def get_nextpageid(self):
        """docstring for get_id"""
        attr = PAGE_STRUCTURE["FIL_PAGE_NEXT"]
        return self.get_attribute(attr)
    
    def get_prevpageid(self):
        """docstring for get_id"""
        attr = PAGE_STRUCTURE["FIL_PAGE_PREV"]
        return self.get_attribute(attr)

        
    def get_type(self):
        
        attr = PAGE_STRUCTURE["FIL_PAGE_TYPE"]
        return self.get_attribute(attr)

    def get_attribute(self, attr):
        """docstring for get_attribute"""
        return data2int(self.data[attr["offset"]:attr["offset"] + attr["size"]])