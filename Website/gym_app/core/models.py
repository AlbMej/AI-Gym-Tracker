from djongo import models

# Create your models here.

class Loan(models.Model):
    BUSINESS_TYPES = (
    ('', 'Choose...'),
    ('FT', 'Food Truck'),
    ('CON', 'Construction'),
    ('OTH', 'Other')
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    phone = models.CharField(max_length=32)

    address = models.CharField(max_length=256)

    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)

    amount_required = models.IntegerField() #label = 'Amount required'
    business_type = models.CharField(max_length=3, choices=BUSINESS_TYPES)
    years_in_business = models.IntegerField() #label='Years in business'
    other = models.CharField(max_length=64)

    agree = models.BooleanField()  #required=True

#A test model, going to experiment to see how we can add these to a database
class Exercise(models.Model):
    exID = models.IntegerField()
    name = models.CharField(max_length=64)          #Exercise name
    primary = models.CharField(max_length=64)       #Primary muscle group
    secondary = models.CharField(max_length=256)    #Secondary muscle groups

class RoutineExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()

class Routine(models.Model):
    routineName = models.CharField(max_length=64)
    exercises = models.ArrayModelField(
        model_container=RoutineExercise,
    )

class LogEntry(models.Model):
    name = models.CharField(max_length=64)  #name of exercise or routine
    time = models.DateField()               #time the entry was completed

class LogDay(models.Model):
    day = models.IntegerField()             #Day of the month (1-31 typically)
    month = models.IntegerField()           #Month represented by integer 1-12
    year = models.IntegerField()            #Year (i.e. 2019)
    entries = ArrayModelField(
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
