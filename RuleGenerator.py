# rules generator
import psycopg2
from userinput import UserInput 
import pandas as pd
from sqlalchemy import create_engine
from DBConnections import *
from PlanSelection import PlanSelection
#connecting to the database
                       
database_connection = psycopg2.connect(
    database = database_name, user = database_user, password = database_password, host = database_host, port = database_port)

engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(database_user,database_password,database_host,database_port,database_name))

#cursor = database_connection.cursor()


class RulesGenerator():
    def workout_plan_generation(self, plan_type:PlanSelection):

        if plan_type.boxing_plan_selection:
            data = pd.read_sql(plan_type.boxing_plan_selection.value.query, engine)
            print('Creating the results \n')
            print(data)

        elif plan_type.strength_plan_selection:
            data = pd.read_sql(plan_type.strength_plan_selection.value.query, engine)
            print('Creating the results \n')
            print(data)
        else:
            print('Not working')

#closing the databse connection
    database_connection.close()
print('DATABSE CONNECTION CLOSED, RERUN PROGRAM IF NEW PLAN IS NEEDED')