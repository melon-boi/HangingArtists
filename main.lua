local lib = loadstring(game:HttpGet"https://raw.githubusercontent.com/dawid-scripts/UI-Libs/main/fluxlib.txt")() 
_G.closeBind = Enum.KeyCode.F2
local win = lib:Window("Hanging Artist", "Best script for SA!", Color3.fromRGB(226, 42, 232), _G.closeBind) 
local tab = win:Tab("Main script", "http://www.roblox.com/asset/?id=6023426915")


tab:Label("Remember, wait 3-5 minutes before submitting art!")
tab:Label("Press F2 to not display UI") 
