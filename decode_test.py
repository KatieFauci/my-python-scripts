

val = [b'55',
b'Snow Flower feat. Peakboy',
b'December 25, 2020',
b'Scenery (\xed\x92\x8d\xea\xb2\xbd)', 
b'\uc774 \ubc24']


val2 = ['이 밤',
"Love Yourself 結 'Answer'"]


for data in val:
    print(data.decode('utf-8'))


for data in val2:
    s = bytes(data, 'utf-8')
    print(s)
    print(s.decode('utf-8'))


#
#