>>> vars_before_import = set(dir())
>>> from json import *
>>> set(dir()) - vars_before_import
set(['load', 'JSONEncoder', 'dump', 'vars_before_import', 'JSONDecoder', 'dumps', 'loads'])




