from metrics import partial_derivatives

derivs = {}

MIN_CU = 100
EMPTY_MASS = 1400

# Critical payload mass gives 0.25 fraction
critical_payload_mass = EMPTY_MASS / 3

for i in range(0, 8):
    for j in range(0, 8):
        for k in range(0, 4):
            derivs[(i, j, k)] = partial_derivatives([i, j, k], EMPTY_MASS)

# write to file
with open(f"derivatives_{EMPTY_MASS:.0f}.csv", "w") as f:
    f.write("Configuration (P/G/T), d/dP, d/dG, d/dT\n")
    for key in derivs:
        f.write(
            f"{'/'.join(str(k) for k in key)}, {derivs[key][0]:.2f}, {derivs[key][1]:.2f}, {derivs[key][2]:.2f}\n"
        )
