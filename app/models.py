from django.db import models


# Create API end-points to
# Create User
# Assign a project to user/users
# Assign mentor to a project
# Assign users to a project
# Get mentees of a given person.
# Get projects user is mentoring
# Get users/mentor of a project
# Create a Swagger end-point and add documentation for these API end-points.


class User(models.Model):
    name = models.CharField(max_length=256, default="")
    joining_data = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=256, default="")
    start_date = models.DateTimeField(null=True)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name


# 0 for developer and 1 for mentor
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, models.CASCADE)
    date_joined = models.DateTimeField(null=True)
    member_type = models.BooleanField()

    def __str__(self):
        if self.member_type == 1:
            return self.user.name + "is mentoring " + self.project.name
        else:
            return self.user.name + "is working on " + self.project.name

