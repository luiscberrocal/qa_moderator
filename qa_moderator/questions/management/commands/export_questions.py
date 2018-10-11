import os

from django.conf import settings
from django.core.management import BaseCommand

from qa_moderator.questions.excel import QuestionExcelAdapter


class Command(BaseCommand):
    """

        $ python manage.py  export_questions
    """

    def add_arguments(self, parser):
        #parser.add_argument('output_filename')
        parser.add_argument("-a", "--amount",
                            dest="amount",
                            help="Ammount",
                            )

    def handle(self, *args, **options):
        adapter = QuestionExcelAdapter()
        xlsx = 'questions_export.xlsx'
        filename = os.path.join(settings.MEDIA_ROOT, xlsx)
        adapter.convert_all(filename)
        self.stdout.write('Wrote {}'.format(filename))
        self.stdout.write('Access {}{}'.format(settings.MEDIA_URL, xlsx))
