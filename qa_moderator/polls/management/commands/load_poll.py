from django.conf import settings
from django.core.management import BaseCommand

from qa_moderator.polls.adapters import JSONAdapter


class Command(BaseCommand):
    """

        $ python manage.py  load_poll -f /paht/to/file
    """

    def add_arguments(self, parser):
        #parser.add_argument('output_filename')
        parser.add_argument("-f", "--filename",
                            dest="filename",
                            help="JSON file with question data",
                            )

    def handle(self, *args, **options):
        filename = settings.APPS_DIR.path('polls', 'tests', 'fixtures', 'poll_01.json').root
        if options.get('filename'):
            filename = options.get('filename')

        adapter = JSONAdapter()
        adapter.load_from_file(filename)
        self.stdout.write('Loaded file {}'.format(filename))
