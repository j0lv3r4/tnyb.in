import os
from datetime import datetime
import dataset
import mistune
from pygments import highlight
from pygments import formatters 
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from bottle import route, error, response, request, redirect, post, get, run, template, TEMPLATE_PATH, static_file
from utils import map_lang, gen_uid, map_ext, datetimeformat


PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH.insert(0, '{0}/templates'.format(PROJECT_PATH))

# database setup

db = dataset.connect('sqlite:///tnybin.sqlite')
pastes = db['pastes']


# static files
@get('/static/<filename:path>')
def static_files(filename):
    """Serve static files"""
    return static_file(filename, root='{0}/static/'.format(PROJECT_PATH))


@get('/')
def home():
    """Home page"""
    return template('pages/home.html')


@post('/')
def create_paste():
    """Create a paste"""
    data = request.forms

    lang = data.get('lang')
    uid = gen_uid(len(pastes))

    pastes.insert(dict(
        uid=uid,
        lang=lang,
        code=data.get('code'),
        date=datetime.utcnow(),
    ))

    return redirect('/{0}/{1}'.format(map_lang(lang), uid))


@get('/<ext>/<uid>')
def show_single(ext, uid):
    """Show a paste"""
    paste = pastes.find_one(uid=uid)
    lang = paste['lang']

    if lang != map_ext(ext):
        return error404('Paste not found :(')

    result = ''

    if lang == 'markdown':
        result = mistune.markdown(paste['code'], escape=True)
    else:
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter(
            linenos=True,
        )
        result = highlight(paste['code'], lexer, formatter)

    return template(
        'pages/paste.html',
        code=result,
        uid=paste['uid'],
        date=paste['date'],
        ext=ext,
        datetimeformat=datetimeformat,
    )


@get('/latest')
def show_latest():
    """Show latest 20 pastes"""

    results = pastes.find(_limit=20)

    return template(
        'pages/latest.html',
        pastes=results,
        datetimeformat=datetimeformat,
        map_lang=map_lang,
    )


# Error pages

@error(404)
def error404(err):
    """Page not found"""
    return template('pages/404.html', error=err)


@error(500)
def error500(err):
    """Server error"""
    return template('pages/500.html', error=err)


run(debug=True, reloader=True, port=2345)
