import re

def capital_letters(text):
    print(re.sub(r'(\w)([A-Z])(\w)', r'\1 \2\3', text))
    # print(re.search(r'(\w)([A-Z])(\w)', text).group())

capital_letters("KbtuFITInformationSystems")
capital_letters("KbtuFitInformationSystems")