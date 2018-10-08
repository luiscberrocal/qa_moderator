from qa_moderator.polls.models import Poll


class JSONAdapter(object):

    def load_from_dict(self, data):
        poll_data = dict()
        poll_data['text'] = data['poll_name']
        poll_data['pub_date'] = data['pub_date']

        poll = Poll.objects.create(**poll_data)
        #for question in data['questions']:


