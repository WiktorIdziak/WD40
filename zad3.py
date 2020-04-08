print("Oryginalny słownik")
towary = {"mleko": "litry", "mentosy": "sztuki", "krówki": "gramy", "parówki": "sztuki"}
print(towary)
print("sztuki")
sztuki = {key: value for key, value in towary.items() if value == "sztuki"}
print(sztuki)