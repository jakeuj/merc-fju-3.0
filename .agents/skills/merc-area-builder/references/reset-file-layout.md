# Reset File Layout

## 何時讀這份
- 你正在建立或修補 `area/<area>/res/*.res`。
- 你需要 reset 指令骨架、欄位順序、依賴順序與常見錯位。

## 搭配閱讀
- `references/reset-runtime-guardrails.md`
- `docs/current-game/reset-file-format.md`
- 對應 area 的 `mob / obj / roo / shp`

## 檔案位置

```text
area/<area>/res/*.res
```

## 常見指令骨架

```text
M <mob_vnum> <limit>   <room_vnum>     <comment>
O <obj_vnum> <const>   <room_vnum>     <comment>
P <obj_vnum> <const>   <obj_vnum>      <comment>
G <obj_vnum> <mob_vnum>                <comment>
E <obj_vnum> <mob_vnum> <wear_loc>     <comment>
D <room_vnum> <exit>   <door_state>    <comment>
R <room_vnum> <exit>                   <comment>
A <mob_vnum>                            <comment>
```

## 指令語意

- `M`：生成怪物
- `O`：把物件放進房間
- `P`：把物件塞進另一個物件
- `G`：把物件給怪物
- `E`：把物件裝到怪物身上
- `D`：設定門或出口狀態
- `R`：隨機化出口
- `A`：讓怪物 reset 時騎馬

## 順序非常重要

`.res` 是逐行執行的命令流，因此：

- `G` / `E` 依賴前面已有對應怪物
- `P` 依賴前面已有母容器
- `D` / `R` 依賴前面提到的房間與出口真的存在

不要把它想成可任意重排的宣告式格式。

## 常見錯位

- 先給裝備，再生怪物
- 對不存在的 `mob_vnum` / `obj_vnum` / `room_vnum` 做操作
- `wear_loc` 不合法
- door state 套到不存在或不可開關的出口

## Repo-specific guardrail

- reset 問題常常不是 `.res` 自己寫錯，而是和 `mob / obj / roo / shp` 不一致。
- area 驗證時一定要把 `.res` 和其餘資料檔一起看，不要只看單檔語法。
