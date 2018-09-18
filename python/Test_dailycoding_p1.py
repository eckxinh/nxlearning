from dailycoding_p1 import problem1

def test_p1(liste, k, resu):
    if problem1(liste, k) == resu:
        return True
    return False

print(test_p1([10, 3 , 7 , 5], 17, [[10, 7]]))
print(test_p1([10, 3 , 7 , 5, 7], 17, [[10, 7], [10, 7]]))
