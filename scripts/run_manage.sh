 #!/usr/bin/env bash
#python manage.py generate_serializers_tests pmp_shield.employees.api.serializers.EmployeeSerializer -f output/employee_ser.py

#python manage.py maximo_data --export-time --fiscal-year=2019

python manage.py generate_factories pmp_shield.employees > output/employees_fact.py
