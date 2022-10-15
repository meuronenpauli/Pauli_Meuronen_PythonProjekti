class Treeni:
    nimi = ""
    liikkeet = []

    def __init__(self, n):
        self.nimi = n
        self.liikkeet = []

class Harjoitus:
    nimi = ""
    sarjat = 0
    toistot = 0
    kuormitus = 0

    def __init__(self, n, s, t, k):
        self.nimi = n
        self.sarjat = s
        self.toistot = t
        self.kuormitus = k