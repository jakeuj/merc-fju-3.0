# Map Spec Template

這份模板是給 `area/<new_area>/map.md` 使用的設計規格參考。它採三層架構：

- Authoring layer: `map.md` 內的人類可讀 prose 與嵌入的 `mapmd-json`
- Internal model layer: `mapmd-json` 是 canonical machine-readable graph schema
- Projection layer: 目前只有 `.roo`

`map.md` is the design document, while the embedded `mapmd-json` block is the canonical machine-readable graph schema used by generators.

source of truth 也分兩種：

- 人類設計語意的 source of truth = `map.md`
- 機器生成的 canonical source of truth = `mapmd-json`

因此若 prose 與 `mapmd-json` 不一致，generator 只會相信 `mapmd-json`，作者必須回頭修正 spec。

重點：

- `map.md` 是 spec-first 設計檔，不是 runtime area map 載入格式
- script 只讀受限結構，**不會**理解自由 prose
- `mapmd-json` 的 graph model 是 `room = node`、`exit = edge`
- `keywords`、`jobs`、`enquires` 是掛在 room/node 上的 Merc runtime metadata
- `coord`、`cluster`、`labels` 是 graph/editor/export metadata，不是 `.roo` runtime 欄位
- 先跑 `--validate-only`，確認房號、方向、reverse exit、Job function 都合法，再輸出 `.roo`

## 建議主檔結構

```md
# 新區名稱

## 設計摘要
- 區域用途
- 玩家預期流程
- 服務點 / 問路點
- 特殊互動與劇情節點

## 拓樸說明
- 平面骨架
- 樓層 / 地下 / 室內外 / enter-out 結構
- 非格狀節點（休息室、傳送點、洞口、捷徑）

## 子圖索引
- `map-core.md`
- `map-floor-2.md`
- `map-services.md`
- `map-special-routes.md`

```mapmd-json
{
  "area": {
    "name": "new_test",
    "title": "測試區",
    "source_of_truth": "map.md"
  },
  "includes": [
    "map-core.md",
    "map-services.md"
  ]
}
```
```

## Graph-Native Room Schema

使用 fenced code block，info string 必須是 `mapmd-json`。

每個 block 是一個 JSON object，可包含：

- `area`: 區域摘要資料
- `includes`: 其他 markdown spec 檔，相對於目前檔案
- `rooms`: 房間列表

script 會遞迴載入 `includes`，並合併所有 `rooms`。

目前合法方向 enum 明確只支援：

- `north`
- `south`
- `east`
- `west`
- `up`
- `down`
- `enter`
- `out`

graph 上預設追求 edge 完整性，所以 reverse exit 預設必須成對；若 runtime intent 本來就是單向通道，才用 `one_way` 明確標示這是合法的非對稱例外。

## 欄位分類

| Field | Category | Generator behavior |
|---|---|---|
| `vnum` | required | validated + emitted |
| `name` | required | emitted |
| `description` | required | emitted |
| `exits` | generation | validated + emitted |
| `keywords` | generation | validated + emitted |
| `jobs` | generation | validated + emitted |
| `enquires` | generation | validated + emitted |
| `coord` | graph metadata | validated if present, not emitted |
| `cluster` | graph metadata | tolerated, validated if present, not emitted |
| `labels` | graph metadata | tolerated, validated if present, not emitted |
| `area.design_notes` | documentation metadata | tolerated, not emitted |

area metadata 再分兩類：

- generation-aware
  - `area.name`
  - `area.title`
- tolerated-but-ignored
  - `area.serial`
  - `area.capital`
  - `area.design_notes`

`labels` are non-runtime graph/editor annotations and are distinct from Merc runtime keywords.

## 機器可讀區塊格式

## Room Schema

```json
{
  "area": {
    "name": "new_test",
    "title": "測試區",
    "serial": 99,
    "capital": "洛陽",
    "design_notes": "這些欄位目前只作為文件與未來地圖工具預留"
  },
  "rooms": [
    {
      "vnum": 9101,
      "name": "測試入口",
      "description": "這裡是測試區的入口。",
      "sector_type": "SECT_CITY",
      "flags": ["Safe", "NoFight"],
      "coord": [0, 0, 0],
      "cluster": "entry-ring",
      "labels": ["入口", "問路點"],
      "notes": [
        "這是主入口，玩家第一次進區會先看到這裡"
      ],
      "exits": [
        {
          "direction": "north",
          "to": 9102
        },
        {
          "direction": "enter",
          "to": 9150,
          "exit_keyword": "gate",
          "exit_desc": "一道厚重的木門。",
          "flags": ["IsDoor", "Closed"]
        }
      ],
      "keywords": [
        {
          "keyword": "sign",
          "description": "牌子上寫著：往北前進可進入訓練區。"
        }
      ],
      "jobs": [
        {
          "keyword": "push",
          "function": "job_push_hidden_door",
          "position": "POS_STANDING",
          "notes": "若 repo 內尚無此 job，先不要輸出正式區域"
        }
      ],
      "enquires": [
        { "keyword": "入口" },
        { "keyword": "測試區" }
      ]
    }
  ]
}
```

## 欄位說明

### Room 常用欄位

- `vnum`: 必填，整數
- `name`: 必填
- `description`: 必填
- `sector_type`: 可省略，預設 `SECT_INSIDE`
- `flags`: 房間旗標陣列，例如 `Safe`、`NoFight`、`Memorize`
- `owner`: 可選，格式為 `[high, low]`
- `coord`: 可選，格式固定是 `[x, y, z]`，只做 graph/layout metadata
- `cluster`: 可選，非空字串，表示房間分群
- `labels`: 可選，字串陣列，只做 graph/editor/export annotation
- `notes`: 純註解，script 忽略

### Exit 欄位

- `direction`: 必填，僅允許 `north/east/south/west/up/down/enter/out`
- `to`: 必填，目標房號
- `exit_desc`: 可選
- `exit_keyword`: 可選，未填時輸出 `~`
- `message`: 可選
- `exit_key`: 可選，預設 `0`
- `flags`: 可選，允許 `IsDoor`、`Closed`、`Locked`、`Pick`
- `one_way`: 可選；若 `true`，script 不強制檢查 reverse exit，這是 graph completeness 的合法非對稱例外

### Keyword 欄位

- `keyword`: 必填
- `description`: 必填

只要玩家需要透過 `look <keyword>` 理解地形、路線或操作，就應該先寫進 spec。

注意：`labels` 不是 `#Keyword` 的替代品；`labels` 給圖工具與編輯器看，`keywords` 才會進 `.roo` 並影響 Merc runtime。

### Job 欄位

- `keyword`: 必填
- `function`: 必填，會對照 `src/job.c` 的 `job_lookup()`
- `position`: 必填，僅允許 `POS_DEAD`、`POS_SLEEPING`、`POS_RESTING`、`POS_FIGHTING`、`POS_STANDING`
- `notes`: 可選，script 忽略

只要玩家要在房間裡輸入特定指令才能觸發移動或事件，就應該在 spec 內明寫。

### Enquire 欄位

- `keyword`: 必填

只要房間要能被 `enquire` 問路找到，就應該在 spec 內列出所有同義詞。常見例子：

- 訓練者 / 訓練師 / 訓練
- 商店 / 道具屋
- 車站 / 驛站
- 碼頭 / 渡船

## 為什麼現在不直接用 SQLite / Mudlet

- 目前 source of truth 需要維持 Git-friendly 與人工可審閱
- 目前產生器的第一投影目標是 Merc `.roo`，不是外部 mapper
- 先把 Merc-specific runtime schema 定清楚，比過早綁定 Mudlet/SQLite 更重要
- 未來若要 export 到其他 mapper，`coord` / `cluster` / `labels` 會是預留的 graph metadata

## 特殊互動範例

### `#Keyword` + `#Job` 路線

```json
{
  "rooms": [
    {
      "vnum": 9211,
      "name": "時空裂縫處",
      "description": "這裡出現了一道裂縫(hole)。",
      "sector_type": "SECT_CITY",
      "exits": [
        { "direction": "north", "to": 9214 },
        { "direction": "south", "to": 9210 }
      ],
      "keywords": [
        {
          "keyword": "hole",
          "description": "有個柔和的聲音驅使你要鑽(bore)過這個裂縫。"
        }
      ],
      "jobs": [
        {
          "keyword": "bore",
          "function": "job_bore_hole",
          "position": "POS_STANDING"
        }
      ]
    }
  ]
}
```

### `#Enquire` 導流

```json
{
  "rooms": [
    {
      "vnum": 9541,
      "name": "宮城口",
      "description": "南邊是城門，北邊接宮城。",
      "sector_type": "SECT_CITY",
      "exits": [
        { "direction": "north", "to": 9535 },
        { "direction": "south", "to": 9501 },
        { "direction": "east", "to": 9542 },
        { "direction": "west", "to": 9540 }
      ],
      "enquires": [
        { "keyword": "訓練者" },
        { "keyword": "訓練師" },
        { "keyword": "訓練" }
      ]
    }
  ]
}
```

## 建議流程

1. 先寫人類可讀的區域設計摘要
2. 再寫 `mapmd-json` 區塊
3. 先跑：

```powershell
python .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/new_test/map.md --validate-only
```

4. 驗證通過後再輸出：

```powershell
python .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/new_test/map.md
```

5. 人工檢查產生的 `.roo`
6. 再補 `mob/obj/res/shp/index` 與系統耦合
