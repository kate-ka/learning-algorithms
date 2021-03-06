
""" Первое решение задачи про анаграмму будет проверять, входит ли каждый из символов первой строки во вторую.
Если все символы будут “отмечены”, то строки являются анаграммами.
“Пометка” символа будет выполняться с помощью замены его на специальное значение Python None.
Однако, поскольку строки в Python иммутабельны, первым шагом обработки станет конвертирование второй строки в список.
Каждый символ из первой может быть сверен с элементами списка и, если будет найден, отмечен оговоренной заменой.
решение является O(n2)

Следующее решение задачи про анаграммы будет использовать тот факт,
что даже если s1 и s2 различны, они будут анаграммами только если состоят из одинаковых символов.
Следовательно, если мы отсортируем каждую строку в алфавитном порядке
от a до z, то в итоге получим одинаковые строки (если, конечно, s1 и s2 - анаграммы).
Это решение показано в ActiveCode 5. Опять же, в Python мы можем использовать встроенный метод sort для списков,
полученных в начале функции конвертацией каждой строки.сортировка обычно имеет O(n2) или O(nlogn)


Последнее решения задачи про анаграммы воспользуется преимуществом того факта,
что любые две анаграммы имеют одинаковое количество букв a, b и так далее.
Для того, чтобы решить, являются ли строки анаграммами,
мы сначала подсчитаем, сколько раз в них встречается каждый символ.
Поскольку возможных букв 26, то мы можем использовать список из 26 счётчиков -
по одному на каждый символ. Каждый раз, когда мы видим конкретную букву,
мы увеличиваем соответствующий ей счётчик на единицу.
В итоге, если оба списка счётчиков идентичны, то строки - анаграммы.Два первых цикла,
используемые для подсчёта символов, базируются на n.
Третий цикл - сравнение двух списков счётчиков -
всегда состоит из 26 итераций (поскольку строки состоят из 26 возможных элементов).
 Складывая всё вместе, получим T(n)=2n+26 шагов, что является O(n).
 Мы нашли алгоритм с линейным порядком величины для решения нашей задачи.

"""


def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('python','typhon'))




def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))


def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution4('apple','pleap'))



