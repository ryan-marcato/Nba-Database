def hash(numero):
    numeros_hash = []
    numero_hash1 = numero * 10 * 2
    numero_hash2 = numero * 20 * 4
    numero_hash3 = numero * 47 * 9
    numero_hash4 = numero * 71 * 2
    
    numeros_hash.append(numero_hash1)
    numeros_hash.append(numero_hash2)
    numeros_hash.append(numero_hash3)
    numeros_hash.append(numero_hash4)
    
    hash_formatado = ''.join([str(numeros_hash[i]) + chr((numeros_hash[i] + i) % 26 + 65) for i in range(4)])
    
    return hash_formatado