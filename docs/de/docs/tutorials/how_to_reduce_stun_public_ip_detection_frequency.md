# STUN-Erkennung der oeffentlichen IP seltener ausfuehren

Das KVM-Geraet verwendet STUN-Anfragen, um seine oeffentliche IP-Adresse fuer den Fernzugriff zu erkennen. Standardmaessig sendet das Geraet in regelmaessigen Abstaenden STUN-Erkennungsanfragen. Wenn Sie nur ueber ein lokales Netzwerk oder VPN auf das KVM zugreifen, koennen Sie die Konfiguration anpassen, um die STUN-Anfragehaeufigkeit zu reduzieren.

Fuehren Sie den folgenden Befehl aus, um das STUN-Erkennungsintervall zu verlaengern und die Anfragehaeufigkeit zu verringern:

```bash
cat > /etc/kvmd/override.yaml << EOF
janus:
    check:
        retries: 10000
EOF
```

> **Hinweis:** Diese Konfiguration reduziert die Anzahl der von Janus initiierten STUN-Anfragen erheblich. Sie kann jedoch auch die Erfolgsrate von STUN Hole Punching fuer externe Netzwerknutzung verringern. **Wenden Sie dies nur an, wenn Sie ausschliesslich ueber ein lokales Netzwerk oder VPN auf das KVM zugreifen.**

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
