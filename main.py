import random
import os
#start 17.11.26

#variables

#universal variables

    #resources
gold   = 0  
credit = 0  
freexp = 0 
    #busters
battle_xp_buster_tier_IV = 0
crew_xp_buster_tier_IV = 0
credit_buster_tier_IV = 0
reloading_equipment_buster_tier_IV = 0
freexp_buster_tier_IV = 0

battle_xp_buster_tier_III = 0
crew_xp_buster_tier_III = 0
credit_buster_tier_III = 0
reloading_equipment_buster_tier_III = 0
freexp_buster_tier_III = 0

battle_xp_buster_tier_II = 0
crew_xp_buster_tier_II = 0
credit_buster_tier_II = 0
reloading_equipment_buster_tier_II = 0
freexp_buster_tier_II = 0

battle_xp_buster_tier_I = 0
crew_xp_buster_tier_I = 0
credit_buster_tier_I = 0
reloading_equipment_buster_tier_I = 0
freexp_buster_tier_I = 0

    #special items
tankcoin = 0
riddle = 0
premium_account = 0
key_to_a_locked_container = 0

mystical_certificate = 0
mystificate = 0
    #Bust
x10bust = 0
x5bust = 0
x4bust = 0
x3bust = 0

    #XP_certificate
certificate_200xp = 0
certificate_2300xp = 0
certificate_28000xp = 0
certificate_350000xp = 0

    #other_containers
guardian_of_the_seas_container = 0
honey_container = 0
supernova_container = 0
bright_image_container = 0
collect_them_all_container = 0
black_box_I = 0
surprise_container = 0
mystical_container_I = 0

#mystical_container_I_vsariables
mystical_container_II_from_mystical_container_I = 0
mystical_container_III_from_mystical_container_I = 0
mystical_container_I_avatar = 0


#mystical_container_II_variables
mystical_container_III_from_mystical_container_II = 0
mystical_container_II_avatar = 0

#mystical_container_III_variables
mystical_container_III_avatar = 0
profile_background_from_mystical_container_III = 0
megamystical_container_from_mystical_container_III = 0

#mystical_container_IV_variables
mystical_container_IV_avatar = 0
profile_background_from_mystical_container_IV = 0
kill_visor_body_kit_from_mystical_container_IV = 0


#simple_space_container_variables
tanks_chance_0_16_from_simple_space_container = [
    "M-IV-Y", "Объект 274а", "Дракула", "Хельсинг", "Крушитель",
    "Chieftain Mk. 6", "Carro 45t", "Kpz 50 t", "VK 90.01 (P)",
    "Concept 1B", "O6. 907", "T-22 ср.", "Объект 268/4", "K-91", "Объект 752",
    "WZ-120-1G FT", "WZ-122 TM", "Škoda T 56", "Progetto 46", "Lansen C",
    "B-C Bourrasque", "AMX CDA 105", "Skorpion G", "M48A2 Räumpanzer",
    "Keiler", "Type 57", "Titan-54d", "GSOR 1008", "Action X", "Chimera", "T77"
]
tanks_chance_0_08_from_simple_space_container = [
    "Уничтожитель",
    "Strv K"
]



#mystical_container_I_opening
def mystical_container_I_opening():
    global mystical_container_II_from_mystical_container_I
    global mystical_container_III_from_mystical_container_I
    global mystical_container_I_avatar , mystical_certificate
    global gold, credit, freexp
    global x3bust , certificate_200xp
    while True:

        open_containers_count = int(input('Input_count_of_containers_to_open: '))
        for i in range(open_containers_count):

            #mystical_container_I XP
            if random.randint(1, 100) <= 20:
                random_num_xp = round(random.uniform(0 , 99) , 2)
                if random_num_xp <= 0.1:
                    freexp += 500000
                elif random_num_xp <= 0.65:
                    freexp += 100000
                elif random_num_xp <= 2.5:
                    freexp += 30000
                elif random_num_xp <= 7.9:
                    freexp += 10000
                elif random_num_xp <= 18.75:
                    freexp += 7000
                elif random_num_xp <= 45.85:
                    freexp += 4000
                else:
                    freexp += 2000

            #mystical_container_I credit
            if random.randint(1, 100) <= 10: 
                random_num_credit = random.uniform(0, 100)
                if random_num_credit <= 0.5:
                    credit += 1000000
                elif random_num_credit <= 5.2:
                    credit += 500000
                elif random_num_credit <= 14.5:
                    credit += 200000
                elif random_num_credit <= 29.9:
                    credit += 100000
                elif random_num_credit <= 53.3:
                    credit += 75000
                else: 
                    credit += 50000

            if random.randint(1, 100) <= 15:
                
                if random.uniform(0, 100) <= 8.8235: gold += 0
                if random.uniform(0, 100) <= 8.8235: gold += 1
                if random.uniform(0, 100) <= 8.8235: gold += 2
                if random.uniform(0, 100) <= 8.8235: gold += 3
                if random.uniform(0, 100) <= 8.8235: gold += 4
                if random.uniform(0, 100) <= 8.8235: gold += 5
                if random.uniform(0, 100) <= 8.8235: gold += 6
                if random.uniform(0, 100) <= 8.8235: gold += 7
                if random.uniform(0, 100) <= 8.8235: gold += 8
                if random.uniform(0, 100) <= 8.8235: gold += 9

                if random.uniform(0, 100) <= 9.8235: gold += 10
                if random.uniform(0, 100) <= 9.8235: gold += 20
                if random.uniform(0, 100) <= 9.8235: gold += 30
                if random.uniform(0, 100) <= 9.8235: gold += 40
                if random.uniform(0, 100) <= 9.8235: gold += 50
                if random.uniform(0, 100) <= 9.8235: gold += 60
                if random.uniform(0, 100) <= 9.8235: gold += 70
                if random.uniform(0, 100) <= 9.8235: gold += 80
                if random.uniform(0, 100) <= 9.8235: gold += 90

                if random.uniform(0, 100) <= 9.8235: gold += 100
                if random.uniform(0, 100) <= 9.8235: gold += 200
                if random.uniform(0, 100) <= 9.8235: gold += 300
                if random.uniform(0, 100) <= 9.8235: gold += 400
                if random.uniform(0, 100) <= 9.8235: gold += 500
                if random.uniform(0, 100) <= 9.8235: gold += 600
                if random.uniform(0, 100) <= 9.8235: gold += 700
                if random.uniform(0, 100) <= 9.8235: gold += 800
                if random.uniform(0, 100) <= 9.8235: gold += 900

                if random.uniform(0, 100) <= 1.0: gold += 1000
                if random.uniform(0, 100) <= 1.0: gold += 2000
                if random.uniform(0, 100) <= 1.0: gold += 3000
                if random.uniform(0, 100) <= 1.0: gold += 4000
                if random.uniform(0, 100) <= 1.0: gold += 5000
                if random.uniform(0, 100) <= 1.0: gold += 6000
                if random.uniform(0, 100) <= 1.0: gold += 7000
                if random.uniform(0, 100) <= 1.0: gold += 8000
                if random.uniform(0, 100) <= 1.0: gold += 9000

                if random.uniform(0, 100) <= 0.0047: gold += 10000

                if gold < 100:
                    gold += 100

            #mystical_container_II_from_mystical_container_I
            if random.randint(1, 100) <= 5:
                mystical_container_II_from_mystical_container_I += 1

            #mystical_container_III_from_mystical_container_I
            if random.randint(1, 100) <= 2:
                mystical_container_III_from_mystical_container_I += 1

            #mystical_container_I_avatar
            if random.randint(1, 100) == 1:
                mystical_container_I_avatar += 1

            #mystical_certificate
            if random.randint(1, 100) <= 5:
                mystical_certificate += 1

            x3bust = open_containers_count
            certificate_200xp = open_containers_count * 2
            
        print("\n    RESULTS:")
        dropped = []
        if mystical_container_II_from_mystical_container_I > 0: dropped.append(f"    Mystical Container II: {mystical_container_II_from_mystical_container_I}")
        if mystical_container_III_from_mystical_container_I > 0: dropped.append(f"    Mystical Container III: {mystical_container_III_from_mystical_container_I}")
        if mystical_container_I_avatar > 0: dropped.append(f"    Mystical Container I Avatar: {mystical_container_I_avatar}")
        if gold > 0: dropped.append(f"    Gold: {gold}")
        if credit > 0: dropped.append(f"    Credit: {credit}")
        if freexp > 0: dropped.append(f"    Free XP: {freexp}")
        if mystical_certificate > 0: dropped.append(f"    Mystical Certificate: {mystical_certificate}")
        if x3bust > 0: dropped.append(f"    X3bust: {x3bust}")
        if certificate_200xp > 0: dropped.append(f"    Certificate_200xp: {certificate_200xp}")
        
        for item in dropped: print(item)
        print()
        
        freexp , credit , gold = 0 , 0 , 0
        mystical_container_II_from_mystical_container_I , mystical_container_III_from_mystical_container_I = 0 , 0
        mystical_container_I_avatar = 0
        mystical_certificate = 0
        if open_containers_count == 0:  
            break


#mystical_container_II_opening
def mystical_container_II():
    global gold, credit, freexp
    global mystical_container_III_from_mystical_container_II , mystical_container_II_avatar
    global mystical_certificate , x4bust , Certificate_2300xp
    global riddle , tankcoin , premium_account
    global mystical_container_II_avatar
    global certificate_2300xp

    while True:
        open_containers_count = int(input('Input_count_of_containers_to_open: '))
        for i in range(open_containers_count):

            #mystical_container_II_XP
            if random.randint(1, 100) <= 20:
                random_num_xp = round(random.uniform(0, 99), 2)
                if random_num_xp <= 54.05:
                    freexp += 2000
                elif random_num_xp <= 81.10: 
                    freexp += 4000
                elif random_num_xp <= 91.90: 
                    freexp += 7000
                elif random_num_xp <= 97.30:  
                    freexp += 10000
                elif random_num_xp <= 99.15:  
                    freexp += 30000
                elif random_num_xp <= 99.70:  
                    freexp += 100000
                elif random_num_xp <= 99.90:  
                    freexp += 500000
                else:                         
                    freexp += 750000   

            #mystical_container_II_credit
            if random.randint(1, 100) <= 15: 
                random_num_credit = round(random.uniform(0, 100), 2)
                
                if random_num_credit <= 46.76:
                    credit += 50000
                elif random_num_credit <= 70.11:   
                    credit += 75000
                elif random_num_credit <= 85.52:   
                    credit += 100000
                elif random_num_credit <= 94.86:   
                    credit += 200000
                elif random_num_credit <= 99.53:  
                    credit += 500000
                else:                              
                    credit += 1000000

            #mystical_container_II_Gold
            if random.randint(1, 100) <= 15:
                
                if random.uniform(0, 100) <= 10.0000: gold += 0
                if random.uniform(0, 100) <= 10.0000: gold += 1
                if random.uniform(0, 100) <= 10.0000: gold += 2
                if random.uniform(0, 100) <= 10.0000: gold += 3
                if random.uniform(0, 100) <= 10.0000: gold += 4
                if random.uniform(0, 100) <= 10.0000: gold += 5
                if random.uniform(0, 100) <= 10.0000: gold += 6
                if random.uniform(0, 100) <= 10.0000: gold += 7
                if random.uniform(0, 100) <= 10.0000: gold += 8
                if random.uniform(0, 100) <= 10.0000: gold += 9

                if random.uniform(0, 100) <= 11.1176: gold += 10
                if random.uniform(0, 100) <= 11.1176: gold += 20
                if random.uniform(0, 100) <= 11.1176: gold += 30
                if random.uniform(0, 100) <= 11.1176: gold += 40
                if random.uniform(0, 100) <= 11.1176: gold += 50
                if random.uniform(0, 100) <= 11.1176: gold += 60
                if random.uniform(0, 100) <= 11.1176: gold += 70
                if random.uniform(0, 100) <= 11.1176: gold += 80
                if random.uniform(0, 100) <= 11.1176: gold += 90

                if random.uniform(0, 100) <= 11.1176: gold += 100
                if random.uniform(0, 100) <= 11.1176: gold += 200
                if random.uniform(0, 100) <= 11.1176: gold += 300
                if random.uniform(0, 100) <= 11.1176: gold += 400
                if random.uniform(0, 100) <= 11.1176: gold += 500
                if random.uniform(0, 100) <= 11.1176: gold += 600
                if random.uniform(0, 100) <= 11.1176: gold += 700
                if random.uniform(0, 100) <= 11.1176: gold += 800
                if random.uniform(0, 100) <= 11.1176: gold += 900

                if random.uniform(0, 100) <= 0.7647: gold += 1000
                if random.uniform(0, 100) <= 0.7647: gold += 2000
                if random.uniform(0, 100) <= 0.7647: gold += 3000
                if random.uniform(0, 100) <= 0.7647: gold += 4000
                if random.uniform(0, 100) <= 0.7647: gold += 5000
                if random.uniform(0, 100) <= 0.7647: gold += 6000
                if random.uniform(0, 100) <= 0.7647: gold += 7000
                if random.uniform(0, 100) <= 0.7647: gold += 8000
                if random.uniform(0, 100) <= 0.7647: gold += 9000

                if random.uniform(0, 100) <= 0.4706: gold += 10000
                if random.uniform(0, 100) <= 0.2353: gold += 20000
                
                if random.uniform(0, 100) <= 0.0471: gold += 30000
                if random.uniform(0, 100) <= 0.0471: gold += 40000
                if random.uniform(0, 100) <= 0.0471: gold += 50000
                if random.uniform(0, 100) <= 0.0471: gold += 60000
                if random.uniform(0, 100) <= 0.0471: gold += 70000
                if random.uniform(0, 100) <= 0.0471: gold += 80000
                if random.uniform(0, 100) <= 0.0471: gold += 90000

                if random.uniform(0, 100) <= 0.0012: gold += 100000

                if gold < 100:
                    gold += 100

            #mystical_container_II_riddle
            if random.randint(1, 100) <= 10:
                riddle += 1

            #mystical_container_III_from_mystical_container_II
            if random.randint(1, 100) <= 5:
                mystical_container_III_from_mystical_container_II += 1

            #mystical_container_II_avatar
            if random.randint(1, 100) == 1:
                mystical_container_II_avatar += 1

            #mystical_certificate
            if random.randint(1, 100) <= 5:
                mystical_certificate += 1

            #tankcoin
            if random.uniform(0, 100) <= 0.01:
                tankcoin += 1

            #mystical_container_II_premium_account
            if random.randint(1, 100) <= 10:
                random_num_premium = random.uniform(0, 100)
                if random_num_premium <= 60.00:
                    premium_account += 1               
                elif random_num_premium <= 90.00:
                    premium_account += 2                  
                elif random_num_premium <= 100.00:
                    premium_account += 3

            #mystical_container_II_X4bust
            if random.randint(1, 100) <= 100:
                random_num_x4bust = random.randint(0, 99)
                if random_num_x4bust <= 50:
                    x4bust += 1
                else:
                    x4bust += 2

            #mystical_container_II_Certificate_2300xp
            if random.randint(1, 100) <= 100:
                random_num_certificate_2300xp = random.randint(0, 99)
                if random_num_certificate_2300xp <= 50:
                    certificate_2300xp += 1
                else:
                    certificate_2300xp += 2

        print("\n    RESULTS:")
        dropped = []
        if mystical_container_III_from_mystical_container_II > 0: dropped.append(f"    Mystical Container III: {mystical_container_III_from_mystical_container_II}")
        if mystical_container_II_avatar > 0: dropped.append(f"    Mystical Container II Avatar: {mystical_container_II_avatar}")
        if gold > 0: dropped.append(f"    Gold: {gold}")
        if credit > 0: dropped.append(f"    Credit: {credit}")
        if freexp > 0: dropped.append(f"    Free XP: {freexp}")
        if mystical_certificate > 0: dropped.append(f"    Mystical Certificate: {mystical_certificate}")
        if riddle > 0: dropped.append(f"    Riddle: {riddle}")
        if tankcoin > 0: dropped.append(f"    Tankcoin: {tankcoin}")
        if premium_account > 0: dropped.append(f"    Premium Account: {premium_account}")
        if x4bust > 0: dropped.append(f"    X4bust: {x4bust}")
        if certificate_2300xp > 0: dropped.append(f"    Certificate_2300xp: {certificate_2300xp}")

        for item in dropped: print(item)
        print()
        
        freexp , credit , gold = 0 , 0 , 0
        mystical_container_III_from_mystical_container_II , mystical_container_II_avatar = 0 , 0
        mystical_certificate = 0
        riddle = 0
        tankcoin = 0
        premium_account = 0
        x4bust = 0
        certificate_2300xp = 0
        if open_containers_count == 0:  
            break


#mystical_container_III_opening
def mystical_container_III():
    global gold, credit, freexp
    global mystical_container_III_avatar , mystical_certificate , megamystical_container_from_mystical_container_III , profile_background_from_mystical_container_III
    global riddle , tankcoin , premium_account
    global x5bust , certificate_28000xp
    while True:
        open_containers_count = int(input('Input_count_of_containers_to_open: '))
        for i in range(open_containers_count):

            #mystical_container_III_XP
            if random.randint(1, 100) <= 20:
                random_num_xp = round(random.uniform(0, 100), 2)
                if random_num_xp <= 53.85:
                    freexp += 2000
                elif random_num_xp <= 80.80:   
                    freexp += 4000
                elif random_num_xp <= 91.60:   
                    freexp += 7000
                elif random_num_xp <= 97.00:   
                    freexp += 10000
                elif random_num_xp <= 98.85:   
                    freexp += 30000
                elif random_num_xp <= 99.40:   
                    freexp += 100000
                elif random_num_xp <= 99.70:   
                    freexp += 500000
                elif random_num_xp <= 99.90:   
                    freexp += 750000
                else:                          
                    freexp += 1000000

            #mystical_container_III_credit 
            if random.randint(1, 100) <= 20: 
                random_num_credit = round(random.uniform(0, 100), 2)
                
                if random_num_credit <= 46.80:
                    credit += 100000
                elif random_num_credit <= 70.15:   
                    credit += 150000
                elif random_num_credit <= 85.55:   
                    credit += 200000
                elif random_num_credit <= 94.90:  
                    credit += 500000
                elif random_num_credit <= 99.55:   
                    credit += 1000000
                else:                              
                    credit += 2000000

            #mystical_container_III_gold          
            if random.randint(1, 100) <= 25:
                
                if random.uniform(0, 100) <= 2.9589: gold += 0
                if random.uniform(0, 100) <= 2.9589: gold += 1
                if random.uniform(0, 100) <= 2.9589: gold += 2
                if random.uniform(0, 100) <= 2.9589: gold += 3
                if random.uniform(0, 100) <= 2.9589: gold += 4
                if random.uniform(0, 100) <= 2.9589: gold += 5
                if random.uniform(0, 100) <= 2.9589: gold += 6
                if random.uniform(0, 100) <= 2.9589: gold += 7
                if random.uniform(0, 100) <= 2.9589: gold += 8
                if random.uniform(0, 100) <= 2.9589: gold += 9

                if random.uniform(0, 100) <= 3.2903: gold += 10
                if random.uniform(0, 100) <= 3.2903: gold += 20
                if random.uniform(0, 100) <= 3.2903: gold += 30
                if random.uniform(0, 100) <= 3.2903: gold += 40
                if random.uniform(0, 100) <= 3.2903: gold += 50
                if random.uniform(0, 100) <= 3.2903: gold += 60
                if random.uniform(0, 100) <= 3.2903: gold += 70
                if random.uniform(0, 100) <= 3.2903: gold += 80
                if random.uniform(0, 100) <= 3.2903: gold += 90

                if random.uniform(0, 100) <= 3.2903: gold += 100
                if random.uniform(0, 100) <= 3.2903: gold += 200
                if random.uniform(0, 100) <= 3.2903: gold += 300
                if random.uniform(0, 100) <= 3.2903: gold += 400
                if random.uniform(0, 100) <= 3.2903: gold += 500
                if random.uniform(0, 100) <= 3.2903: gold += 600
                if random.uniform(0, 100) <= 3.2903: gold += 700
                if random.uniform(0, 100) <= 3.2903: gold += 800
                if random.uniform(0, 100) <= 3.2903: gold += 900

                if random.uniform(0, 100) <= 1.1481: gold += 1000
                if random.uniform(0, 100) <= 1.1481: gold += 2000
                if random.uniform(0, 100) <= 1.1481: gold += 3000
                if random.uniform(0, 100) <= 1.1481: gold += 4000
                if random.uniform(0, 100) <= 1.1481: gold += 5000
                if random.uniform(0, 100) <= 1.1481: gold += 6000
                if random.uniform(0, 100) <= 1.1481: gold += 7000
                if random.uniform(0, 100) <= 1.1481: gold += 8000
                if random.uniform(0, 100) <= 1.1481: gold += 9000

                if random.uniform(0, 100) <= 0.4024: gold += 10000
                if random.uniform(0, 100) <= 0.2012: gold += 20000

                if random.uniform(0, 100) <= 0.0355: gold += 30000
                if random.uniform(0, 100) <= 0.0355: gold += 40000
                if random.uniform(0, 100) <= 0.0355: gold += 50000
                if random.uniform(0, 100) <= 0.0355: gold += 60000
                if random.uniform(0, 100) <= 0.0355: gold += 70000
                if random.uniform(0, 100) <= 0.0355: gold += 80000
                if random.uniform(0, 100) <= 0.0355: gold += 90000

                if random.uniform(0, 100) <= 0.0012: gold += 100000

                if gold < 100:
                    gold += 100

            #mystical_container_III_premium_account
            if random.randint(1, 100) <= 20:
                random_num_premium = random.uniform(0, 100)
                if random_num_premium <= 60.00:
                    premium_account += 1               
                elif random_num_premium <= 90.00:
                    premium_account += 3                  
                elif random_num_premium <= 100.00:
                    premium_account += 7

            #mystical_container_III_riddle
            if random.randint(1, 100) <= 25:
                riddle += 1

            #mystical_container_III_tankcoin
            if random.uniform(0, 100) <= 0.01:
                tankcoin += 1

            #mystical_container_III_avatar_and_profile_background
            if random.randint(1, 100) <= 3:
                if random.randint(1, 100) <= 50:
                    mystical_container_III_avatar += 1
                else:
                    profile_background_from_mystical_container_III += 1

            #mystical_container_III_mystical_certificate
            if random.randint(1, 100) <= 7:
                mystical_certificate += 1

            #megamystical_container_from_mystical_container_III
            if random.randint(1, 100) <= 5:
                megamystical_container_from_mystical_container_III += 1

            #mystical_container_certificate_28000xp
            certificate_28000xp = open_containers_count

            #mystical_container_III_x5bust
            if random.randint(1, 100) <= 100:
                random_num_x5bust = random.randint(0, 99)
                if random_num_x5bust <= 33:
                    x5bust += 1
                elif random_num_x5bust <= 66:
                    x5bust += 2
                else:
                    x5bust += 3

        print("\n    RESULTS:")
        dropped = []
        if mystical_container_III_avatar > 0: dropped.append(f"    Mystical Container III Avatar: {mystical_container_III_avatar}")
        if profile_background_from_mystical_container_III > 0: dropped.append(f"    Mystical Container III Profile Background: {profile_background_from_mystical_container_III}")
        if mystical_certificate > 0: dropped.append(f"    Mystical Certificate: {mystical_certificate}")
        if megamystical_container_from_mystical_container_III > 0: dropped.append(f"    Megamystical Container: {megamystical_container_from_mystical_container_III}")
        if gold > 0: dropped.append(f"    Gold: {gold}")
        if credit > 0: dropped.append(f"    Credit: {credit}")
        if freexp > 0: dropped.append(f"    Free XP: {freexp}")
        if riddle > 0: dropped.append(f"    Riddle: {riddle}")
        if tankcoin > 0: dropped.append(f"    Tankcoin: {tankcoin}")
        if premium_account > 0: dropped.append(f"    Premium Account: {premium_account}")
        if x5bust > 0: dropped.append(f"    X5bust: {x5bust}")
        if certificate_28000xp > 0: dropped.append(f"    Certificate_28000xp: {certificate_28000xp}")

        for item in dropped: print(item)
        print()

        freexp , credit , gold = 0 , 0 , 0
        mystical_container_III_avatar , mystical_certificate = 0 , 0
        profile_background_from_mystical_container_III = 0
        megamystical_container_from_mystical_container_III = 0
        riddle , tankcoin , premium_account = 0 , 0 , 0
        x5bust , certificate_28000xp = 0 , 0
        if open_containers_count == 0:
            break


def mystical_container_IV():
    global gold, credit, freexp
    global battle_xp_buster_tier_IV, crew_xp_buster_tier_IV, credit_buster_tier_IV, reloading_equipment_buster_tier_IV, freexp_buster_tier_IV
    global tankcoin, riddle, premium_account
    global mystificate, x10bust
    global certificate_28000xp, certificate_350000xp
    global guardian_of_the_seas_container, honey_container, supernova_container, bright_image_container
    global mystical_container_IV_avatar, profile_background_from_mystical_container_IV, kill_visor_body_kit_from_mystical_container_IV

    while True:
        open_containers_count = int(input('Input_count_of_containers_to_open: '))
        for i in range(open_containers_count):

            #mystical_container_IV_XP
            if random.randint(1, 100) <= 39:
                random_num_xp = round(random.uniform(0, 100), 2)
                if random_num_xp <= 64.10:
                    freexp += 10000
                elif random_num_xp <= 85.89:
                    freexp += 30000
                elif random_num_xp <= 92.30:
                    freexp += 100000
                elif random_num_xp <= 96.15:
                    freexp += 500000
                elif random_num_xp <= 98.71:
                    freexp += 750000
                else:
                    freexp += 1000000

            #mystical_container_IV_credit
            if random.randint(1, 100) <= 21: 
                random_num_credit = round(random.uniform(0, 100), 2)
                
                if random_num_credit <= 46.71:
                    credit += 100000
                elif random_num_credit <= 70.09:
                    credit += 250000
                elif random_num_credit <= 85.52:
                    credit += 500000
                elif random_num_credit <= 94.85:
                    credit += 1000000
                elif random_num_credit <= 99.52:
                    credit += 2000000
                else:
                    credit += 5000000

            #mystical_container_IV_gold
            if random.randint(1, 100) <= 25:
                random_num_gold = round(random.uniform(0, 100), 2)
                
                if random_num_gold <= 54.38:
                    gold += 1000
                elif random_num_gold <= 81.57:
                    gold += 2500
                elif random_num_gold <= 92.45:
                    gold += 5000
                elif random_num_gold <= 96.11:
                    gold += 10000
                elif random_num_gold <= 97.97:
                    gold += 15000
                elif random_num_gold <= 99.06:
                    gold += 25000
                elif random_num_gold <= 99.60:
                    gold += 50000
                elif random_num_gold <= 99.83:
                    gold += 100000
                elif random_num_gold <= 99.94:
                    gold += 250000
                else:
                    gold += 500000

            #mystical_container_IV_premium_account
            if random.randint(1, 100) <= 50:
                random_num_premium = round(random.uniform(0, 100), 2)
                if random_num_premium <= 60.00:
                    premium_account += 3
                elif random_num_premium <= 90.00:
                    premium_account += 9
                else:
                    premium_account += 15

            #mystical_container_IV_riddle
            if random.randint(1, 100) <= 25:
                riddle += 1

            #mystical_container_IV_tankcoin
            if random.uniform(0, 100) <= 0.05:
                tankcoin += 1

            #mystical_container_IV_avatar_and_profile_background
            if random.randint(1, 100) <= 3:
                if random.randint(1, 100) <= 50:
                    mystical_container_IV_avatar += 1
                else:
                    profile_background_from_mystical_container_IV += 1

            #mystificate and containers from mystical_container_IV
            if random.randint(1, 100) <= 20:
                random_num_containers_from_mystical_container_IV = random.randint(1, 4)
                if random_num_containers_from_mystical_container_IV == 1:
                    mystificate += 1
                elif random_num_containers_from_mystical_container_IV == 2:
                    guardian_of_the_seas_container += 1
                elif random_num_containers_from_mystical_container_IV == 3:
                    honey_container += 1
                else: 
                    supernova_container += 1

            #mystical_container_IV_kill_visor_body_kit
            if random.randint(1, 100) <= 35:
                kill_visor_body_kit_from_mystical_container_IV += 1

            #mystical_container_IV_certificate_350000xp
            if random.randint(1, 100) <= 3.23:
                certificate_350000xp += 1

            #mystical_container_IV_busters
            random_num_buster = random.randint(1,100)
            
            if random_num_buster <= 20: #credit_buster
                random_num_credit_booster = round(random.uniform(0, 100), 2)
                if random_num_credit_booster <= 52.65:
                    credit_buster_tier_IV += 1
                elif random_num_credit_booster <= 78.95:
                    credit_buster_tier_IV += 3
                elif random_num_credit_booster <= 94.75:
                    credit_buster_tier_IV += 5
                else:
                    credit_buster_tier_IV += 10

            elif random_num_buster <= 40: #freexp_buster
                random_num_freexp_booster = round(random.uniform(0, 100), 2)
                if random_num_freexp_booster <= 52.65:
                    freexp_buster_tier_IV += 1
                elif random_num_freexp_booster <= 78.95:
                    freexp_buster_tier_IV += 3
                elif random_num_freexp_booster <= 94.75:
                    freexp_buster_tier_IV  += 5
                else:
                    freexp_buster_tier_IV += 10

            elif random_num_buster <= 60: #reloading_equipment_buster
                random_num_equip_booster = round(random.uniform(0, 100), 2)
                if random_num_equip_booster <= 52.65:
                    reloading_equipment_buster_tier_IV += 1
                elif random_num_equip_booster <= 78.95:
                    reloading_equipment_buster_tier_IV += 3
                elif random_num_equip_booster <= 94.75:
                    reloading_equipment_buster_tier_IV += 5
                else:
                    reloading_equipment_buster_tier_IV += 10

            elif random_num_buster <= 80: #crew_xp_buster
                random_num_crew_booster = round(random.uniform(0, 100), 2)
                if random_num_crew_booster <= 52.65:
                    crew_xp_buster_tier_IV += 1
                elif random_num_crew_booster <= 78.95:
                    crew_xp_buster_tier_IV += 3
                elif random_num_crew_booster <= 94.75:
                    crew_xp_buster_tier_IV += 5
                else:
                    crew_xp_buster_tier_IV += 10

            else: #battle_xp_buster
                random_num_battle_xp_booster = round(random.uniform(0, 100), 2)
                if random_num_battle_xp_booster <= 52.65:
                    battle_xp_buster_tier_IV += 1
                elif random_num_battle_xp_booster <= 78.95:
                    battle_xp_buster_tier_IV += 3
                elif random_num_battle_xp_booster <= 94.75:
                    battle_xp_buster_tier_IV += 5
                else:
                    battle_xp_buster_tier_IV += 10

            #bright_image_container
            bright_image_container = open_containers_count

            #mystical_container_IV_certificate_28000xp
            if random.randint(1, 100) <= 32.36:
                certificate_28000xp += 2
            else:
                certificate_28000xp += 1

            #mystical_container_IV_x10bust
            random_num_x10bust = random.randint(1, 100)
            if random_num_x10bust <= 71.43:
                x10bust += 1
            elif random_num_x10bust <= 92.86:
                x10bust += 3
            else:
                x10bust += 5

        print("\n    RESULTS:")
        dropped = []
        if mystical_container_IV_avatar > 0: dropped.append(f"    Mystical Container IV Avatar: {mystical_container_IV_avatar}")
        if profile_background_from_mystical_container_IV > 0: dropped.append(f"    Mystical Container IV Profile Background: {profile_background_from_mystical_container_IV}")
        if kill_visor_body_kit_from_mystical_container_IV > 0: dropped.append(f"    Mystical Container IV Kill Visor Body Kit: {kill_visor_body_kit_from_mystical_container_IV}")
        if mystificate > 0: dropped.append(f"    Mystificate: {mystificate}")
        if guardian_of_the_seas_container > 0: dropped.append(f"    Guardian of the Seas Container: {guardian_of_the_seas_container}")
        if honey_container > 0: dropped.append(f"    Honey Container: {honey_container}")
        if supernova_container > 0: dropped.append(f"    Supernova Container: {supernova_container}")
        if credit > 0: dropped.append(f"    Credit: {credit}")
        if freexp > 0: dropped.append(f"    Free XP: {freexp}")
        if gold > 0: dropped.append(f"    Gold: {gold}")
        if riddle > 0: dropped.append(f"    Riddle: {riddle}")
        if tankcoin > 0: dropped.append(f"    Tankcoin: {tankcoin}")
        if premium_account > 0: dropped.append(f"    Premium Account: {premium_account}")
        if credit_buster_tier_IV > 0: dropped.append(f"    Credit Buster Tier IV: {credit_buster_tier_IV}")
        if freexp_buster_tier_IV > 0: dropped.append(f"    Free XP Buster Tier IV: {freexp_buster_tier_IV}")
        if reloading_equipment_buster_tier_IV > 0: dropped.append(f"    Reloading Equipment Buster Tier IV: {reloading_equipment_buster_tier_IV}")
        if crew_xp_buster_tier_IV > 0: dropped.append(f"    Crew XP Buster Tier IV: {crew_xp_buster_tier_IV}")
        if battle_xp_buster_tier_IV > 0: dropped.append(f"    Battle XP Buster Tier IV: {battle_xp_buster_tier_IV}")
        if certificate_350000xp > 0: dropped.append(f"    Certificate (350,000 XP): {certificate_350000xp}")
        if certificate_28000xp > 0: dropped.append(f"    Certificate (28,000 XP): {certificate_28000xp}")
        if bright_image_container > 0: dropped.append(f"    Bright Image Container: {bright_image_container}")
        if x10bust > 0: dropped.append(f"    X10bust: {x10bust}")
        
        for item in dropped: print(item)
        print()

        freexp , credit , gold = 0 , 0 , 0
        mystical_container_IV_avatar , profile_background_from_mystical_container_IV , kill_visor_body_kit_from_mystical_container_IV = 0 , 0 , 0
        mystificate , guardian_of_the_seas_container , honey_container , supernova_container = 0 , 0 , 0 , 0
        riddle , tankcoin , premium_account = 0 , 0 , 0
        credit_buster_tier_IV , freexp_buster_tier_IV , reloading_equipment_buster_tier_IV , crew_xp_buster_tier_IV , battle_xp_buster_tier_IV = 0 , 0 , 0 , 0 , 0
        certificate_28000xp , x10bust = 0 , 0 
        certificate_350000xp = 0
        bright_image_container = 0
        if open_containers_count == 0:  
            break


# collect_them_all_container = 0
# black_box_I = 0
# surprise_container = 0
# mystical_container_I = 0

#simple space container 
def simple_space_container():
    global gold, credit, freexp
    global mystical_container_I, collect_them_all_container, black_box_I, surprise_container
    global tankcoin, key_to_a_locked_container, certificate_200xp, certificate_2300xp, certificate_28000xp
    
    # Объявляем глобальными ВСЕ редкости бустеров
    global freexp_buster_tier_IV, credit_buster_tier_IV, crew_xp_buster_tier_IV, battle_xp_buster_tier_IV
    global freexp_buster_tier_III, credit_buster_tier_III, crew_xp_buster_tier_III, battle_xp_buster_tier_III
    global freexp_buster_tier_II, credit_buster_tier_II, crew_xp_buster_tier_II, battle_xp_buster_tier_II
    global freexp_buster_tier_I, credit_buster_tier_I, crew_xp_buster_tier_I, battle_xp_buster_tier_I
    
    global x3bust, x4bust, x5bust

    while True:
        try:
            open_containers_count = int(input('Input_count_of_containers_to_open: '))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        dropped_tanks_list = []
        
        for i in range(open_containers_count):

            # simple_space_container_XP
            if random.randint(1, 100) <= 33:
                random_num_xp = round(random.uniform(0, 100), 4)
                if random_num_xp <= 19.4849:
                    freexp += 200
                elif random_num_xp <= 38.9697:
                    freexp += 500
                elif random_num_xp <= 58.4545:
                    freexp += 1000
                elif random_num_xp <= 73.0909:
                    freexp += 2000
                elif random_num_xp <= 82.8485:
                    freexp += 5000
                elif random_num_xp <= 90.6364:
                    freexp += 10000
                elif random_num_xp <= 95.5152:
                    freexp += 15000
                elif random_num_xp <= 98.4546:
                    freexp += 20000
                elif random_num_xp <= 99.4243:
                    freexp += 50000
                elif random_num_xp <= 99.9091:
                    freexp += 100000
                elif random_num_xp <= 99.9697:
                    freexp += 250000
                elif random_num_xp <= 99.9879:
                    freexp += 500000
                else:
                    freexp += 1000000 

            # simple_space_container_gold
            if random.randint(1, 100) <= 50:
                random_num_gold = round(random.uniform(1, 100), 2)
                if random_num_gold <= 23.74:
                    gold += 100
                elif random_num_gold <= 42.74:
                    gold += 200
                elif random_num_gold <= 59.36:
                    gold += 500
                elif random_num_gold <= 73.60:
                    gold += 750
                elif random_num_gold <= 85.48:
                    gold += 1000
                elif random_num_gold <= 91.66:
                    gold += 1500
                elif random_num_gold <= 95.46:
                    gold += 3000
                elif random_num_gold <= 98.30:
                    gold += 5000
                elif random_num_gold <= 99.96:
                    gold += 10000
                else:
                    gold += 100000

            # simple_space_container_containers
            if random.randint(1, 100) <= 50:
                random_num_simple_space_containers = round(random.uniform(1, 100), 1)
                if random_num_simple_space_containers <= 25.0:
                    mystical_container_I += 1
                elif random_num_simple_space_containers <= 50.0:
                    collect_them_all_container += 1
                elif random_num_simple_space_containers <= 75.0:
                    black_box_I += 1
                else:
                    surprise_container += 1

            # simple_space_container_xpcertificates
            random_num_xp_certificate_simple_space_container = random.uniform(1, 100)
            if random_num_xp_certificate_simple_space_container <= 60.61:
                certificate_200xp += 3
            elif random_num_xp_certificate_simple_space_container <= 90.91:
                certificate_2300xp += 2
            else:
                certificate_28000xp += 1

            buster_roll = random.uniform(0, 100)

            if buster_roll <= 12.50:
                freexp_buster_tier_III += 15
            elif buster_roll <= 25.00:
                credit_buster_tier_III += 15
            elif buster_roll <= 37.50:
                crew_xp_buster_tier_III += 15
            elif buster_roll <= 50.00:
                battle_xp_buster_tier_III += 15

            elif buster_roll <= 58.33:
                freexp_buster_tier_II += 15
            elif buster_roll <= 66.66:
                credit_buster_tier_II += 15
            elif buster_roll <= 74.99:
                crew_xp_buster_tier_II += 15
            elif buster_roll <= 83.32:
                battle_xp_buster_tier_II += 15

            elif buster_roll <= 87.49:
                freexp_buster_tier_I += 15
            elif buster_roll <= 91.66:
                credit_buster_tier_I += 15
            elif buster_roll <= 95.83:
                crew_xp_buster_tier_I += 15
            else: # до 100.00%
                battle_xp_buster_tier_I += 15

            # simple_space_container_multipliers
            random_num_mult_simple_space_container = random.uniform(0, 100)
            if random_num_mult_simple_space_container <= 21.21:
                x3bust += 1
            elif random_num_mult_simple_space_container <= 36.36:
                x3bust += 2
            elif random_num_mult_simple_space_container <= 45.45:
                x3bust += 3
            elif random_num_mult_simple_space_container <= 63.63:
                x4bust += 1
            elif random_num_mult_simple_space_container <= 75.75:
                x4bust += 2
            elif random_num_mult_simple_space_container <= 81.81:
                x4bust += 3
            elif random_num_mult_simple_space_container <= 90.90:
                x5bust += 1
            elif random_num_mult_simple_space_container <= 96.96:
                x5bust += 2
            else:
                x5bust += 3

            # key_to_a_locked_container
            if random.randint(1, 100) <= 7:
                key_to_a_locked_container += 1

            # tankcoin
            if random.uniform(0, 100) <= 0.01:
                tankcoin += 1

            # tanks
            all_tanks = tanks_chance_0_16_from_simple_space_container + tanks_chance_0_08_from_simple_space_container
            tank_weights = [16] * len(tanks_chance_0_16_from_simple_space_container) + [8] * len(tanks_chance_0_08_from_simple_space_container)

            if random.uniform(0, 100) <= 5.12:
                dropped_tank = random.choices(all_tanks, weights=tank_weights, k=1)[0]
                dropped_tanks_list.append(dropped_tank)

        print("\n    RESULTS:")
        dropped = []
        
        if gold > 0: dropped.append(f"    Gold: {gold}")
        if freexp > 0: dropped.append(f"    Free XP: {freexp}")
        
        if mystical_container_I > 0: dropped.append(f"    Mystical Container I: {mystical_container_I}")
        if collect_them_all_container > 0: dropped.append(f"    Collect Them All Container: {collect_them_all_container}")
        if black_box_I > 0: dropped.append(f"    Black Box I: {black_box_I}")
        if surprise_container > 0: dropped.append(f"    Surprise Container: {surprise_container}")
        
        if key_to_a_locked_container > 0: dropped.append(f"    Key to a Locked Container: {key_to_a_locked_container}")
        if tankcoin > 0: dropped.append(f"    Tankcoin: {tankcoin}")
        
        if certificate_200xp > 0: dropped.append(f"    Certificate 200xp: {certificate_200xp}")
        if certificate_2300xp > 0: dropped.append(f"    Certificate 2300xp: {certificate_2300xp}")
        if certificate_28000xp > 0: dropped.append(f"    Certificate 28000xp: {certificate_28000xp}")
        
        if freexp_buster_tier_III > 0: dropped.append(f"    Free XP Buster Tier III: {freexp_buster_tier_III}")
        if credit_buster_tier_III > 0: dropped.append(f"    Credit Buster Tier III: {credit_buster_tier_III}")
        if crew_xp_buster_tier_III > 0: dropped.append(f"    Crew XP Buster Tier III: {crew_xp_buster_tier_III}")
        if battle_xp_buster_tier_III > 0: dropped.append(f"    Battle XP Buster Tier III: {battle_xp_buster_tier_III}")

        if freexp_buster_tier_II > 0: dropped.append(f"    Free XP Buster Tier II: {freexp_buster_tier_II}")
        if credit_buster_tier_II > 0: dropped.append(f"    Credit Buster Tier II: {credit_buster_tier_II}")
        if crew_xp_buster_tier_II > 0: dropped.append(f"    Crew XP Buster Tier II: {crew_xp_buster_tier_II}")
        if battle_xp_buster_tier_II > 0: dropped.append(f"    Battle XP Buster Tier II: {battle_xp_buster_tier_II}")

        if freexp_buster_tier_I > 0: dropped.append(f"    Free XP Buster Tier I: {freexp_buster_tier_I}")
        if credit_buster_tier_I > 0: dropped.append(f"    Credit Buster Tier I: {credit_buster_tier_I}")
        if crew_xp_buster_tier_I > 0: dropped.append(f"    Crew XP Buster Tier I: {crew_xp_buster_tier_I}")
        if battle_xp_buster_tier_I > 0: dropped.append(f"    Battle XP Buster Tier I: {battle_xp_buster_tier_I}")

        if x3bust > 0: dropped.append(f"    X3bust: {x3bust}")
        if x4bust > 0: dropped.append(f"    X4bust: {x4bust}")
        if x5bust > 0: dropped.append(f"    X5bust: {x5bust}")
        
        if dropped_tanks_list:
            dropped.append(f"    Tanks: {', '.join(dropped_tanks_list)}")

        for item in dropped: 
            print(item)
        print()

        gold = 0
        freexp = 0
        mystical_container_I = 0
        collect_them_all_container = 0
        black_box_I = 0
        surprise_container = 0
        key_to_a_locked_container = 0
        tankcoin = 0
        certificate_200xp = 0
        certificate_2300xp = 0
        certificate_28000xp = 0
        
        freexp_buster_tier_III = 0
        credit_buster_tier_III = 0
        crew_xp_buster_tier_III = 0
        battle_xp_buster_tier_III = 0

        freexp_buster_tier_II = 0
        credit_buster_tier_II = 0
        crew_xp_buster_tier_II = 0
        battle_xp_buster_tier_II = 0

        freexp_buster_tier_I = 0
        credit_buster_tier_I = 0
        crew_xp_buster_tier_I = 0
        battle_xp_buster_tier_I = 0
        
        x3bust = 0
        x4bust = 0
        x5bust = 0

        if open_containers_count == 0:  
            break


def show_container_contents():
    print('''
    =========================================
             CONTAINER CONTENTS
    =========================================
    1. Mystical Container I
    2. Mystical Container II
    3. Mystical Container III
    4. Mystical Container IV
    5. Simply Space Container
    0. Back to Main Menu
    ''')
    choice = input('Select_container_to_view: ')

    if choice == '1':
        print('''
    --- Mystical Container I ---
    XP (Chance: 20%):
      - 2000 (54.15%) | 4000 (27.10%) | 7000 (10.85%)
      - 10k (5.40%) | 30k (1.85%) | 100k (0.55%)
      - 500k (0.10%)
    Credits (Chance: 10%):
      - 50k (46.70%) | 75k (23.40%) | 100k (15.40%)
      - 200k (9.30%) | 500k (4.70%) | 1M (0.50%)
    Gold (Chance: 15%):
      - 0-9 (32.46%) | 10-90 (32.48%) | 100-900 (32.48%)
      - 1k-9k (2.23%) | 10k (0.15%) [Min Drop: 100 gold]
    Other:
      - Container II (5%) | Container III (2%)
      - Avatar (1%) | Mystical Certificate (5%)
    Guaranteed:
      - X3bust: 1 (100.00%)
      - Certificate_200xp: 2 (100.00%)
    ''')
    elif choice == '2':
        print('''
    --- Mystical Container II ---
    XP (Chance: 20%):
      - 2000 (54.05%) | 4000 (27.05%) | 7000 (10.80%)
      - 10k (5.40%) | 30k (1.85%) | 100k (0.55%)
      - 500k (0.20%) | 750k (0.10%)
    Credits (Chance: 15%):
      - 50k (46.76%) | 75k (23.35%) | 100k (15.41%)
      - 200k (9.34%) | 500k (4.67%) | 1M (0.47%)
    Gold (Chance: 15%):
      - 0-9 (32.46%) | 10-90 (32.48%) | 100-900 (32.48%)
      - 1k-9k (2.23%) | 10k (0.15%) | 20k (0.08%)
      - 30k-90k (0.11%) | 100k (rare) [Min Drop: 100 gold]
    Premium Account (Chance: 10%):
      - 1 Day (6.00%) | 2 Days (3.00%) | 3 Days (1.00%)
    Other:
      - Riddle (10%) | Container III (5%) | Avatar (1%)
      - Mystical Certificate (5%) | Tankcoin (0.01%)
    Guaranteed:
      - X4bust: 1 (51.00%) | 2 (49.00%)
      - Certificate_2300xp: 1 (50.00%) | 2 (50.00%)
    ''')
    elif choice == '3':
        print('''
    --- Mystical Container III ---
    XP (Chance: 20%):
      - 2000 (53.85%) | 4000 (26.95%) | 7000 (10.80%)
      - 10k (5.40%) | 30k (1.85%) | 100k (0.55%)
      - 500k (0.30%) | 750k (0.20%) | 1M (0.10%)
    Credits (Chance: 20%):
      - 100k (46.80%) | 150k (23.35%) | 200k (15.40%)
      - 500k (9.35%) | 1M (4.65%) | 2M (0.45%)
    Gold (Chance: 25%):
      - 0-9 (29.59%) | 10-90 (29.61%) | 100-900 (29.61%)
      - 1k-9k (10.33%) | 10k (0.40%) | 20k (0.20%)
      - 30k-90k (0.25%) | 100k (rare) [Min Drop: 100 gold]
    Premium Account (Chance: 20%):
      - 1 Day (12.00%) | 3 Days (6.00%) | 7 Days (2.00%)
    Other:
      - Riddle (25%) | Tankcoin (0.01%) | Avatar/Background (3%)
      - Mystical Certificate (7%) | Megamystical Container (5%)
    Guaranteed:
      - Certificate_28000xp: 1 (100.00%)
      - X5bust: 1 (33.33%) | 2 (33.33%) | 3 (33.33%)
    ''')
    elif choice == '4':
        print('''
    --- Mystical Container IV ---
    XP (Chance: 39%):
      - 10k (64.10%) | 30k (21.79%) | 100k (6.41%)
      - 500k (3.85%) | 750k (2.56%) | 1M (1.29%)
    Credits (Chance: 21%):
      - 100k (46.71%) | 250k (23.38%) | 500k (15.43%)
      - 1M (9.33%) | 2M (4.67%) | 5M (0.48%)
    Gold (Chance: 25%):
      - 1000 (54.38%) | 2500 (27.19%) | 5000 (10.88%)
      - 10k (3.66%) | 15k (1.86%) | 25k (1.09%)
      - 50k (0.54%) | 100k (0.23%) | 250k (0.11%) | 500k (0.06%)
    Premium Account (Chance: 50%):
      - 3 Days (30.00%) | 9 Days (15.00%) | 15 Days (5.00%)
    Other:
      - Riddle (25%) | Tankcoin (0.05%) | Avatar/Background (3%)
      - Mystificate / Other Containers (20%)
      - Kill Visor Body Kit (35%) | Cert_350000xp (3.23%)
    Busters (20% per type, % conditional on that type):
      - Credit Buster: 1 (52.65%) | 3 (26.30%) | 5 (15.80%) | 10 (5.25%)
      - Free XP Buster: same
      - Reloading Equip Buster: same
      - Crew XP Buster: same
      - Battle XP Buster: same
    Guaranteed:
      - Bright Image Container: 1 (100.00%)
      - Certificate_28000xp: 1 (67.64%) | 2 (32.36%)
      - X10bust: 1 (71.43%) | 3 (21.43%) | 5 (7.14%)
    ''')
    elif choice == '5':
        print('''
    --- Simply Space Container ---
    XP (Chance: 33%):
      - 200 (19.48%) | 500 (19.48%) | 1000 (19.48%)
      - 2000 (14.64%) | 5000 (9.76%) | 10k (7.79%)
      - 15k (4.88%) | 20k (2.94%) | 50k (0.97%)
      - 100k (0.48%) | 250k (0.06%) | 500k (0.02%) | 1M (0.01%)
    Gold (Chance: 50%):
      - 100 (23.74%) | 200 (19.00%) | 500 (16.62%)
      - 750 (14.24%) | 1000 (11.88%) | 1500 (6.18%)
      - 3000 (3.80%) | 5000 (2.84%) | 10k (1.66%) | 100k (0.04%)
    Other Containers (Chance: 50% to drop one, % of drops):
      - Mystical Container I (12.50%)
      - Collect Them All Container (12.50%)
      - Black Box I (12.50%)
      - Surprise Container (12.50%)   
    XP Certificates (Guaranteed):
      - 200xp (x3): 60.61% | 2300xp (x2): 30.30% | 28000xp (x1): 9.09%
    Busters (Chance: 50% for any):
      - 15x Free XP (12.50%) | 15x Credit (12.50%)
      - 15x Crew XP (12.50%) | 15x Battle XP (12.50%)
    Multipliers (Guaranteed):
      - x3 (1): 21.21% | x3 (2): 15.15% | x3 (3): 9.09%
      - x4 (1): 18.18% | x4 (2): 12.12% | x4 (3): 6.06%
      - x5 (1): 9.09% | x5 (2): 6.06% | x5 (3): 3.03%
    Special:
      - Key to Locked Container (7%) | Tankcoin (0.01%)
      - Tanks (Total: 5.12%):
        - 31 Regular Tanks (0.16% each)
        - 2 Rare Tanks [Уничтожитель, Strv K] (0.08% each)
    ''')
    elif choice == '0':
        pass
    else:
        print("Invalid choice.")

#container selection
while True:
    print('''
    1. Containers
    2. View Container Contents

    3. Information about the program
    0. Exit
    ''')
    category_selection = input('Select_category: ')
    
    if category_selection == '1':
        print('''
        1. Mystical Container I
        2. Mystical Container II
        3. Mystical Container III
        4. Mystical Container IV
        5. Simply Space Container
        ''')

        container_selection = input('Select_container: ')

        if container_selection == '1':
            mystical_container_I_opening()
        elif container_selection == '2':
            mystical_container_II()
        elif container_selection == '3':
            mystical_container_III()
        elif container_selection == '4':
            mystical_container_IV()
        elif container_selection == '5':
            simple_space_container()

    elif category_selection == '2':
        show_container_contents()

    elif category_selection == '3':
        print('''
    This program simulates the opening of Containers in a game.
    You can select a container type and specify how many containers to open.
    project start date: 17.11.26
    ''')

    elif category_selection == '0':
        break
    else:
        print("Invalid choice.")

