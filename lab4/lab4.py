import math


# Алгоритм LZ77
def lz77_compress(data, window_size=10):
    i = 0
    compressed = []

    while i < len(data):
        match = (-1, 0)  
        for j in range(max(0, i - window_size), i):
            length = 0
            while (i + length < len(data) and
                   j + length < i and
                   data[j + length] == data[i + length]):
                length += 1
            if length > match[1]:
                match = (i - j, length)

        if match[1] > 0:
            next_char = data[i + match[1]] if i + match[1] < len(data) else ''
            compressed.append((match[0], match[1], next_char))
            i += match[1] + 1
        else:
            compressed.append((0, 0, data[i]))
            i += 1

    return compressed


# Алгоритм LZW
def lzw_compress(data):
    dictionary = {chr(i): i for i in range(256)}
    current = ""
    result = []
    dict_size = 256

    for char in data:
        combined = current + char
        if combined in dictionary:
            current = combined
        else:
            result.append(dictionary[current])
            dictionary[combined] = dict_size
            dict_size += 1
            current = char

    if current:
        result.append(dictionary[current])

    return result


# Обчислення CR
def compression_ratio(original_text, compressed_bits):
    original_bits = len(original_text) * 8
    return round(original_bits / compressed_bits, 2)


if __name__ == "__main__":
    text = "ABABABCABABABCABABABC"
    print("Вхідний текст:", text)
    print("Довжина (символів):", len(text))
    print("Оригінальний розмір:", len(text) * 8, "біт\n")

    # LZ77
    lz77_result = lz77_compress(text)
    lz77_bits = len(lz77_result) * (4 + 4 + 8)  # offset(4) + length(4) + symbol(8)
    print("Стиснення LZ77:")
    for triple in lz77_result:
        print(triple)
    print("Розмір стисненого (біт):", lz77_bits)
    print("CR (LZ77):", compression_ratio(text, lz77_bits), "\n")

    # LZW
    lzw_result = lzw_compress(text)
    lzw_code_size = math.ceil(math.log2(len(set(text)) + len(lzw_result)))  # оцінка біт на символ
    lzw_bits = len(lzw_result) * lzw_code_size
    print("Стиснення LZW:")
    print(lzw_result)
    print("Розмір стисненого (біт):", lzw_bits)
    print("CR (LZW):", compression_ratio(text, lzw_bits))
