@echo off

::

type assets/logo.txt

::

echo ::

echo [INFO] Installing dependencies...

py -m pip install -r requirements.txt

::

echo [INFO] Dependencies installed!

::

echo [INFO] Starting Server...

start cmd /k py -m uvicorn server:app

echo [INFO] Starting Bot...

start cmd /k py run.py

echo [INFO] Done!

::

exit 0