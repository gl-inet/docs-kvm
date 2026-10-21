# KVM per dynamischem Code mit der Cloud binden {#how-to-bind-kvm-to-the-cloud-via-dynamic-code}

> Hinweis: Aktualisieren Sie Ihre KVM-Firmware auf Version 1.7, bevor Sie diese Funktion verwenden.

Dieses Tutorial zeigt, wie Sie GL.iNet KVM einfach per dynamischem Code mit der Cloud binden.

## Bindungsschritte {#binding-steps}

1. Melden Sie sich lokal per Domain oder IP-Adresse an Ihrem GL.iNet KVM an. Details finden Sie [hier](../faq/local_access_via_browser.md). 

2. Navigieren Sie nach der Anmeldung oben rechts zu **Cloud Service** und klicken Sie auf **Bind With Code**.

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Für die Gerätebindung wird zufällig ein 8-stelliger dynamischer Code erzeugt, der 60 Sekunden gültig ist. Klicken Sie auf den Code, um ihn zu kopieren.

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Öffnen Sie [https://glkvm.com/](https://glkvm.com/){target="_blank"} und melden Sie sich mit Ihrem glinet Cloud-Konto an. 

    ![bind with code 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Nach der Anmeldung wird die Seite wie folgt angezeigt.

    ![bind with code 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Klicken Sie auf **Add Device** und wählen Sie **Bind with Code**.

    ![bind with code 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Geben Sie im Pop-up-Fenster den 8-stelligen dynamischen Code ein und klicken Sie auf **Bind**.

    ![bind with code 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Hinweis**: Der dynamische Code ist 60 Sekunden gültig. Wenn er abläuft, kehren Sie zur KVM-Konsole zurück und klicken Sie auf **Regenerate Code**, um einen neuen Code zu erhalten.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

7. Das Gerät wird erfolgreich mit Ihrem Cloud-Konto gebunden. Klicken Sie auf **Done**.

    ![bind with code 7](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    Das KVM erscheint in der Geräteliste. Jetzt können Sie über den Cloud-Dienst remote darauf zugreifen.

    ![bind with code 8](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. Klicken Sie auf das Gerät, auf das Sie remote zugreifen möchten. Geben Sie auf der neu geöffneten Webseite Ihr Admin-Passwort ein, um sich anzumelden.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Danach können Sie über die Cloud remote auf das KVM und das gesteuerte Gerät zugreifen.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## FAQ {#faq}

1. **F: Wie lange ist der dynamische Code gültig? Was kann ich tun, wenn er abläuft?** 

    A: Der dynamische Code ist 60 Sekunden gültig. Wenn er abläuft, kehren Sie zur KVM-Konsole zurück und klicken Sie auf **Regenerate Code**, um einen neuen Code zu erhalten.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **F: Was kann ich tun, wenn der dynamische Code nicht erzeugt werden kann?** 

    A: Wenn der dynamische Code nicht erzeugt werden kann, kann dies an einem instabilen Netzwerk oder an der Upstream-DNS-Konfiguration liegen. 
    
    - Prüfen Sie, ob Ihr Netzwerk stabil ist, oder wechseln Sie zu einem anderen Netzwerk und versuchen Sie es erneut.

    - Ändern Sie Ihre Upstream-DNS-Einstellungen und erzeugen Sie den Code erneut.
    
    Wenn das Problem weiterhin besteht, kontaktieren Sie unseren Support unter [support@gl-inet.com](mailto:support@gl-inet.com).

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
