@echo off
SET "ROOT_DIR=%~dp0.."


setlocal
cd /d "%ROOT_DIR%"

start /b save_all_s4p\save_all_s4p.exe
