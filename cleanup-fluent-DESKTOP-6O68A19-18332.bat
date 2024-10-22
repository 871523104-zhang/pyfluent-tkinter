echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="E:\ANSYS Inc\v222\fluent/ntbin/win64/winkill.exe"

"E:\ANSYS Inc\v222\fluent\ntbin\win64\tell.exe" DESKTOP-6O68A19 19846 CLEANUP_EXITING
if /i "%LOCALHOST%"=="DESKTOP-6O68A19" (%KILL_CMD% 34752) 
if /i "%LOCALHOST%"=="DESKTOP-6O68A19" (%KILL_CMD% 18332) 
if /i "%LOCALHOST%"=="DESKTOP-6O68A19" (%KILL_CMD% 23604)
del "F:\yuri_pyfulent_tkinter\cleanup-fluent-DESKTOP-6O68A19-18332.bat"
