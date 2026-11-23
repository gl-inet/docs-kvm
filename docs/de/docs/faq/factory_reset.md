# So setzen Sie Ihr GL.iNet-KVM auf Werkseinstellungen zurück {#how-do-i-factory-reset-my-glinet-kvm}

## Methode 1 – Die RESET-Taste am Gerät verwenden {#method-1-use-the-physical-reset-button}

Stellen Sie sicher, dass das KVM eingeschaltet und vollständig hochgefahren ist.

Halten Sie die RESET-Taste am Gerät **8 bis 10 Sekunden** lang gedrückt und lassen Sie sie dann los. Wenn Ihr KVM eine versenkte Reset-Taste hat, drücken Sie die Taste in der Öffnung mit einem Stift 8 Sekunden lang und lassen Sie sie dann los. Verwenden Sie beim Comet X (GL-RM4PE) die Umschalttaste an der Vorderseite.

Warten Sie, bis das KVM automatisch neu startet. Trennen Sie während des Zurücksetzens nicht die Stromversorgung.

Halten Sie die Reset-Taste beim Einschalten des KVM nicht gedrückt. Verwenden Sie weder die Reset-Taste am angeschlossenen Computer noch die auf der ATX-Platine.

## Methode 2 – Die lokale Weboberfläche verwenden {#method-2-use-the-local-web-interface}

Verbinden Sie Ihren Computer und das KVM mit demselben lokalen Netzwerk. Öffnen Sie die lokale IP-Adresse des KVM im Browser und melden Sie sich an. Siehe [So greifen Sie lokal per Browser auf das KVM zu](local_access_via_browser.md).

Wenn auf Ihrem KVM Firmware v1.10 oder neuer installiert ist, öffnen Sie oben rechts **Settings** und wechseln Sie zu **System** -> **Reset Device**. Klicken Sie auf **Reset**, bestätigen Sie den Vorgang und warten Sie, bis das KVM automatisch neu startet. Trennen Sie während des Zurücksetzens nicht die Stromversorgung.

![reset 1](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset1.png){class="glboxshadow"}

Wenn auf Ihrem KVM Firmware v1.9 oder älter installiert ist, öffnen Sie oben links **Settings** und wechseln Sie zu **System** -> **Reset KVM**. Klicken Sie auf **Reset**, bestätigen Sie den Vorgang und warten Sie, bis das KVM automatisch neu startet. Trennen Sie während des Zurücksetzens nicht die Stromversorgung.

![reset 2](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset2.png){class="glboxshadow"}

## Nach dem Zurücksetzen {#after-the-reset}

Beim Zurücksetzen auf Werkseinstellungen werden die benutzerdefinierten Einstellungen des KVM gelöscht. Die lokale IP-Adresse des KVM kann sich nach dem Neustart ändern. Öffnen Sie die lokale Weboberfläche erneut, folgen Sie den Anweisungen der Ersteinrichtung, um ein Administratorpasswort festzulegen, und konfigurieren Sie die benötigten Einstellungen erneut manuell.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
