local SolarisLib = loadstring(game:HttpGet("https://raw.githubusercontent.com/bloodball/-back-ups-for-libs/main/sol"))()

local win = SolarisLib:New({
  Name = "Hanging Artists v1.1",
  FolderToSave = "SolarisLibStuff"
})

--win:Tab(title <string>)
local tab = win:Tab("Main Script")
local tab2 = win:Tab("Credits")

--tab:Section(title <string>)
local sec = tab:Section("Main")
local slider = sec:Slider("Delay", 0,2,0,0.1,"Delay", function(t)
  print(t)
end)


local sec2 = tab2:Section("Credits")
sec2:Label("Owners - melon boi#2511, MrAWAY#0069")
sec2:Label("Developers - melonboi#2511")
sec2:Label("Discord Server - https://discord.gg/rtcz9nUP57")
--sec:Button(title <string>, callback <function>)    
