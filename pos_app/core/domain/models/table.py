# Description: Table model.
class Table:
    def __init__(self, id: int, number: int, seats: int, status: str):
        self.id = id
        self.number = number
        self.seats = seats
        self.status = status
        self.subTables = []
        
    def add_sub_table(self, table) -> None:
        self.subTables.append(table)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Table):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"<Table {self.id}>"