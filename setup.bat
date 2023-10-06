@echo off
echo Upgrading pip...
pip uninstall discord.py -y
pip install --upgrade pip
echo Downloading...
title Downloading requriments...
color 4
cls
pip install intents
pip install psutil
pip install discord==1.7.3
echo Downloaded discord.py
pip install colorama
echo Downloadec colorama
pip install smtplib
echo Downloaded smtplib
pip install sys
echo Downloaded sys
pip install os
echo Downloaded os
pip install webbroswer
echo Downloaded webbroswer
pip install asyncio
echo Downloaded asyncio
pip install json
echo Downloaded json
pip install requests
echo Downloaded requests
echo Downloading Aze libariy
cls
title AzeTool is starting...
title Welcome to AzeTool!
call start.bat
