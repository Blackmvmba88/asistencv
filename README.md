# BLACKMAMBA SENTINEL X

Modular prototype for camera motion, irrigation simulation, and sports target scoring.

**Status:** experimental software, not validated hardware.

## Modules
- **VISION:** Sony Cyber-shot capture adapter (compatibility depends on camera model); opt-in face verification is a future feature.
- **MOTION:** two-axis PAN/TILT simulation for a camera or inert training prop. No weapon aiming or firing integration.
- **AQUA:** moisture-based irrigation decisions with dry-tank and runtime interlocks.
- **ARENA:** target detection and scoring only; paintball markers remain manually operated.

## Quick start

Requires Python 3.10+; core simulations use the standard library.

```bash
python -m unittest discover -s tests -v
python -m sentinel.demo
```

## Safety boundaries
The software does not actuate pumps, motors, or firing mechanisms. All outputs are simulated. For physical deployment, use independent power cutoff, emergency stop, mechanical limits, flow verification, and supervised commissioning. Never connect facial recognition or automated tracking to a projectile launcher.

## Roadmap
1. Validate simulation and state machines.
2. Identify exact Sony Cyber-shot model and supported capture interface.
3. Implement camera-only PAN/TILT with limits and physical emergency stop.
4. Test irrigation on a water-only bench with a safe low-voltage pump.
5. Add opt-in access controls, retention limits and documented consent.

BlackMamba Corp — Build · Test · Measure · Evolve.
