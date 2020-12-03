from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)

    def handle(self, *args, **options):
        action = options['action']
        if action == 'raise':
            raise CommandError('raise error')
        self.stdout.write('testpoll')
        return 'testpoll'
