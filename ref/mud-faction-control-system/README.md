
# 三國 MUD 勢力控制系統 (Faction Control System)

此系統讓三國勢力在世界中動態控制城市與區域。

勢力：
- 魏
- 蜀
- 吳
- 群雄

玩家可以：
- 加入勢力
- 參與攻城戰
- 改變城市控制權

---

## 系統結構

```
factions/
  factions.json
  territories.json
  battles.json
```

---

## 核心概念

City / Fort 具有控制勢力：

```
洛陽 -> 魏
襄陽 -> 蜀
建業 -> 吳
```

當勢力改變：

- NPC 改變
- 商店改變
- 任務改變
