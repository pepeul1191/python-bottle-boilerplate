#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request, template
from config.models import Estacion
from sqlalchemy.sql import select
from config.middleware import enable_cors, headers
from config.database import engine, session_db
from config.constants import constants

estacion_view = Bottle()

@estacion_view.route('/', method='GET')
@headers
def listar():
  locals = {'title': 'Estaciones', 'constants': constants}
  return template('templates/estacion/index', locals = locals)


@estacion_view.route('/listar', method='GET')
@enable_cors
@headers
def listar():
  conn = engine.connect()
  stmt = select([Estacion])
  return json.dumps([dict(r) for r in conn.execute(stmt)])
