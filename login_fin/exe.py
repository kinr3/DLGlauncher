import PyInstaller.__main__
import os
#PyInstaller.__main__.run([
#    '--name=%s' % 'lau-script',
#    '--onefile',
#    os.path.join('lau-script.py'),
#])
#    '--windowed',
#   '--add-binary=%s' % os.path.join('resource', 'path', '*.png'),
#   '--add-data=%s' % os.path.join('resource', 'path', '*.txt'),
#   '--icon=%s' % os.path.join('resource', 'path', 'icon.ico')
#os.system('pyinstaller tk_log_in.py --name Log_in --onefile --noconsole --icon=image\elements\LogoLauncher1.ico')
#time.sleep(99999999999)
import string


def encode(data):
    letters = string.ascii_letters + string.digits + string.punctuation
    encode_str = ''
    data = str(data)
    data = data.replace('u', '-ou-')
    data = data.replace(' ', '#@-@-@#')
    len_ = data.__len__()
    for data_st in range(len_):
        i = -1
        while data[data_st] != letters[i]:
            i += 1
            if data[data_st] == letters[i]:
                encode_str += str(i / 2) + '#'
        data_st += 1
    return encode_str

print(encode("non data"))


def decode(data):
    letters = string.ascii_letters + string.digits + string.punctuation
    decode_str = ''
    data_n = data.split('#')
    data = []
    for data_z in data_n[:-1]:
        data.append(float(data_z))
    i = 0
    for data_z in data:
        ascii_ = data_z * 2
        decode_str += letters[int(ascii_)]
        i += 1
    decode_str = decode_str.replace('-ou-', 'u')
    decode_str = decode_str.split('#@-@-@#')
    return decode_str

print(decode('45.0#32.0#41.5#37.0#41.5#37.0#41.5#32.0#8.5#7.0#7.0#9.5#38.5#32.0#41.5#37.0#41.5#37.0#41.5#32.0#8.5#7.0#7.0#9.5#41.5#8.5#7.0#7.0#9.5#32.0#41.5#37.0#41.5#37.0#41.5#32.0#7.5#0.0#9.0#9.0#38.5#32.0#41.5#37.0#41.5#37.0#41.5#32.0#8.5#7.0#7.0#9.5#37.0#9.5#7.0#7.0#8.5#26.5#27.0#27.5#46.0#'))
