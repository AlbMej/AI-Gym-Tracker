from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from .models import Loan
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