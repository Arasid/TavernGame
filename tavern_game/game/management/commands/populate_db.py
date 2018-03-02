import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from game.models import Person


class Command(BaseCommand):
    help = 'Populate DB.'

    def _populate_people(self):
        with open(Path(settings.BASE_DIR) / 'people.csv', 'r') as csv_file:
            people = []
            for line in csv_file:
                id, name = line.strip().split(',')
                people.append({
                    'id': id,
                    'name': name,
                })

        for person in people:
            person_obj, created = Person.objects.update_or_create(
                id=person['id'],
                name=person['name'],
            )

            if created:
                self.stdout.write(self.style.NOTICE(f'Created ‘{person_obj.name}’ person.'))

    def handle(self, *args, **options):
        self._populate_people()
