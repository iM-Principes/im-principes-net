from eth_utils import encode_hex, to_bytes, keccak
from rlp import encode

validators = input()

validators_bytes = [to_bytes(hexstr=addr) for addr in validators]

extra_data = b"\x00" * 32 + encode(validators_bytes) + b"\x00" * 65

print("extraData:", encode_hex(extra_data))
