
$mode=$args[0]

if ( $args.Count -lt 1 ) {
    Write-Output "Usage:  buildit.ps1 [build | clean]"
    exit
}

function Invoke-Clean {
    rm -ErrorAction SilentlyContinue .\ui\ui_mainwindow.py
    rm -ErrorAction SilentlyContinue .\ui\ui_aboutdialog.py
    rm -Recurse -Force -ErrorAction SilentlyContinue .\__pycache__
    rm -Recurse -Force -ErrorAction SilentlyContinue .\ui\__pycache__
}

function Invoke-Build {
    pyside6-uic .\ui\mainwindow.ui -o .\ui\ui_mainwindow.py
    pyside6-uic .\ui\aboutdialog.ui -o .\ui\ui_aboutdialog.py
}


if ( $mode -eq "clean" ){
    Invoke-Clean
}
elseif ( $mode -eq "build" ) {
    Invoke-Clean
    Invoke-Build
}