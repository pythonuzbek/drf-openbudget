from django.core.management.base import BaseCommand

from faker import Faker

from apps.models import Region


class Command(BaseCommand):
    help = 'Populate AFakeModel with fake data'

    def handle(self, *args, **options):
        fake = Faker()
        infos = [{"name": fake.first_name()} for _ in range(500000)]
        objs = [Region(**info) for info in infos]
        Region.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS('Successfully populated AFakeModel with fake data'))