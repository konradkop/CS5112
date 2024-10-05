import unittest
import sys
sys.path.append("..")

from problem_3.p3_a import number_of_large_inversions_3a
from problem_3.p3_b import number_of_large_inversions_3b

class TestProblem3(unittest.TestCase):
    ### Public tests for 3a
    def test_correctness_public_a_n4_1(self):
        """Public test # 1 for n = 4"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n4_1.txt", 1)
        self.assertEqual(num_inversions, 2)

    def test_correctness_public_a_n4_2(self):
        """Public test # 2 for n = 4"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n4_1.txt", 2)
        self.assertEqual(num_inversions, 1)

    def test_correctness_public_a_n4_3(self):
        """Public test # 3 for n = 4"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n4_2.txt", 1)
        self.assertEqual(num_inversions, 2)

    def test_correctness_public_a_n4_4(self):
        """Public test # 4 for n = 4"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n4_2.txt", 2)
        self.assertEqual(num_inversions, 0)

    def test_correctness_public_a_n8_1(self):
        """Public test # 1 for n = 8"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n8.txt", 1)
        self.assertEqual(num_inversions, 9)

    def test_correctness_public_a_n8_2(self):
        """Public test # 2 for n = 8"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n8.txt", 2)
        self.assertEqual(num_inversions, 7)

    def test_correctness_public_a_n8_3(self):
        """Public test # 3 for n = 8"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n8.txt", 3)
        self.assertEqual(num_inversions, 5)

    def test_correctness_public_a_n10(self):
        """Test for n = 10"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n10.txt", 1)
        self.assertEqual(num_inversions, 27)

    ### Private tests 3a
    def test_correctness_a_n5(self):
        """Test for n = 5"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n5.txt", 2)
        self.assertEqual(num_inversions, 3)

    def test_correctness_a_n7(self):
        """Test for n = 7"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n7.txt", 1)
        self.assertEqual(num_inversions, 15)

    def test_correctness_a_n10_1(self):
        """Test # 1 for n = 10"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n10_2.txt", 3)
        self.assertEqual(num_inversions, 5)

    def test_correctness_a_n10_2(self):
        """Test # 2 for n = 10"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n10_2.txt", 6)
        self.assertEqual(num_inversions, 1)

    def test_correctness_a_n100_1(self):
        """Test # 1 for n = 100"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n100.txt", 10)
        self.assertEqual(num_inversions, 1609)

    def test_correctness_a_n100_2(self):
        """Test # 2 for n = 100"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n100.txt", 21)
        self.assertEqual(num_inversions, 1169)

    def test_correctness_a_n1000_1(self):
        """Test # 1 for n = 1000"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n1000.txt", 20)
        self.assertEqual(num_inversions, 237752)

    def test_correctness_a_n1000_2(self):
        """Test # 2 for n = 1000"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n1000.txt", 354)
        self.assertEqual(num_inversions, 102140)

    def test_correctness_a_n10000_1(self):
        """Test # 1 for n = 10000"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n10000.txt", 43)
        self.assertEqual(num_inversions, 24925769)

    def test_correctness_a_n10000_2(self):
        """Test # 2 for n = 10000"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n10000.txt", 2971)
        self.assertEqual(num_inversions, 12445458)

    ### Public tests 3b
    def test_correctness_public_b_n4_1(self):
        """Public test # 1 for n = 4"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n4_1.txt", 1)
        self.assertEqual(num_inversions, 2)

    def test_correctness_public_b_n4_2(self):
        """Public test # 2 for n = 4"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n4_1.txt", 2)
        self.assertEqual(num_inversions, 1)

    def test_correctness_public_b_n4_3(self):
        """Public test # 3 for n = 4"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n4_2.txt", 1)
        self.assertEqual(num_inversions, 2)

    def test_correctness_public_b_n4_4(self):
        """Public test # 4 for n = 4"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n4_2.txt", 2)
        self.assertEqual(num_inversions, 0)

    def test_correctness_public_b_n8_1(self):
        """Public test # 1 for n = 8"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n8.txt", 1)
        self.assertEqual(num_inversions, 9)

    def test_correctness_public_b_n8_2(self):
        """Public test # 2 for n = 8"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n8.txt", 2)
        self.assertEqual(num_inversions, 7)

    def test_correctness_public_b_n8_3(self):
        """Public test # 3 for n = 8"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n8.txt", 3)
        self.assertEqual(num_inversions, 5)
    
    def test_correctness_public_b_n10(self):
        """Test for n = 10"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n10.txt", 1)
        self.assertEqual(num_inversions, 27)

    ### Private tests 3b
    def test_correctness_b_n5(self):
        """Test for n = 5"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n5.txt", 2)
        self.assertEqual(num_inversions, 3)

    def test_correctness_b_n7(self):
        """Test for n = 7"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n7.txt", 1)
        self.assertEqual(num_inversions, 15)

    def test_correctness_b_n10_1(self):
        """Test # 1 for n = 10"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n10_2.txt", 2)
        self.assertEqual(num_inversions, 9)

    def test_correctness_b_n10_2(self):
        """Test # 2 for n = 10"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n10_2.txt", 3)
        self.assertEqual(num_inversions, 5)

    def test_correctness_b_n100_1(self):
        """Test # 1 for n = 100"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n100.txt", 1)
        self.assertEqual(num_inversions, 2011)

    def test_correctness_b_n100_2(self):
        """Test # 2 for n = 100"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n100.txt", 45)
        self.assertEqual(num_inversions, 517)

    def test_correctness_b_n1000_1(self):
        """Test # 2 for n = 1000"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n1000.txt", 28)
        self.assertEqual(num_inversions, 233863)

    def test_correctness_b_n1000_2(self):
        """Test # 2 for n = 1000"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n1000.txt", 177)
        self.assertEqual(num_inversions, 166452)

    def test_correctness_b_n10000_1(self):
        """Test # 1 for n = 10000"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n10000.txt", 93)
        self.assertEqual(num_inversions, 24677610)

    def test_correctness_b_n10000_2(self):
        """Test # 2 for n = 10000"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n10000.txt", 1775)
        self.assertEqual(num_inversions, 17025499)

if __name__ == '__main__':
    unittest.main()