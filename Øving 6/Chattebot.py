import random

def pick_sentence(sentences):
  return sentences[random.randint(0, len(sentences)-1)]

questions = ['Hva gjør du', 'Hvordan går det', 'Hvorfor heter du',
              'Liker du å hete', 'Føler du deg bra', 'Hva har du gjort idag',
              'Hva tenker du om framtida', 'Hva gjør deg glad', 'Hva gjør deg trist']
follow_ups = ['Hvorfor sier du', 'Hva mener du med', 'Hvor lenge har du sagt',
               'Hvilke tanker har du om', 'Kan du si litt mer om',
               'Når tenkte du første gang på']
responses = ['Fint du sier det', 'Det skjønner jeg godt', 'Så dumt da', 'Føler meg også sånn',
              'Blir trist av det du sier', 'Så bra', 'Du er jammen frekk']

def print_sentence():
    no = 1

def main():
    answer = 'ikke hade'
    name = input('Hva heter du? ')
    while answer != 'hade':
        print(f'{pick_sentence(questions)}, {name}?')
        answer = input('Svar: ')
        print(f'{pick_sentence(follow_ups)} {answer}?')
        input('Svar: ')
        print(f'{pick_sentence(responses)} {name}.')

main()
