from metrics import (
    objective_factor,
    total_volume,
    total_cargo_units,
    total_payload_mass,
)
from matplotlib import pyplot as plt

configs = {}
volumes = {}
masses = {}

MIN_CU = 100
EMPTY_MASS = 1400

# Critical payload mass gives 0.25 fraction
critical_payload_mass = EMPTY_MASS / 3

for i in range(0, 9):
    for j in range(0, 9):
        for k in range(0, 5):
            if total_cargo_units([i, j, k]) < 100:
                # Infeasible
                continue
            if total_payload_mass([i, j, k]) > critical_payload_mass:
                # Excessive
                continue

            configs[(i, j, k)] = objective_factor([i, j, k], EMPTY_MASS)
            volumes[(i, j, k)] = total_volume([i, j, k])
            masses[(i, j, k)] = total_payload_mass([i, j, k])

config_values = list(configs.values())
volume_values = list(volumes.values())
mass_values = list(masses.values())

# find the best configuration in terms of payload to mass ratio
payload_to_mass_ratio = {key: value / masses[key] for key, value in configs.items()}
best_config = max(payload_to_mass_ratio, key=payload_to_mass_ratio.get)
print(f"Best configuration: {best_config}")

# write to file
with open("configurations.csv", "w") as f:
    f.write(
        "Configuration (P/G/T), Objective Multiplier, Total Volume (cm^3), Payload Mass (g), Score/Mass Ratio\n"
    )
    for key in configs:
        f.write(
            f"{''.join(str(k) for k in key)}, {configs[key]:.2f}, {volumes[key]:.2f}, {masses[key]:.2f}, {payload_to_mass_ratio[key]:.4f}\n"
        )


plt.subplot(121)
plt.scatter(volume_values, config_values)
plt.xlabel("Total Volume (cm^3)")
plt.ylabel("Objective Multiplier")
plt.title("Objective Multiplier vs Total Volume")
plt.axhline(y=1, color="r", linestyle="-")
plt.grid()

plt.subplot(122)
plt.scatter(mass_values, config_values)
plt.xlabel("Payload Mass (g)")
plt.ylabel("Objective Multiplier")
plt.title("Objective Multiplier vs Payload Mass")
plt.axhline(y=1, color="r", linestyle="-")
plt.grid()

plt.suptitle(f"Empty Mass: {EMPTY_MASS}g")
plt.show()
