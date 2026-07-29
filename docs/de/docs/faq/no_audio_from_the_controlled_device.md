# Was tun, wenn vom gesteuerten Gerät kein Audio zu hören ist

Wenn Sie nach dem Verbinden von KVM und gesteuertem Gerät kein Audio vom gesteuerten Gerät hören (z. B. kein Ton beim Abspielen von Videos auf dem Gerät), helfen möglicherweise die folgenden Schritte zur Fehlerbehebung:

1. Stellen Sie sicher, dass Speaker in der KVM-Konsole aktiviert ist.

    Navigieren Sie in der KVM-Konsole zu **Settings** -> **Remote Device Settings** -> **Speaker** und stellen Sie sicher, dass der Lautsprecher aktiviert ist. Prüfen Sie außerdem, ob das Symbol unten rechts leuchtet; dies zeigt an, dass die Funktion aktiv ist.

    ![speaker](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/speaker.png){class="glboxshadow"}

2. Stellen Sie sicher, dass alle Kabel zwischen KVM und gesteuertem Gerät fest angeschlossen sind. Lose Kabelverbindungen können die Audioausgabe beeinträchtigen.

3. Prüfen Sie, ob ein HDMI-Konverter angeschlossen ist. Manche Konverter unterstützen kein Audio.

    Es wird empfohlen, das mitgelieferte HDMI-Kabel zu verwenden, da einige HDMI-Kabel älterer Standards keine Audioübertragung unterstützen.

4. Prüfen Sie, ob das Host-Gerät und das gesteuerte Gerät stummgeschaltet sind.

5. Prüfen Sie die Ausgabeeinstellungen Ihres gesteuerten Geräts und stellen Sie sicher, dass das Ausgabegerät **GLKVM** ist.

    ??? "macOS"

        Gehen Sie auf dem gesteuerten Gerät zu **Settings** -> **Sound** -> **Output & Input** -> **Output** und stellen Sie das Ausgabegerät auf **GLKVM** um.

        ![mac output settings](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        Gehen Sie auf dem gesteuerten Gerät zu **Settings** -> **Sound** -> **Output** und stellen Sie das Ausgabegerät auf **GLKVM** um.

        ![wins output settings 1](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![wins output settings 2](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        Alternativ können Sie unten rechts auf dem gesteuerten Gerät auf das Tonsymbol klicken und **GLKVM** als Wiedergabegerät auswählen.

        ![wins output settings 3](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. Prüfen Sie den Grafikkartentreiber des gesteuerten Geräts. Wenn auf dem gesteuerten Gerät kein Grafikkartentreiber vorhanden ist, kann es kein Audio ausgeben; dadurch ist am steuernden Ende kein Ton hörbar.

7. Prüfen Sie die erweiterten Soundeinstellungen auf Ihrem Host-Gerät und stellen Sie sicher, dass Ihr Browser eine aktive Lautstärkeausgabe hat.

    Unten sehen Sie als Referenz ein Beispiel für die erweiterten Soundeinstellungen in Windows 10 Pro.

    Gehen Sie zu **Settings** -> **Sound** -> **Advanced sound options**.

    ![advanced sound options](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/advanced_sound_options.png){class="glboxshadow"}

    Passen Sie die Lautstärke für bestimmte Apps und Systemtöne an.

    ![app volume](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/app_volume.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
