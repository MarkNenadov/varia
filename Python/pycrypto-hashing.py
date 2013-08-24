# PyCrypto Hashing - Sample code by Mark Nenadov.
#
# Tested with Python 2.6.5, Python 3.3.2 with PyCrypto 2.6. You can get
# PyCrypto at https://www.dlitz.net/software/pycrypto/
#
# You may use this however you wish, but I retain no responsibility whatsoever for how
# you use it and provide it with no warranty, either.

from Crypto.Hash import MD2, MD4, MD5, RIPEMD, SHA

def getHash( hashType, message ):
   cipher = hashType.new()
   cipher.update( message.encode( 'utf-8' ) )
   return cipher.hexdigest()

msg = "I'm a parrot."

print( "The string '" + msg + "' can be produced into the following hashes:\n" )

print( "MD2: " + getHash( MD2, msg ) )
print( "MD4: " + getHash( MD4, msg ) )
print( "MD5: " + getHash( MD5, msg ) )
print( "RIPEMD: " + getHash( RIPEMD, msg ) )
print( "SHA: " + getHash( SHA, msg ) )


