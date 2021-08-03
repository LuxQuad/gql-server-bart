#!/bin/bash
PORT=8000
ENV=.misc/env/prod.env
SERVICE=app.main:app

uvicorn ${SERVICE} --port=${PORT} --reload --env-file=${ENV}
