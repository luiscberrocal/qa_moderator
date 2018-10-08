import json

from qa_moderator.polls.models import Poll, Question, Choice


class JSONAdapter(object):

    def load_from_file(self, filename):
        with open(filename) as data_file:
            poll = json.load(data_file)
        return self.load_from_dict(poll)

    def load_from_dict(self, data):
        poll_data = dict()
        poll_data['text'] = data['poll_name']
        poll_data['pub_date'] = data['pub_date']

        poll = Poll.objects.create(**poll_data)
        for question_data in data['questions']:
            q_d = dict()
            q_d['poll'] = poll
            q_d['content'] = question_data['content']
            question = Question.objects.create(**q_d)
            if question_data.get('choices'):
                for choice_info in question_data['choices']:
                    choice_data = dict()
                    choice_data['question'] = question
                    choice_data['value'] = choice_info['value']
                    choice_data['numeric_value'] = choice_info['numeric_value']
                    Choice.objects.create(**choice_data)
