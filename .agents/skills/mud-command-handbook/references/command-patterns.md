# Command Patterns

## Merc-FJU first

When the workspace is this repo, answer from checked-in files before giving generic MUD syntax.

Read in this order:

1. `command/<initial>/<command>.ins`
2. matching `do_<command>` implementation in `src/`
3. verification/readback command output in source if the visible fields matter

## Common Merc-FJU command families

### Character edits

- Primary write command: `mset <target> <field> <value>`
- Primary readback command: `mstat <target>`
- Typical fields to confirm in repo help/source:
  - stats: `str`, `int`, `wis`, `dex`, `con`
  - progression: `level`, `practice`, `align`
  - money/state: `gold`, `bank`, `thirst`, `drunk`, `full`

### Object edits

- Primary write command: `oset <object> <field> <value>`
- Primary readback command: `ostat <object>`

### Money handling

- On-hand money often uses `gold`
- Bank deposit often uses `bank`
- Player-facing banking may use `deposit`, `withdraw`, `check`
- Always distinguish:
  - set administrative value
  - give/spend player transaction
  - on-hand money vs banked money

### Movement and admin relocation

- Common admin movement families to verify in repo:
  - `goto`
  - `transfer`
  - room lookup helpers such as `find_location`

## Verification habits

- After a write, prefer a direct readback command over inference.
- If money or stats change, `mstat` is usually better than `score` because it exposes admin-visible fields.
- If the help file shows a level gate, mention it when the answer depends on permissions.
- If the implementation resolves targets with world lookup, say the target typically must be online or present in the world state.

## Common answer notes

Use short notes like these when supported by source:

- "This sets the value directly; it does not add to the current amount."
- "This only works on an online/in-world target."
- "This requires GM level `L_DEI`."
- "Use `bank` instead of `gold` if you want stored money rather than on-hand money."

## Generic variants fallback

Only use these when the repo does not establish one clear command:

- `set <target> <stat> <value>`
- `setattr <target> <stat> <value>`
- `mset <target> <stat> <value>`
- `@set <target>/<stat>=<value>`

## Safety checklist

1. Confirm permission level and target identity.
2. Confirm whether the command overwrites or increments.
3. Confirm whether the target must be online.
4. Execute the command.
5. Verify with readback.
6. Mention rollback by restoring the previous value when relevant.
