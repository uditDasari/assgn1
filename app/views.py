import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from app.models import Project, User, Membership
from app.serializers import ProjectSerializer, UserSerializer, MemShipSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MemShipSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MemShipSerializer


def get_mentees(request, n):
    user = User.objects.get(pk=n)
    projects = user.project_set.all()
    query_set = Membership.objects.filter(member_type=1, project__in=projects)
    response = [t.user.name for t in query_set]
    return HttpResponse(json.dumps(response), status=200)


def get_mentoring_projects(request, n):
    # user = User.objects.get(pk=n)
    query_set = Membership.objects.filter(member_type=1, user__id=n)
    response = [t.project.name for t in query_set]
    return HttpResponse(json.dumps(response), status=200)


def get_users_of_project(request, n):
    # project = Project.objects.get(pk=n)
    # response = project.members
    # return HttpResponse(json.dumps(response), status=200)
    query_set = Membership.objects.filter( project__id=n)
    response = [t.user.name for t in query_set]
    return HttpResponse(json.dumps(response), status=200)

