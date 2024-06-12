from flask import Flask, render_template, request
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 10000))

def calculate_new_gyro_sensitivity(old_phone_weight, old_phone_gyro_sensitivity, new_phone_weight, old_phone_screen_size=None, new_phone_screen_size=None, weight_factor=0.7):
    """
    Calculates the new gyro sensitivity for a phone based on weight and screen size (optional).
    """
    # Calculate weight ratio
    weight_ratio = new_phone_weight / old_phone_weight

    # Calculate screen size ratio (if provided)
    screen_size_ratio = 1.0
    if old_phone_screen_size and new_phone_screen_size:
        screen_size_ratio = new_phone_screen_size / old_phone_screen_size

    # Combine adjustment factors with weighting
    combined_factor = (weight_factor * weight_ratio) + ((1 - weight_factor) * screen_size_ratio)

    # Calculate new gyro sensitivity
    new_gyro_sensitivity = old_phone_gyro_sensitivity * combined_factor

    return new_gyro_sensitivity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/how_does_this_work')
def how_does_this_work():
    return render_template('how_does_this_work.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        old_phone_weight = float(request.form['old_phone_weight'])
        old_phone_gyro_sensitivity = int(request.form['old_phone_gyro_sensitivity'])
        new_phone_weight = float(request.form['new_phone_weight'])
        old_phone_screen_size = request.form.get('old_phone_screen_size')
        new_phone_screen_size = request.form.get('new_phone_screen_size')

        old_phone_screen_size = float(old_phone_screen_size) if old_phone_screen_size else None
        new_phone_screen_size = float(new_phone_screen_size) if new_phone_screen_size else None

        # Calculate new general gyro sensitivity
        new_gyro_sensitivity = calculate_new_gyro_sensitivity(old_phone_weight, old_phone_gyro_sensitivity, new_phone_weight, 
                                                              old_phone_screen_size, new_phone_screen_size)

        # Calculate new scope sensitivities
        old_phone_3x_sensitivity = request.form.get('old_phone_3x_sensitivity')
        old_phone_4x_sensitivity = request.form.get('old_phone_4x_sensitivity')
        old_phone_6x_sensitivity = request.form.get('old_phone_6x_sensitivity')
        old_phone_8x_sensitivity = request.form.get('old_phone_8x_sensitivity')

        new_3x_sensitivity = calculate_new_gyro_sensitivity(old_phone_weight, float(old_phone_3x_sensitivity), new_phone_weight, 
                                                            old_phone_screen_size, new_phone_screen_size) if old_phone_3x_sensitivity else None
        new_4x_sensitivity = calculate_new_gyro_sensitivity(old_phone_weight, float(old_phone_4x_sensitivity), new_phone_weight, 
                                                            old_phone_screen_size, new_phone_screen_size) if old_phone_4x_sensitivity else None
        new_6x_sensitivity = calculate_new_gyro_sensitivity(old_phone_weight, float(old_phone_6x_sensitivity), new_phone_weight, 
                                                            old_phone_screen_size, new_phone_screen_size) if old_phone_6x_sensitivity else None
        new_8x_sensitivity = calculate_new_gyro_sensitivity(old_phone_weight, float(old_phone_8x_sensitivity), new_phone_weight, 
                                                            old_phone_screen_size, new_phone_screen_size) if old_phone_8x_sensitivity else None

        return render_template('result.html', new_gyro_sensitivity=round(new_gyro_sensitivity, 2),
                               new_3x_sensitivity=round(new_3x_sensitivity, 2) if new_3x_sensitivity else "N/A",
                               new_4x_sensitivity=round(new_4x_sensitivity, 2) if new_4x_sensitivity else "N/A",
                               new_6x_sensitivity=round(new_6x_sensitivity, 2) if new_6x_sensitivity else "N/A",
                               new_8x_sensitivity=round(new_8x_sensitivity, 2) if new_8x_sensitivity else "N/A")
    except ValueError:
        return "Invalid input. Please enter valid numbers.", 400

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)
