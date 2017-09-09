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

    def evaluate_good_color_bad_position(self, other):
        print(self)
        print(other)
        answer = Answer.Answer("44444")
        copie = [pawn.couleur for pawn, opawn in zip(self, other) if pawn.couleur != opawn.couleur]
        for self_pawn, other_pawn, index in zip(self, other, self.range):
            print("Référence", self_pawn, "comparé", other_pawn, "index", index)
            if self_pawn.couleur == other_pawn.couleur:
                try:
                    copie.remove(self_pawn.couleur)
                except ValueError:
                    pprint(locals())
                    assert False
                continue
            if other_pawn.couleur in copie:
                copie.remove(other_pawn.couleur)
                answer[index] = "1"
            print("copie", copie)
            print("answer", answer)
        print("\n\n\n")
        return answer

    def evaluate_good_color_good_position(self, other):
        answer = Answer.Answer("44444")
        for self_pawn, other_pawn, index in zip(self, other, self.range):
            if self_pawn.couleur == other_pawn.couleur:
                answer[index] = "2"
        return answer

    def evaluate_bad_color(self, other):
        answer = Answer.Answer("44444")
        copie = [pawn.couleur for pawn in self]
        for self_pawn, other_pawn, index in zip(self, other, self.range):
            if other_pawn.couleur in copie:
                copie.remove(other_pawn.couleur)
            else:
                answer[index] = "0"
        return answer

    def evaluate(self, other):
        """
        :type other: Combination
        :rtype: Answer.Answer
        """
        answer = Answer.Answer("44444")  # todo: nombre de pions joués
        answer = answer.merge(self.evaluate_good_color_bad_position(other))
        answer = answer.merge(self.evaluate_good_color_good_position(other))
        answer = answer.merge(self.evaluate_bad_color(other))
        return answer

    @staticmethod
    def seed(length):
        return Combination(*[str(random.randint(0, 9)) for _ in range(length)])


if __name__ == '__main__':
    # a = Combination("rouge", "vert", "rouge", "bleu", "noir")
    # b = Combination("rouge", "rouge", "noir", "vert", "rouge")
    # res = a.evaluate(b)
    # print(res)
    for _ in range(25):
        a = Combination.seed(5)
        b = Combination.seed(5)
        # print(a, b, sep='\n')
        res = a.evaluate(b)
        # print(res)
        # print()
