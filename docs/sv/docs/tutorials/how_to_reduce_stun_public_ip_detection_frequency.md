# Så minskar du hur ofta den publika IP-adressen identifieras via STUN {#how-to-reduce-stun-public-ip-detection-frequency}

KVM-enheten använder STUN-förfrågningar för att identifiera sin publika IP-adress för fjärråtkomst. Som standard skickar enheten STUN-förfrågningar med jämna mellanrum. Om du bara kommer åt KVM-enheten via ett lokalt nätverk eller VPN kan du ändra konfigurationen för att minska hur ofta STUN-förfrågningar skickas.

Logga in på KVM-enheten via SSH eller öppna **Toolbox** > **Terminal** i KVM-konsolen. Säkerhetskopiera den befintliga override-filen innan du redigerar den:

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

Om du redan har en säkerhetskopia med namnet `override.yaml.bak` väljer du ett annat filnamn för säkerhetskopian så att den befintliga bevaras. Om `override.yaml` inte finns hoppar du över kommandot för säkerhetskopiering och skapar filen med redigeraren.

Lägg in följande inställning i filen och behåll alla befintliga åsidosättningar:

```yaml
janus:
    check:
        retries: 10000
```

Om det redan finns ett `janus`-avsnitt lägger du till eller uppdaterar `check.retries` i det avsnittet. Om `check` redan finns under `janus` uppdaterar du värdet för `retries` eller lägger till det där. Skapa inte dubbla nycklar för `janus` eller `check`. Använd blanksteg för YAML-indraget och spara filen när du är klar.

> **Obs!** Den här konfigurationen minskar avsevärt antalet STUN-förfrågningar som Janus skickar. Den kan dock även sänka andelen lyckade STUN-hålslagningar (hole punching) för att ta sig igenom externa nätverk. **Använd den bara om du uteslutande kommer åt KVM-enheten via ett lokalt nätverk eller VPN.**

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
