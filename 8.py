def digit_detect(string):
    '''

    :param string: Строка с цифрами и математическими операторами (пробелы не важны)
    :return: массив из чисел и математических операторов
    '''
    digital = ""
    result = []
    for el in string:
        if el.isdigit():
            digital += el
        elif not el.isdigit() and digital != "" and el not in ("*","/","-","+","(",")"):
            result.append(int(digital))
            digital = ""
        elif el in ("*","/","-","+","(",")"):
            if el == ")" and digital.isdigit():
                result.append(int(digital))
                digital = ""
            result.append(el)
    if digital.isdigit():
        result.append(int(digital))
    return result

def operation(detdig):
    '''

    :param detdig: массив из чисел и математических операторов ( "*","/","-","+","(",")" )
    :return: результат вычислений
    '''
    while len(detdig) != 1:
        if "(" in detdig:
            newdetdig = []
            i = detdig.index("(")
            for ind in range(len(detdig)):
                if detdig[ind + i + 1] != ")":
                    newdetdig.append(detdig[ind + i + 1])
                else:
                    while detdig[i] != ")":
                        detdig.pop(i)
                    detdig.pop(i)
                    detdig.append(operation(newdetdig)[0])
                    break
        elif "*" in detdig:
            i = detdig.index("*")
            a = detdig.pop(i+1)
            detdig.pop(i)
            b = detdig.pop(i-1)
            detdig.insert(i-1, a * b)
        elif "/" in detdig:
            i = detdig.index("/")
            a = detdig.pop(i+1)
            detdig.pop(i)
            b = detdig.pop(i-1)
            detdig.insert(i-1, b/a)
        elif "+" in detdig:
            i = detdig.index("+")
            a = detdig.pop(i+1)
            detdig.pop(i)
            b = detdig.pop(i-1)
            detdig.insert(i-1, a + b)
        elif "-" in detdig:
            i = detdig.index("-")
            a = detdig.pop(i+1)
            detdig.pop(i)
            b = detdig.pop(i-1)
            detdig.insert(i-1, b-a)
    return detdig



print("2 / 3 - 10 * 11 - (11 - 1) = ", operation(digit_detect("2 / 3 - 10 * 11 - (11 - 1)"))[0])

