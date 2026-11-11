# ==================================================
# LENGTH CONVERSIONS
# ==================================================

def km_to_m(value):
    """Convert kilometres to metres."""
    return value * 1000


def m_to_km(value):
    """Convert metres to kilometres."""
    return value / 1000


# ==================================================
# WEIGHT CONVERSIONS
# ==================================================

def kg_to_gm(value):
    """Convert kilograms to grams."""
    return value * 1000


def gm_to_kg(value):
    """Convert grams to kilograms."""
    return value / 1000


# ==================================================
# TEMPERATURE CONVERSIONS
# ==================================================

def celsius_to_fahrenheit(value):
    """Convert Celsius to Fahrenheit."""
    return (value * 9 / 5) + 32


def fahrenheit_to_celsius(value):
    """Convert Fahrenheit to Celsius."""
    return (value - 32) * 5 / 9


def celsius_to_kelvin(value):
    """Convert Celsius to Kelvin."""
    return value + 273.15


def kelvin_to_celsius(value):
    """Convert Kelvin to Celsius."""
    return value - 273.15


def fahrenheit_to_kelvin(value):
    """Convert Fahrenheit to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(value))


def kelvin_to_fahrenheit(value):
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(value))


# ==================================================
# VOLUME CONVERSIONS
# ==================================================

def litre_to_ml(value):
    """Convert litres to millilitres."""
    return value * 1000


def ml_to_litre(value):
    """Convert millilitres to litres."""
    return value / 1000


# ==================================================
# GENERAL CONVERSION ROUTER
# ==================================================

def convert_units(category, value, from_unit, to_unit):
    """
    Convert a value between supported units.

    Supported categories:
    - Length: Kilometers, Meters
    - Weight: Kilograms, Grams
    - Temperature: Celsius, Fahrenheit, Kelvin
    - Volume: Litres, Millilitres
    """

    if from_unit == to_unit:
        return value

    conversions = {
        "Length": {
            ("Kilometers", "Meters"): km_to_m,
            ("Meters", "Kilometers"): m_to_km,
        },
        "Weight": {
            ("Kilograms", "Grams"): kg_to_gm,
            ("Grams", "Kilograms"): gm_to_kg,
        },
        "Temperature": {
            ("Celsius", "Fahrenheit"): celsius_to_fahrenheit,
            ("Fahrenheit", "Celsius"): fahrenheit_to_celsius,
            ("Celsius", "Kelvin"): celsius_to_kelvin,
            ("Kelvin", "Celsius"): kelvin_to_celsius,
            ("Fahrenheit", "Kelvin"): fahrenheit_to_kelvin,
            ("Kelvin", "Fahrenheit"): kelvin_to_fahrenheit,
        },
        "Volume": {
            ("Litres", "Millilitres"): litre_to_ml,
            ("Millilitres", "Litres"): ml_to_litre,
        },
    }

    try:
        converter = conversions[category][(from_unit, to_unit)]
    except KeyError as exc:
        raise ValueError(
            f"Conversion from {from_unit} to {to_unit} "
            f"is not supported for {category}."
        ) from exc

    return converter(value)
