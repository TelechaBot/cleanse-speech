import io

from cleanse_speech.dlfa import DLFA

if __name__ == '__main__':
    dfa = DLFA(words_resource=[
        ['你好'],
        io.BytesIO(b'sensitive'),
    ])
    print(dfa.contains_illegal('This is a 你好 word.'))
    print(dfa.censor_all('This is a 你好 word.'))
    print(dfa.extract_illegal_words('This is a 你好 word.'))
    dfa.update_words(['sensitive', 'word', 'new'])
    print(dfa.contains_illegal('This is a new sensitive word.'))
    print(dfa.censor_all('This is a new sensitive word.'))
    print(dfa.extract_illegal_words('This is a new sensitive word.'))
