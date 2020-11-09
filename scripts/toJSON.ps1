$dataPath = Join-Path $PSScriptRoot '../data'

Get-ChildItem -Path $dataPath -Filter *.csv | ForEach-Object {
  $baseName = $_.BaseName
  Get-Content $_ | ConvertFrom-Csv | ConvertTo-Json | Out-File -FilePath (Join-Path $dataPath "$($baseName).json")
}
