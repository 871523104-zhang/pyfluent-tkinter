echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="E:\ANSYS Inc\v222\fluent/ntbin/win64/winkill.exe"

"E:\ANSYS Inc\v222\fluent\ntbin\win64\tell.exe" DESKTOP-6O68A19 5529 CLEANUP_EXITING
if /i "%LOCALHOST%"=="DESKTOP-6O68A19" (%KILL_CMD% 21316) 
if /i "%LOCALHOST%"=="DESKTOP-6O68A19" (%KILL_CMD% 9552) 
if /i "%LOCALHOST%"=="DESKTOP-6O68A19" (%KILL_CMD% 5296)
del "F:\yuri_pyfulent_tkinter\source\case\cleanup-fluent-DESKTOP-6O68A19-9552.bat"
