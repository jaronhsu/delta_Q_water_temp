print("Calculates energy change in joules for temperature change in water")

heat_fus = 334  # J/g
heat_vap = 2257  # J/g
spec_heat_s = 2.108  # J/g
spec_heat_l = 4.184  # J/g
spec_heat_g = 1.996  # J/g
fus_pt = 0  # melting or freezing point
vap_pt = 100  # boiling or condensation point
mass, init_temp, fin_temp = "", "", ""

while mass == "":
    try:
        mass = float(input("Enter mass (g): "))
        if mass < 0:
            float("")
    except ValueError:
        mass = ""
        print("Invalid input.")
while init_temp == "":
    try:
        init_temp = float(input("Enter initial temperature (C): "))
        if init_temp == fus_pt:
            sol_liq = input("That temperature is on solid-liquid border. Specify 'solid' or 'liquid': ")
            if sol_liq == "solid":
                init_temp = init_temp - 0.0000000000001
            elif sol_liq == "liquid":
                init_temp = init_temp + 0.0000000000001
            else:
                float("")
        elif init_temp == vap_pt:
            sol_liq = input("That temperature is on liquid-gas border. Specify 'liquid' or 'gas': ")
            if sol_liq == "liquid":
                init_temp = init_temp - 0.0000000000001
            elif sol_liq == "gas":
                init_temp = init_temp + 0.0000000000001
            else:
                float("")
    except ValueError:
        init_temp = ""
        print("Invalid input.")
while fin_temp == "":
    try:
        fin_temp = float(input("Enter final temperature (C): "))
        if fin_temp == fus_pt:
            sol_liq = input("That temperature is on solid-liquid border. Specify 'solid' or 'liquid': ")
            if sol_liq == "solid":
                fin_temp = fin_temp - 0.0000000000001
            elif sol_liq == "liquid":
                fin_temp = fin_temp + 0.0000000000001
            else:
                float("")
        elif fin_temp == vap_pt:
            sol_liq = input("That temperature is on liquid-gas border. Specify 'liquid' or 'gas': ")
            if sol_liq == "liquid":
                fin_temp = fin_temp - 0.0000000000001
            elif sol_liq == "gas":
                fin_temp = fin_temp + 0.0000000000001
            else:
                float("")
    except ValueError:
        fin_temp = ""
        print("Invalid input.")
        
if fin_temp - init_temp >= 0:
    up_down_holder = 1
else:
    up_down_holder = init_temp
    init_temp = fin_temp
    fin_temp = up_down_holder
    up_down_holder = -1


def phase_id(temp):
    if temp <= fus_pt:
        return [1, fus_pt, heat_fus, spec_heat_s]  # solid
    elif temp <= vap_pt:
        return [2, vap_pt, heat_vap, spec_heat_l]  # liquid
    else:
        return [3, 0, 0, spec_heat_g]  # gas


def q_calc(i_temp, f_temp):
    if phase_id(i_temp) == phase_id(f_temp):
        return mass * phase_id(i_temp)[3] * (f_temp - i_temp)
    elif phase_id(i_temp)[0] < phase_id(f_temp)[0]:
        return q_calc(i_temp, phase_id(i_temp)[1])\
               + q_calc(phase_id(i_temp)[1] + 0.0000000000001, f_temp)\
               + mass * phase_id(i_temp)[2]


print(str(round(q_calc(init_temp, fin_temp) * up_down_holder, 3)) + " joules")

input()
