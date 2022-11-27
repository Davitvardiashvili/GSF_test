from django.db import models
from django.contrib.auth.models import AbstractUser
import math

class Season(models.Model):
    season_name = models.CharField(max_length=50)

    def __str__(self):
        return self.season_name


class Stage(models.Model):
    stage_name = models.CharField(max_length=50)

    def __str__(self):
        return self.stage_name


class Group(models.Model):
    group_name = models.CharField(max_length=45)

    def __str__(self):
        return self.group_name


class Gender(models.Model):
    gender = models.CharField(max_length=3)

    def __str__(self):
        return self.gender


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=30)

    def __str__(self):
        return self.discipline_name


class School(models.Model):
    school_name = models.CharField(max_length=20)

    def __str__(self):
        return self.school_name


class Competitor(models.Model):
    surname = models.CharField(max_length=40, )
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'staff_competitor'

    def __str__(self):
        return f' {self.surname} {self.name} '


class Shake(models.Model):
    season_name = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    stage_name = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.SET_NULL, null=True)
    group_name = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(Competitor, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f' {self.season_name} - {self.stage_name} - {self.discipline} - {self.group_name} - {self.participants}'


