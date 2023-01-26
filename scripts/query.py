class RdvQuery:
    code_postal = None
    distance = None
    personnes = None
    _is_set = False

    def __str__(self):
        if not self._is_set:
            return "RdvQuery not set"
        return f"{self.code_postal} - {self.distance} - {self.personnes}"

    def set_values(self, code_postal, distance, personnes):

        if not code_postal:
            return
        self.code_postal = code_postal

        if not distance:
            distance = 10
        self.distance = distance

        if not personnes:
            personnes = 1
        self.personnes = personnes

        self._is_set = True

    @property
    def is_set(self):
        return self._is_set
