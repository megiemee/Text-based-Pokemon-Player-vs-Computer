from random import randint

#ansi codes to colour text
ansi_blue = '\033[94m'
ansi_yellow = '\033[93m'
ansi_red = '\033[91m'
ansi_green = '\033[92m'
ansi_reset = '\033[0m'
ansi_bluebg = '\033[48;5;75m'
ansi_redbg = '\033[48;5;203m'

class pokemon:
    def __init__(self, name, ptype, skills):
        self.name = name #string
        self.ptype = ptype #string
        self.health = 100 #integer
        self.skills = skills #dictionary
        
    #get and set methods
    def get_name(self):
        return self.name
    
    def get_ptype(self):
        return self.ptype
    
    def get_health(self):
        return self.health
    
    def get_skills(self):
        return self.skills
    
    def set_name(self, name):
        self.name = name
    
    def set_ptype(self, ptype):
        self.ptype = ptype
    
    def set_health(self, health):
        self.health = health
        
    def set_skills(self, skills):
        self.skills = skills
    
    #Method to display status
    def display_status(self):
        print(f"{self.get_name()}'s current health: {self.get_health()}")
    
    #method to display all skills of pokemon
    def display_skills(self):
        print(f"{self.get_name()}'s skills:")
        print()
        for index, (key, value) in enumerate(self.get_skills().items(), start=1):
            print(f"{index}. {key.title()} [{value[0]}]")
            print(f"Damage: {value[1]['damage']}")
            print(f"Chance: {value[1]['chance']}")
        print()
    
    def is_alive(self):
        if self.get_health() <= 0:
            return False
        else:
            return True
        
        
        
###Child classes - One for Each type of pokemon###
#Polymorphism - damage_received function

#Water
class waterpokemon(pokemon):
    
    def init(self):
        super(waterpokemon, self).init(name, ptype, health, skills)
    
    #Parameters: 
    #optype - type of opponent pokemon (string)
    #damage - base damage by opponent (integer)
    #change - probability of successful attack (float between 0 and 1 inclusive)
    #Return Value: If attack is successful (boolean)
    def damage(self, optype, damage, chance):
        
        #Generate float between 0 and 1 inclusive to determine if attack is successful
        rno = randint(0,100)/100
        
        if rno <= chance: 
            
            if optype.lower() == "fire":
                damage_received = damage*0.95
                print("Attack was ineffective :(")
            elif optype.lower() == "grass":
                damage_received = damage*1.09
                print("Attack was super effective!")
            else:
                damage_received = damage*1
            
            #Damage message
            print(f"{self.get_name()} received {damage_received} damage!")
            
            #Update health of pokemon
            self.set_health(self.get_health() - damage_received)
            
            return True
        else:
            print("Attack missed!")
            return False
    
#Fire
class firepokemon(pokemon):
    def init(self):
        super(firepokemon, self).init(name, ptype, health, skills)
        
    #Parameters: 
    #optype - type of opponent pokemon (string)
    #damage - base damage by opponent (integer)
    #change - probability of successful attack (float between 0 and 1 inclusive)
    #Return Value: If attack is successful (boolean)
    def damage(self, optype, damage, chance):
        
        #Generate float between 0 and 1 inclusive to determine if attack is successful
        rno = randint(0,100)/100
        
        if rno <= chance: 
            if optype.lower() == "grass":
                damage_received = damage*0.95
                print("Attack was ineffective :(")
            elif optype.lower() == "water":
                damage_received = damage*1.09
                print("Attack was super effective!")
            else:
                damage_received = damage*1
                
            #Damage message
            print(f"{self.get_name()} received {damage_received} damage!")
            
            #Update health of pokemon
            self.set_health(self.get_health() - damage_received)
            
            return True
        else:
            print("Attack missed!")
            return False
    
#Grass
class grasspokemon(pokemon):
    def init(self):
        super(grasspokemon, self).init(name, ptype, health, skills)

    #Parameters: 
    #ptype - type of opponent pokemon (string)
    #damage - base damage by opponent (integer)
    #change - probability of successful attack (float between 0 and 1 inclusive)
    #Return Value: If attack is successful (boolean)
    def damage(self, optype, damage, chance):
        
        #Generate float between 0 and 1 inclusive to determine if attack is successful
        rno = randint(0,100)/100
        
        if rno <= chance: 
            if optype == "water":
                damage_received = damage*0.95
                print("Attack was ineffective :(")
            elif optype == "fire":
                damage_received = damage*1.09
                print("Attack was super effective!")
            else:
                damage_received = damage*1
            
            #Damage message
            print(f"{self.get_name()} received {damage_received} damage!")
            
            #Update health of pokemon
            self.set_health(self.get_health() - damage_received)
            
            return True
        
        else:
            print("Attack missed!")
            return False

 
        
###SKILLS DATABASE###

#SKILLS - [List] of [List] of basic skills that is common for all types

basic = [["kick",{"damage": 13, "chance": 1}],["punch", {"damage": 12, "chance": 1}],["flick",{"damage":11, "chance": 1}]]

#[Dictionary] of [List] of PType specific skills

waterskills = {"normal": [
        ["watersquirty", {"damage": 10, "chance": 0.9}],
        ["whirlpoop", {"damage": 8, "chance": 0.95}],
        ["waterbasher", {"damage": 11, "chance": 0.8}]],
    "ulti": [
        ["hydroflask", {"damage": 22, "chance": 0.45}],
        ["hydropumpin", {"damage": 20, "chance": 0.5}]]}

fireskills = {"normal": [
        ["firebowl", {"damage": 9, "chance": 0.95}],
        ["firefly", {"damage": 8, "chance": 0.95}],
        ["firespitter", {"damage": 11, "chance": 0.75}]],
    "ulti": [
        ["firenado", {"damage": 21, "chance": 0.45}],
        ["bbq", {"damage": 23, "chance": 0.4}]]}

grassskills = {"normal": [
        ["dirttoss", {"damage": 7, "chance": 0.99}],
        ["dirthose", {"damage": 9, "chance": 0.90}],
        ["grassshooter", {"damage": 11, "chance": 0.75}]],
    "ulti": [
        ["earthquake", {"damage": 22, "chance": 0.45}],
        ["vinesnap", {"damage": 20, "chance": 0.5}]]}

###Random Skill Generator###
#Parameter: [List] of dictionaries of skills of skills to choose from
#Return Value: [Dictionary] of skills 

def random_skill(skillList): 
    #dictionary to store all skills
    skills = {"basic": None, "norm1": None, "norm2": None, "ulti": None}
    
    ###randomise basic skill from common pool###
    skills["basic"] = basic[randint(0,len(basic)-1)]
    
    ###randomise normal skills from provided list###
    
    #randomise 2 different numbers within index of list of normal skills
    numbers = [randint(0, len(skillList["normal"])-1)]
    while True:
        nnumber = randint(0,len(skillList["normal"])-1)
        if nnumber != numbers[0]:
            numbers.append(nnumber)
            break
    
        #assign normal skills in dictionary of pokemon's skill
    skills["norm1"], skills["norm2"] = skillList["normal"][numbers[0]], skillList["normal"][numbers[1]]
    
    ###randomise ultimate skill from provided list###
    skills["ulti"] = skillList["ulti"][randint(0,len(skillList["ulti"])-1)]
    
    return skills
    
###Creation of random Pokemon###
#Parameter: -
#Return Value: Pokemon Object
def random_pokemon():
    
    #List of pokemon names and their corresponding ptypes

    pokemon_list = [
    {"name": "Bulbasaur", "ptype": "grass"},
    {"name": "Meowscarada", "ptype": "grass"},
    {"name": "Leafeon", "ptype": "grass"},
    {"name": "Charmander", "ptype": "fire"},
    {"name": "Arcaine", "ptype": "fire"},
    {"name": "Ponyta", "ptype": "fire"},
    {"name": "Squirtle", "ptype": "water"},
    {"name": "Lapras", "ptype": "water"},
    {"name": "Psyduck", "ptype": "water"},
    ]
    
    #choose a random pokemon from the list of pokemon
    rpokemon = pokemon_list[randint(0, len(pokemon_list)-1)] #dictionary containing name, type
    
    #generate skills & pokemon object based on its type 
    if rpokemon["ptype"] == "grass":
        skills = random_skill(grassskills)
        return grasspokemon(rpokemon["name"], rpokemon["ptype"], skills)
    
    elif rpokemon["ptype"] == "fire":
        skills = random_skill(fireskills)
        return firepokemon(rpokemon["name"], rpokemon["ptype"], skills)
    
    elif rpokemon["ptype"] == "water":
        skills = random_skill(waterskills)
        return waterpokemon(rpokemon["name"], rpokemon["ptype"], skills)
    
###Select random skill to utilize###
#Parameter: Name of pokemon using skill(String), [Dictionary] of skills
#Return Value: [List]: skill type (string), Selected skill (Dictionary [Key: Skill name, Value: {Damage, Chance}])
def use_random_skill(skills):
    
    #Decide on which skill to use
    
    rno = randint(0,100)/100
    #20% chance for basic skill
    if rno <= 0.2: 
        return ["basic", skills["basic"]]
    #35% chance for each normal skill
    elif rno <= 0.55: 
        return ["norm1", skills["norm1"]]
    elif rno <= 0.90: 
        return ["norm2", skills["norm2"]]
    #10% chance for ultimate skill
    else:
        return ["ulti", skills["ulti"]]

    
###Function to display type specific skills in selection phase###
#Parameter: [List] of skills
#Return Value: List of skill names
def display_skills(skills):
    
    valid_skills = []
    for skill in range(len(skills)):
        print(f"{skill + 1}. Name: {skills[skill][0]} | Damage: {skills[skill][1]['damage']} | Chance: {skills[skill][1]['chance']}")
        valid_skills.append(skills[skill][0])
    
    return valid_skills


###Function to validate input of type specific skills in selecton phase###
#Parameter: Inputed skill name, valid list of skill names
#Return Value: List of skill names
def validate_skill(skill, valid_list):
    if skill.isalpha() == True:
        if skill.lower() in valid_list:
            return True
    #show player error message
    print("Invalid skill name entered :(")
    return False
        
###Function for player to create pokemon###
#Parameter: -
#Return Value: Pokemon object created according to player's specifications
def create_pokemon():
    
    #asking player to name their pokemons
    print("Please name your pokemon.")
    name_decision = input("Enter the name of your pokemon:")  
    
    #asking player to choose type of pokemon
    print("Please choose one pokemon type: water, fire, grass.")  
    valid_types = ["water", "fire", "grass"]
    ptype = input("Enter your decision:")
    
    #Validate choice of pokemon type, ask player to re-enter if it is not a valid type
    while True:
        if ptype.isalpha() == True:
            if ptype.lower() in valid_types:
                break
        
        #re-enter if invalid
        print("Invalid type entered :( Please choose from water, fire or grass.")
        ptype = input("Re-enter your decision: ")
            
    
    #display possible basic skills to choose from
    print("Basic skills: ")
    
    chosen_skills = {"basic": None, "norm1": None, "norm2": None, "ulti": None}
    
    #get player to choose a basic attack
    valid_basic = []
    for skill in range(len(basic)):
        print(f"{skill + 1}. Name: {basic[skill][0]} | Damage: {basic[skill][1]['damage']} | Chance: {basic[skill][1]['chance']}")
        valid_basic.append(basic[skill][0])
        
    basic_skill = input("Please enter the skill name of the basic skill you would like to select: ")
    
    #Validate basic_skill
    while True:
        if basic_skill.isalpha() == True:
            if basic_skill.lower() in valid_basic:
                break
        
        #re-enter if invalid
        print("Invalid skill name entered :(")
        basic_skill = input("Re-enter your decision: ")
    
    for skill in basic:
        if skill[0] == basic_skill.lower():
            chosen_skills["basic"] = skill
            break
    
    #get player to select type-specific skills
    
    if ptype == "water":
        #selection of 2 normal attacks
        valid_norm = display_skills(waterskills["normal"])
        
        norm1 = input("Please enter the skill name of the first normal skill you would like to select: ")
        #validate normal skill 1
        while validate_skill(norm1, valid_norm) == False:
            norm1 = input("Re-enter your decision: ")
        
        norm2 = input("Please enter the skill name of the second normal skill you would like to select: ")
        #validate normal skill 2 & ensure it is not a repeat of 1
        while True:
            if validate_skill(norm2, valid_norm) == True and norm2 != norm1:
                break
            elif norm2 == norm1:
                print("Your first and second normal skills cannot be the same.")    
            norm2 = input("Re-enter your decision: ")
                
        for skill in waterskills["normal"]:
            if skill[0] == norm1.lower():
                chosen_skills["norm1"] = skill
            elif skill[0] == norm2.lower():
                chosen_skills["norm2"] = skill
        
        #selection of ultimate
        valid_ulti = display_skills(waterskills["ulti"])
        ulti = input("Please enter the skill name of the ultimate skill you would like to select: ")
        while validate_skill(ulti, valid_ulti) == False:
            ulti = input("Re-enter your decision: ")
            
        for skill in waterskills["ulti"]:
            if skill[0] == ulti.lower():
                chosen_skills["ulti"] = skill
                break
                
        #create pokemon object        
        return waterpokemon(name_decision, "water", chosen_skills)        
        
            
    elif ptype == "fire":
        valid_norm = display_skills(fireskills["normal"])
        
        norm1 = input("Please enter the skill name of the first normal skill you would like to select: ")
        #validate normal skill 1
        while validate_skill(norm1, valid_norm) == False:
            norm1 = input("Re-enter your decision: ")
        
        norm2 = input("Please enter the skill name of the second normal skill you would like to select: ")
        #validate normal skill 2 & ensure it is not a repeat of 1
        while True:
            if validate_skill(norm2, valid_norm) == True and norm2 != norm1:
                break
            elif norm2 == norm1:
                print("Your first and second normal skills cannot be the same.")    
            norm2 = input("Re-enter your decision: ")
            
        for skill in fireskills["normal"]:
            if skill[0] == norm1.lower():
                chosen_skills["norm1"] = skill
            elif skill[0] == norm2.lower():
                chosen_skills["norm2"] = skill
                
        #selection of ultimate
        valid_ulti = display_skills(fireskills["ulti"])
        ulti = input("Please enter the skill name of the ultimate skill you would like to select: ")
        while validate_skill(ulti, valid_ulti) == False:
            ulti = input("Re-enter your decision: ")
            
        for skill in fireskills["ulti"]:
            if skill[0] == ulti.lower():
                chosen_skills["ulti"] = skill
                break
                
        return firepokemon(name_decision, "fire", chosen_skills)
        
    elif ptype == "grass":
        valid_norm = display_skills(grassskills["normal"])
        
        norm1 = input("Please enter the skill name of the first normal skill you would like to select: ")
        #validate normal skill 1
        while validate_skill(norm1, valid_norm) == False:
            norm1 = input("Re-enter your decision: ")
        
        norm2 = input("Please enter the skill name of the second normal skill you would like to select: ")
        #validate normal skill 2 & ensure it is not a repeat of 1
        while True:
            if validate_skill(norm2, valid_norm) == True and norm2 != norm1:
                break
            elif norm2 == norm1:
                print("Your first and second normal skills cannot be the same.")    
            norm2 = input("Re-enter your decision: ")
            
        for skill in grassskills["normal"]:
            if skill[0] == norm1.lower():
                chosen_skills["norm1"] = skill
            elif skill[0] == norm2.lower():
                chosen_skills["norm2"] = skill
                
        #selection of ultimate
        valid_ulti = display_skills(grassskills["ulti"])
        ulti = input("Please enter the skill name of the ultimate skill you would like to select: ")
        while validate_skill(ulti, valid_ulti) == False:
            ulti = input("Re-enter your decision: ")
            
        for skill in grassskills["ulti"]:
            if skill[0] == ulti.lower():
                chosen_skills["ulti"] = skill
        
        return grasspokemon(name_decision, "grass", chosen_skills)
    

###Function for player's turn###
#Parameter: player pokemon (pokemon object), ai pokemon (pokemon object)
#Return Value: If game has ended (Boolean)
def player_turn(p_pokemon,a_pokemon):
    
    print()
    print(ansi_blue + "PLAYER'S TURN")
    
    #display skills player can choose from to use
    p_pokemon.display_skills()
    
    #Get and validate user's choice of skill
    valid_choices = ["basic", "norm1", "norm2", "ulti"]
    use = input("Enter type of your choice of skill [basic/norm1/norm2/ulti]: ") 
    
    while use not in valid_choices:
        print("Invalid choice. Please only use from [basic/norm1/norm2/ulti]")
        use = input("Re-enter choice: ")

    print(f"{p_pokemon.get_name().title()} uses {p_pokemon.get_skills()[use][0]}!")
    
    #Utilize skill on enemy pokemon
    if use == "basic":
        success = a_pokemon.damage("basic", p_pokemon.get_skills()[use][1]['damage'], p_pokemon.get_skills()[use][1]['chance'])
                
    else:
        success = a_pokemon.damage(p_pokemon.get_ptype(), p_pokemon.get_skills()[use][1]['damage'], p_pokemon.get_skills()[use][1]['chance'])
            
    #check if receipient of damage is still alive if attack was successful, end game if receipient of damage is dead
    if success:
        if a_pokemon.is_alive() == False:
            print(f"{a_pokemon.get_name().title()} has died! Congratulations! You win!")
            return  False #exit game
        
    return True #continue game if neither pokemon is dead


###Function for AI's turn###
#Parameter: player pokemon (pokemon object), ai pokemon (pokemon object)
#Return Value: If game has ended (Boolean)
def ai_turn(p_pokemon, a_pokemon):

    print()
    print(ansi_red + "AI'S TURN")
            
    aiuse = use_random_skill(a_pokemon.get_skills())
    print(f"{a_pokemon.get_name().title()} uses {aiuse[1][0]}!")
                
    if aiuse[0] != "basic":
        success = p_pokemon.damage(a_pokemon.get_ptype(), aiuse[1][1]['damage'], aiuse[1][1]['chance'])
    else:
        success = p_pokemon.damage(aiuse[0], aiuse[1][1]['damage'], aiuse[1][1]['chance'])
            
    #check if receipient of damage is still alive if attack was successful, end game if receipient of damage is dead
    if success:
        if p_pokemon.is_alive() == False:
            print(f"{p_pokemon.get_name().title()} has died! Boo! You Have Lost")
            return False
    return True

###Function to display status of both pokemon###
#Parameter: Pokemon 1 (pokemon object), Pokemon 2 (pokemon object)
def display_statuses(p1, p2):
    print(ansi_reset)
    print(ansi_bluebg)
    p1.display_status()
    print(ansi_redbg)
    p2.display_status()
    print(ansi_reset)

    
###Game Function###

def Player_vs_AI():
    
    #player create pokemon
    p_pokemon = create_pokemon()
    
    #Generate AI pokemon
    a_pokemon = random_pokemon()
    
    notend = True
    
    #Randomize who to begin
    coinflip = randint(0,1)
    
    #coinflip = 1 #temp to test when ai has first move
    
    if coinflip == 0:
        print(ansi.green)
        print("Player has the first move!" + ansi_reset)
        
        #continue game until either pokemon dies
    
        while notend:
            
            #display status of both pokemon before each attack
            display_statuses(p_pokemon, a_pokemon)
            
            #player turn
            if player_turn(p_pokemon, a_pokemon) == False:
                break
            
            #display status of both pokemon before each attack
            display_statuses(p_pokemon, a_pokemon)
    
            #AI turn
            if ai_turn(p_pokemon, a_pokemon) == False:
                break
        
    else:
        print(ansi_green)
        print("AI has the first move!" + ansi_reset)
        
        #continue game until either pokemon dies
    
        while notend:
            
            #display status of both pokemon before each attack
            display_statuses(p_pokemon, a_pokemon)
    
            #AI turn
            if ai_turn(p_pokemon, a_pokemon) == False:
                break
                
            #display status of both pokemon before each attack
            display_statuses(p_pokemon, a_pokemon)
            
            #player turn
            if player_turn(p_pokemon, a_pokemon) == False:
                break  

    
Player_vs_AI()