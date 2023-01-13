"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    missPlaced = each_wagons_id[0:2]
    firstWagon = each_wagons_id[2:3]
    leftWagons = each_wagons_id[3:]

    output = firstWagon + missing_wagons + leftWagons + missPlaced
    return output


# TODO: define the 'add_missing_stops()' function
def add_missing_stops(*args):
  """Add missing stops to route dict.

  :param route: dict - the dict of routing information.
  :param: arbitrary number of stops.
  :return: dict - updated route dictionary.
  """
  stops_list = []

  for v in args[1].values():
      stops_list.append(v)

  args[0]["stops"] = stops_list
  return args[0]


# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    pass


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    pass
