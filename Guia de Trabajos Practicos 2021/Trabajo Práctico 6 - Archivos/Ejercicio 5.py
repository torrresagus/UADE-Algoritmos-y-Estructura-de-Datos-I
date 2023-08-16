# Se dispone de tres formatos diferentes de archivos de texto en los que se almacenan datos de empleados. Los formatos se indican más abajo. Desarrollar un programa para cada uno de los formatos suministrados, que permitan leer cada uno de
# los archivos y grabar los datos obtenidos en otro archivo de texto con formato CSV.
# Archivo 1: Todos los campos son de longitud fija.
#  1 2 3 4 5 6
# 012345678901234567890123456789012345678901234567890123456789012
# Pérez Juan 20080211 Corrientes 348
# González Ana M 20080115 Juan de Garay 1111 3er piso dto A
# Archivo 2: Los campos están separados por el signo #.
# Pérez Juan#20080211#Corrientes 348
# González Ana M#20080115#Juan de Garay 1111 3er piso Dto A
# Archivo 3: Todos los campos de este archivo están precedidos por un
# número de dos dígitos que indica la longitud del campo a leer.
# 10Pérez Juan082008021114Corrientes 348
# 14González Ana M082008011533Juan de Garay 1111 3er piso dto A
# NOTA: Los espacios que se encuentren al final de las cadenas en el archivo 1 deberán ser eliminados.
