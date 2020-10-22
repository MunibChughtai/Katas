class Card:
    def __init__(self, card_no, card_shape):
        self._card_no = card_no
        self._card_shape = card_shape

    def get_card_no(self):
        return self._card_no

    def display_card(self):
        return(f"['{self._card_no}', '{self._card_shape}']")
