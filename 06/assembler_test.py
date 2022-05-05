import io
import os
import unittest

import assembler

class TestAssembler(unittest.TestCase):
    def test_add(self):
        self.helper_test_file_equality("add/Add.asm")

    def test_maxL(self):
        self.helper_test_file_equality("max/MaxL.asm")

    def test_pongL(self):
        self.helper_test_file_equality("pong/PongL.asm")

    def test_rectL(self):
        self.helper_test_file_equality("rect/RectL.asm")

    def test_max(self):
        self.helper_test_file_equality("max/Max.asm")

    def test_pong(self):
        self.helper_test_file_equality("pong/Pong.asm")

    def test_rect(self):
        self.helper_test_file_equality("rect/Rect.asm")

    def helper_test_file_equality(self, filename: str):
        filenameBase, _ = os.path.splitext(filename)
        if os.path.exists(f"{filenameBase}.hack"): os.remove(f"{filenameBase}.hack")
        assembler.assemble(filename)
        with io.open(f"{filenameBase}.correct.hack") as expcted, io.open(f"{filenameBase}.hack") as actual:
            self.assertListEqual(
                list(expcted),
                list(actual)
            )



if __name__ == "__main__":
    unittest.main()