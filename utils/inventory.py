from .offer import Offer


class Inventory:
    def __init__(self,
                 product_id: int,
                 product_name: str,
                 product_quantity: int,
                 price_per_quantity: int,
                 offers: Offer
                 ) -> None:
        self._product_id = product_id
        self._product_name = product_name
        self._product_quantity = product_quantity
        self._price_per_quantity = price_per_quantity
        self._offer = offers

    def __repr__(self):
        return f'DETAILS: {self.product_id}|{self.product_name}|{self.product_quantity}|{self.price_per_quantity}, ' \
               f'OFFERS: {self.offer}'

    @property
    def product_id(self) -> int:
        return self._product_id

    @property
    def product_name(self) -> str:
        return self._product_name

    @property
    def product_quantity(self) -> int:
        return self._product_quantity

    @product_quantity.setter
    def product_quantity(self, quantity) -> None:
        self._product_quantity = quantity

    @property
    def price_per_quantity(self) -> int:
        return self._price_per_quantity

    @property
    def offer(self) -> Offer:
        return self._offer
