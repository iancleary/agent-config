# agent-config

Personal Codex instructions and curated command policies, deployed with mise.

## Managed files

| Source | Destination |
| --- | --- |
| `codex/AGENTS.md` | `~/.codex/AGENTS.md` |
| `codex/rules/user-policy.rules` | `~/.codex/rules/user-policy.rules` |
| `codex/config/workspace-write.toml.tera` | Managed workspace-write block in `~/.codex/config.toml` |
| `codex/config/features.toml.tera` | Managed Codex feature block in `~/.codex/config.toml` |

The workspace-write block grants access to `~/Work/skills`,
`~/Work/agent-config`, and `~/Work/release-skills`. It does not grant access
to the whole home directory.

Use mise with `bootstrap dotfiles` support (verified with 2026.9.6).
If your Codex configuration already has a `[features]` table, complete the
[feature-block adoption](#standalone-codex-sessions) before applying this baseline.
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

Only the named files and configuration blocks are managed. Credentials,
sessions, the rest of `config.toml`, `rules/default.rules`, and other Codex
runtime files stay local. Automatic history watching and bidirectional
synchronization are not configured.

Skills remain installed separately from `iancleary/skills` and
`iancleary/release-skills`. Curated GitHub rules allow common reads and route
writes through approval. Machine-generated approvals in `rules/default.rules`
remain local and should be reviewed periodically.

See https://mise.jdx.dev/dotfiles.html for mise's dotfile contract.

## Standalone Codex sessions

The managed feature block sets `features.daemon_auto_start = false`.
Standalone sessions retain their terminal context for Moshi hooks. This baseline
does not use Codex's shared daemon or its shared-session and remote-control features.

Before first applying on a host with an existing `[features]` table, back up
`~/.codex/config.toml`. Wrap its table header and any existing `daemon_auto_start`
setting in the managed markers. Leave other feature keys below the closing marker:

```toml
# >>> mise:codex-features >>> managed by mise — do not edit between markers
[features]
daemon_auto_start = false
# <<< mise:codex-features <<<
# Existing host-owned feature keys stay here, before the next table header.
```

Do not add a second `[features]` table. Mise appends missing blocks; a duplicate
TOML table would invalidate the file. Other feature keys remain host-owned.

Preview and apply only this configuration from the checkout:

```sh
mise bootstrap dotfiles diff '~/.codex/config.toml'
mise bootstrap dotfiles apply --dry-run '~/.codex/config.toml'
mise bootstrap dotfiles apply '~/.codex/config.toml'
```

After exiting sessions attached to an existing shared daemon, stop it with
`codex app-server daemon stop`. Stop its remaining `app-server daemon pid-update-loop`
process as well. Do not stop unrelated desktop or IDE app servers.
The setting does not disconnect an already-running daemon by itself.

Verify the setting with `codex features list`. Confirm that the managed daemon
and its updater are no longer running. `codex app-server daemon version` requires
a running server; after stopping it, the missing-socket error is expected.
Run `uv run --no-project --managed-python --python '>=3.11' python scripts/test_codex_config.py`
to check fresh application, existing feature preservation, and drift correction.

## Releases

Releases use UTC CalVer `YYYY.MM.DD.XX` and the checked-in `release.toml`
contract. See [`docs/release.md`](docs/release.md).
