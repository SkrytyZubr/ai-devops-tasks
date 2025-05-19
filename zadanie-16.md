Główne różnice między skryptami bash i PowerShell zaobserwowane w tym przykładzie:

1. **Składnia zmiennych**: 
   - Bash: `$VARIABLE` 
   - PowerShell: `$VARIABLE` (podobnie, ale PowerShell używa bardziej zaawansowanego typowania)

2. **Formatowanie daty**:
   - Bash: `date +%Y%m%d_%H%M%S`
   - PowerShell: `Get-Date -Format "yyyyMMdd_HHmmss"`

3. **Sprawdzanie istnienia katalogu**:
   - Bash: `if [ ! -d "$BACKUP_DIR" ]`
   - PowerShell: `if (-not (Test-Path -Path $BACKUP_DIR))`

4. **Tworzenie katalogu**:
   - Bash: `mkdir -p "$BACKUP_DIR"`
   - PowerShell: `New-Item -ItemType Directory -Path $BACKUP_DIR -Force`

5. **Wykonywanie poleceń**:
   - Bash: bezpośrednie wywołanie `mysqldump | gzip > plik`
   - PowerShell: `& mysqldump | Out-File` i oddzielna kompresja przez .NET

6. **Obsługa błędów**:
   - Bash: sprawdzanie kodu wyjścia `if [ $? -eq 0 ]`
   - PowerShell: blok `try/catch`

7. **Kompresja**:
   - Bash: bezpośrednio przez `gzip`
   - PowerShell: przez bibliotekę .NET `System.IO.Compression.ZipFile`

8. **Struktura ścieżek**:
   - Bash: `/var/backups/db` (format Unix)
   - PowerShell: `C:\Backups\db` (format Windows)

9. **Przekierowanie wyjścia**:
   - Bash: `> "$FILENAME"`
   - PowerShell: `Out-File -FilePath $filename -Encoding ASCII`
