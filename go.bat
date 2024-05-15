@echo off

(
@echo: 
@echo ------
@echo Started: %date% %time%
C:\"Program Files"\Python310\python.exe C:\Users\Administrador.AGRICOVIAL\Scripts\sync.py
C:\"Program Files"\Python310\python.exe C:\Users\Administrador.AGRICOVIAL\Scripts\get-nv.py
@echo FINISH
@echo ------
@echo:  
) >> "C:\Users\Administrador.AGRICOVIAL\Scripts\log.txt"