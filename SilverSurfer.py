destinations = ["Paris, France", "Shangai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erwin Wilkes", "Shangai, China", ["historical site", "art"]]

def get_destination_index(destination):
  for i in range(len(destinations)):
    if destinations[i] == destination:
      return i

print(str(get_destination_index("Los Angeles, USA")))
