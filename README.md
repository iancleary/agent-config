# agent-config

Personal Codex instructions and curated command policies, deployed with mise.

## Managed files

| Source | Destination |
| --- | --- |
| `codex/AGENTS.md` | `~/.codex/AGENTS.md` |
| `codex/rules/user-policy.rules` | `~/.codex/rules/user-policy.rules` |
| `codex/config/workspace-write.toml.tera` | Managed block in `~/.codex/config.toml` |

Use mise with `bootstrap dotfiles` support (verified with 2026.9.6).
Clone this repository on each machine, then run from the checkout:

```sh
mise trust mise.toml
mise bootstrap dotfiles diff
mise bootstrap dotfiles apply --dry-run
mise bootstrap dotfiles apply
mise bootstrap dotfiles status
```

For updates, commit and push source changes intentionally. On another machine,
run `git pull --ff-only`, review the diff, and apply with the commands above.
Edit source files in this repository. Copy mode can overwrite direct edits to
the destination; bring any wanted local changes into the source before applying.
If an existing destination conflicts, review and back it up before using `--force`.
Restart Codex after deploying instructions or rules.

Only the named files and workspace-write block are managed. Credentials,
sessions, the rest of `config.toml`, `rules/default.rules`, and other Codex
runtime files stay local. Automatic history watching and bidirectional
synchronization are not configured.

Skills remain installed separately from `iancleary/skills` and
`iancleary/release-skills`. Curated GitHub rules allow common reads and route
writes through approval. Machine-generated approvals in `rules/default.rules`
remain local and should be reviewed periodically.

See https://mise.jdx.dev/bootstrap/dotfiles.html for mise's dotfile contract.
