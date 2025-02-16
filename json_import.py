import json
from questionbank.models import Question  # Replace `myapp` with your app name
# To run this file
# 1. python manage.py shell
# 2. >>> exec(open('json_import.py').read())
with open('question_data.json') as file:
    data = json.load(file)
    for item in data:
        Question.objects.update_or_create(
            title=item['title'],  # The unique field condition
            defaults={
            'difficulty' : item['difficulty'],
            'category' : item['category'],
            'doc_link' : item['doc_link'],
            'sol_link' : item['sol_link']
            }
        )
