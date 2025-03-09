import os
from flask import Flask, render_template, jsonify, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate harmonic oscillator data based on parameters."""
    # Get parameters from request
    data = request.get_json()
    mass = float(data.get('mass', 1.0))
    spring_constant = float(data.get('spring_constant', 1.0))
    initial_position = float(data.get('initial_position', 1.0))
    initial_velocity = float(data.get('initial_velocity', 0.0))
    damping = float(data.get('damping', 0.1))
    time_span = float(data.get('time_span', 20.0))
    
    # Calculate angular frequency
    omega = np.sqrt(spring_constant / mass)
    
    # Generate time points
    t = np.linspace(0, time_span, 500)
    
    # Calculate position
    if damping == 0:
        # Undamped oscillation
        x = initial_position * np.cos(omega * t) + (initial_velocity / omega) * np.sin(omega * t)
    else:
        # Damped oscillation
        gamma = damping / (2 * mass)
        if gamma < omega:  # Underdamped
            omega_d = np.sqrt(omega**2 - gamma**2)
            x = np.exp(-gamma * t) * (
                initial_position * np.cos(omega_d * t) +
                ((initial_velocity + gamma * initial_position) / omega_d) * np.sin(omega_d * t)
            )
        elif gamma == omega:  # Critically damped
            x = np.exp(-gamma * t) * (
                initial_position + (initial_velocity + gamma * initial_position) * t
            )
        else:  # Overdamped
            r1 = -gamma + np.sqrt(gamma**2 - omega**2)
            r2 = -gamma - np.sqrt(gamma**2 - omega**2)
            c1 = (initial_velocity - r2 * initial_position) / (r1 - r2)
            c2 = (r1 * initial_position - initial_velocity) / (r1 - r2)
            x = c1 * np.exp(r1 * t) + c2 * np.exp(r2 * t)
    
    # Calculate potential energy
    potential_energy = 0.5 * spring_constant * x**2
    
    # Calculate kinetic energy (approximate derivative for velocity)
    dt = t[1] - t[0]
    v = np.gradient(x, dt)
    kinetic_energy = 0.5 * mass * v**2
    
    # Calculate total energy
    total_energy = potential_energy + kinetic_energy
    
    # Prepare data for response
    return jsonify({
        'time': t.tolist(),
        'position': x.tolist(),
        'velocity': v.tolist(),
        'potential_energy': potential_energy.tolist(),
        'kinetic_energy': kinetic_energy.tolist(),
        'total_energy': total_energy.tolist(),
        'parameters': {
            'omega': omega,
            'period': 2 * np.pi / omega if omega > 0 else 0,
            'damping_ratio': gamma / omega if 'gamma' in locals() else 0
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 