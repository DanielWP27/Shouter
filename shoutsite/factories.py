import factory
import factory.fuzzy 
from .models import Shout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import datetime
#import pytz

class UserFactory(factory.django.DjangoModelFactory):
    '''
    Creates a user
    '''

    class Meta:
        model = User

    '''Used for random:
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    '''
    first_name = 'first'
    last_name = 'last'
    username = first_name
    password = make_password('test')

class ShoutFactory(factory.django.DjangoModelFactory):
    '''
    Creates a shout
    '''

    class Meta:
        model = Shout

    shout_text = "TEXT"
    ''' Used for random in range:
    UTC = pytz.utc
    pub_date = factory.fuzzy.FuzzyDateTime(datetime.datetime(2018, 1, 1, tzinfo=UTC))
    likes = factory.fuzzy.FuzzyInteger(0, 10000)
    '''
    pub_date = '2019-01-22 10:06:09.268029'
    likes = 0
    user = factory.SubFactory(UserFactory)
