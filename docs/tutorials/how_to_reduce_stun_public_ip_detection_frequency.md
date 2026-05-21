# How to reduce STUN Public IP detection frequency?

The KVM device uses STUN requests to detect its public IP address for remote access. By default, the device sends STUN detection requests at regular intervals. If you only access the KVM over a local network or VPN, you can adjust the configuration to reduce the STUN request frequency.

Run the following command to extend the STUN detection interval and lower request frequency:

```bash
cat > /etc/kvmd/override.yaml << EOF
janus:
    check:
        retries: 10000
EOF
```

> **Note:** This configuration greatly reduces the number of STUN requests initiated by Janus. However, it may also lower the success rate of STUN hole punching for external network penetration. **Only apply this if you exclusively access the KVM via a local network or VPN.**

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
