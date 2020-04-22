#Sample Makefile

RootDir:=$(shell cd)\..
PackName=xbelko02_xhusca00_xjuram00_xlazor02
PackArchive=$(RootDir)\$(PackName).zip
PackDir:=$(RootDir)\..\$(PackName)
PackDocDir=$(PackDir)\doc
PackInstallDir=$(PackDir)\install
PackRepoDir=$(PackDir)\repo
DocOutputDir=$(RootDir)\src
InstallerName=kalkulačkaSetup.exe
InstallerDir=$(RootDir)\src\$(InstallerName)

all:
	python calculator.py

run:
	python calculator.py

profile:
	python profiling.py

pack:
	if exist "$(PackDir)" del "$(PackDir)" /f /s /q 1>nul & rmdir "$(PackDir)" /s /q
	mkdir "$(PackDir)"
	if exist "$(PackArchive)" del "$(PackArchive)" /f /s /q 1>nul

	mkdir "$(PackRepoDir)"
	make clean
	xcopy /s "$(RootDir)" "$(PackRepoDir)"
	mkdir "$(PackRepoDir)\.git"
	xcopy /s "$(RootDir)\.git\*" "$(PackRepoDir)\.git"

	cd "$(PackDir)\.." & powershell Compress-Archive "$(PackName)" $(PackArchive)
	del "$(PackDir)" /f /s /q 1>nul
	rmdir "$(PackDir)" /s /q

	mkdir "$(PackDocDir)"
	xcopy /s "$(DocOutputDir)\html" "$(PackDocDir)"

	mkdir "$(PackInstallDir)"
	xcopy /s "$(InstallerDir)" "$(PackInstallDir)"

clean:

help:
	echo "make / make all / make run == runs the file calculator.py"
	echo "make profile == runs the file profiling.py"
	echo "make pack == packs all needed files into xbelko02_xhusca00_xjuram00_xlazor02.zip file"
	echo "make clean == makes nothing"