def cobs_encoded(data_in):
    encode_list = [0]
    len_data = len(data_in)
    zero_pos = 0
    zero_adds = 1

    # copy data to encode_list
    encode_list.extend(data_in)
    encode_list.append(0)

    i = 1
    while i < len(encode_list):
        temp = encode_list[i]
        if temp == 0:
            encode_list[zero_pos] = zero_adds
            zero_pos += zero_adds
            zero_adds = 0
        zero_adds += 1
        if zero_adds >= 0xFF:
            encode_list[zero_pos] = 0xFF
            if i == len_data:
                break

            encode_list.insert(i + 1, 0)
            i += 1
            zero_pos += zero_adds
            zero_adds = 1
        i += 1

    return encode_list

# example data
# data_in = [0x00]
# data_in = [0x00,0x00]
# data_in = [0x00,0x11,0x00]
# data_in = [0x11,0x22,0x00,0x33]
# data_in = [0x11,0x22,0x33,0x44]
# data_in = [0x11,0x00,0x00,0x00]
# data_in = [i for i in range(0x01, 0xFF)]
# data_in = [0xFF,0xFF,0xFF,0x00]
# data_in.append(0xFF)
# data_in.append(0x00)
# data_in.append(0x01)
# print(data_in)

# debug
# encoded_data = cobs_encoded(data_in)
# print("Encoded data:", encoded_data)
