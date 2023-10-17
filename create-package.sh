#!/bin/sh
set -o nounset -o errexit

test ! -f "${HANDLER}"

cd "/deps" && zip -r "${HANDLER}" ./*
cd /src/src && zip "${HANDLER}" handler.py
