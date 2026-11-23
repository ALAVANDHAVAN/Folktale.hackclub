while True:
    #from now on, in every input, always make b the resting thingy.
    what_r_u_gonna_do = input("You are now a superhero. Pick A B or C for your superpower and only put the letters.\nA: Invisibility.\nB: Super Strength.\nC: Supreme Knowledge.\n").strip().lower()

    match what_r_u_gonna_do:
#First Case
        case "a":
            print("\nGreat, now no one can see you!\n")

            while True:

                crime1_invisibility = input("Oh nooooo! You have to fight your first crime: it is a jailbreak near your city. What will you do?\nA: Use invisibility to attack enemies by surprise.\nB: Stay home and rest.\n").strip().lower()

                match crime1_invisibility:
                #Second Case
                    case "a":
                        print("\nOh yeah! With your amazing power, you have successfully defeated the villains, but now you have to rest since you are tired. While you were resting, the infamous bank robbers robbed all the banks of the city. You are being criticized by the city now.")

                        while True:

                            crime2_invisibility = input("\nNow that criminals know about your invisible power, they are now using a thermographic camera, which see things through heat waves, to spot you. What will you do now to defeat these criminals?\nA: Go full ambush and try to defeat them.\nB: Why fight when you can watch Sunday Night Football and stay home.\nC. Consult scientists and others to aid you in designing a material that blocks your heat waves from reaching the thermographic camera.\n").strip().lower()

                            match crime2_invisibility:
                            #Third Case
                                case "a":
                                    print("\nUh oh!!! That was a total falure! The criminals outnumbered you and outpowered you! You have been defeated. Try a different strategy.")
                                    continue
                            #Third Case
                                case "b":
                                    print("\nNo no no. The city hates you now! Do better next time.")
                                    while True:
                                
                                        crime3_invisibility = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a radiating, invisibility defusing, machine. You will lose your ability to turn invisible once this happens. What will you do:\nA: It's ok, without invisibility I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Inject yourself with a fluid that you have been creating so that you can retain your powers despite the machines they have.\n").strip().lower()

                                        match crime3_invisibility:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting...again! You have been resting, and resting. City despises you now, once again. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break          
                            #Third Case
                                case "c":
                                    print("\nGood choice! Finding ways to outsmart the criminals is a signature move. But now that you do that, the city criticizes you more becuase the criminals escaped and you made no effort to stop them.")

                                    while True:
                                
                                        crime3_invisibility = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a radiating, invisibility defusing, machine. You will lose your ability to turn invisible once this happens. What will you do:\nA: It's ok, without invisibility I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Inject yourself with a fluid that you have been creating so that you can retain your powers despite the machines they have.\n").strip().lower()

                                        match crime3_invisibility:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting! You have been resting, and resting. City despises you now. Although you did do well for some crimes, the city revoked your power of being a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case    
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case _:
                                    print("\nNope. A, B, or C\n")
                                    continue

                            break

                #Second Case
                    case "b":
                        print("\nYou have gained enough rest, but the city has been criticizing you for not helping defeat the jailbreakers.")

                        while True:

                            crime2_invisibility = input("\nNow that criminals know about your invisible power, they are now using a thermographic camera, which see things through heat waves, to spot you. What will you do now to defeat these criminals?\nA: Go full ambush and try to defeat them.\nB: Why fight when you can watch Sunday Nigh Football and stay home.\nC. Consult scientists and others to aid you in designing a material that blocks your heat waves from reaching the thermographic camera.\n").strip().lower()

                            match crime2_invisibility:
                            #Third Case
                                case "a":
                                    print("\nUh oh!!! That was a total falure! The criminals outnumbered you and outpowered you! You have been defeated. Try a different strategy.")
                                    continue
                            #Third Case
                                case "b":
                                    print("\nResting for 2 crimes in a row? Now the city thinks you had gotten the superpower of laziness instead of invisibility.")

                                    while True:
                                
                                        crime3_invisibility = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a radiating, invisibility defusing, machine. You will lose your ability to turn invisible once this happens. What will you do:\nA: It's ok, without invisibility I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Inject yourself with a fluid that you have been creating so that you can retain your powers despite the machines they have.\n").strip().lower()

                                        match crime3_invisibility:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting...again! You have been resting, and resting. City despises you now, once again. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case "c":
                                    print("\nGood choice! Finding ways to outsmart the criminals is a signature move. But now that you do that, the city criticizes you more becuase the criminals escaped and you made no effort to stop them.\n")

                                    while True:
                                
                                        crime3_invisibility = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a radiating, invisibility defusing, machine. You will lose your ability to turn invisible once this happens. What will you do:\nA: It's ok, without invisibility I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Inject yourself with a fluid that you have been creating so that you can retain your powers despite the machines they have.\n").strip().lower()

                                        match crime3_invisibility:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting...again! You have been resting, and resting. City despises you now, once again. You chose to upgrade your tech, but did not use it! You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            
                            #Third Case
                                case _:
                                    print("\nNope. A, B, or C\n")
                                    continue

                            break

                #Second Case
                    case _:
                        print("\nNope, A or B\n")
                        continue

                break

#First Case
        case "b":
            print("\nYay! Now you can boast about your muscles!\n")

            while True:

                crime1_super_strength = input("Oh nooooo! You have to fight your first crime: it is a jailbreak near your city. What will you do?\nA: Use super strength to overpower enemies and defeat them.\nB: Stay home and rest.\n").strip().lower()

                match crime1_super_strength:
                #Second Case
                    case "a":
                        print("\nOh yeah! With your amazing power, you have successfully defeated the villains, but now you have to rest since you are tired. While you were resting, the infamous bank robbers robbed all the banks of the city. You are being criticized by the city now.")

                        while True:

                            crime2_super_strength = input("\nNow that criminals know about your strength, they are now using molten tungsten that generates power to a gauntlet to overpower you. What will you do now to defeat these criminals?\nA: Go full ambush and try to defeat them.\nB: Why fight when you can watch Sunday Night Football and stay home.\nC. Consult scientists and others to aid you in designing a material that is stronger and sort of like vibranium so that you can win your next battle.\n").strip().lower()

                            match crime2_super_strength:
                            #Third Case
                                case "a":
                                    print("\nUh oh!!! That was a total falure! The criminals outnumbered you and outpowered you! You have been defeated. Try a different strategy.")
                                    continue
                            #Third Case
                                case "b":
                                    print("\nNo no no. The city hates you now! Do better next time.")

                                    while True:
                                
                                        crime3_super_strength = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a radiating, strength defusing, machine. You will lose your ability to be super strong once this happens. What will you do:\nA: It's ok, without strength I'm still smart, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Inject yourself with a fluid that you have been creating so that you can retain your powers despite the machines they have.\n").strip().lower()

                                        match crime3_super_strength:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting...again! You have been resting, and resting. City despises you now, once again. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case "c":
                                    print("\nGood choice! Finding ways to outsmart the criminals is a signature move. But now that you do that, the city criticizes you more becuase the criminals escaped and you made no effort to stop them.")

                                    while True:
                                
                                        crime3_super_strength = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a radiating, strength defusing, machine. You will lose your ability to be super strong once this happens. What will you do:\nA: It's ok, without invisibility I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Inject yourself with a fluid that you have been creating so that you can retain your powers despite the machines they have.\n").strip().lower()

                                        match crime3_super_strength:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting! You have been resting, and resting. City despises you now. Although you did try your best and fought, while upgrading your tech, the city took away your position as a superhero. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case _:
                                    print("\nNope. A, B, or C\n")
                                    continue

                            break
                #Second Case
                    case "b":
                        print("\nYou have gained enough rest, but the city has been criticizing you for not helping defeat the jailbreakers.")

                        while True:

                            crime2_super_strength = input("\nNow that criminals know about your strength, they are now using molten tungsten that generates power to a gauntlet to overpower you. What will you do now to defeat these criminals?\nA: Go full ambush and try to defeat them.\nB: Why fight when you can watch Sunday Night Football and stay home.\nC. Consult scientists and others to aid you in designing a material that is stronger and sort of like vibranium so that you can win your next battle.\n").strip().lower()

                            match crime2_super_strength:
                            #Third Case
                                case "a":
                                    print("\nUh oh!!! That was a total falure! The criminals outnumbered you and outpowered you! You have been defeated. Try a different strategy.")
                                    continue
                            #Third Case
                                case "b":
                                    print("\nDang, using your superpower for no good, just resting. Come on, save your fellow people!")

                                    while True:
                                
                                        crime3_super_strength = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a radiating, strength defusing, machine. You will lose your ability to be super strong once this happens. What will you do:\nA: It's ok, without strength I'm still smart, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Inject yourself with a fluid that you have been creating so that you can retain your powers despite the machines they have.\n").strip().lower()

                                        match crime3_super_strength:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting...again! You have been resting, and resting. City despises you now, once again. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("Wonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case "c":
                                    print("\nGood choice! Finding ways to outsmart the criminals is a signature move. But now that you do that, the city criticizes you more becuase the criminals escaped and you made no effort to stop them.")

                                    while True:
                                
                                        crime3_super_strength = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a radiating, strength defusing, machine. You will lose your ability to be super strong once this happens. What will you do:\nA: It's ok, without invisibility I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Inject yourself with a fluid that you have been creating so that you can retain your powers despite the machines they have.\n").strip().lower()

                                        match crime3_super_strength:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting! You have been resting, and resting. City despises you now. Although you tried your best and upgraded your tech, the city revoked your permission to be a superhero. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case _:
                                    print("\nNope. A, B, or C\n")
                                    continue

                            break
                #Second Case
                    case _:
                        print("\nNope, A or B\n")
                        continue

                break

#First Case
        case "c":
            print("\nWow! Your mind will take you places!\n")

            while True:

                crime1_supreme_knowledge = input("Oh nooooo! You have to fight your first crime: it is a jailbreak near your city. What will you do?\nA: Use supreme knowledge to outsmart enemies and defeat them.\nB: Stay home and rest.\n").strip().lower()

                match crime1_supreme_knowledge:
                #Second Case
                    case "a":
                        print("\nOh yeah! With your amazing power, you have successfully defeated the villains, but now you have to rest since you are tired. While you were resting, the infamous bank robbers robbed all the banks of the city. You are being criticized by the city now.")
                        
                        while True:

                            crime2_supreme_knowledge = input("\nNow that criminals know about your awesome wisdom, they are now using molten a radiating machine that makes a person significantly lose their knowledge to overpower you. What will you do now to defeat these criminals?\nA: Go full ambush and try to defeat them.\nB: Why fight when you can watch Sunday Night Football and stay home.\nC. Consult scientists and other people, or don't because you are the supreme knowledge holder, and design a material that sends the radiating waves back at the villains so that you can win your next battle.\n").strip().lower()

                            match crime2_supreme_knowledge:
                            #Third Case
                                case "a":
                                    print("\nUh oh!!! That was a total falure! The criminals outnumbered you and outpowered you! You have been defeated. Try a different strategy.")
                                    continue
                            #Third Case
                                case "b":
                                    print("\nNo no no. The city hates you now! Do better next time.")

                                    while True:
                                
                                        crime3_supreme_knowledge = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicopter? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a machine that gives them the abilities to predict future and about equal knowledge to you. You will lose your ability to be super strong once this happens. What will you do:\nA: It's ok, with them smart, I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Create a machine that nullifies their machine.\n").strip().lower()

                                        match crime3_supreme_knowledge:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting...again! You have been resting, and resting. City despises you now, once again. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case "c":
                                    print("\nGood choice! Finding ways to outsmart the criminals is a signature move. But now that you do that, the city criticizes you more becuase the criminals escaped and you made no effort to stop them.")

                                    while True:
                                
                                        crime3_supreme_knowledge = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicopter? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a machine that gives them the abilities to predict future and about equal knowledge to you. You will lose your ability to be super strong once this happens. What will you do:\nA: It's ok, with them smart, I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Create a machine that nullifies their machine.\n").strip().lower()

                                        match crime3_supreme_knowledge:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting! You have been resting, and resting. City despises you now. Although you have done good for some crimes, the city does not want you as their superhero. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case _:
                                    print("\nNope. A, B, or C\n")
                                    continue

                            break
                #Second Case
                    case "b":
                        print("\nYou have gained enough rest, but the city has been criticizing you for not helping defeat the jailbreakers.")

                        while True:

                            crime2_supreme_knowledge = input("\nNow that criminals know about your awesome wisdom, they are now using molten a radiating machine that makes a person significantly lose their knowledge to overpower you. What will you do now to defeat these criminals?\nA: Go full ambush and try to defeat them.\nB: Why fight when you can watch Sunday Night Football and stay home.\nC. Consult scientists and other people, or don't because you are the supreme knowledge holder, and design a material that sends the radiating waves back at the villains so that you can win your next battle.\n").strip().lower()

                            match crime2_super_strength:
                            #Third Case
                                case "a":
                                    print("\nUh oh!!! That was a total falure! The criminals outnumbered you and outpowered you! You have been defeated. Try a different strategy.")
                                    continue
                            #Third Case
                                case "b":
                                    print("\nNo no no. Resting for many crimes in a row!!! The city despises you, make them feel better.")

                                    while True:
                                
                                        crime3_supreme_knowledge = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicopter? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a machine that gives them the abilities to predict future and about equal knowledge to you. You will lose your ability to be super strong once this happens. What will you do:\nA: It's ok, with them smart, I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Create a machine that nullifies their machine.\n").strip().lower()

                                        match crime3_supreme_knowledge:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting...again! You have been resting, and resting. City despises you now, once again. You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case "c":
                                    print("\nGood choice! Finding ways to outsmart the criminals is a signature move. But now that you do that, the city criticizes you more becuase the criminals escaped and you made no effort to stop them.")

                                    while True:
                                
                                        crime3_supreme_knowledge = input("\n Let's go to the next crime: There are 4 criminals that are trying to steal a...helicoptor? (I don't know why they wanted to steal that, but anyways) You have to fight them and take them down. At first glance, four people may look easy to beat, but they are armed with a machine that gives them the abilities to predict future and about equal knowledge to you. You will lose your ability to be super strong once this happens. What will you do:\nA: It's ok, with them smart, I'm still strong, let's go and fight!\nB: Nope, I'm out. I just want to play Spiderman in Playstation man. I would prefer being a hero in a game than in real life.\nC: Create a machine that nullifies their machine.\n").strip().lower()

                                        match crime3_supreme_knowledge:
                                        #Fourth Case
                                            case "a":
                                                print("\nNope, that plan failed. Try again.\n")
                                                continue
                                        #Fourth Case
                                            case "b":
                                                print("\nMan, resting...again! You have been resting, and resting. City despises you now, once again. Although you upgraded your tech, you did not use it! You have failed miserably as a superhero.\n")
                                        #Fourth Case
                                            case "c":
                                                print("\nWonderful, this was the right choice! Now, after this crime, you are fighting off villains as if they are a piece of cake. Good job, you have earned your place as a superhero.\n")
                                        #Fourth Case:
                                            case _:
                                                print("\nNope. A, B, or C\n")
                                                continue
                                        break
                            #Third Case
                                case _:
                                    print("\nNope. A, B, or C\n")
                                    continue

                            break         
                #Second Case
                    case _:
                        print("\nNope, A or B\n")
                        continue

                break

#First Case
        case _:
            print("\nNope. A, B, or C.\n")
            continue
    
    break



while True:

    finish = input("\nYou have finished the game, what do you want to do?\nA: Play again with different powers and situations\nB: Finish the game.\n").strip().lower()

    match finish:
    #Finish
        case "a":
            print("\nHit run again!")
    #Finish
        case "b":
            print("\nGood job finishing your game!")
    #Finish
        case _:
            print("\nNope, A or B.\n")
            continue
        
    break