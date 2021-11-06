from dataclasses import dataclass


@dataclass
class Cell:
    row_idx: int
    col_idx: int
    value: bool

    def lives(self):
        self.value = True

    def dies(self):
        self.value = False

    def __str__(self):
        return "#" if self.value else "-"

    def __repr__(self):
        return "#" if self.value else "-"
