$String = Get-Content -Path "$PSScriptRoot\input.txt" | Out-String

$NewLine = [System.Environment]::NewLine
$Items = ($String -split "$NewLine$NewLine")

$TopThree = $Items | ForEach-Object {$Iteration = 1}{
    $ElfNumber = $Iteration
    $Iteration++
    $Supplies = $_ -split "$NewLine"
    [PSCustomObject]@{
        Name = "elf$ElfNumber"
        Total = ($Supplies | Measure-Object -Sum).Sum
        Supplies = $Supplies
    } 
} | Sort-Object -Property Total | Select-Object -Last 3 -ExpandProperty Total

$Sum =0
[array]$TopThree.ForEach({$Sum+=$_})
$Sum