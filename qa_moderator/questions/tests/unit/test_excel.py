from django.test import TestCase
from django_test_tools.utils import create_output_filename_with_date

from qa_moderator.questions.excel import QuestionExcelAdapter
from qa_moderator.questions.tests.factories import QuestionFactory


class QuestionExcelAdapterTest(TestCase):

    def test_convert_all(self):
        QuestionFactory.create_batch(30)
        filename = create_output_filename_with_date('question_adapter.xlsx')
        adapter = QuestionExcelAdapter()
        adapter.convert_all(filename)
