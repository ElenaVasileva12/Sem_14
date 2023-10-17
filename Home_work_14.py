# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

from HW_14_primer_1 import *

import pytest

@pytest.fixture
def data():
    return Company('N')

def test1(data):     #Проверка на наличие
    assert data.login('Евстафий Авдеевич Лихачев','610285')

def test2(data):     #Проверка на количнство символов ID
    with pytest.raises(Exception):
        assert data.login('Евстафий Авдеевич Лихачев','61025')

def test3(data):     #Проверка на возврат из login
    with pytest.raises(Exception):
        assert data.login('Евстафий Авдеевич Лихачев','61025')==('Евстафий Авдеевич Лихачев','61025',5) 

def test4(data):                      
    with pytest.raises(LevelError):
        me=data.login('Никонова Ольга Андреевна','001114') #2
        n.hiring(me,'Ирина Хак','111211',3)  #если 1 то ошибка

if __name__ == '__main__':
    pytest.main(['-v'])


