# How to reduce STUN Public IP detection frequency

The KVM device uses STUN requests to detect its public IP address for remote access. By default, the device sends STUN detection requests at regular intervals. If you only access the KVM over a local network or VPN, you can adjust the configuration to reduce the STUN request frequency.

Log in to the KVM via SSH or open **Toolbox** > **Terminal** in the KVM console. Back up the existing override file before editing it:

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

If you already have an `override.yaml.bak` backup, choose a different backup filename to preserve it. If `override.yaml` does not exist, skip the backup command and create it with the editor.

Merge the following setting into the file, preserving all existing overrides:

```yaml
janus:
    check:
        retries: 10000
```

If a `janus` section already exists, add or update `check.retries` within that section. If `check` already exists under `janus`, update its `retries` value or add it there. Do not create duplicate `janus` or `check` keys. Use spaces for YAML indentation and save the file when finished.

> **Note:** This configuration greatly reduces the number of STUN requests initiated by Janus. However, it may also lower the success rate of STUN hole punching for external network penetration. **Only apply this if you exclusively access the KVM via a local network or VPN.**

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
