class Card:
    def __init__(self, number, sign):
        self._number = number
        self._sign = sign
        # assigning value to a card

    def get_value(self):
        if self._number.isdigit():
            return int(self._number)
        elif self._number in ('J', 'Q', 'K'):
            return 10
        else:
            return 11

        #return f"['{self._number}', '{self._sign}']"
