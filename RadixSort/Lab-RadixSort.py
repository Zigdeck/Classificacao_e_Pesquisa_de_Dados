# Laboratorio 3
# Nome: Thiago Leonel Rancan Bischoff e Fernando Vieira Utzig
# Turma: B
import time

# Função que retira passa para outro vetor apenas palavras que contém caracteres entre A e Z
def tratar_texto(texto):
    for i in range(0, len(texto)):
        if len(texto[i]) >= 4:
            if texto[i] >= 'A' and texto[i] <= 'Z':
                texto_correto.append(texto[i])


# Radix sort
def radix_sort(array, i):
    if len(array) <= 1:
        return array

    aux_pronta = []
    aux = [[] for x in range(64, 100)]  # tabela ASCII: 64 até 90

    for s in array:
        if i >= len(s):
            aux_pronta.append(s)
        else:
            aux[ord(s[i]) - ord('a')].append(s)

    aux = [radix_sort(b, i + 1) for b in aux]
    return aux_pronta + [b for blist in aux for b in blist]


# Função que conta a quantidade de palavras iguais e escreve em um arquivo
def contar_e_escrever(texto, nome_arq):
    # Se i estiver apontando para a primeira palavra
    for i in range(0, len(texto)):
        if i == 0:
            vet_palavra.append(texto[i])
        # Se i estiver apontando para a ultima palavra
        elif i == len(texto) - 1:
            # .count conta a quantidade de palavras (usada apenas uma vez pois é lenta)
            count = texto.count(texto[i])
            with open(nome_arq, 'a') as arq:
                arq.write(f'{texto[i]} {count}\n')
            vet_palavra.clear()
        else:
            if texto[i] == texto[i + 1]:
                vet_palavra.append(texto[i])
            else:
                with open(nome_arq, 'a') as arq:
                    arq.write(f'{texto[i]} {len(vet_palavra) + 1}\n')
                vet_palavra.clear()


texto_correto = []
vet_palavra = []

# Abre e le o arquivo inteiro.
with open('frankestein_clean.txt', 'r') as f:
    data = f.readline()
    texto = [str(i) for i in data.split()]

# Trata o texto removendo caracteres indesejados
tratar_texto(texto)
# Ordena o texto em ordem alfabética
inicio = time.time()
texto_ordenado = radix_sort(texto_correto, 0)
fim = time.time()
tempo = fim - inicio
print(tempo)
# Conta a quantidade de palavras repetidas e escreve no arquivo de saída
contar_e_escrever(texto_ordenado, 'frankenstein_ordenado.txt')

# ---------------- Mesma coisa para war_and_peace -------------------

texto_correto = []  # Limpa o vetor para usar novamente

with open('war_and_peace_clean.txt', 'r') as f:
    data = f.readline()
    texto = [str(i) for i in data.split()]

tratar_texto(texto)
inicio = time.time()
texto_ordenado = radix_sort(texto_correto, 0)
fim = time.time()
tempo = fim - inicio
print(tempo)
contar_e_escrever(texto_ordenado, 'war_and_peace_ordenado.txt')
