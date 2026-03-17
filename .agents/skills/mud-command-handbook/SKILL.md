---
name: mud-command-handbook
description: Answer MUD/MMORPG player and GM command questions with executable syntax, permission notes, verification steps, and repo-grounded guidance. Use when the user asks how to run in-game commands, GM/admin operations, stat or money changes, item edits, teleport/spawn actions, moderation commands, or rollback/safety procedures. In this Merc-FJU repo, prefer the actual checked-in command/help/source files over generic MUD variants.
---

# MUD Command Handbook

Provide short, executable command guidance.
Prefer the exact syntax implemented in the current game before offering generic variants.

## Workflow

1. Identify the execution context.
- Distinguish `player`, `GM`, `admin`, `console`, and offline data edit.
- If the repo is available, inspect checked-in command/help/source files before answering from memory.

2. Identify the target and scope.
- Determine whether the action affects self, another player, NPC, online-only target, offline target, or persistent storage.
- Call out scope when it matters: overwrite vs increment, on-body money vs bank, temporary vs permanent.

3. Prefer repo-grounded answers.
- In Merc-FJU, check command help under `command/**/*.ins` and implementation under `src/` for the exact command name, syntax, and level gate.
- Use the repo's actual verification command when available, such as `mstat`, `ostat`, `rstat`, `score`, `inventory`, `where`, or bank/check commands.
- Only provide common engine variants when the repo does not establish one clear answer.

4. Return the shortest usable answer first.
- Lead with the exact command block.
- Add 1-3 short notes: permission, verification, and any important behavior such as "sets value directly" or "target must be online".

5. Add safety guardrails for high-impact actions.
- Warn before destructive or moderation actions.
- Prefer readback after write.
- Never suggest bypassing auth, editing production data behind the game's permission model, or exploiting bugs.

## Merc-FJU lookup guide

When answering against this repo, inspect the smallest relevant set:

- Command help and level gate:
  - `command/<initial>/<command>.ins`
- Command implementation and field semantics:
  - usually `src/act_wiz.c`, `src/act_obj.c`, `src/act_move.c`, or nearby `src/act_*.c`
- Validation/readback command:
  - often the matching `*stat` command help plus its source output fields

Useful patterns:

- Character edits: search `do_mset`, `do_mstat`
- Object edits: search `do_oset`, `do_ostat`
- Room/admin movement: search `goto`, `transfer`, `find_location`
- Money and banking: search `gold`, `bank`, `deposit`, `withdraw`, `check`

## Response format

Use this shape when it helps:

1. `Assumption`: role and engine assumptions.
2. `Command`: exact command to type.
3. `Verify`: fastest readback command.
4. `Notes`: permission, overwrite/increment behavior, target limitations, or rollback hint.
5. `Variants`: only if the implementation is genuinely ambiguous.

Keep the answer compact unless the user asks for comparison or deeper explanation.

## Repo-specific defaults

- Treat Merc-FJU as the primary target when the workspace is this repo.
- Prefer `mset`/`mstat` style answers when supported by repo files; do not default to generic `set` syntax.
- Mention command levels when the `.ins` file exposes them and the answer depends on GM rank.
- If the implementation uses `get_char_world` or similar runtime lookup, tell the user the target usually needs to be online/in-world.
- If a field writes directly (`victim->gold = value`), explicitly say it is a direct set, not an increment.

## Example

User asks:
- "GM 如何把自己金錢設成 100000？"

Answer pattern:

- `Assumption`: You are a GM with permission to use `mset`.
- `Command`: `mset <your_name> gold 100000`
- `Verify`: `mstat <your_name>`
- `Notes`: This sets on-hand money directly. If you want bank deposit instead, use `mset <your_name> bank 100000`. In Merc-FJU, the target is typically found in-world rather than edited offline.

## References

Load [references/command-patterns.md](references/command-patterns.md) when you need:
- Merc-FJU-specific command lookup patterns,
- common command families and verification habits,
- short safety and rollback reminders.
