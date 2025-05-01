import random

def insert_parity_bits(data_bits):
    
    code = [0] * 12
    j = 0
    for i in range(12):
        if i + 1 in [1, 2, 4, 8]:
            continue
        code[i] = int(data_bits[j])
        j += 1

    
    code[0] = code[2] ^ code[4] ^ code[6] ^ code[8] ^ code[10]
    code[1] = code[2] ^ code[5] ^ code[6] ^ code[9] ^ code[10]
    code[3] = code[4] ^ code[5] ^ code[6] ^ code[11]
    code[7] = code[8] ^ code[9] ^ code[10] ^ code[11]
    return code

def introduce_error(codeword, pos=None):
    if pos is None:
        pos = random.randint(1, 12)
    codeword[pos - 1] ^= 1
    return codeword, pos

def calculate_syndrome(codeword):
    s1 = codeword[0] ^ codeword[2] ^ codeword[4] ^ codeword[6] ^ codeword[8] ^ codeword[10]
    s2 = codeword[1] ^ codeword[2] ^ codeword[5] ^ codeword[6] ^ codeword[9] ^ codeword[10]
    s4 = codeword[3] ^ codeword[4] ^ codeword[5] ^ codeword[6] ^ codeword[11]
    s8 = codeword[7] ^ codeword[8] ^ codeword[9] ^ codeword[10] ^ codeword[11]
    syndrome = s8 << 3 | s4 << 2 | s2 << 1 | s1
    return syndrome

def correct_error(codeword, syndrome):
    if syndrome != 0:
        codeword[syndrome - 1] ^= 1
    return codeword

def extract_data(codeword):
    return [codeword[i] for i in range(12) if i + 1 not in [1, 2, 4, 8]]

def to_bit_string(bits):
    return ''.join(str(b) for b in bits)


char = 'P'
ascii_bits = format(ord(char), '08b')
print(f"Вхідні біти (\"{char}\"): {ascii_bits}")


codeword = insert_parity_bits(ascii_bits)
print(f"Кодоване слово: {to_bit_string(codeword)}")


corrupted, error_pos = introduce_error(codeword[:])
print(f"Слово з помилкою (позиція {error_pos}): {to_bit_string(corrupted)}")


syndrome = calculate_syndrome(corrupted)
print(f"Синдром (бінарно): {format(syndrome, '04b')} → позиція помилки: {syndrome}")


corrected = correct_error(corrupted, syndrome)
print(f"Виправлене слово: {to_bit_string(corrected)}")


decoded_bits = extract_data(corrected)
print(f"Відновлені біти: {to_bit_string(decoded_bits)} → символ: {chr(int(to_bit_string(decoded_bits), 2))}")
