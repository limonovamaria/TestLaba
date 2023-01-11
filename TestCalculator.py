import MyLibrary as ml
import numpy as np
import pytest


class TestCalculator:

    #подставляем подходящие данные
    def test1(self):
        a = 7
        b = -3
        d = a/b
        assert (ml.Deistvie(a,"/",b) == d)

    # подставляем неподходящие данные
    def test2(self):
        a = 7
        b = -3
        d = 1
        assert (ml.Deistvie(a, "*", b) == d)

    # подставляем данные, которые сломают программу
    def test3(self):
        with pytest.raises(ZeroDivisionError):
            ml.Deistvie(7,"/",0)
