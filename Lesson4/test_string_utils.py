import pytest
from string_utils import StringUtils 

utils = StringUtils()

"""capitalize"""


def test_capitalize():
    # POSITIVE
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("123") == "123"
    
    # NEGATIVE
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("12345тест") == "12345тест"


"""trim"""

def test_trim():
    # POSITIVE
    assert utils.trim("  skypro") == "skypro"
    assert utils.trim("  hello world  ") == "hello world"  
    assert utils.trim("   SKY") == "SKY"
    
    # NEGATIVE
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim("  SKY  ") == "  SKY  "


"""to_list"""

@pytest.mark.parametrize('string, delimiter, result', [
    # POSITIVE
    ("яблоко,банан,апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    # NEGATIVE
    ("", None, []), 
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),  
])
def test_to_list(string, delimiter, result):
    if delimiter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimiter)
    assert res == result

"""contain"""

pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE
    ("банан", "б", True),
    ("гвоздь", "д", True),
    ("мир", "р", True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("", "", True),  
    ("Москва", "М", True), 
    # NEGATIVE
    ("привет", "з", False),
    ("кот", "№", False),
    ("", "з", False),  
    ("12345", "h", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

"""delete_symbol"""

@pytest.mark.parametrize('string, symbol, result', [
    ("корень", "к", "орень"),                
    ("Женя", "н", "Жея"),                    
    ("Море", "М", "оре"),                    
    ("123", "1", "23"),                      
    ("Красная площадь", " ", "КраснаяПлощадь"),  
    ("ножик", "з", "ножик"),                
    ("", "", ""),                             
    ("", "с", ""),                            
    ("кофе", "", "кофе"),                    
    ("зелень", " ", "зелень"),              
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

"""starts_with"""


@pytest.mark.parametrize('string, symbol, result', [

    ("светофор", "с", True),                
    ("", "", True),                          
    ("Москва", "М", True),                
    ("Film ", "F", True),                   
    ("Мира-Зина", "М", True),              
    ("123", "1", True),                     
    
    ("Ваня", "в", False),                   
    ("мир", "М", False),                    
    ("", "@", False),                       
    ("плащ", "ж", False),                   
    ("зверь", "н", False)                   
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

"""end_with"""

@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE
    ("Мария", "я", True),                 
    ("", "", True),                          
    ("собака", "", True),                   
    ("67", "7", True),                      
    ("ONE-Two", "o", True),                 
    ("Петр1", "1", True),                   
    ("Баобаб", "Б", True),                  

    # NEGATIVE
    ("Тортик", "К", False),                
    ("природа", "л", False),                
    ("тигр", "с", False),                   
    ("дверь", "ь", False),                  
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

"""is_empty"""

@pytest.mark.parametrize('string, result', [
    ("", True),                
    (" ", False),             
    ("  ", False),            

    ("не пусто", False),      
    (" не пусто с пробелом", False),  
    ("345", False),           
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


    """list_to_strin"""


@pytest.mark.parametrize('lst, joiner, result', [ 
     # POSITIVE
    (["s", "o", "5"], ",", "s,o,5"),                  
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),     
    (["первый", "второй"], "-", "первый-второй"),    
    (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),  
    (["в", "у", "з"], "", "вуз"),                    

    # NEGATIVE
    ([], None, ""),                                    
    ([], ",", ""),                                     
    ([], "кот", ""),                                   
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
    





                         
                         
                         
                         
                         
                
                
