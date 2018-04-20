from conn_conf import client
import unicodedata

db = client.proyecto_sinf
cpaises = db.paises
	

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


	

todos_paises = cpaises.find({})

for pais in todos_paises: 
	cpaises.update({'_id' : pais['_id']}, {'$set': {'nombrePaisNormalizado': strip_accents( pais['nombrePais'].lower().replace(' ', ''))}  }) 