# coding: utf-8

import os
import random
import traceback
import base64
import gzip


def gzip_compress_string(raw_string, encoding='utf-8'):
    assert type(raw_string) is str
    if len(raw_string) < 0:
        return ''

    encode_data = raw_string.encode(encoding)
    zipped_data = gzip.compress(encode_data)
    b64_data = base64.b64encode(zipped_data)
    return b64_data.decode(encoding)


def gzip_decompress_string(zipped_string, encoding='utf-8'):
    assert type(zipped_string) is str
    if len(zipped_string) <= 0:
        return ''

    encode_data = zipped_string.encode(encoding)
    b64_data = base64.b64decode(encode_data)
    unzipped_data = gzip.decompress(b64_data)
    clear_string = unzipped_data.decode(encoding)
    return clear_string


def calc_percentage(denominator, molecular):
    d = float(denominator)
    m = float(molecular)
    perc = d / m

    result = 0
    if perc <= 0.0:
        result = int(0)
    elif (perc > 0.0) and (perc < 1.0):
        result = perc * 100.0
        result = int(result)
    else:
        result = int(100)
    return result


def copy_file(source_file_path, target_file_dir, target_file_name):
    try:
        with open(source_file_path, 'rb') as source_file_ptr:
            # trim dir
            target_file_dir = os.path.join(target_file_dir, '')

            if not os.path.exists(target_file_dir):
                os.makedirs(target_file_dir)

            target_file_path = os.path.join(target_file_dir, target_file_name)
            with open(target_file_path, 'wb') as target_file_ptr:
                source_file_size = int(os.path.getsize(source_file_path))
                buff_size = 1024
                while True:
                    buff = source_file_ptr.read(buff_size)
                    if buff:
                        target_file_ptr.write(buff)
                    else:
                        break
        return target_file_path
    except:
        print(traceback.format_exc())
    return ''


def execute_full_path():
    return os.path.dirname(os.path.abspath(__file__))


def gen_rand_str_from_A_to_Z(length):
    enums = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    return __gen_rnd_str(enums, length)


def gen_rand_str_from_A0_to_Z9(length):
    enums = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    return __gen_rnd_str(enums, length)


def gen_rand_str_from_Aa_to_Zz(length):
    enums = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    return __gen_rnd_str(enums, length)


def gen_rand_str_from_Aa0_to_Zz9(length):
    enums = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    return __gen_rnd_str(enums, length)


def gen_rand_str_from_a_to_z(length):
    enums = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    return __gen_rnd_str(enums, length)


def gen_rand_str_from_a0_to_z9(length):
    enums = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    return __gen_rnd_str(enums, length)


def gen_rand_str_from_0_to_9(length):
    enums = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ]
    return __gen_rnd_str(enums, length)


def __gen_rnd_str(enums, length):
    assert type(enums) is list
    assert type(length) is int
    if length <= 0:
        return ''
    elif length >= len(enums):
        length = int(len(enums))
        pass

    rnd_string = ''

    chars = list()
    for i in range(0, length):
        chars.append(random.choice(enums))
        pass
    for c in chars:
        rnd_string += c
        pass
    del chars
    return rnd_string
    pass
