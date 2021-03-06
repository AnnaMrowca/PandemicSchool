from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.name} {self.surname}'


class Subject(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student,related_name='subjects', null=True, blank=True)
    #null=True, blank=True mean that list can be empty + I have to do makemigrations + migrate


    def __str__(self):
        return self.name

class Status: #enum
    PRESENT = 'present'
    COVID = 'absent - covid'
    ABSENT = 'absent - other'

    CHOICES = [(PRESENT, 'present'), (COVID,'absent - covid'), (ABSENT, 'absent - other')]

class PresenceStatus(models.Model):
    person = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_class = models.ForeignKey(Subject, on_delete=models.CASCADE)
    presence_status = models.CharField(max_length=30, choices= Status.CHOICES)

    def __str__(self):
        return f'{self.person.name} {self.person.surname} {self.subject_class} {self.presence_status}'