import numpy as np
import math


class QuantumLab:
    """
    Lab implementation for classical components of Shor's Algorithm.
    """

    def __init__(self):
        pass

    # =========================================================================
    # Problem 1: Compute Modular Exponentiation (2 points)
    # =========================================================================
    def modular_exponentiation(self, a, x, N):
        """
        Compute a^x mod N efficiently using built-in pow().
        """
        return pow(a, x, N)

    # =========================================================================
    # Problem 2: Find Period Classically (3 points)
    # =========================================================================
    def find_period(self, a, N):
        """
        Find the smallest positive integer r where a^r ≡ 1 (mod N).
        """
        for r in range(1, N):
            if self.modular_exponentiation(a, r, N) == 1:
                return r
        return None  # in case no period found (shouldn’t happen for valid inputs)

    # =========================================================================
    # Problem 3: Extract Factors from Period (3 points)
    # =========================================================================
    def extract_factors(self, a, N, r):
        """
        Use the period r to compute potential non-trivial factors of N.
        """
        if r % 2 != 0:
            return (None, None)

        x = self.modular_exponentiation(a, r // 2, N)
        p = math.gcd(x - 1, N)
        q = math.gcd(x + 1, N)

        return (p, q)

    # =========================================================================
    # Problem 4: Verify Factorization (2 points)
    # =========================================================================
    def verify_factorization(self, N, p, q):
        """
        Verify that p and q are valid non-trivial factors of N.
        """
        if p is None or q is None:
            return False
        if p * q != N:
            return False
        if not (1 < p < N and 1 < q < N):
            return False
        return True


if __name__ == "__main__":
    lab = QuantumLab()

    # Quick sanity tests
    print("Testing modular_exponentiation:")
    print(lab.modular_exponentiation(2, 4, 15))  # Expected 1

    print("\nTesting find_period:")
    print(lab.find_period(2, 15))  # Expected 4

    print("\nTesting extract_factors:")
    p, q = lab.extract_factors(2, 15, 4)
    print(p, q)  # Expected (3, 5)

    print("\nTesting verify_factorization:")
    print(lab.verify_factorization(15, p, q))  # Expected True
