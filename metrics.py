# Metrics related to the objective function
from items import PAYLOAD_ITEMS


def payload_fraction_score(empty_weight: float, payload_weight: float) -> float:
    """
    Calculates the fraction of the total weight that is payload

    pf_score = min(0.25, payload_frac)
    """
    payload_frac = payload_weight / (empty_weight + payload_weight)
    return min(0.25, payload_frac)


def total_cargo_units(payload_configuration: list[int]) -> int:
    """
    Calculates the total number of cargo units

    Payload configuration goes like [number of ping pong balls, number of golf balls, number of tennis balls]
    """
    # Calculate the total number of cargo units
    total_cargo_units = 0
    for i in range(len(payload_configuration)):
        total_cargo_units += payload_configuration[i] * PAYLOAD_ITEMS[i].points

    return total_cargo_units


def total_payload_mass(payload_configuration: list[int]) -> float:
    """
    Calculates the total mass of the payload

    Payload configuration goes like [number of ping pong balls, number of golf balls, number of tennis balls]
    """
    # Calculate the total mass of the payload
    total_payload_mass = 0
    for i in range(len(payload_configuration)):
        total_payload_mass += payload_configuration[i] * PAYLOAD_ITEMS[i].mass

    return total_payload_mass


def cargo_units_score(payload_configuration: list[int]) -> float:
    """
    Calculates the number of cargo units

    formula is (total cargo units)^0.7
    """
    return total_cargo_units(payload_configuration) ** 0.7


def objective_factor(payload_configuration: list[int], empty_weight: float) -> float:
    """
    Calculates the objective factor for the given payload configuration

    Payload configuration goes like [number of ping pong balls, number of golf balls, number of tennis balls]

    Empty weight is the weight of the empty plane
    """
    pf_score = payload_fraction_score(
        empty_weight, total_payload_mass(payload_configuration)
    )
    cu_score = cargo_units_score(payload_configuration)

    return pf_score * cu_score


def total_volume(payload_configuration: list[int]) -> float:
    """
    Calculates the total volume of the payload

    Payload configuration goes like [number of ping pong balls, number of golf balls, number of tennis balls]
    """
    # Calculate the total volume of the payload
    total_payload_volume = 0
    for i in range(len(payload_configuration)):
        total_payload_volume += payload_configuration[i] * PAYLOAD_ITEMS[i].volume

    return total_payload_volume
