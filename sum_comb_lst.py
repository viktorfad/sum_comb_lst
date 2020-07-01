from itertools import combinations
from errors import *

def search_pairs(array,k):
    pair=[]
    try:
        for el in array:
            if isinstance(el,int)== False:
                raise ArrayTypeError('Ошибка! \nЭлементы массива array должны являться числами типа int.\nВы передали {} - {}'.format(el,type(el)))
        if isinstance(k,int)==False:
            raise kTypeError('Ошибка! \nАргумент k должен являться числом типа int. \nВы передали {}.'.format(type(k)))
        for item in combinations(array, 2): 
            if sum(item)==k:
                if item not in pair and tuple(reversed(item)) not in pair:
                    pair.append(item)
        if pair==[]:
            raise NullValue('Не найдено пар чисел, сумма которых равна числу {}'.format(k))
        return pair
    except TypeError as t:
        print('Ошибка! \nФункция search_pairs(array,k)(где array - массив, k - целое число) получила неверные данные: array - {}, k - {}. \nТакже массив должен состоять из целых чисел!\n{}'.format(type(array),type(k),t))
        return
    except kTypeError as k:
        print(k)
        return
    except NullValue as e:
        print(e)
        return
    except ArrayTypeError as a:
        print(a)
        return
    
    
