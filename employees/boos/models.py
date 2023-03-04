from django.db import models

# Create your models here.


class Employee(models.Model):
    female = 0
    male = 1

    GANDER_OPTIONS = [(male, 'male'), (female, 'female')]

    name = models.CharField(max_length=100, null=True)
    gander = models.IntegerField(
        choices=GANDER_OPTIONS, null=True)  # drop down list
    email = models.EmailField(max_length=200, null=True)
    phonenum = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, null=True)
    manager = models.ForeignKey("Employee", blank=True, null=True,
                                on_delete=models.SET_NULL)
    # img = models.models.FileField(_(""), upload_to=None, max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100, null=True)
    start_date = models.DateTimeField(auto_now=True, null=True)
    employee = models.ManyToManyField(Employee, null=True)


class Job(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=400, null=True)
    employee = models.ForeignKey(
        Employee, blank=True, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey("Department", blank=True, null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=150, null=True)

    # def get_jobs(self):
    #     return Job.objects.filter(department__pk=self.pk)

    def __str__(self):
        return f'{self.id} -- {self.name}'
