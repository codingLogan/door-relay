Write-Host "Program Examples... Pass in an argument to test"

$argument1 = $args[0]

if ( $argument1 ) {
  Write-Host "You provided an argument."
  Write-Host $argument1
} else {
  Write-Host "No argument was provided."
}