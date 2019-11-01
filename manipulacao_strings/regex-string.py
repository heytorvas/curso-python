#regex de string
def get_string(variavel, inicio, fim):	
    variavel_array_primario = variavel.split(inicio)
    variavel_array_secundario = variavel_array_primario[1].split(fim)
    resultado = variavel_array_secundario[0]
    return resultado

frase = "GitHub brings together the world's largest community of developers to discover, share, and build better software"
frase_filtrada = get_string(frase, 'together', 'to')

print(frase_filtrada)