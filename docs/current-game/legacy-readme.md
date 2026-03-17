---
layout: default
title: Legacy Document README
---

# Legacy `document/README` 導讀

這頁整理 `document/README` 的重點，讓 GitHub Pages 可以直接看到這份舊版 Merc-FJU 釋出手冊的核心資訊。

## Source Of Truth

- legacy 文件來源：`document/README`
- 現行 build / startup / config 仍以 repo 內這些檔案為準：
  - `README.md`
  - `src/Makefile`
  - `src/Makefile.lin`
  - `src/startup`
  - `src/startup.bash`
  - `src/merc.sample.ini`
  - `src/merc.ini`

若這頁與目前 repo 流程不一致，以現行檔案為準。

## 這份文件在講什麼

`document/README` 是早期釋出包的總覽手冊，主要涵蓋：

- 基本系統需求
- 舊版安裝與解壓縮流程
- 初次編譯與啟動
- `merc.ini` 的最小必要設定
- area 目錄的基本組成
- 錯誤回報與共享原則

## 舊版安裝流程摘要

文件假設使用者拿到 `merc-fju.tar.gz`，並在 Linux / FreeBSD 環境下執行：

```bash
cd ~
tar zxvf merc-fju.tar.gz > /dev/null
cd ~/mud/src
make clean; make
startup &
```

這是 legacy 釋出包的操作方式，和目前 repo 在 macOS、Linux、Docker、WSL 下的開發流程不完全相同。

## 文件列出的目錄結構

`document/README` 把舊版工作樹分成幾個主要區塊：

- `src/`
- `area/`
- `data/`
- `document/`
- `skill/`
- `help/`
- `social/`
- `player/`
- `mail/`
- `log/`
- `debug/`

對 area builder 最有用的，是它明確說明一個 area 至少包含：

- `index`
- `mob/`
- `obj/`
- `res/`
- `roo/`
- `shp/`

## `merc.ini` 最先要改的欄位

文件特別點名初次啟動至少要先設定：

- `NAME`
- `MUD PORT`
- `HOME DIRECTORY`

這個觀念仍然重要，但實際欄位來源應改查目前 repo 的 `src/merc.sample.ini` / `src/merc.ini`。

## 對目前 repo 仍有用的重點

- 它解釋了 `document/` 這批手冊原本的角色。
- 它說明了 area 子目錄的基本拆分方式。
- 它提醒技能與 area data 不是單靠原始碼就能理解，還要回看資料格式文件。

## 對目前 repo 已過時的部分

- 舊版 Linux kernel、CPU、記憶體需求
- `tar.gz` 釋出包安裝步驟
- 直接用 `startup &` 當唯一建議入口
- 舊 BBS 與 email 回報管道

## 建議搭配閱讀

- [Legacy `document/` 入口](./legacy-documentation.html)
- [Area index / title 檔格式說明](./title-file-format.html)
- `README.md`
- `src/merc.sample.ini`
- `src/startup.bash`
