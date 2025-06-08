@echo off
set USER=bankuser
set PASS=bank123
set DB=localhost:1521/freepdb1

for %%F in (enriched*.csv) do (
    echo Loading file: %%F
    sqlldr %USER%/%PASS%@%DB% control=review.ctl data=%%F log=%%~nF.log bad=%%~nF.bad
)
echo ✅ All CSV files processed.
pause
