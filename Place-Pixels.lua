local Pixels = data[option]
local UI = game.Players.LocalPlayer.PlayerGui.MainGui.PaintFrame.GridHolder.Grid
for i,v in pairs(Pixels) do
    UI[i].BackgroundColor3  = Color3.fromRGB(v.R, v.G, v.B), wait(0.2)
    end
end)
