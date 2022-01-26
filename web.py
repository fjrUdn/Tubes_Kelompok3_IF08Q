from browser import document, console, alert

input = document['input']
button = document['btn']
output = document['output']
select = document['select']
select2 = document['select2']

def NumOnly(x):      
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = str(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

def formula(x, y, z):
    LingkR = [  lambda a: 3.14 * 2 * a,
                lambda a: 3.14 * (a ** 2)]
    LingkD = [  lambda a: 3.14 * a,
                lambda a: 1 / 4 * 3.14 * (a ** 2)]
    if x == 'keliling lingkaran':
        if y == 'Jari-jari':
            return LingkR[0](z)
        elif y == 'Diameter':
            return LingkD[0](z)
    elif x == 'luas lingkaran':
        if y == 'Jari-jari':
            return LingkR[1](z)
        elif y == 'Diameter':
            return LingkD[1](z)
    else:
        return 0
"""
    match x:
        case 'keliling lingkaran':
            match y:
                case 'Jari-jari':
                    return L[0](z)
                case 'Diameter':
                    return K[0](z)    
        case 'luas lingkaran':
            match y:
                case 'Jari-jari':
                    return L[1](z)
                case 'Diameter':
                    return K[1](z)
        case _:        
            return 0
"""

# def f(x):
#     return {
#         'keliling persegi': 1,
#         'luas persegi': 2,
#     }[x]

def main(ev):
    num = NumOnly(input.value)
    result = formula(select.value, select2.value, num)
    output.textContent = str(result)

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)
input.bind("keypress", keyEnter)
