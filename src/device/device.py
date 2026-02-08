import math


def resistive_divider(voltage: float, r1: float, r2: float) -> float:
    """Вычисляет напряжение в простом резистивном делителе."""
    return voltage * (r2 / (r1 + r2))

def power(voltage: float, current: float) -> float:
    """Вычисляет мощность."""
    return voltage * current

def current_from_voltage_resistance(voltage: float, resistance: float) -> float:
    """Вычисляет силу тока."""
    return voltage / resistance

def current_from_voltage_power(voltage: float, power: float) -> float:
    """Вычисляет силу тока, зная напряжение и мощность."""
    return power / voltage

def and_gate(a: float, b: float) -> float:
    """Логический элемент И."""
    return 1.0 if a > 0 and b > 0 else 0.0

def or_gate(a: float, b: float) -> float:
    """Логический элемент ИЛИ."""
    return 1.0 if a > 0 or b > 0 else 0.0

def not_gate(a: float) -> float:
    """Логический элемент НЕ."""
    return 1.0 if a == 0 else 0.0

def nand_gate(a: float, b: float) -> float:
    """Логический элемент И-НЕ."""
    return 1.0 - and_gate(a, b)

def nor_gate(a: float, b: float) -> float:
    """Логический элемент ИЛИ-НЕ."""
    return 1.0 - or_gate(a, b)

def euclidean_distance(pointA: list[float], pointB: list[float]) -> float:
    """Вычисляет Евклидово расстояние между двумя точками."""
    return math.dist(pointA, pointB)

def kinetic_energy(mass: float, velocity: float) -> float:
    """Вычисляет кинетическую энергию."""
    return (mass * (velocity ** 2)) * 0.5

def is_error_acceptable(value: float, expected: float, tolerance: float) -> bool:
    """Проверяет, допустима ли ошибка."""
    return ((value - expected) ** 2) < tolerance


