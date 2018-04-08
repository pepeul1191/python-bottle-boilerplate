#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request, template
from config.models import Estacion
from sqlalchemy.sql import select
from config.middleware import enable_cors, headers
from config.database import engine, session_db
from config.constants import constants
from config.helpers import load_css, load_js

estacion_view = Bottle()

@estacion_view.route('/', method='GET')
@headers
def listar():
  helpers = {}
  helpers['css'] = load_css([
    'bower_components/bootstrap/dist/css/bootstrap.min',
    'bower_components/font-awesome/css/font-awesome.min',
  ])
  helpers['js'] = load_js([
    'bower_components/jquery/dist/jquery.min',
    'bower_components/bootstrap/dist/js/bootstrap.min',
  ])
  locals = {'title': 'Estaciones', 'constants': constants}
  return template('templates/estacion/index', locals = locals, helpers = helpers)


@estacion_view.route('/listar', method='GET')
@enable_cors
@headers
def listar():
  conn = engine.connect()
  stmt = select([Estacion])
  return json.dumps([dict(r) for r in conn.execute(stmt)])
