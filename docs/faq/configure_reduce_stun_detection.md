# How to configure reduce STUN public IP detection

The KVM device uses STUN requests to detect the public IP address for remote access. By default, the device sends STUN requests at regular intervals. If you only access the KVM via local network or VPN, you can reduce the frequency of these requests.

## Configuration

Run the following command to increase the STUN detection interval:

```bash
cat > /etc/kvmd/override.yaml << EOF
janus:
    check:
        retries: 10000
EOF
```

> **Note:** This configuration significantly reduces the frequency of STUN requests sent by Janus, but it may also decrease the success rate of STUN hole punching. Only apply this configuration if you are certain that you only access the KVM via local network or VPN.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
