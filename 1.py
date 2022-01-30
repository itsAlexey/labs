alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
new_alphabet = ""
fold = open('WarAndWorld.txt', 'r')
a = fold.read()
a = a.lower()

print()
print(a)
print()

#print("Введите числовой ключ: ")
#key = int(input())
#print("Введите ключевое слово: ")
#keyword = input()

def encrypt(key, alphabet, keyword):
    new_alphabet = "" + alphabet
    alphabet = list(alphabet)
    for i in range(len(keyword)):
        alphabet[i + key] = keyword[i]
        new_alphabet = new_alphabet.replace(keyword[i], '')
    for i in range(len(alphabet)-len(keyword)):
        alphabet[(i+key+len(keyword))%len(alphabet)] = new_alphabet[0]
        new_alphabet = new_alphabet.replace(new_alphabet[0],'')
    return alphabet

def encryptmsg(msg, alphabet2, alphabet):
    alph_msg = ""
    for i in msg:
        if i not in alphabet2:
            alph_msg += i
        else:
            mesto = alphabet2.find(i)
            alph_msg += alphabet[mesto]
    return alph_msg

def encrypt1(msg, shift=12):
    ret = ""
    for x in msg:
      if x in alphabet2:
         ind2 = alphabet2.index(x)
         ret += alphabet2[(ind2+shift+32)%32]
      else:
         ret += x
    return ret

def searching(msg, alphabet2):
   c = 0
   a = ""
   for k in msg:
     if k.isalpha():
       if c < msg.count(k):
         c = msg.count(k)
         a = k
       elif c == msg.count(k) and k not in a:
         a += k

   print("Самая частая буква", "".join(sorted(a)), " - ", c)
   ret = ""
   for i in alphabet2:
      if (a == i):
         ind = alphabet2.index(i)
   for x in msg:
      if x in alphabet2:
         ind2 = alphabet2.index(x)
         ret += alphabet2[(ind2-ind+32)%32]
      else:
         ret += x
   return ret

print(encrypt1(a))
a=encrypt1(a)
print (searching(a, alphabet2))
#alphabet = encrypt(key, alphabet, keyword)
#print('Измененный алфавит: ', alphabet)
#print()
#print(encryptmsg(a, alphabet2,alphabet))
#a = encryptmsg(a, alphabet2, alphabet)
#print(searching(a,alphabet2))
