class Answer(list):

    GOOD_COLOR_AND_PLACE = "2"
    GOOD_COLOR_BAD_POSITION = "1"
    BAD_COLOR = "0"

    def __init__(self, args=''):
        super().__init__()
        for answer in args:
            self.append(answer)

    @property
    def range(self):
        return range(len(self))

    # todo: __str__
    def __repr__(self):
        rep = "[ "
        for value in self:
            if value == "2":
                rep += "GOOD_COLOR_AND_PLACE"
            elif value == "1":
                rep += "GOOD_COLOR_BAD_POSITION"
            elif value == "0":
                rep += "BAD_COLOR"
            else:
                rep += str(value)
            rep += " - "
        return rep[:-3] + " ]"

    def merge(self, other, resolve_conflicts=False):
        assert len(self) == len(other)
        response = Answer("55555")
        for self_rep, other_rep, index in zip(self, other, self.range):
            if self_rep in "012" and other_rep in "012" and not resolve_conflicts:
                raise ValueError
            if self_rep in "012":
                response[index] = self_rep
            if other_rep in "012":
                response[index] = other_rep
        return response

    def merge_all(self, *args, resolve_conflicts=False):
        response = self
        for answer in args:
            response = response.merge(answer, resolve_conflicts)
        return response


if __name__ == '__main__':
    a = Answer("01201")
    assert a[2] is Answer.GOOD_COLOR_AND_PLACE
    b = Answer("44444")
    rep = a.merge(b)
    try:
        rep.merge("01210")
        assert False
    except ValueError:
        pass
    rep = rep.merge("22444", True)
    a.merge(Answer("00000"), True)
    b = Answer("41111")
    c = Answer("44222")
    d = Answer("44400")
    e = Answer("44441")
    rep = a.merge_all(b, c, d, e, resolve_conflicts=True)
    print(rep)
