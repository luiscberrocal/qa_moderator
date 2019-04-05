from django.core.management import BaseCommand

from qa_moderator.questions.tests.factories import QuestionFactory


class Command(BaseCommand):
    """

        $ python manage.py  unit_assignments --assign --office=TINO-RE --start-date=2016-10-01 -u maveces jaasyn fjcastaneda jocarrillo lkquintero dardines
    """

    def add_arguments(self, parser):
        #parser.add_argument('output_filename')
        parser.add_argument("-a", "--amount",
                            dest="amount",
                            help="Ammount",
                            )

    def handle(self, *args, **options):
        """
        Load Old Structure Offices
        """
        # filename = settings.APPS_DIR.path('employees', 'tests', 'fixtures', 'base_offices_old_org.json').root
        amount = int(options.get('amount', "50"))
        for i in range(0, amount):
            q = QuestionFactory.create()
            self.stdout.write('{}. {}'.format(i, q))

        # nfileame = settings.APPS_DIR.path('questions', 'tests', 'fixtures', 'fake_questions.json').root
        # self.stdout.write('Currently {} questions'.format(Question.objects.count()))
        # adapter = QuestionDataAdapter()
        # adapter.save_to_db_from_file(filename)
        #
        # self.stdout.write('After run {} question'.format(Question.objects.count()))
