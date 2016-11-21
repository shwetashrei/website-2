from django.core.management.base import BaseCommand, CommandError
from website.models import Project, Grant, Match
import datetime
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

class Command(BaseCommand):
    help = 'Matches'

    def handle(self, *args, **options):
        today = datetime.datetime.today()
        grants = Grant.objects.filter(deadline__gte=today)
        projects = Project.objects.all().order_by('?')
        
        for grant in grants:
            for project in projects:
                # similarity = similar(
                #     grant.name + " " + grant.organization.name + " " + grant.comments + " " + grant.tags, 
                #     project.name + " " + 
                #     project.slug + " " + 
                #     project.description + " " + 
                #     project.tags + " " + 
                #     (project.problem and project.problem or "") + 
                #     ''.join([group.name+ " " for group in project.group_set.all()]) + 
                #     ''.join([benefit.name+ " " for benefit in project.benefit_set.all()]) + 
                #     ''.join([barrier.name+ " " for barrier in project.barrier_set.all()]) + 
                #     ''.join([collaborator.name+ " " for collaborator in project.collaborator_set.all()]) 
                # )
                similarity = similar(
                    grant.name + " " + grant.organization.name + " " + grant.comments + " " + grant.tags, 
                    project.name + " " + 
                    project.description
                )
                match, created = Match.objects.update_or_create(
                    project=project, grant=grant, defaults={'similarity': similarity})

        self.stdout.write(self.style.SUCCESS('Successfully matched projects'))