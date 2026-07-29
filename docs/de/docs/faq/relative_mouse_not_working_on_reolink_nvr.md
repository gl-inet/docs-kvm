# Was tun, wenn der relative Mausmodus auf Reolink NVR nicht funktioniert

Wenn Sie GL.iNet KVM zur Steuerung eines Reolink NVR verwenden (insbesondere bei Modellen, die keine zwei Mäuse unterstützen) oder bestimmte ältere Computer steuern (z. B. Geräte ohne USB-Schnittstellen), funktioniert der relative Mausmodus möglicherweise nicht. Häufige Probleme sind ein vollständiger Ausfall des Modus oder verfolgbare Mausbewegungen bei nicht reagierenden Klicks.

Dieses Problem entsteht hauptsächlich durch eine Kompatibilitätseinschränkung zwischen der Maussimulation des KVM und den begrenzten Fähigkeiten von Geräten wie Reolink NVR:

- **Vor Firmware v1.4.0**: Das KVM war darauf ausgelegt, nur eine Maus zu simulieren. Beim Wechsel zwischen relativem und absolutem Modus musste das KVM neu gestartet werden, funktionierte aber mit den meisten älteren oder spezialisierten Geräten gut.

- **Nach Firmware v1.4.0**: Um einen nahtlosen Moduswechsel ohne Neustart zu ermöglichen, wurde die Standardlogik so geändert, dass zwei Mäuse gleichzeitig simuliert werden (eine für den relativen Modus, die andere für den absoluten Modus). Reolink NVR und einige ältere Computer unterstützen jedoch keine zwei Mäuse. Dadurch treten zwei typische Probleme auf:

    - Der relative Mausmodus funktioniert überhaupt nicht;
    - die Mausbewegung wird weiterhin verfolgt, Klicks reagieren jedoch nicht.

Um das Problem zu beheben, können Sie den relativen Mausmodus im Terminal erzwingen. Führen Sie die folgenden Schritte aus:

1. Rufen Sie die KVM-Konsole auf und navigieren Sie zu **Toolbox** -> **Terminal**. Klicken Sie auf **Access**, um das KVM-Terminal zu öffnen.

2. Öffnen Sie die Konfigurationsdatei mit folgendem Befehl:

    `vi /etc/kvmd/override.yaml`

3. Führen Sie die folgende Konfiguration aus, um den relativen Mausmodus zu erzwingen:

    ```
    kvmd:
        hid:
            mouse:
                absolute: false
    ```

4. Speichern Sie die Datei und verlassen Sie den Editor.

5. Starten Sie das KVM-Gerät neu, damit die Änderungen wirksam werden.

!!! note

    1. Wenn die oben genannte Methode nicht funktioniert, versuchen Sie, die KVM-Firmware auf eine Version vor v1.4 zurückzusetzen (falls verfügbar). Diese unterstützt Ein-Maus-Emulation und ist mit älteren Geräten kompatibel.

    2. Die eigenständige GLKVM App für Mac OS unterstützt den relativen Mausmodus aufgrund von Einschränkungen des Browser-Kernels nicht (fehlende Unterstützung für die requestPointerLock API). Verwenden Sie stattdessen die Webkonsole.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
