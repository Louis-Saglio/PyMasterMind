import random
from pprint import pprint

import Answer
import Pawn


class Combination(list):
    def __init__(self, *args):
        """
        :type args: Pawn.Pawn | str
        """
        super().__init__()
        for pawn in args:
            if isinstance(pawn, str):
                pawn = Pawn.Pawn(pawn)
            self.append(pawn)

    @property
    def range(self):
        return range(len(self))

    def evaluate(self, other):
        assert len(self) == len(other)
        copie = [pawn.couleur for pawn in self]
        answer = Answer.Answer(len(self), '0')
        for i in self.range:
            if self[i].couleur == other[i].couleur:
                answer[i] = '2'
                copie.remove(self[i].couleur)
        for i in self.range:
            if other[i].couleur in copie and answer[i] != '2':
                answer[i] = '1'
                copie.remove(other[i].couleur)
        # print(self, other, answer.digit, sep='\n', end='\n\n')
        return answer

    @staticmethod
    def seed(length, maxi=9):
        return Combination(*[str(random.randint(0, maxi)) for _ in range(length)])


if __name__ == '__main__':
    a = Combination("rouge", "vert", "rouge", "bleu", "noir")
    b = Combination("rouge", "rouge", "noir", "vert", "rouge")
    res = a.evaluate(b)
    assert res == Answer.Answer('21110')
    for _ in range(25):
        maxi = random.randint(3, 7)
        a = Combination.seed(maxi, maxi)
        b = Combination.seed(maxi, maxi)
        res = a.evaluate(b)
