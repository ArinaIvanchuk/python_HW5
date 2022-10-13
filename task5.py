# 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('file_with_string.txt', 'r') as data:
    my_string = data.read()

def encode_rle(f_string):
    str_encode = ''
    str_code = ''
    count = 1
    i=0
    for i in f_string:
        if  i != str_code:
            if str_code:
                str_encode+=str(count)+str_code
            count = 1
            str_code = i
        else:
          count +=1      
    return str_encode

print(encode_rle(my_string))

with open('fale_with_string2.txt', 'r') as data:
    my_string2 = data.read()

def decode_rle(f_string:str):
    total = ''
    str_decode = ''
    for i in f_string:
        if i.isdigit():
            total += i 
        else:
            str_decode += i * int(total)
            total = ''
    return str_decode

        
print(decode_rle(my_string2))