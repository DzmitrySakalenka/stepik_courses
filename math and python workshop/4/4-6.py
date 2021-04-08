import random


def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    zcaesar = ''
    for x in text.upper():
        if x in alphabet:
            zcaesar += alphabet[(alphabet.find(x) + key) % len(alphabet)]
    return zcaesar


def bruteforce(text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for key in range(1, len(alphabet)):
        print(caesar(text, -key, alphabet))


def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    answer = ''
    for i in text.upper():
        if i in alphabet:
            k = int(str(key)[len(answer) % len(str(key))])
            if reverse:
                k *= -1
            answer += alphabet[(alphabet.index(i) +  k) % len(alphabet)]
    return answer


def jarriquez_bruteforce(text, alphabet):
    words = ['ПРЕСТУП', 'АЛМАЗ']

    for k in range(1000, 999999):
        decoder = jarriquez_encryption(text, k, alphabet, reverse=True)
        if all(word in decoder for word in words):
            print(k)
            print(decoder)
            print()


def disc_generator(alphabet):
    alph_list = [] 
    alph_list[:0] = alphabet
    random.shuffle(alph_list)
    return ''.join(alph_list)


def discs_generator(alphabet, n):
    discs = []
    for _ in range(n):
        discs.append(disc_generator(alphabet))
    return discs

'''
def jefferson_encryption(text, discs, step, reverse=False):
    rev = lambda x: 1 if x == False else -1
    answer, n = '', 0
    for i in text.upper():
        if i in discs[n]:
            answer += discs[n][(discs[n].find(i) + (rev(reverse)) * step) % len(discs[0])]
            n = (n + 1) % len(discs)
    return answer
'''
def jefferson_encryption(text, discs, step, reverse=False):
    text = ''.join([i for i in text.upper() if i in discs[0]])
    return ''.join([caesar(text[i],step*(1,-1)[reverse],discs[i % len(discs)]) for i in range(len(text))])


def kidds_encryption(text, reverse=False):
    alphabet = ['ethosnairfdlmbyguvcp', '8;4‡)*56(1†092:3?¶-.']
    answer = ''

    if reverse:
        alphabet.reverse()

    return ''.join([alphabet[1][alphabet[0].index(i)] for i in text.lower() if i in alphabet[0]])


random.seed(42)
print(caesar('Ave, Caesar', 3))
bruteforce('BQQMF')
print(jarriquez_encryption('У СУДЬИ ЖАРРИКЕСА ПРОНИЦАТЕЛЬНЫЙ УМ', 423, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', reverse=False))
jarriquez_bruteforce('ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС', 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
print(disc_generator('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
discs = discs_generator('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 6)
print(jefferson_encryption('Some encripted text', discs, 4))
print(jefferson_encryption('NUXHUEVGQBIJJZNVI', discs, 4, True))
print(kidds_encryption('ethosnairfdlmbyguvcp'))