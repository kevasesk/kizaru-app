Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = oWS.ExpandEnvironmentStrings("%HOMEPATH%") + "\Desktop\DSBot.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "C:\\Program Files\DSBot\DSBot.exe"
oLink.Description = "DSBot"
oLink.WorkingDirectory = "C:\\Program Files\DSBot"
oLink.Save
Set oWS = Nothing