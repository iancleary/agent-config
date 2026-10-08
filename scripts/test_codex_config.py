"""Verify managed Codex feature settings against isolated host configuration."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import tomllib

repo = Path(__file__).resolve().parents[1]
mise = shutil.which('mise')
assert mise, 'mise is required'

with tempfile.TemporaryDirectory(prefix='agent-config-features-') as scratch:
    root = Path(scratch)
    for existing_features in (False, True):
        home = root / ('existing' if existing_features else 'fresh')
        config = home / '.codex/config.toml'
        config.parent.mkdir(parents=True)
        feature_section = '''# >>> mise:codex-features >>> managed by mise — do not edit between markers
[features]
# <<< mise:codex-features <<<
hooks = true
js_repl = false

''' if existing_features else ''
        config.write_text(feature_section + '[local]\nkeep = "host-owned"\n')
        env = {key: value for key, value in os.environ.items()
               if not key.startswith('MISE_')}
        env.update(HOME=str(home), XDG_CONFIG_HOME=str(home / '.config'),
                   XDG_DATA_HOME=str(home / '.local/share'),
                   XDG_STATE_HOME=str(home / '.local/state'),
                   XDG_CACHE_HOME=str(home / '.cache'),
                   MISE_CONFIG_DIR=str(home / '.config/mise'),
                   MISE_SYSTEM_CONFIG_DIR=str(root / 'system'),
                   MISE_CONFIG_FILE=str(repo / 'mise.toml'),
                   MISE_TRUSTED_CONFIG_PATHS=str(repo), MISE_AUTO_UPDATE='0')
        command = [mise, 'bootstrap', 'dotfiles', 'apply', '--yes', str(config)]
        result = subprocess.run(command, cwd=repo, env=env,
                                capture_output=True, text=True)
        assert result.returncode == 0, result.stdout + result.stderr
        actual = tomllib.loads(config.read_text())
        expected_features = ({'daemon_auto_start': False, 'hooks': True, 'js_repl': False}
                             if existing_features else {'daemon_auto_start': False})
        assert actual['features'] == expected_features, actual
        assert actual['local'] == {'keep': 'host-owned'}, actual
        assert actual['sandbox_workspace_write']['writable_roots'] == [
            str(home / 'Work/skills'),
            str(home / 'Work/agent-config'),
            str(home / 'Work/release-skills'),
        ], actual['sandbox_workspace_write']
        config.write_text(config.read_text().replace(
            'daemon_auto_start = false', 'daemon_auto_start = true'))
        result = subprocess.run(command, cwd=repo, env=env,
                                capture_output=True, text=True)
        assert result.returncode == 0, result.stdout + result.stderr
        assert tomllib.loads(config.read_text()) == actual

print('PASS: standalone Codex setting, existing feature preservation, and repeat apply')
