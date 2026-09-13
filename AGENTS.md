# Agent configuration maintenance

This repository owns the global Codex baseline and curated command policies.
The deployable baseline is `codex/AGENTS.md`; this file governs this repository.

- Keep changes scoped to the requested configuration.
- Manage only the explicit targets in `mise.toml`.
- Preserve machine-local configuration outside the managed block, credentials,
  sessions, and `rules/default.rules`.
- Preview deployment with `mise bootstrap dotfiles diff` and `mise bootstrap dotfiles apply --dry-run`.
- Apply when deployment is authorized, then verify with `mise bootstrap dotfiles status`.
- Run `git diff --check`. For rule changes, use `codex execpolicy check` with representative commands.
- Do not push or enable automatic synchronization unless requested.

## Releases

- Use the repository-local `cut-release` skill for ordinary releases.
- Use UTC CalVer `YYYY.MM.DD.XX` through `uv run scripts/release.py`.
- Read `docs/release.md` before changing or running the release workflow.
