import unittest


def setUpModule():
    print("*** setUpModule ***")


def tearDownModule():
    print("*** tearDownModule ***")


class TestDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("=== setUpClass1 ===")

    @classmethod
    def tearDownClass(cls):
        print("=== tearDownClass1 ===")

    def setUp(self):
        print("--- setUp ---")

    def tearDown(self):
        print("--- tearDown ---")

    def test_b(self):
        print("test_b")

    def test_a(self):
        print("test_a")

    def test_A(self):
        print("test_A")


class TestDemo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("=== setUpClass2 ===")

    @classmethod
    def tearDownClass(cls):
        print("=== tearDownClass2 ===")

    def test_c(self):
        print("test_c")


if __name__ == "__main__":
    unittest.main()

# *** setUpModule ***
# === setUpClass1 ===
# --- setUp ---
# test_A
# --- tearDown ---
# --- setUp ---
# test_a
# --- tearDown ---
# --- setUp ---
# test_b
# --- tearDown ---
# === tearDownClass1 ===
# === setUpClass2 ===
# test_c
# === tearDownClass2 ===
# *** tearDownModule ***