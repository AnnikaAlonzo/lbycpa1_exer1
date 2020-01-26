##################################################

# Author: Annika Alonzo
# Date: Jan. 26, 2020
# Course: LBYCPA1

# Program description:
# For laboratory activity 4, the function of the program is to present a selection screen to the user, there will be two selections, both are engineering 
# equations.
# There is also a quit option, the user may opt to choose 1, 2, or q for their selection. The program should then be able to show the user what thy have 
# chosen.
# Depending on the equation they have chosen, on the terminal it should allow the user to choose what variable they are calculating for in the equation,
# ater choosing the unknown variable, they should be able to input the values of the other variables and then the program should be able to calculate 
# for the unknown variable
# After all of that, the user should be able to either go back to the selection screen or quit the program. 

##################################################

def initializeEngineeringFormula():

    while True:


        print("~~~~~Engineering Formulas~~~~~")
        print("\nNote: type 'unknown' for the variable you are looking for.")
        print("\nFormulas available: \n[1] Acceleration: Acceleration(a) = Final Velocity(vf) - Initial Velocity(vi) / Time(t) \n[2] Potential Energy: Potential Energy(U) = Mass(m) * Acceleration Due to Gravity(g) * Height(h)")
        print("[Q] Quit")
        user_formula = input("\nWhich among theses formulas would you like to use? \n")


        if user_formula == '1':

            print("Choose what variable or Type 'b' to go back to Formula Screen\n")
            variable = input(" Acceleration \n Final Velocity \n Initial Velocity \n Time \n")
            # acceleration = input("\nWrite acceleration (in m/s^2) or 'b' to go back to the selection screen. ")
            # final_velocity = input("Final Velocity (in m/s)? ")
            # initial_velocity = input("Initial Velocity (in m/s)? ")
            # time = input("Time (in s)? ")

            if variable == "b":
                initializeEngineeringFormula()

            elif variable.lower() == 'acceleration':
                final_velocity = input("\nFinal Velocity (in m/s)? ")
                initial_velocity = input("Initial Velocity (in m/s)? ")
                time = input("Time (in s)? ")

                vf = int(final_velocity)
                vi = int(initial_velocity)
                t = int(time)
                ans_accel = (vf - vi) / t

                print("The acceleration is", ans_accel, "m/s^2")

            elif variable.lower() == 'final velocity':
                acceleration = input("\nAcceleration (in m/s^2)? ")
                initial_velocity = input("Initial Velocity (in m/s)? ")
                time = input("Time (in s)? ")

                a = int(acceleration)
                vi_2 = int(initial_velocity)
                t_2 = int(time)
                ans_finvel = (a * t_2) + vi_2

                print("The final velocity is", ans_finvel, "m/s")

            elif variable.lower() == 'initial velocity':
                acceleration = input("\nAcceleration (in m/s^2)? ")
                final_velocity = input("Final Velocity (in m/s)? ")
                time = input("Time (in s)? ")

                a_2 = int(acceleration)
                vf_2 = int(final_velocity)
                t_3 = int(time)
                ans_inivel = vf_2 - (a_2 * t_3)

                print("The initial velocity is", ans_inivel, "m/s")

            elif variable.lower() == 'time':
                acceleration = input("\nAcceleration (in m/s^2)? ")
                final_velocity = input("Final Velocity (in m/s)? ")
                initial_velocity = input("Initial Velocity (in m/s)? ")


                a_3 = int(acceleration)
                vf_3 = int(final_velocity)
                vi_3 = int(initial_velocity)
                ans_time = (vf_3 - vi_3) / a_3

                print("The time is", ans_time, "s")

        elif user_formula == '2':
            # potential_energy = input("\nWrite potential energy (in J) or 'b' to go back to the selection screen. ")
            # mass = input("Mass (in kg)? ")
            # accel_dueto_grav = input("Acceleration due to Gravity (in m/s^2)? ")
            # height = input("Height (in ft)? ")

            print("Choose what variable or Type 'b' to go back to Formula Screen\n")
            variable2 = input(" Potential Energy \n Mass \n Accel \n Height \n")

            if variable2 == "b":
                initializeEngineeringFormula()

            elif variable2.lower() == 'potential energy':
                mass = input("\nMass (in kg)? ")
                accel_dueto_grav = input("Acceleration due to Gravity (in m/s^2)? ")
                height = input("Height (in ft)? ")


                m = int(mass)
                g = int(accel_dueto_grav)
                h = int(height)
                ans_potene = m * g * h

                print("The potential energy is", ans_potene, "J")

            elif variable2.lower() == 'mass':
                potential_energy = input("\nPotential energy (in J)? ")
                accel_dueto_grav = input("Acceleration due to Gravity (in m/s^2)? ")
                height = input("Height (in ft)? ")


                u = int(potential_energy)
                g_2 = int(accel_dueto_grav)
                h_2 = int(height)
                ans_mass = u / (g_2 * h_2)

                print("The mass is", ans_mass, "kg")

            elif variable2.lower() == 'accel':
                potential_energy = input("\nPotential energy (in J)? ")
                mass = input("Mass (in kg)? ")
                height = input("Height (in ft)? ")


                u_2 = int(potential_energy)
                m_2 = int(mass)
                h_3 = int(height)
                ans_grav = u_2 / (m_2 * h_3)

                print("The acceleration due to gravity is", ans_grav, "m/s^2")

            elif variable2.lower() == 'height':
                potential_energy = input("\nPotential energy (in J)? ")
                mass = input("Mass (in kg)? ")
                accel_dueto_grav = input("Acceleration due to Gravity (in m/s^2)? ")


                u_3 = int(potential_energy)
                m_3 = int(mass)
                g_3 = int(accel_dueto_grav)
                ans_height = u_3 / (m_3 * g_3)

                print("The height is", ans_height, "ft")

        elif user_formula == "Q" or user_formula == "q":
            print("Goodbye!")
            exit()

        else:
            print ("Sorry, that was an invalid input!")
initializeEngineeringFormula()