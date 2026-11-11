# Wie kann ich bidirektionales Audio für Remote-Meetings nutzen? {#how-can-i-use-two-way-audio-for-remote-meetings}

Wenn Sie von zu Hause arbeiten, können Sie per KVM auf Ihren Bürocomputer zugreifen und über Zoom, Microsoft Teams oder eine ähnliche App an Audiokonferenzen teilnehmen. Mit der bidirektionalen Audiofunktion des GL.iNet KVM können Sie über das Mikrofon Ihres lokalen Computers sprechen und andere Teilnehmer über dessen Lautsprecher oder Kopfhörer hören.

## Schnelle Einrichtung {#quick-setup}

Die folgenden Schritte zeigen am Beispiel eines Zoom-Meetings, wie Sie Mikrofon und Lautsprecher Ihres lokalen Geräts für Remote-Meetings verwenden.

1. Melden Sie sich vor dem Meeting auf dem steuernden Computer bei Ihrem KVM an und öffnen Sie **Session** -> **Audio & Camera**. Aktivieren Sie **Speaker** und **Microphone**. Prüfen Sie, ob beide Symbole unten rechts aktiv sind.

    ![Lautsprecher und Mikrofon aktivieren](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/enable-speaker-and-microphone.png){class="glboxshadow"}

    Beim Aktivieren von **Microphone** kann Ihr Browser beispielsweise um Zugriff auf das Mikrofon bitten. Wählen Sie das gewünschte Mikrofon aus und erlauben Sie den Zugriff.

    ![Anfrage für Mikrofonzugriff](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/microphone-permission-popup.png){class="glboxshadow"}

2. Öffnen Sie Zoom auf dem gesteuerten Computer und nehmen Sie am Meeting teil. Klicken Sie auf den Pfeil neben der Audioschaltfläche und wählen Sie die folgenden Geräte wie im Beispiel aus:

    - **Microphone**: Microphone (6-Comet Microphone)

    - **Speaker**: EPSON PJ (HD Audio Driver for Display Audio)

    ![Mikrofon und Lautsprecher auswählen](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/select-microphone-and-speaker.png){class="glboxshadow"}

    Heben Sie anschließend die Stummschaltung Ihres Mikrofons auf, um mit anderen Teilnehmern zu sprechen. Sie hören sie über die Lautsprecher oder Kopfhörer des steuernden Computers.

    Wenn Sie den Teilnehmern auch das Bild Ihrer lokalen Kamera zeigen möchten, lesen Sie die [Anleitung zur Kameradurchleitung](../faq/use_camera_passthrough_for_remote_meetings.md).

## Fehlerbehebung {#troubleshooting}

??? note "Was kann ich tun, wenn andere Teilnehmer mich nicht hören?"

    Öffnen Sie auf dem gesteuerten Computer **Settings** -> **System** -> **Sound**. Suchen Sie unter **Input** das virtuelle Mikrofon des KVM, in diesem Beispiel **Comet Microphone**. Prüfen Sie, ob dieses Mikrofon auch in der Meeting-App ausgewählt ist.

    ![Eingabe prüfen](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-input.png){class="glboxshadow"}

    - Wenn das virtuelle Mikrofon des KVM nicht angezeigt wird, prüfen Sie die USB-Datenverbindung zwischen dem KVM und dem gesteuerten Computer. Über diese Verbindung wird der Mikrofonton an den gesteuerten Computer übertragen.

    - Wenn das virtuelle Mikrofon des KVM angezeigt und ausgewählt wird, aber kein Ton ankommt, prüfen Sie, ob das Mikrofon auf dem steuernden Computer und in der Meeting-App auf dem gesteuerten Computer eingeschaltet und nicht stummgeschaltet ist. Prüfen Sie die Mikrofonberechtigungen im System und Browser des steuernden Computers und schließen Sie andere Apps oder Browser-Tabs, die das Mikrofon möglicherweise verwenden.

??? note "Was kann ich tun, wenn ich andere Teilnehmer nicht höre?"

    Öffnen Sie auf dem gesteuerten Computer **Settings** -> **System** -> **Sound**. Suchen Sie unter **Output** den mit dem KVM verbundenen HDMI-Audioausgang, in diesem Beispiel **EPSON PJ**. Prüfen Sie, ob dasselbe Gerät in Ihrer Meeting-App als Lautsprecher ausgewählt ist.

    ![Ausgabe prüfen](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-output.png){class="glboxshadow"}

    - Wenn der HDMI-Audioausgang nicht angezeigt wird, prüfen Sie die HDMI-Verbindung zwischen dem gesteuerten Computer und dem KVM. Über diese Verbindung wird der Ton des gesteuerten Computers übertragen. Falls Sie einen HDMI-Adapter verwenden, prüfen Sie, ob er Audio unterstützt.

    - Wenn der HDMI-Audioausgang angezeigt und ausgewählt wird, Sie aber weiterhin keine anderen Teilnehmer hören, prüfen Sie, ob der steuernde Computer, der Browser-Tab und die Lautsprecher oder Kopfhörer stummgeschaltet sind.

    Weitere Informationen finden Sie unter [Kein Ton vom gesteuerten Gerät](../faq/no_audio_from_the_controlled_device.md).

??? note "Was kann ich tun, wenn nach dem Neuladen oder erneuten Verbinden kein Ton mehr zu hören ist?"

    Prüfen Sie **Speaker** und **Microphone** erneut in der KVM-Konsole. Die Sicherheitsrichtlinien des Browsers können nach dem Neuladen der Seite oder dem erneuten Verbinden die Lautsprecherwiedergabe deaktivieren oder das Mikrofon stummschalten.

    Weitere Informationen finden Sie unter [Lautsprecher- und Mikrofoneinstellungen bleiben nicht erhalten](../faq/speaker_microphone_settings_cannot_be_retained.md).

??? note "Was kann ich tun, wenn die Meldung „Microphone Access Denied“ erscheint?"

    Prüfen Sie Folgendes auf dem steuernden Computer:

    - **Systemberechtigungen**: Öffnen Sie unter Windows 11 **Settings** -> **Privacy & security** -> **Microphone**. Aktivieren Sie **Microphone access**, **Let apps access your microphone** und **Let desktop apps access your microphone**.

    - **Browserberechtigungen**: Erlauben Sie der KVM-Website den Zugriff auf Ihr Mikrofon. Wenn der Zugriff zuvor blockiert wurde, ändern Sie die Mikrofonberechtigungen der Website und laden Sie die Seite neu.

    - **Mikrofonnutzung**: Schließen Sie andere Apps oder Browser-Tabs, die das Mikrofon möglicherweise verwenden.

    Aktivieren Sie danach **Microphone** erneut in der KVM-Konsole.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
