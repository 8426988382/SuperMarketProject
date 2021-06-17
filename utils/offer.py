all_offers = []

'''
OFFER:
-> offer_id=None
-> offer_name=None
-> minimum_quantity=None
-> discount_percent=None
'''


class Offer:
    def __init__(self, product_id) -> None:
        self._offers = []
        self.product_id = product_id
        for offer in all_offers:
            if str(self.product_id) == str(offer['product_id']):
                self._offers.append(offer)

    def __repr__(self):
        return f'{self.offers}'

    @property
    def offers(self):
        return self._offers

    def add_offer(self, offer: dict) -> None:
        self._offers.append(offer)
        all_offers.append(offer)

    @classmethod
    def display_all_offers(cls):
        for offer in all_offers:
            print(offer)
