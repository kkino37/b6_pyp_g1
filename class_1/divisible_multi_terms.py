import unittest

"""
def is_divisible_by(x, a_list_of_terms):
    divisible_terms = [term for term in a_list_of_terms if x % term == 0]
    return (a_list_of_terms == divisible_terms)
"""

def is_divisible_by(x, a_list_of_terms):
    # x = 12
    # [2, 3]
    terms = [x % term == 0 for term in a_list_of_terms]
    [True, True]
    
    return all(terms)



def divisible_numbers(a_list, a_list_of_terms):
    # return [x for x in a_list if is_divisible_by(x, a_list_of_terms)]
    return [x for x in a_list if len(a_list_of_terms) == len([y for y in a_list_of_terms if x % y == 0])]
    return [x for x in a_list if all([x % term == 0 for term in a_list_of_terms])]
    return [x for x in a_list if [y for y in a_list_of_terms if x % y == 0] == a_list_of_terms]



class DivisibleNumbersTestCase(unittest.TestCase):
    def test_many_divisible_numbers(self):
        self.assertEqual(set(divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])),
                         set([6, 12]))

    def test_one_divisible_numbers(self):
        self.assertEqual(divisible_numbers([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4]), [12])

    def test_empty_list(self):
        self.assertEqual(divisible_numbers([], [5, 7]),  [])

    def test_both_empty_lists(self):
        self.assertEqual(divisible_numbers([], []),  [])

    def test_no_result(self):
        self.assertEqual(divisible_numbers([2, 4, 8], [5, 7]),  [])
        
unittest.main()

# return [x for x in a_list if all([x % term == 0 for term in a_list_of_terms])]