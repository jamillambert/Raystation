@ECHO OFF
ECHO Calculating meterset weight
ECHO.
python select_weights.py
octave-cli.exe calculate_weights_tot.m
del weights*.txt
pause