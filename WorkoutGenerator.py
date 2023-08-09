#libraries needed

from userinput import UserInput 
from RuleGenerator import RulesGenerator


user_input =  UserInput()
user_input.workout_type_selection()
user_input.plan_selection()
rules_generator = RulesGenerator()
rules_generator.workout_plan_generation(user_input)

#breaks for readability
print('\n\n')

