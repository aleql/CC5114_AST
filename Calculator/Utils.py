
bin8 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(8)]))
int8 = lambda x: int(x, 2)
# int8 = lambda x : (x[:,:0:-1]<<range(7)).sum(1)*(1-2*x[:,0])
# def int8(bin):
#     bin = list(bin)
#     num = int(''.join(map(str, bin[1:])), 2)
#     if bin[0] == 1:
#         num *= -1
#     return num



#print(int8(bin8(-2**7)))
#print(int8(bin8(2**7)))
# print(bin8(2**7 - 1))
# print(int8(bin8(2**7)))


# range -2**7 ->bin8(2**7 - 1)