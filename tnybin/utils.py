from hashids import Hashids
import arrow


LANGS = {
    'text': 'txt',
    'python': 'py',
    'javascript': 'js',
    'ruby': 'rb',
}


def map_lang(lang):
    return LANGS[lang]


def map_ext(ext):
    for lang, extension in LANGS.iteritems():
        if extension == ext:
            return lang


def gen_uid(num, name=''):
    hashids = Hashids(salt='some salt', min_length=6)
    return hashids.encrypt(num + 1)


def datetimeformat(date):
    past = arrow.get(date)
    return past.humanize()
