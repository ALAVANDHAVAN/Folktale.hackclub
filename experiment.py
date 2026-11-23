what_r_u_gonna_do = input("You are now a superhero. Pick A B or C for your superpower and only put the letters.\nA: Invisibility.\nB: Super Strength.\nC: Supreme Knowledge.\n").strip().lower()

if what_r_u_gonna_do == "a":
    print("Great, now no one can see you!\n")


    crime1_invisibility = input("Oh nooooo! You have to fight your first crime: it is a jailbreak near your city. What will you do?\nA: Use invisibility to attack enemies by surprise.\nB: Stay home and rest.\n").strip().lower()

    if crime1_invisibility == "a":
        print("Oh yeah! With your amazing power, you have successfully defeated the villains, but now you have to rest since you are tired. While you were resting, the infamous bank robbers robbed all the banks of the city. You are being criticized by the city now.")

    elif crime1_invisibility == "b":
        print("You have gained enough rest, but the city has been criticizing you for not helping defeat the jailbreakers.")

    else:
        print("Nope, A or B")


elif what_r_u_gonna_do == "b":
    print("Yay! Now you can boast about your muscles!")


    crime1_super_strength = input("Oh nooooo! You have to fight your first crime: it is a jailbreak near your city. What will you do?\nA: Use super strength to overpower enemies and defeat them.\nB: Stay home and rest.\n").strip().lower()

    if crime1_super_strength == "a":
        print("Oh yeah! With your amazing power, you have successfully defeated the villains, but now you have to rest since you are tired. While you were resting, the infamous bank robbers robbed all the banks of the city. You are being criticized by the city now.")

    elif crime1_super_strength == "b":
        print("You have gained enough rest, but the city has been criticizing you for not helping defeat the jailbreakers.")

    else:
        print("Nope, A or B")


elif what_r_u_gonna_do == "c":
    print("Wow! Your mind will take you places!")


    crime1_supreme_knowledge = input("Oh nooooo! You have to fight your first crime: it is a jailbreak near your city. What will you do?\nA: Use supreme knowledge to outsmart enemies and defeat them.\nB: Stay home and rest.\n")

    if crime1_supreme_knowledge == "a":
        print("Oh yeah! With your amazing power, you have successfully defeated the villains, but now you have to rest since you are tired. While you were resting, the infamous bank robbers robbed all the banks of the city. You are being criticized by the city now.")

    elif crime1_supreme_knowledge == "b":
        print("You have gained enough rest, but the city has been criticizing you for not helping defeat the jailbreakers.")

    else:
        print("Nope, A or B")


else:
    print("Nope, do A, B, or C.")