# De frequentie van STUN-detectie van het openbare IP-adres verlagen {#how-to-reduce-stun-public-ip-detection-frequency}

Het KVM-apparaat gebruikt STUN-verzoeken om zijn openbare IP-adres te detecteren voor externe toegang. Standaard verzendt het apparaat met regelmatige tussenpozen STUN-detectieverzoeken. Als u de KVM alleen via een lokaal netwerk of VPN opent, kunt u de configuratie aanpassen om de frequentie van STUN-verzoeken te verlagen.

Meld u via SSH aan bij de KVM of open **Toolbox** > **Terminal** in de KVM-console. Maak een back-up van het bestaande override-bestand voordat u het bewerkt:

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

Als u al een back-up `override.yaml.bak` hebt, kiest u een andere bestandsnaam voor de back-up om die te behouden. Als `override.yaml` niet bestaat, slaat u de back-upopdracht over en maakt u het bestand aan met de editor.

Voeg de volgende instelling samen met het bestand en behoud daarbij alle bestaande overrides:

```yaml
janus:
    check:
        retries: 10000
```

Als er al een sectie `janus` bestaat, voegt u `check.retries` toe binnen die sectie of werkt u deze bij. Als `check` al onder `janus` bestaat, werkt u de waarde van `retries` bij of voegt u deze daar toe. Maak geen dubbele sleutels `janus` of `check` aan. Gebruik spaties voor de YAML-inspringing en sla het bestand op als u klaar bent.

> **Opmerking:** Deze configuratie vermindert het aantal STUN-verzoeken van Janus aanzienlijk. Het kan echter ook de kans verkleinen dat STUN-hole-punching voor verbindingen via externe netwerken slaagt. **Pas dit alleen toe als u de KVM uitsluitend via een lokaal netwerk of VPN opent.**

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
