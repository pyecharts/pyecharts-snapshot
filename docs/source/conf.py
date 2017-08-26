# -*- coding: utf-8 -*-
DESCRIPTION = (
    'renders pyecharts as image' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyecharts-snapshot'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.7'
release = '0.0.7'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyecharts-snapshotdoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyecharts-snapshot.tex',
     'pyecharts-snapshot Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyecharts-snapshot',
     'pyecharts-snapshot Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyecharts-snapshot',
     'pyecharts-snapshot Documentation',
     'Onni Software Ltd.', 'pyecharts-snapshot',
     DESCRIPTION,
     'Miscellaneous'),
]
