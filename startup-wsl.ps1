$ErrorActionPreference = 'Stop'

$repoRootWin = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$repoRootForWsl = $repoRootWin -replace '\\', '/'
$repoRootWsl = (& wsl.exe wslpath -a $repoRootForWsl).Trim()

if (-not $repoRootWsl) {
    throw "Unable to convert Windows path to WSL path: $repoRootWin"
}

$startupDirWsl = "$repoRootWsl/src"
$command = "cd '$startupDirWsl' && exec ./startup.bash"

& wsl.exe bash -lc $command
exit $LASTEXITCODE
