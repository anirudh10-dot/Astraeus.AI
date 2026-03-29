def simulate_life_support(crew_count, activity_level):
    # Base rates per person per hour (kg or liters)
    # Activity multipliers: Resting=0.8, Moderate=1.0, Intense=1.5
    multipliers = {"resting": 0.8, "moderate": 1.0, "intense": 1.5}
    modifier = multipliers.get(activity_level.lower(), 1.0)

    # Initial Station Levels
    stats = {
        "Oxygen (kg)": 500.0,
        "CO2 (kg)": 5.0,
        "Water (L)": 1000.0,
        "Humidity (%)": 45.0,
        "Hydrogen (kg)": 50.0,
        "Radiation (mSv)": 0.05
    }

    # Hourly Change Rates (Consumption/Production per person)
    o2_rate = -0.035 * modifier * crew_count  # Decreasing
    co2_rate = 0.042 * modifier * crew_count   # Increasing
    h2o_rate = -0.15 * modifier * crew_count   # Decreasing (Drinking/Usage)
    humidity_rate = 0.5 * modifier * crew_count # Increasing (Sweat/Respiration)
    rad_rate = 0.002                            # Constant background cosmic radiation
    h2_rate = 0.01 * crew_count                 # Increase (Byproduct of electrolysis)

    print(f"--- Space AI Life Support Report ({activity_level.upper()} Activity) ---")
    print(f"{'Parameter':<18} | {'Current Level':<15} | {'Rate (per hr)':<12}")
    print("-" * 50)

    results = [
        ("Oxygen", stats["Oxygen (kg)"], o2_rate, "kg"),
        ("Carbon Dioxide", stats["CO2 (kg)"], co2_rate, "kg"),
        ("Water Storage", stats["Water (L)"], h2o_rate, "L"),
        ("Humidity", stats["Humidity (%)"], humidity_rate, "%"),
        ("Hydrogen", stats["Hydrogen (kg)"], h2_rate, "kg"),
        ("Radiation", stats["Radiation (mSv)"], rad_rate, "mSv")
    ]

    for name, val, rate, unit in results:
        trend = "↑" if rate > 0 else "↓"
        print(f"{name:<18} | {val:>7.2f} {unit:<6} | {trend} {abs(rate):>6.3f} {unit}")

# Example Usage
crew = int(input("Enter number of crew members: "))
activity = input("Enter activity level (Resting, Moderate, Intense): ")
simulate_life_support(crew, activity)
  
