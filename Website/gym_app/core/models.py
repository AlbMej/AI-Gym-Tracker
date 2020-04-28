from djongo import models

# Create your models here.

#A test model, going to experiment to see how we can add these to a database
class Exercise(models.Model):
    exID = models.IntegerField()
    name = models.CharField(max_length=64)          #Exercise name
    primary = models.CharField(max_length=64)       #Primary muscle group
    secondary = models.CharField(max_length=256)    #Secondary muscle groups

class RoutineExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    #references an exercise from the exercises table
    sets = models.IntegerField()
    reps = models.IntegerField()
    value = models.IntegerField()
    #value represents weight, time, or whatever other metric to measure

class Routine(models.Model):
    routineName = models.CharField(max_length=64)
    exercises = models.ArrayModelField(
        model_container=RoutineExercise,
    )

class LogEntry(models.Model):
    name = models.CharField(max_length=64)  #name of exercise or routine
    time = models.DateTimeField()               #time the entry was completed

class LogDay(models.Model):
    day = models.IntegerField()             #Day of the month (1-31 typically)
    month = models.IntegerField()           #Month represented by integer 1-12
    year = models.IntegerField()            #Year (i.e. 2019)
    entries = models.ArrayModelField(
        model_container=LogEntry,           #names of exercises/routines
    )

class LogMonth(models.Model):
    month = models.IntegerField()           #Month represented by integer 1-12
    year = models.IntegerField()            #Year (i.e. 2019)
    days = models.ArrayModelField(
        model_container=LogDay,
    )

class LogYear(models.Model):
    year = models.IntegerField()            #Year (i.e. 2019)
    months = models.ArrayModelField(
        model_container=LogMonth,
    )

class User(models.Model):
    uID = models.IntegerField()
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    routines = models.ArrayModelField(
        model_container=Routine,
    )
    log = models.ArrayModelField(
        model_container=LogYear,
    )
