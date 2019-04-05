 #!/usr/bin/env bash
OUTPUT_FILE=output/question_w_ser.py
python manage.py generate_serializers_tests qa_moderator.questions.api.serializers.QuestionWriteSerializer -f $OUTPUT_FILE
echo 'Wrot $OUTPUT_FILE'

#python manage.py maximo_data --export-time --fiscal-year=2019

#python manage.py generate_factories pmp_shield.employees > output/employees_fact.py
