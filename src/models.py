import attr

@attr.s
class Athlete:
    id = attr.ib()  # type: int
    username = attr.ib()  # type: str
