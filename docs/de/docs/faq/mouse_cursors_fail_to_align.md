# Was tun, wenn die Mauszeiger nicht deckungsgleich sind

Wenn der Mauszeiger auf dem steuernden Gerät nicht mit dem Mauszeiger auf dem gesteuerten Gerät übereinstimmt, führen Sie die folgenden Schritte zur Fehlerbehebung aus.

![cursor misalignment](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. **Prüfen Sie, ob das Problem während der Mausbewegung oder im Ruhezustand auftritt.**

    <u>Fall 1</u>. Wenn die Zeiger im Ruhezustand korrekt übereinstimmen, während der Bewegung aber auseinanderlaufen, prüfen Sie das Netzwerk auf beiden Seiten und stellen Sie eine stabile Verbindung sicher.

    Zusätzlich können Sie den lokalen Zeiger ausblenden, sodass auf dem Steuerungsbildschirm nur der Remote-Zeiger angezeigt wird. Dadurch lassen sich Probleme mit versetzten Mauszeigern vermeiden.

    Navigieren Sie in der KVM-Konsole zu **Settings** -> **Remote Device Settings** -> **Show Local Cursor** und deaktivieren Sie diese Option.

    ![hide local cursor](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

    <u>Fall 2</u>. Wenn die Zeiger selbst im Ruhezustand nicht übereinstimmen, wählen Sie in der KVM-Konsole den Gerätetyp erneut aus (nur für Comet Q / GL-RMQ1).

    ![device type](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}

    Wenn das Problem weiterhin besteht, fahren Sie mit dem nächsten Schritt fort.

2. **Wenn das gesteuerte Gerät ein Laptop ist, liegt die Ursache wahrscheinlich in einer falschen Bildschirmauflösung.**

    Prüfen Sie das Seitenverhältnis des Laptop-Bildschirms. Anschließend können Sie entweder die Auflösung auf dem gesteuerten Laptop anpassen oder die EDID-Einstellung Ihres KVM-Geräts ändern.

    ??? note "Auflösung auf dem gesteuerten Laptop anpassen"

        **Für macOS**:

        1. Gehen Sie zu **Settings** -> **Displays** -> **Optimize for**.

            ![mac displays](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. Ändern Sie die Einstellung auf **GLKVM**.

            ![select glkvm](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. Wählen Sie die passende Auflösung aus und prüfen Sie anschließend, ob die Mauszeiger übereinanderliegen.

            ![resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **Für Windows**:

        1. Gehen Sie zu **Settings** -> **System** -> **Displays**.

            ![windows display](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. Scrollen Sie nach unten zu **Display resolution** und klicken Sie auf das Feld rechts.

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. Wählen Sie die passende Bildschirmauflösung aus und klicken Sie im Popup-Fenster auf **Keep changes**, um sie zu übernehmen.

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "EDID-Einstellung Ihres KVM-Geräts ändern"

        EDID steht für Extended Display Identification Data und gleicht automatisch die optimalen Anzeigeparameter ab. Die Standard-EDID ist für die meisten Szenarien geeignet und muss normalerweise nicht geändert werden. Details finden Sie [hier](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}.

        Wenn die EDID geändert wurde, der Bildschirm aber nicht aktualisiert wird, versuchen Sie, das gesteuerte Gerät neu zu starten.

3. **Wenn das gesteuerte Gerät kein Laptop ist (z. B. ein Desktop-PC mit externem Monitor)**, prüfen Sie das Seitenverhältnis der Hauptanzeige und stellen Sie anschließend die EDID Ihres KVM entsprechend um. Details finden Sie [hier](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
