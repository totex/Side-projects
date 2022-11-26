
# kilometers to miles
def km_to_mi(km: float) -> float:
    """Converts kilometers to miles."""
    # return km * 0.621371
    return f"{km} kilometer(s) = {km * 0.621371} miles."



# miles to kilometers
def mi_to_km(mi: float) -> float:
    """Converts miles to kilometers."""
    # return mi * 1.609344 
    return f"{mi} mile(s) = {mi * 1.609344} kilometers."


print(km_to_mi(1))
print(mi_to_km(1))

# Define the following unit converters:
# meters to feet
# feet to meters
# kilograms to pounds(lbs)
# pounds(lbs) to kilograms
