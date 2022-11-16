from django.forms import ModelForm
from .models import Competitor, School, Season, Stage, Group, Shake
from django.contrib.auth.forms import UserCreationForm


class SeasonForm(ModelForm):
    class Meta:
        model = Season
        fields = '__all__'


class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = '__all__'


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['group_name']


class ShakeForm(ModelForm):
    class Meta:
        model = Shake
        fields = ['season_name','stage_name','discipline','group_name']
        labels = {'season_name': 'სეზონი', 'stage_name': 'ეტაპი', 'discipline': 'დისციპლინა', 'group_name': 'ჯგუფი'}


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        labels = {'school_name': 'სკოლა'}


class CompetitorForm(ModelForm):
    class Meta:
        model = Competitor
        fields = '__all__'
        labels = {'surname': 'გვარი', 'name': 'სახელი', 'year': 'წელი', 'school': 'სკოლა', 'gender': 'სქესი'}
