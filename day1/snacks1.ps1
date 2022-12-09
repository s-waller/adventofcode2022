$String = Get-Content -Path "$PSScriptRoot\input.txt" | Out-String

$NewLine = [System.Environment]::NewLine
$Items = ($String -split "$NewLine$NewLine")

$Items | ForEach-Object {$Iteration = 1}{
    $ElfNumber = $Iteration
    $Iteration++
    $Supplies = $_ -split "$NewLine"
    [PSCustomObject]@{
        Name = "elf$ElfNumber"
        Total = ($Supplies | Measure-Object -Sum).Sum
        Supplies = $Supplies
    } 
} | Sort-Object -Property Total | Select-Object -Last 1 -ExpandProperty Total