#user input classes
from PlanSelection import PlanSelection

workout_type_dictionary = {1: 'Boxing', 2:'Strength'}

boxing_workout_selections = {1:PlanSelection.DYNAMIC_STRETCHING, 2:PlanSelection.DYNAMIC_WARMUP, 3:PlanSelection.FINISHER}

strength_workout_selections = {1:PlanSelection.FULL_PLAN,2:PlanSelection.DYNAMIC_STRETCHING, 3:PlanSelection.DYNAMIC_WARMUP, 4:PlanSelection.CORE, 5:PlanSelection.CARDIO, 6:PlanSelection.UPPER_BODY, 7:PlanSelection.LOWER_BODY, 8:PlanSelection.PUSH, 9:PlanSelection.PULL}


class UserInput():

    selected_workout_type = None
    boxing_plan_selection = None
    strength_plan_selection = None

    def __str__(self) -> str:
        return ["Selected Type: " , self.selected_workout_type ,"Boxing Plan: ",self.boxing_plan_selection ," Strength Plan ",self.strength_plan_selection].__str__()

    def workout_type_selection(self):
        print('''
   _             _   _        __        __                               ____            _                ____ _       _     
    / \  _   _ ___| |_(_)_ __   \ \      / ___  _ __ ___   ___ _ __  ___  | __ )  _____  _(_)_ __   __ _   / ___| |_   _| |__  
   / _ \| | | / __| __| | '_ \   \ \ /\ / / _ \| '_ ` _ \ / _ | '_ \/ __| |  _ \ / _ \ \/ | | '_ \ / _` | | |   | | | | | '_ \ 
  / ___ | |_| \__ | |_| | | | |   \ V  V | (_) | | | | | |  __| | | \__ \ | |_) | (_) >  <| | | | | (_| | | |___| | |_| | |_) |
 /_/   \_\__,_|___/\__|_|_| |_|    \_/\_/ \___/|_| |_| |_|\___|_| |_|___/ |____/ \___/_/\_|_|_| |_|\__, |  \____|_|\__,_|_.__/ 
                                                                                                   |___/                       
                                            =======================================
                                            |                                     |
                                            |  Welcome to the Workout Generator   |
                                            |                                     |
                                            =======================================


What type of workout do you want?
---------------------------------------
Options Are:
    1) Boxing
    2) Strength
''')
        print('\n')
#Ask what type of workout needs to be created
        workout_type = input("What type of workout needs to be created? ")

        print('\n')

        self.selected_workout_type = workout_type_dictionary[int(workout_type)]

#taking the workout type and selecting the options from the database
        print('The workout plan you picked is: '+ self.selected_workout_type)
        print('\n')

        self.make_sure_selected_plan_is_correct()

#making sure the plan selected is correct
    def make_sure_selected_plan_is_correct(self):
        is_plan_selected_correct = input('Is the plan you selected correct? Yes or No: ')
        print('\n\n')
#if plan is yes move foward, if plan selection is no then have user select a different plan
        if is_plan_selected_correct == 'Yes':
            print('Generating plan options for '+ self.selected_workout_type)
        else:
            print('Going to the start of the program......')
            self.workout_type_selection()

#picking the plans for the selected workout type
    def plan_selection(self):
        if self.selected_workout_type == 'Boxing':
            print('''
        Boxing Plan Options Are:
        1) Dynamic Stretching
        2) Dynamic Warmup
        3) Finisher
                    ''')
            print('\n')
            self.selected_boxing_workout = input('What type of Boxing workout do you want? ')
            self.boxing_plan_selection = boxing_workout_selections[int(self.selected_boxing_workout)]

            print('\n')
            print('The plan you selected is: '+ self.boxing_plan_selection.value.name + '. Now generating the ' + self.boxing_plan_selection.value.name + ' boxing workout plan...')

        elif self.selected_workout_type == 'Strength':
            print('''
        Strength Plan Options Are:
        1) Full Plan
        2) Dynamic Stretching
        3) Dynamic Warmup
        4) Core
        5) Cardio
        6) Upper Body
        7) Lower Body
        8) Push
        9) Pull
                    ''')
            print('\n')
            self.selected_strength_workout = input('What type of Strength workout do you want? ')
            self.strength_plan_selection = strength_workout_selections[int(self.selected_strength_workout)]
            print('\n')
            print('The plan you selected is: '+ self.strength_plan_selection.value.name + '. Now generating the ' + self.strength_plan_selection.value.name + ' strength workout plan...')
        else:
            print('No workout plan has been selected')






    

    
    


