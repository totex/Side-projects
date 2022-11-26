# converts kilometers to miles
# km * 0.621
def km_to_mi(km: float | int) -> float | int:
    return km * 0.621371


# converts miles to kilometers
# mi * 1.609
def mi_to_km(mi: float | int) -> float | int:
    return mi * 1.609


print(km_to_mi(10))
print(mi_to_km(10))
