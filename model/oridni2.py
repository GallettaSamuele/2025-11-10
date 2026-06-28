from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ordini2:
    order_id : int
    order_date: datetime
    quantity : int

    def __hash__(self):
        return hash(self.order_id)

    def __str__(self):
        return f"{self.order_id}"

    def __eq__(self, other):
        return self.order_id == other.order_id