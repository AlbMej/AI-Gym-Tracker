from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from gym_app.core.models import *
import datetime as dt
# Create your tests here.

class TestUserSignUp(TestCase):
    """
    My signup view uses the UserCreationForm which is part of the Django Core
    (it is already tested with test cases ensuring length validators, common password, numeric password, user already exists, etc.)
    So I am only testing if a valid sign up populates the database correctly
    """
    def setUp(self):
        self.client = Client()

    def test_get(self):
        # Test GET
        url = reverse_lazy('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_valid_credentials(self):
        url = reverse_lazy('signup')
        # Test POST with valid data
        req_data = {
          'username': 'secretusertest',
          'password1': 'secret321',
          'password2': 'secret321',
        }
        response = self.client.post(url, req_data)
        self.assertRedirects(response, '/') #Signup redirects to home page after user signup
        self.assertEqual(User.objects.count(), 1)

class TestUserLogIn(TestCase):
    """
    Test to see if login feature works
    """
    def setUp(self):
        self.credentials = {
            'username': 'superuser',
            'password': 'supersecret321'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # Send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # Check if user ia logged in now
        self.assertTrue(response.context['user'].is_authenticated)


class TestHiddenPages(TestCase):
    """
    Test to see if the user is prevented from accessing the loan application page before loggin in
    """
    def test_loan_view_denies_anonymous(self):
        response = self.client.get(reverse('loanform'), follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/submit_form')#

        response = self.client.post(reverse('loanform'), follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/submit_form')

    def test_loan_view_loads(self):
        user = User.objects.create(username='whitehathacker')
        user.set_password('LETMEIN!!!!')
        user.save()
        self.client.force_login(user)
        response = self.client.get(reverse('loanform'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')


class ModelTestCase(TestCase):
    """This class defines the test suite for the Loan model."""
    def setUp(self):
        """Define the test client and test variables."""
        self.loanee_first_name = "Alberto"
        self.loanee_last_name = "Mejia"
        self.email = "me@albertomejia.com"
        self.phone = "914 123 4567"
        self.address = "C103 Colonie Apartments"
        self.city = "Yonkers"
        self.state = "NY"
        self.zip = "10701"
        self.amt_req = '7500'
        self.buss_type = 'CON'
        self.years_in_bus = '3'
        self.other = 'N/A'
        self.agree = True

        self.loan = Loan(first_name=self.loanee_first_name,
            last_name=self.loanee_last_name,
            email=self.email,
            phone=self.phone,
            address=self.address,
            city=self.city,
            state=self.state,
            zip_code=self.zip,
            amount_required=self.amt_req,
            business_type=self.buss_type,
            years_in_business=self.years_in_bus,
            other=self.other,
            agree=self.agree
            )

    def test_model_create_loan_application(self):
        """Test that the Loan model can create a loan application."""
        old_count = Loan.objects.count()
        self.loan.save()
        new_count = Loan.objects.count()
        self.assertNotEqual(old_count, new_count)

class ExerciseTestCase(TestCase):
    """This class defines a basic test suite for the Exercise model"""
    def setUp(self):
        """Define the test client and test variables."""
        self.exercise_id = 0
        self.exercise_name = "benchpress (test)"
        self.primary_muscle = "chest"
        self.secondary_muscles = "triceps, biceps"

        self.exercise = Exercise(exID=self.exercise_id,
            name=self.exercise_name,
            primary=self.primary_muscle,
            secondary=self.secondary_muscles)

    def test_model_create_exercise(self):
        """Test that the exercise is properly saved"""
        old_count = Exercise.objects.count()
        self.exercise.save()
        new_count = Exercise.objects.count()
        self.assertNotEqual(old_count, new_count)

        retrieved = Exercise.objects.get(exID=0)
        self.assertEqual(retrieved.name, "benchpress (test)")

class UserRoutineLogTestCase(TestCase):
    """This class defines the test suite for the models User, Routine, Log*, and their contained models"""
    def setUp(self):
        """Define the test client and test variables."""
        self.bench_id = 0
        self.bench_name = "benchpress (test)"
        self.bench_primary = "chest"
        self.bench_secondary = "triceps, biceps"

        self.exercise1 = Exercise(exID=self.bench_id,
            name=self.bench_name,
            primary=self.bench_primary,
            secondary=self.bench_secondary)
        self.exercise1.save()

        self.curls_id = 1
        self.curls_name = "curls (test)"
        self.curls_primary = "biceps"
        self.curls_secondary = "forearms"

        self.exercise2 = Exercise(exID=self.curls_id,
            name=self.curls_name,
            primary=self.curls_primary,
            secondary=self.curls_secondary)
        self.exercise2.save()

        self.routineEx1 = RoutineExercise(exercise=self.exercise1,sets=5,reps=5)
        self.routineEx2 = RoutineExercise(exercise=self.exercise2,sets=3,reps=8)

        self.routineEx1.save()
        self.routineEx2.save()

        self.name = "big arms"
        self.routine = Routine(routineName=self.name, exercises=[])
        self.routine.save()
        self.routine.exercises.append(self.routineEx1)
        self.routine.exercises.append(self.routineEx2)

        self.user = User(uID=0,username="rcos_is_fun",email="turnew2@rpi.edu",routines=[],log=[])
        self.user.save()
        self.user.routines.append(self.routine)

        self.datetime1 = dt.datetime(2019, 12, 25, 8, 8, 8, 0)
        self.datetime2 = dt.datetime(2019, 12, 25, 9, 9, 9, 0)

        entry1 = LogEntry(name=self.routine.routineName, time=self.datetime1)
        entry2 = LogEntry(name=self.routineEx1.exercise.name, time=self.datetime2)
        entry1.save()
        entry2.save()
        day = LogDay(day=25,month=12,year=2019,entries=[entry1,entry2])
        month = LogMonth(month=12,year=2019,days=[day])
        self.year = LogYear(year=2019,months=[month])
        day.save()
        month.save()
        self.year.save()

    def test_model_info_RoutineExercise(self):
        self.assertEqual(self.routineEx1.sets, 5)
        self.assertEqual(self.routineEx2.reps, 8)
        self.assertEqual(self.routineEx1.exercise.exID, 0)
        self.assertEqual(self.routineEx2.exercise.exID, 1)

    def test_model_info_Routine(self):
        self.assertEqual(self.routine.routineName, "big arms")

    def test_model_access_array_Routine(self):
        rEx = self.routine.exercises[0]
        ex = rEx.exercise
        self.assertEqual(ex.exID, 0)

    def test_model_info_LogYear(self):
        yearInt = self.year.year
        self.assertEqual(yearInt, 2019)

    def test_model_accesses_LogYear(self):
        logEntry = self.year.months[0].days[0].entries[0]
        self.assertEqual(logEntry.name, "big arms")

    def test_user_query(self):
        #good example of djongo query
        userQuerySet = User.objects.filter(username="rcos_is_fun")
        self.assertEqual(len(userQuerySet), 1)
        user = userQuerySet[0]
        self.assertEqual(user.email, "turnew2@rpi.edu")

    def test_single_entry_query(self):
        entryQuerySet = LogEntry.objects.filter(name="big arms")
        self.assertEqual(len(entryQuerySet), 1)
        entry = entryQuerySet[0]
        self.assertEqual(entry.time, self.datetime1)
