#dictoinary of elements with their properties
elements = {
    "Hydrogen": {"atomic_number": 1, "atomic_mass": 1.008, "symbol": "H"},
    "Helium": {"atomic_number": 2, "atomic_mass": 4.0026, "symbol": "He"},
    "Lithium": {"atomic_number": 3, "atomic_mass": 6.94, "symbol": "Li"},
    "Carbon": {"atomic_number": 6, "atomic_mass": 12.011, "symbol": "C"},
    "Oxygen": {"atomic_number": 8, "atomic_mass": 15.999, "symbol": "O"},
    "Iron": {"atomic_number": 26, "atomic_mass": 55.845, "symbol": "Fe"},
    "Boron": {"atomic_number": 5, "atomic_mass": 10.81, "symbol": "B"},
    "Gold": {"atomic_number": 79, "atomic_mass": 196.966569, "symbol": "Au"},
    "Copper": {"atomic_number": 29, "atomic_mass": 63.546, "symbol": "Cu"},
    "Silver": {"atomic_number": 47, "atomic_mass": 107.8682, "symbol": "Ag"},
    "Platinum": {"atomic_number": 78, "atomic_mass": 195.084, "symbol": "Pt"},
    "Uranium": {"atomic_number": 92, "atomic_mass": 238.02891, "symbol": "U"},
    "Neon": {"atomic_number": 10, "atomic_mass": 20.1797, "symbol": "Ne"},
    "Potassium": {"atomic_number": 19, "atomic_mass": 39.0983, "symbol": "K"},
    "Mercury": {"atomic_number": 80, "atomic_mass": 200.59, "symbol": "Hg"},
    "Sodium": {"atomic_number": 11, "atomic_mass": 22.98976928, "symbol": "Na"},
    "Calcium": {"atomic_number": 20, "atomic_mass": 40.078, "symbol": "Ca"},
    "Magnesium": {"atomic_number": 12, "atomic_mass": 24.305, "symbol": "Mg"},
    "Aluminum": {"atomic_number": 13, "atomic_mass": 26.9815385, "symbol": "Al"},
}
#input
element_name = input("Enter an element name: ").strip().title()
element = elements.get(element_name)
#process input and output
if element is not None:
    print(f"{element_name}:")
    print(f"  Atomic number: {element['atomic_number']}")
    print(f"  Atomic mass: {element['atomic_mass']}")
    print(f"  Symbol: {element['symbol']}")
else:
    print(f"Unknown element: {element_name}")
#dictionary tracking
print(f"Total elements in the database: {len(elements)}")