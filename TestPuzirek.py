import MyLibrary as ml
import numpy as np
import pytest


class TestPuzirek:

    #подставляем подходящие данные
    def test1(self):
        a = np.array([7,-1,4,13,9])
        b = np.array([13,9,7,4,-1])
        assert (ml.Puzirek(a) == b).all()

    # подставляем неподходящие данные
    def test2(self):
        a = np.array([7, -1, 4, 13, 9])
        b = np.array([9, 7, 13, 4, -1])
        assert (ml.Puzirek(a) == b).all()

    # подставляем данные, которые сломают программу
    def test3(self):
        with pytest.raises(TypeError):
            ml.Puzirek(0)
