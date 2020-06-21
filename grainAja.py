from collections import deque

bits = []
plaintext = []
pesanasli = []
lfsr = []
nfsr = []
keystream = []
cipher = []
desimal =[]

#key 1
def init():
    for i in range(80):
        nfsr.append(0)
    for i in range(80):
        if(i<64):
            lfsr.append(0)
        else:
            lfsr.append(1)




def decToBin(plain):
    bits.append(str(0 if plain%2 == 0 else 1))
    while plain > 1:
        plain = plain // 2
        bits.append(str(0 if plain%2 == 0 else 1))
    bits.reverse()
    return "".join(bits)

# def encrypt():
#     i = 0
#     while i < len(biint):
#         cipher.append(biint[i] ^ keystream[i])
#         i += 1
    #hasil_cipher = ''.join(str (e) for e in cipher)
    #print hasil_cipher

def grain():
    rnfsr = deque(nfsr)
    rlfsr = deque(lfsr)

    for i in range(240):
        if(i < 160):
            hx = rlfsr[25] ^ rnfsr[63] \
                 ^ (rlfsr[3] and rlfsr[64]) \
                 ^ (rlfsr[46] and rlfsr[64]) \
                 ^ (rlfsr[64] and rnfsr[63]) \
                 ^ (rlfsr[3] and rlfsr[25] and rlfsr[46]) \
                 ^ (rlfsr[3] and rlfsr[46] and rlfsr[64]) \
                 ^ (rlfsr[3] and rlfsr[46] and rnfsr[63]) \
                 ^ (rlfsr[25] and rlfsr[46] and rnfsr[63]) \
                 ^ (rlfsr[46] and rlfsr[64] and rnfsr[63])
            #print hx
            zi = (rnfsr[1] ^ rnfsr[2] ^ rnfsr[4] ^ rnfsr[10] ^ rnfsr[31] ^ rnfsr[43] ^ rnfsr[56]) ^ hx
            #print zi
            # testzi.append(zi)
            # print testzi

            fx_init = rlfsr[62] ^ rlfsr[51] ^ rlfsr[38] ^ rlfsr[23] ^ rlfsr[13] ^ rlfsr[0] ^ zi
            #print fx_init
            gx_init = rlfsr[0] ^ rnfsr[62] ^ rnfsr[60] ^ rnfsr[52] ^ rnfsr[45] ^ rnfsr[37] \
                      ^ rnfsr[33] ^ rnfsr[28] ^ rnfsr[21] ^ rnfsr[14] ^ rnfsr[9] ^ rnfsr[0] \
                      ^ (rnfsr[63] and rnfsr[60]) ^ (rnfsr[37] and rnfsr[33]) ^ (rnfsr[15] and rnfsr[9]) \
                      ^ (rnfsr[60] and rnfsr[52] and rnfsr[45]) ^ (rnfsr[33] and rnfsr[28] and rnfsr[21]) \
                      ^ (rnfsr[63] and rnfsr[45] and rnfsr[28] and rnfsr[9]) ^ (rnfsr[60] and rnfsr[52] and rnfsr[37] and rnfsr[33]) \
                      ^ (rnfsr[63] and rnfsr[60] and rnfsr[21] and rnfsr[15]) ^ (rnfsr[63] and rnfsr[60] and rnfsr[52] and rnfsr[45] and rnfsr[37]) \
                      ^ (rnfsr[33] and rnfsr[28] and rnfsr[21] and rnfsr[15] and rnfsr[9]) ^ (rnfsr[52] and rnfsr[45] and rnfsr[37] and rnfsr[33] and rnfsr[28] and rnfsr[21]) ^ zi
            #print gx_init
            #rlfsr.rotate(-1)
            rlfsr.popleft()
            rlfsr.append(fx_init)
            #print rlfsr
            #rnfsr.rotate(-1)
            rnfsr.popleft()
            rnfsr.append(gx_init)
            #print rnfsr
        else:
            hx = rlfsr[25] ^ rnfsr[63] ^ (rlfsr[3] and rlfsr[64]) ^ (rlfsr[46] and rlfsr[64]) \
                 ^ (rlfsr[64] and rnfsr[63]) ^ (rlfsr[3] and rlfsr[25] and rlfsr[46]) \
                 ^ (rlfsr[3] and rlfsr[46] and rlfsr[64]) ^ (rlfsr[3] and rlfsr[46] and rnfsr[63]) \
                 ^ (rlfsr[25] and rlfsr[46] and rnfsr[63]) ^ (rlfsr[46] and rlfsr[64] and rnfsr[63])
            #print hx

            zi = (rnfsr[1] ^ rnfsr[2] ^ rnfsr[4] ^ rnfsr[10] ^ rnfsr[31] ^ rnfsr[43] ^ rnfsr[56]) ^ hx

            keystream.append(zi)
            #print keystream

            fx = rlfsr[62] ^ rlfsr[51] ^ rlfsr[38] ^ rlfsr[23] ^ rlfsr[13] ^ rlfsr[0]
            #print fx
            gx = rlfsr[0] ^ rnfsr[62] ^ rnfsr[60] ^ rnfsr[52] ^ rnfsr[45] ^ rnfsr[37] \
                ^ rnfsr[33] ^ rnfsr[28] ^ rnfsr[21] ^ rnfsr[14] ^ rnfsr[9] ^ rnfsr[0] \
                ^ (rnfsr[63] and rnfsr[60]) ^ (rnfsr[37] and rnfsr[33]) ^ (rnfsr[15] and rnfsr[9]) \
                ^ (rnfsr[60] and rnfsr[52] and rnfsr[45]) ^ (rnfsr[33] and rnfsr[28] and rnfsr[21]) \
                ^ (rnfsr[63] and rnfsr[45] and rnfsr[28] and rnfsr[9]) ^ (rnfsr[60] and rnfsr[52] and rnfsr[37] and rnfsr[33]) \
                ^ (rnfsr[63] and rnfsr[60] and rnfsr[21] and rnfsr[15]) ^ (rnfsr[63] and rnfsr[60] and rnfsr[52] and rnfsr[45] and rnfsr[37]) \
                ^ (rnfsr[33] and rnfsr[28] and rnfsr[21] and rnfsr[15] and rnfsr[9]) ^ (rnfsr[52] and rnfsr[45] and rnfsr[37] and rnfsr[33] and rnfsr[28] and rnfsr[21])
            #print gx

            #rlfsr.rotate(-1)
            rlfsr.popleft()
            rlfsr.append(fx)
            #print rlfsr
            #rnfsr.rotate(-1)
            rnfsr.popleft()
            rnfsr.append(gx)
            #print rnfsr

#jalan
init()

print ("key  : " + ''.join(str (e) for e in nfsr))
print ("iv   : " + ''.join(str (e) for e in lfsr))

grain()

print ("Keystream    : " + ''.join(str (e) for e in keystream))

#plain = input("Masukkan nilai: ")

#print "Plaint : " + str(plain)

#konversi plain ke biner
#decToBin(plain)
#print bits

#ubah string ke int di list
#biint = [int(i) for i in bits]
#print biint

#panggil method enkripsi
#encrypt()
#print cipher

#ubah list cipher ke string biar bisa di kirim
#pesan = ''.join(str (e) for e in cipher)
#print pesan

#ubah string ke int di list
#a = [int(i) for i in pesan]
#print a

#print "Cipher       : " + ''.join(str (e) for e in cipher)
