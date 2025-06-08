lisst = [2,5,8,2,11,32,5,5,1]
lissst = [1,-1,4,-5,12,-10,-3,55]
abcd = ["helppp", "me", "hehehepl","heheh", "memem"]

#beginer

def sum_list(lisst):
    s = 0
    for i in lisst:
        s += i
    return s
print(sum_list(lisst))

def min_list(lisst):
    min_el = min(lisst)
    return min_el
print(min_list(lisst))


#def reversed_list(lisst):
#    lisst.reverse()
#    return lisst
#print(reversed_list(lisst))

def odd_list(lisst):
    odd_lisst = []
    for i in lisst:
        if i%2 == 1:
            odd_lisst.append(i)
    return odd_lisst
print(odd_list(lisst))

def multipl_list(lisst):
    mul_lisst = []
    n = 2
    for i in lisst:
        mul_lisst.append(i*n)
    return mul_lisst
print(multipl_list(lisst))

#easy

#я не впев чи ми можемо використовувати тут прям фільтри, бо не пам'ятаю чи ми їх використовували на практиках, все одно не бийте пж
def filt_list(lisst):
    filt_lisst = []
    x = 10
    for i in lisst:
        if i > x:
            filt_lisst.append(i)
    return filt_lisst
print(filt_list(lisst))

def av_positive(lissst):
    pos_lisst = []
    for i in lissst:
        if i > 0:
            pos_lisst.append(i)
    av_pos = sum(pos_lisst) / len(pos_lisst)
    return av_pos
print(av_positive(lissst))

def filt_max(lisst):
    filt_lisst = []
    x = 10
    for i in lisst:
        if i > x:
            filt_lisst.append(i)
    cnt = len(filt_lisst)
    return cnt
print(filt_max(lisst))

def div_y(lisst):
    filt_lisst = []
    y = 2
    for i in lisst:
        if i%y == 0:
            filt_lisst.append(i)
    sum_l = sum(filt_lisst)
    return sum_l
print(div_y(lisst))

def square_list(lisst):
    sq_lisst = []
    x = 0
    for i in lisst:
        x = i**2
        sq_lisst.append(x)
    return sq_lisst
print(square_list(lisst))

def positive(lissst):
    pos_lisst = []
    for i in lissst:
        if i > 0:
            pos_lisst.append(i)
    return pos_lisst
print(positive(lissst))

#є зручний метод startswith, але щось я переживаю що дуже душно буде перевірятись дз щоб використовували тільки те що вчили на практичних

def pref_check(abcd):
    pref_lisst = []
    pref = "he"
    for i in abcd:
        if i.startswith(pref):
            pref_lisst.append(i)
    return pref_lisst
print(pref_check(abcd))

def first_n_sum(lisst):
    new_lisst = []
    n = 4
    for i in range(n):
        new_lisst.append(lisst[i])
    return new_lisst
print(first_n_sum(lisst))

def is_palindrom(abcd):
    palindroms = []
    for i in abcd:
        if i == i[::-1]:
            palindroms.append(i)
    return palindroms
print(is_palindrom(abcd))


def divi_test(lisst):
    check_lisst = []
    n = 2
    for i in lisst:
        if i%n == 0:
            check_lisst.append(True)
        else:
            check_lisst.append(False)
    return check_lisst
print(divi_test(lisst))

#medium

def x_not_y(lisst):
    div_x = []
    div_y = []
    x = 2
    y = 4
    for i in lisst:
        if i%x == 0:
            div_x.append(i)
            div_y.append(i)
    for j in div_x:
        if j%y == 0:
            div_y.remove(j)
    return div_y
print(x_not_y(lisst))

big_list = [[2,3,4],[1,2,4],[4,3,2]]
def convert_to_one(big_list):
    small_list = []
    for i in big_list:
        for j in i:
            small_list.append(j)
    return small_list
print(convert_to_one(big_list))

radok = "sHalAlAlALLa"
def radochki(radok):
    RADOK = ""
    for i in radok:
        if i.isupper():
            RADOK += i
    return RADOK
print(radochki(radok))

#def strange_sort(lisst):
#    lisst.sort(reverse=True)
#    return lisst
#print(strange_sort(lisst))
    
def count_longer_x(abcd):
    x = 5
    cnt = 0
    for i in abcd:
         if len(i) > x:
             cnt += 1
    return cnt
print(count_longer_x(abcd))

def multiple_if(lisst):
   x = 3
   y = 5
   new_list = []
   for i in lisst:
      if i > x:
          new_list.append(i*y)
      else:
          new_list.append(i)
   return new_list
print(multiple_if(lisst))
