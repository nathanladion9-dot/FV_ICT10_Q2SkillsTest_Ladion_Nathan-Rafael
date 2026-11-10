from pyscript import display, document

# Define a dictionary of Non-Metal elements with their details

Element = {
    "Hydrogen": ("H", "Hydrogen","1", "1.008"),
    "Helium": ("He", "Helium", "2", "4.0026"),
    "Carbon": ("C", "Carbon", "6", "12.011"),
    "Nitrogen": ("N", "Nitrogen", "7", "14.007"),
    "Oxygen": ("O", "Oxygen", "8", "15.999"),
    "Fluorine": ("F", "Fluorine", "9", "18.998"),
    "Neon": ("Ne", "Neon", "10", "20.180"),
    "Phosphorus": ("P", "Phosphorus", "15", "30.974"),
    "Sulfur": ("S", "Sulfur", "16", "32.06"),
    "Chlorine": ("Cl", "Chlorine", "17", "35.45"),
    "Argon": ("Ar", "Argon", "18", "39.948"),
    "Selenium": ("Se", "Selenium", "34", "78.971"),
    "Bromine": ("Br", "Bromine", "35", "79.904"),
    "Krypton": ("Kr", "Krypton", "36", "83.798"),
    "Iodine": ("I", "Iodine", "53", "126.90"),
    "Xenon": ("Xe", "Xenon", "54", "131"),
    "Radon": ("Rn", "Radon", "86", "222"),
    "Astatine": ("At", "Astatine", "85", "210"),
    "Oganesson": ("Og", "Oganesson", "118", "294")

}


def check(e):

    element = document.getElementById("element").value.strip() # Get the value of the input field and remove leading/trailing whitespace

    result = Element.get(element, (" Sorry, the element you entered is not a Non-Metal element. Please check your spelling and try again.", "", "", "")) # Look up the element in the dictionary, or return a default message if not found

    document.getElementById("Code").innerText = result[0] # Set the inner text of the Code element to the symbol of the element (or the default message)
    document.getElementById("Name").innerText = result[1] # Set the inner text of the Name element to the name of the element (or an empty string if not found)
    document.getElementById("AtomicNumber").innerText = result[2] # Set the inner text of the AtomicNumber element to the atomic number of the element (or an empty string if not found)
    document.getElementById("AtomicMass").innerText = result[3] # Set the inner text of the AtomicMass element to the atomic mass of the element (or an empty string if not found)
