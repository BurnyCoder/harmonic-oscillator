# Interactive Harmonic Oscillator Visualization

A web-based interactive harmonic oscillator visualization tool that allows users to explore the dynamics of a simple harmonic oscillator. This tool includes mathematical equations, animated visualizations, and interactive plots.

## Features

- Interactive controls to adjust:
  - Mass
  - Spring constant
  - Damping coefficient
  - Initial position
  - Initial velocity
  - Time span
- Real-time animation of the oscillating mass-spring system
- Plots of position, velocity, and energy components
- Mathematical equations explaining the harmonic oscillator physics
- Support for undamped, underdamped, critically damped, and overdamped systems

## Requirements

- Python 3.6+
- Flask
- NumPy
- Plotly
- Modern web browser with JavaScript enabled

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`
3. Use the interactive controls to adjust parameters and observe the changes in the system behavior

## Physics Background

The simple harmonic oscillator is a fundamental model in physics that describes oscillatory motion where a restoring force is proportional to the displacement from equilibrium. The core equation of motion is:

```
m(d²x/dt²) + b(dx/dt) + kx = 0
```

Where:
- m is the mass
- b is the damping coefficient
- k is the spring constant
- x is the displacement from equilibrium

The behavior of the system depends on the damping ratio (ζ = b/(2√(km))):
- ζ = 0: Undamped oscillation
- 0 < ζ < 1: Underdamped oscillation
- ζ = 1: Critically damped
- ζ > 1: Overdamped

## License

MIT 