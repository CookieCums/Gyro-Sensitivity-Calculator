# Gyro Sensitivity Calculator

A Flask-based calculator that estimates adjusted gyro sensitivity when moving between phones with different weights and, optionally, different screen sizes.

## Features

- Calculates a new general gyro sensitivity
- Supports optional screen-size adjustment
- Calculates 3x, 4x, 6x, and 8x scope sensitivities when provided
- Includes a dedicated explanation page for the calculation
- Simple browser-based interface
- Runs with a configurable `PORT` environment variable

## How it works

The calculator compares the old and new phone characteristics and combines the weight and screen-size ratios using a configurable weighting factor. The current implementation uses a **0.7 weight factor** for phone weight and the remaining **0.3** for screen size when both screen sizes are supplied.

In simplified form:

```text
weight ratio      = new phone weight / old phone weight
screen ratio      = new screen size / old screen size
combined factor   = (0.7 × weight ratio) + (0.3 × screen ratio)
new sensitivity   = old sensitivity × combined factor
```

If screen sizes are not supplied, the screen-size ratio remains `1.0`.

## Tech Stack

- **Python**
- **Flask**
- **HTML / CSS**

## Run locally

### 1. Clone

```bash
git clone https://github.com/CookieCums/Gyro-Sensitivity-Calculator.git
cd Gyro-Sensitivity-Calculator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the server

```bash
python main.py
```

The application uses port `10000` by default. Set `PORT` to use another port.

## Project structure

```text
Gyro-Sensitivity-Calculator/
├── main.py
├── requirements.txt
├── static/
└── templates/
```

## Important note

The calculator provides an estimate based on the formula implemented by the project. It should not be treated as a guarantee of identical in-game feel across different devices.

## Links

- [Source code](https://github.com/CookieCums/Gyro-Sensitivity-Calculator/blob/main/main.py)
- [Dependencies](https://github.com/CookieCums/Gyro-Sensitivity-Calculator/blob/main/requirements.txt)
- [Templates](https://github.com/CookieCums/Gyro-Sensitivity-Calculator/tree/main/templates)
- [Static files](https://github.com/CookieCums/Gyro-Sensitivity-Calculator/tree/main/static)
