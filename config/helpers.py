from config.constants import constants

# views
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

# archivos estaticos
def estacion_index_css():
  switcher = {
    'desarrollo': [
      'bower_components/bootstrap/dist/css/bootstrap.min',
      'bower_components/font-awesome/css/font-awesome.min',
      'css/style'
    ],
    'produccion': ['dist/estacion.min'],
  }
  return switcher.get(constants['ambiente'])

def estacion_index_js():
  switcher = {
    'desarrollo': [
      'bower_components/jquery/dist/jquery.min',
      'bower_components/bootstrap/dist/js/bootstrap.min',
      'js/app'
    ],
    'produccion': ['dist/estacion.min'],
  }
  return switcher.get(constants['ambiente'])
