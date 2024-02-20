from django.core.management.base import BaseCommand
from voting_app.models import Candidate

class Command(BaseCommand):
    help = 'Create candidates'

    def handle(self, *args, **kwargs):
        candidates_data = [
            {'name': 'Candidate 1', 'position': 'President', 'picture': 'candidate1.jpg'},
            {'name': 'Candidate 2', 'position': 'Vice President', 'picture': 'candidate2.jpg'},
            # Add more candidates as needed
        ]

        for data in candidates_data:
            candidate = Candidate.objects.create(
                name=data['name'],
                position=data['position'],
                picture=data['picture']
            )
            self.stdout.write(self.style.SUCCESS(f'Created candidate: {candidate}'))
