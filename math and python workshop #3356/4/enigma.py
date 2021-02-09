RDICT = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
         2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
         3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N'),
         4: ('AEPLIYWCOXMRFZBSTGJQNH', 'DV', 'KU'),
         5: ('AVOLDRWFIUQ', 'BZKSMNHYC', 'EGTJPX'),
         6: ('AJQDVLEOZWIYTS', 'CGMNHFUX', 'BPRK'),
         7: ('ANOUPFRIMBZTLWKSVEGCJYDHXQ'),
         8: ('AFLSETWUNDHOZVICQ', 'BKJ', 'GXY', 'MPR'),
         'beta': ('ALBEVFCYODJWUGNMQTZSKPR', 'HIX'),
         'gamma': ('AFNIRLBSQWVXGUZDKMTPCOYJHE'),
         }

ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
          2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
          3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
          4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
          5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
          6: 'JPGVOUMFYQBENHZRDKASXLICTW',
          7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT', 
          8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
          'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
          'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
          }

REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
              2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
              3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
              4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
              }

SHIFTS = {1: [17],
          2: [5],
          3: [22],
          4: [10],
          5: [0],
          6: [0, 13],
          7: [0, 13],
          8: [0, 13]
          }


def rotor_alt(symbol, n, reverse=False):
    r_out, r_in = (ROTORS[0], ROTORS[n]) if reverse else (ROTORS[n], ROTORS[0])
    return r_out[r_in.index(symbol)]


def rotor(symbol, n, reverse=False):
    if not n:
        return symbol
    
    for k in RDICT[n]:
        index = k.find(symbol)

        if index != -1:
            return k[(index + (1, -1)[reverse]) % len(k)]


def reflector(symbol, n):
    index = REFLECTORS[0].find(symbol)
    return REFLECTORS[n][index] if index != -1 else None


def shift_symbol(symbol, shift):
    return REFLECTORS[0][(REFLECTORS[0].find(symbol) + shift) % len(REFLECTORS[0])]


def create_switching_list(pairs):
    switching_list = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] 
    pairs = pairs.upper()
    pairs = pairs.split(' ')

    if len(pairs[0]) != 0:
        for pair in pairs:
            idx0 = switching_list[0].index(pair[0])
            idx1 = switching_list[0].index(pair[1])
            
            if (switching_list[0][idx0] == switching_list[1][idx0]) and (switching_list[0][idx1] == switching_list[1][idx1]):
                switching_list[1] = switching_list[1][:idx0] + pair[1] + switching_list[1][idx0 + 1:]
                switching_list[1] = switching_list[1][:idx1] + pair[0] + switching_list[1][idx1 + 1:]
            else:
                return None

    return switching_list


def rotor_rotation():
    return 0


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    switching_list = create_switching_list(pairs)
    if not switching_list:
        return 'Извините, невозможно произвести коммутацию'

    text = ''.join([i for i in text.upper() if i.isalpha()])
    rot_list = [rot3, rot2, rot1]
    shift_list = [shift3, shift2, shift1]
    last_shift = 0
    len_alphabet = len(REFLECTORS[0])
    answer = ''

    for symbol in text:
        symbol = switching_list[1][switching_list[0].index(symbol)]

        rot_step = [0] * len(shift_list)
        rot_step[0] += 1

        if shift_list[0]+1 in SHIFTS[rot_list[0]]:
            rot_step[1] += 1

        for index, rot in enumerate(rot_list[1:-1]):
            if shift_list[index+1] + 1 in SHIFTS[rot]:
                rot_step[index+1] += 1
                rot_step[index+2] += 1

        shift_list = [(x + y)%len_alphabet for x, y in zip(shift_list, rot_step)]
        print(shift_list)

        for i in range(len(rot_list)):
            shift = shift_list[i] - last_shift
            symbol = shift_symbol(symbol, shift)
            last_shift = shift_list[i]
            symbol = rotor(symbol, rot_list[i], False)

        symbol = shift_symbol(symbol, -last_shift)
        last_shift = 0
        symbol = reflector(symbol, ref)

        rot_list.reverse()
        shift_list.reverse()

        for i in range(len(rot_list)):
            shift = shift_list[i] - last_shift
            symbol = shift_symbol(symbol, shift)
            last_shift = shift_list[i]
            symbol = rotor(symbol, rot_list[i], True)

        symbol = shift_symbol(symbol, -last_shift)
        last_shift = 0
        symbol = switching_list[1][switching_list[0].index(symbol)]

        answer += symbol

        rot_list.reverse()
        shift_list.reverse()


    return answer


print(rotor('E', 1, reverse=False))
print(reflector('A', 1))
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, ''))
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC'))
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd'))
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd az'))
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd za'))
print(enigma('AAAAAAA', 1, 1, 0, 2, 0, 3, 0))