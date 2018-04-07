#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from config.middleware import enable_cors, headers

departamento_view = Bottle()

@departamento_view.route('/listar', method='GET')
@enable_cors
@headers
def listar():
  return "departamento/listar"
