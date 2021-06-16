offers = []

'''
OFFER:
-> offer_id=None
-> offer_name=None
-> minimum_quantity=None
-> discount_percent=None
'''


class Offer:
    def __init__(self) -> None:
        self._offers = []

    def __repr__(self):
        return f'{self.offers}'

    @property
    def offers(self):
        return self._offers

    def add_offer(self, offer: dict) -> None:
        self._offers.append(offer)
