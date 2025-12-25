import msgspec


class UpdateCartRequest(msgspec.Struct, omit_defaults=True):
    key: str
    quantity: int