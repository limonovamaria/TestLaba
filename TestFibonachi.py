import MyLibrary as ml
import numpy as np
import pytest


class TestFibonachi:

    #подставляем подходящие данные
    def test1(self):
        a = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        assert (ml.Fibonachi(10) == a).all()

    # подставляем неподходящие данные
    def test2(self):
        a = np.array([1])
        assert (len(ml.Fibonachi(1)) == len(a))

    # подставляем данные, которые сломают программу
    def test3(self):
        with pytest.raises(TypeError):
            ml.Fibonachi(-1.2)
