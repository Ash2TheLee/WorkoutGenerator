from enum import Enum

class PlanData():
    def __init__(self, name, query):
        self.name = name
        self.query = query

class PlanSelection(Enum):
    DYNAMIC_STRETCHING = PlanData('Dynamic Stretching','select dynamic_stretching_moves_name as Stretch, dynamic_stretching_moves_reps as Number_Of_Times from dimension.dynamic_stretching_moves ORDER BY RANDOM() limit 5;')
    DYNAMIC_WARMUP = PlanData('Dynamic Warmup', 'select dynamic_warmup_moves_name as Warmup, dynamic_warmup_moves_reps as Number_Of_Times from dimension.dynamic_warmup_moves ORDER BY RANDOM() limit 1;')
    FINISHER = PlanData('Finisher', 'select finnisher_moves_name as Finisher, finnisher_moves_reps as Number_Of_Times from dimension.finnisher_moves ORDER BY RANDOM() limit 1;')
    CORE = PlanData('Core','select core_workout_name as "Core Move", core_workout_reps as Reps from dimension.core_workouts limit 5 ORDER BY RANDOM();')
    CARDIO = PlanData('Cardio','select cardio_workout_name as "Cardio Move", cardio_workout_reps as Reps from dimension.cardio_workouts ORDER BY RANDOM() limit 5;')
    UPPER_BODY = PlanData('Upper Body','select upper_body_workout_name as "Upper Body Move", upper_body_workout_reps as Reps from dimension.upper_body_workouts ORDER BY RANDOM() limit 5;')
    LOWER_BODY = PlanData('Lower Body','select lower_body_workout_name as "Lower Body Move", lower_body_workout_reps as Reps from dimension.lower_body_workouts ORDER BY RANDOM() limit 5;')
    PUSH = PlanData('Push','select push_workout_name as "Push Move", push_workout_reps as Reps from dimension.push_workouts ORDER BY RANDOM() limit 5;')
    PULL = PlanData('Pull','select pull_workout_name as "Pull Move", pull_workout_reps as Reps from dimension.pull_workouts ORDER BY RANDOM() limit 5;')
    FULL_PLAN = PlanData('Full Plan','''WITH dynamic_stretching AS (
                            select dynamic_stretching_moves_name as workout_moves, dynamic_stretching_moves_reps as workout_reps 
                            from dimension.dynamic_stretching_moves 
                            ORDER BY RANDOM() 
                            limit 5
                            )

                        ,	dynamic_warmup AS (
                            select dynamic_warmup_moves_name as workout_moves, dynamic_warmup_moves_reps as workout_reps 
                            from dimension.dynamic_warmup_moves 
                            ORDER BY RANDOM() 
                            limit 1
                        	)

                        ,	core_workout AS (
                            select core_workout_name as workout_moves, core_workout_reps as workout_reps 
                            from dimension.core_workouts
                            ORDER BY RANDOM()
                            limit 5 
                        	)

                        ,   lower_body_workout AS (
                            select lower_body_workout_name as workout_moves, lower_body_workout_reps as workout_reps 
                            from dimension.lower_body_workouts 
                            ORDER BY RANDOM() 
                            limit 5
                            )

                        ,	upper_body_workout AS (
                            select upper_body_workout_name as workout_moves, upper_body_workout_reps as workout_reps 
                            from dimension.upper_body_workouts 
                            ORDER BY RANDOM() 
                            limit 5
                            )

                        ,	cardio_workout AS (
                            select cardio_workout_name as workout_moves, cardio_workout_reps as workout_reps 
                            from dimension.cardio_workouts 
                            ORDER BY RANDOM()
                            limit 4
                            )


                            SELECT * FROM dynamic_stretching
                            UNION ALL
                            SELECT * FROM dynamic_warmup
                            UNION ALL
                            SELECT * FROM core_workout
                            UNION ALL
                            SELECT * FROM lower_body_workout
                            UNION ALL
                            SELECT * FROM upper_body_workout
                            UNION ALL
                            SELECT * FROM cardio_workout''')



