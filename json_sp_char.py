import json

withSpChars = {
  'K0': 'V0 \$%',
  'K1': 'V1 `~!@#',
  'K2': 'V2 $%^&*()',
  'K3': 'V3 -+=/?//\\,..,',
  "sp:eci@l": "ch@ra.cters",
  "0": "\u0000",
	"1": "\u0001",
	"31": "\u001f"
}

print (json.dumps(withSpChars))