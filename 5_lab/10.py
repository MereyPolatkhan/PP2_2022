import re

def camel_to_snake(text):
    x = re.sub(r'([a-z])([A-Z])([a-z])', r'\1_\2\3', text)
    print(x.lower())

camel_to_snake("KbtuUniversityStudents")

