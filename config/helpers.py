from config.constants import constants

def load_css(csss):
  rpta = ''
  if len(csss) > 0:
    for css in csss:
      temp = '<link href="' + constants['STATIC_URL'] + css + '.css" rel="stylesheet"/>'
      rpta = rpta + temp
  return rpta

def load_js(jss):
  rpta = ''
  if len(jss) > 0:
    for js in jss:
      temp = '<script src="' + constants['STATIC_URL'] + js + '.js" type="text/javascript"></script>'
      rpta = rpta + temp
  return rpta
