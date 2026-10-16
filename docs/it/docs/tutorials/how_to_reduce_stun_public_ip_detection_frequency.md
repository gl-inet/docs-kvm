# Come ridurre la frequenza di rilevamento dell'IP pubblico tramite STUN {#how-to-reduce-stun-public-ip-detection-frequency}

Il dispositivo KVM usa richieste STUN per rilevare il proprio indirizzo IP pubblico per l'accesso remoto. Per impostazione predefinita, invia le richieste di rilevamento a intervalli regolari. Se accedi al KVM solo tramite una rete locale o una VPN, puoi modificare la configurazione per ridurre la frequenza delle richieste STUN.

Accedi al KVM tramite SSH oppure apri **Toolbox** > **Terminal** nella console del KVM. Prima di modificare il file delle impostazioni personalizzate, eseguine una copia di backup:

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

Se hai già una copia di backup chiamata `override.yaml.bak`, scegli un altro nome per conservarla. Se `override.yaml` non esiste, salta il comando di backup e crea il file con l'editor.

Integra la seguente impostazione nel file, mantenendo tutte le impostazioni personalizzate esistenti:

```yaml
janus:
    check:
        retries: 10000
```

Se esiste già una sezione `janus`, aggiungi o aggiorna `check.retries` al suo interno. Se sotto `janus` esiste già `check`, aggiorna o aggiungi lì il valore `retries`. Non creare chiavi `janus` o `check` duplicate. Usa spazi per l'indentazione YAML e salva il file al termine.

> **Nota:** questa configurazione riduce notevolmente il numero di richieste STUN avviate da Janus. Può tuttavia ridurre anche la percentuale di successo dell'hole punching STUN per l'accesso dalle reti esterne. **Applicala solo se accedi al KVM esclusivamente tramite una rete locale o una VPN.**

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
