#!/usr/bin/env python3
"""
Big5 → UTF-8 批次轉換腳本
用於 MUD2 專案中文編碼轉換
"""

import os
import sys
from typing import Optional, Tuple

# 排除的目錄（.git 版本控制、log 和 debug 為執行時產生的日誌）
SKIP_DIRS = {'.git', 'log', 'debug'}

# 排除的副檔名（二進位檔）
SKIP_EXTENSIONS = {
    '.gz', '.zip', '.tar', '.bz2', '.xz',
    '.png', '.jpg', '.gif', '.bmp',
    '.exe', '.so', '.o', '.a',
    '.pdf', '.doc', '.xls',
}

CANDIDATE_ENCODINGS = (
    'utf-8',        # 優先確認是否已是 UTF-8
    'utf-8-sig',    # Windows 產生的 UTF-8 with BOM
    'big5hkscs',    # Big5 + 香港增補字集
    'cp950',        # Big5 + ETen
)

def is_pure_ascii(data: bytes) -> bool:
    """判斷是否為純 ASCII"""
    return all(b < 128 for b in data)

def decode_with_candidates(data: bytes) -> Optional[Tuple[str, str]]:
    """
    嘗試使用多種常見編碼解碼字串，成功則回傳 (encoding, text)。
    """
    for encoding in CANDIDATE_ENCODINGS:
        try:
            return encoding, data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return None

def convert_file(filepath: str) -> str:
    """
    嘗試將檔案轉為 UTF-8。
    回傳: 'ascii' | 'utf8' | 'converted:<來源編碼>' | 'skip_invalid' | 'skip_binary' | 'error:...'
    """
    # 跳過副檔名屬於二進位類型的檔案
    _, ext = os.path.splitext(filepath)
    if ext.lower() in SKIP_EXTENSIONS:
        return 'skip_binary'

    try:
        with open(filepath, 'rb') as f:
            raw = f.read()
    except OSError as e:
        return f'error:{e}'

    # 純 ASCII 不需要轉換
    if is_pure_ascii(raw):
        return 'ascii'

    decoded = decode_with_candidates(raw)
    if not decoded:
        return 'skip_invalid'

    encoding, text = decoded

    # 已是 UTF-8（無 BOM）直接跳過
    if encoding == 'utf-8':
        return 'utf8'

    # 編碼回 UTF-8 並寫入
    # 若原本為 UTF-8 with BOM，重新寫入可順便移除 BOM
    utf8_data = text.encode('utf-8')
    if utf8_data == raw:
        # 避免重複寫入
        return 'utf8'

    try:
        with open(filepath, 'wb') as f:
            f.write(utf8_data)
        if encoding == 'utf-8-sig':
            return 'converted:utf-8-sig'
        return f'converted:{encoding}'
    except OSError as e:
        return f'error:{e}'

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    print(f"掃描目錄：{root}")

    stats = {
        'ascii': 0,
        'utf8': 0,
        'converted': 0,
        'skip_invalid': 0,
        'skip_binary': 0,
        'error': 0,
    }
    converted_files = []
    skipped_files = []
    error_files = []
    converted_detail = []

    for dirpath, dirnames, filenames in os.walk(root):
        # 跳過排除的目錄（in-place 修改 dirnames 讓 os.walk 不進入）
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            rel = os.path.relpath(filepath, root)

            result = convert_file(filepath)

            if result == 'converted':
                stats['converted'] += 1
                converted_files.append(rel)
            elif result.startswith('converted:'):
                stats['converted'] += 1
                converted_files.append(rel)
                converted_detail.append(f"{rel} ({result.split(':',1)[1]})")
            elif result == 'ascii':
                stats['ascii'] += 1
            elif result == 'utf8':
                stats['utf8'] += 1
            elif result == 'skip_invalid':
                stats['skip_invalid'] += 1
                skipped_files.append(rel)
            elif result == 'skip_binary':
                stats['skip_binary'] += 1
            else:
                stats['error'] += 1
                error_files.append((rel, result))

    # 輸出統計
    print("\n===== 轉換完成 =====")
    print(f"  成功轉換 (Big5→UTF-8) : {stats['converted']:4d} 個")
    print(f"  純 ASCII (跳過)        : {stats['ascii']:4d} 個")
    print(f"  已是 UTF-8 (跳過)      : {stats['utf8']:4d} 個")
    print(f"  無效 Big5 (跳過)       : {stats['skip_invalid']:4d} 個")
    print(f"  二進位檔 (跳過)        : {stats['skip_binary']:4d} 個")
    print(f"  錯誤                   : {stats['error']:4d} 個")

    if skipped_files:
        print(f"\n--- 無法辨識為 Big5 的檔案 ({len(skipped_files)}) ---")
        for f in skipped_files[:20]:
            print(f"  {f}")
        if len(skipped_files) > 20:
            print(f"  ...（共 {len(skipped_files)} 個，僅顯示前 20）")

    if error_files:
        print(f"\n--- 錯誤檔案 ({len(error_files)}) ---")
        for f, msg in error_files:
            print(f"  {f}: {msg}")

    if converted_files:
        print(f"\n--- 已轉換的檔案 ({len(converted_files)}) ---")
        for f in converted_files[:30]:
            print(f"  {f}")
        if len(converted_files) > 30:
            print(f"  ...（共 {len(converted_files)} 個，僅顯示前 30）")
    if converted_detail:
        print("\n--- 來源編碼摘要 ---")
        for line in converted_detail[:30]:
            print(f"  {line}")

if __name__ == '__main__':
    main()
