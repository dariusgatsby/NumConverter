def convert(feet, inches):
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    return meters

if __name__ == "__main__":
    meters = convert(6,2)
    print(meters)
