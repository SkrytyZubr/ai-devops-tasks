<no message>

Read file: backup-db.sh
```powershell
# Prosty skrypt do backupu bazy danych

$DB_NAME = "app_database"
$BACKUP_DIR = "C:\Backups\db"
$DATE = Get-Date -Format "yyyyMMdd_HHmmss"
$FILENAME = "$BACKUP_DIR\${DB_NAME}_${DATE}.sql.gz"

# Sprawdź czy katalog istnieje
if (-not (Test-Path -Path $BACKUP_DIR)) {
    New-Item -ItemType Directory -Path $BACKUP_DIR -Force
    Write-Output "Utworzono katalog $BACKUP_DIR"
}

# Wykonaj backup
Write-Output "Rozpoczynam backup bazy $DB_NAME..."

try {
    # W PowerShell używamy mysqldump z parametrami, a następnie kompresujemy plik
    # Zakładając, że MySQL jest zainstalowany i dostępny w PATH
    & mysqldump -u root -p $DB_NAME | 
        Out-File -FilePath "$BACKUP_DIR\${DB_NAME}_${DATE}.sql" -Encoding ASCII
    
    # Kompresja pliku przy użyciu .NET
    $inputFile = "$BACKUP_DIR\${DB_NAME}_${DATE}.sql"
    $outputFile = "$FILENAME"
    
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    [System.IO.Compression.CompressionLevel]$compressionLevel = "Optimal"
    [System.IO.Compression.ZipFile]::CreateFromDirectory($inputFile, $outputFile, $compressionLevel, $false)
    
    # Usuń niekompresowany plik
    Remove-Item -Path $inputFile
    
    Write-Output "Backup zakończony sukcesem: $FILENAME"
}
catch {
    Write-Error "Błąd podczas wykonywania backupu: $_"
    exit 1
}
```
