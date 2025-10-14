from plates import its_valid

def main():
    test_plates()

def test_plates():
    assert its_valid("50") == False
    assert its_valid("cs50") == True
    assert its_valid("cs05") == False
    assert its_valid("Pi3.14") == False
    assert its_valid("H") == False
    assert its_valid("Hello") == True
    assert its_valid("one, two") == False
    assert its_valid("cs50p") == False