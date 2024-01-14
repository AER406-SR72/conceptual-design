from metrics import total_cargo_units, partial_derivatives

derivs = {}

MIN_CU = 100
MAX_CU = 800
EMPTY_MASS = 800

# Critical payload mass gives 0.25 fraction
critical_payload_mass = EMPTY_MASS / 3

for i in range(0, 8):
    for j in range(0, 8):
        for k in range(0, 4):
            if (
                total_cargo_units([i, j, k]) < MIN_CU
                or total_cargo_units([i, j, k]) > MAX_CU
            ):
                # Infeasible
                continue
            derivs[(i, j, k)] = partial_derivatives([i, j, k], EMPTY_MASS)

# write to file
with open(f"derivatives_{EMPTY_MASS:.0f}.csv", "w") as f:
    f.write("Configuration (P|G|T), d/dP, d/dG, d/dT\n")
    for key in derivs:
        f.write(
            f"{'|'.join(str(k) for k in key)}, {derivs[key][0]:.2f}, {derivs[key][1]:.2f}, {derivs[key][2]:.2f}\n"
        )
