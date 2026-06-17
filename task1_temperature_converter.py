"""
PRODIGY INFOTECH INTERNSHIP - TASK 1
Temperature Conversion Program
Converts temperatures between Celsius, Fahrenheit, and Kelvin
"""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature(value, unit):
    unit = unit.upper()
    if unit == 'C':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"\n  {'='*40}")
        print(f"  Temperature Conversion Results")
        print(f"  {'='*40}")
        print(f"  Input      : {value}°C (Celsius)")
        print(f"  Fahrenheit : {f:.2f}°F")
        print(f"  Kelvin     : {k:.2f} K")
        print(f"  {'='*40}\n")
    elif unit == 'F':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"\n  {'='*40}")
        print(f"  Temperature Conversion Results")
        print(f"  {'='*40}")
        print(f"  Input      : {value}°F (Fahrenheit)")
        print(f"  Celsius    : {c:.2f}°C")
        print(f"  Kelvin     : {k:.2f} K")
        print(f"  {'='*40}\n")
    elif unit == 'K':
        if value < 0:
            print("  ❌ Kelvin cannot be negative!")
            return
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"\n  {'='*40}")
        print(f"  Temperature Conversion Results")
        print(f"  {'='*40}")
        print(f"  Input      : {value} K (Kelvin)")
        print(f"  Celsius    : {c:.2f}°C")
        print(f"  Fahrenheit : {f:.2f}°F")
        print(f"  {'='*40}\n")
    else:
        print("  ❌ Invalid unit! Please enter C, F, or K.")

def main():
    print("\n" + "="*44)
    print("   🌡️  TEMPERATURE CONVERSION PROGRAM  🌡️")
    print("   Prodigy Infotech Internship - Task 1")
    print("="*44)

    while True:
        print("\n  Units: C = Celsius | F = Fahrenheit | K = Kelvin")
        print("  Type 'exit' to quit.\n")

        temp_input = input("  Enter temperature value: ").strip()
        if temp_input.lower() == 'exit':
            print("\n  Goodbye! 👋\n")
            break
        try:
            value = float(temp_input)
        except ValueError:
            print("  ❌ Please enter a valid number.")
            continue

        unit = input("  Enter unit (C / F / K): ").strip()
        if unit.lower() == 'exit':
            print("\n  Goodbye! 👋\n")
            break

        convert_temperature(value, unit)

        again = input("  Convert another? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("\n  Thank you for using the Temperature Converter! 👋\n")
            break

if __name__ == "__main__":
    main()
