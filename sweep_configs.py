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
with open(f"configurations_{EMPTY_MASS:.0f}.csv", "w") as f:
    f.write(
        "Configuration (P/G/T), Objective Multiplier, Total Volume (cm^3), Payload Mass (g), Score/Mass Ratio\n"
    )
    for key in configs:
        f.write(
            f"{'/'.join(str(k) for k in key)}, {configs[key]:.2f}, {volumes[key]:.2f}, {masses[key]:.2f}, {payload_to_mass_ratio[key]:.4f}\n"
        )

# plot

# generate colours based on the configuration:
# ping pong balls = red
# golf balls = green
# tennis balls = blue

# find the max of each
max_p = max(configs, key=lambda x: x[0])[0]
max_g = max(configs, key=lambda x: x[1])[1]
max_t = max(configs, key=lambda x: x[2])[2]

# list of colours
colours = []
for config in configs:
    # red
    r = config[0] / max_p
    # green
    g = config[1] / max_g
    # blue
    b = config[2] / max_t
    colours.append((r, g, b))

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.scatter(mass_values, config_values, c=colours, edgecolors="black")
plt.xlabel("Payload Mass (g)")
plt.ylabel("Objective Multiplier")
plt.title("Objective Multiplier vs Total Payload Mass")
plt.axhline(y=1, color="r", linestyle="-")
plt.grid()

plt.subplot(122)
plt.scatter(volume_values, config_values, c=colours, edgecolors="black")
plt.xlabel("Total Volume (cm^3)")
plt.ylabel("Objective Multiplier")
plt.title("Objective Multiplier vs Total Volume")
plt.axhline(y=1, color="r", linestyle="-")
plt.grid()


plt.suptitle(f"Empty Mass: {EMPTY_MASS}g")
plt.savefig(f"configurations_{EMPTY_MASS:.0f}.png")

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
# scatter: colour = score, position = configuration
ax.scatter(
    [key[0] for key in configs],
    [key[1] for key in configs],
    [key[2] for key in configs],
    c=config_values,
    s=[5 * c for c in config_values],
    alpha=0.3,
)
ax.set_xlabel("Ping Pong Balls")
ax.set_ylabel("Golf Balls")
ax.set_zlabel("Tennis Balls")


plt.show()
