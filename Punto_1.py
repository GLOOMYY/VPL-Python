import re


def encontrar_codigos(texto:str) -> int:
    """De un string dado encontramos todos los codigos
    coincidentes.

    Parametros:
        - texto (str): Cadena inicial de donde se
                       buscaran los codigos.
    
    Retorna:
        - int: Con el total de codigos encontrados.
    """
    # Patron para identificar los codigos
    patron = '^REF-[98765]{2}[PQRWXYZ]{4}[_#&%]{1}$'
    # Podemos usar MULTILINE para hacer la coincidencia en cada linea
    codigos = re.findall(patron, texto, re.MULTILINE)

    print('Estos son los codigos encontrados:\n', codigos, sep='')
    return len(codigos)


ejemplo = """
REF-86PQXY%
REF-99ZZWW#
REF-34ABC1&
REF-75QRWP&
REF-123ABC#
REF-68XYQR#
REF-57PWRX%
REF-88WQXY_
REF-XYZ987%
"""
c = encontrar_codigos(ejemplo)
print('Total de codigos encontrados en la cadena:', c)