@echo off
SET "ROOT_DIR=%~dp0.."


setlocal
cd /d "%ROOT_DIR%"


REM clean
rmdir /S /Q build
rmdir /S /Q dist
