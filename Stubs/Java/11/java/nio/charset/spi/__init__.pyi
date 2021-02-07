import java.lang
import java.nio.charset
import java.util


class CharsetProvider(java.lang.Object):
    """
    Java class 'java.nio.charset.spi.CharsetProvider'
    
        Extends:
            java.lang.Object
    
    """
    def charsetForName(self, string: java.lang.String) -> java.nio.charset.Charset: ...
    def charsets(self) -> java.util.Iterator[java.nio.charset.Charset]: ...
