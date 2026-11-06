from dataclasses import dataclass

@dataclass(frozen=True)
class IrrigationDecision:
    request_water: bool
    reason: str


def decide_irrigation(moisture_percent: float, threshold_percent: float, tank_has_water: bool, runtime_seconds: int = 0, max_runtime_seconds: int = 120) -> IrrigationDecision:
    """Simulation only: return a request, never switch a pump."""
    if not (0 <= moisture_percent <= 100 and 0 <= threshold_percent <= 100):
        raise ValueError("Percentages must be in [0,100]")
    if runtime_seconds < 0 or max_runtime_seconds <= 0:
        raise ValueError("Invalid runtime")
    if not tank_has_water:
        return IrrigationDecision(False, "empty_tank")
    if runtime_seconds >= max_runtime_seconds:
        return IrrigationDecision(False, "runtime_limit")
    if moisture_percent >= threshold_percent:
        return IrrigationDecision(False, "moisture_sufficient")
    return IrrigationDecision(True, "dry_soil")
