from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent.parent.parent) + '/import_files/'

User = get_user_model()


class Command(BaseCommand):
    help = 'Adds user to'

    def add_arguments(self, parser):
        parser.add_argument('users', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(BASE_DIR + options['users'][0]) as file:
            content = file.readlines()
            for i in content:
                line = i.strip().split(',')
                password = line[0]
                username = line[1]
                email = line[2]
                phone_number = line[3]
                created = User.objects.create(password=password, username=username, email=email,
                                              phone_number=phone_number)
                created.save()
        self.stdout.write(self.style.SUCCESS(''
                                             'Successfully added'))
