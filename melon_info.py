"""Print out all the melons in our inventory."""

from melons import melons
# from melons import melon_names, melon_seedlessness, melon_prices

print(melons["Crenshaw"])


def print_melon(melon_name):
    """Print each melon with corresponding attribute information."""

    # have_or_have_not = "have"

    # iterates through each melon name
    for melon, attributes in melons.items():
        print(melon.upper())

        # iterates through attributes of each melon
        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")

        print()

print_melon("melons.py")