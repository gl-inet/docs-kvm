# KVM per dynamischem Code mit der Cloud binden

> Hinweis: Aktualisieren Sie Ihre KVM-Firmware auf Version 1.7, bevor Sie diese Funktion verwenden.

Dieses Tutorial zeigt, wie Sie GL.iNet KVM einfach per dynamischem Code mit der Cloud binden.

## Bindungsschritte

1. Melden Sie sich lokal per Domain oder IP-Adresse an Ihrem GL.iNet KVM an. Details finden Sie [hier](../faq/local_access_via_browser.md). 

2. Navigieren Sie nach der Anmeldung oben rechts zu **Cloud Service** und klicken Sie auf **Bind With Code**.

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Fuer die Geraetebindung wird zufaellig ein 8-stelliger dynamischer Code erzeugt, der 60 Sekunden gueltig ist. Klicken Sie auf den Code, um ihn zu kopieren.

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Oeffnen Sie [https://glkvm.com/](https://glkvm.com/){target="_blank"} und melden Sie sich mit Ihrem glinet Cloud-Konto an. 

    ![bind with code 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Nach der Anmeldung wird die Seite wie folgt angezeigt.

    ![bind with code 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Klicken Sie auf **Add Device** und waehlen Sie **Bind with Code**.

    ![bind with code 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Geben Sie im Pop-up-Fenster den 8-stelligen dynamischen Code ein und klicken Sie auf **Bind**.

    ![bind with code 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Hinweis**: Der dynamische Code ist 60 Sekunden gueltig. Wenn er ablaeuft, kehren Sie zur KVM-Konsole zurueck und klicken Sie auf **Regenerate Code**, um einen neuen Code zu erhalten.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

7. Das Geraet wird erfolgreich mit Ihrem Cloud-Konto gebunden. Klicken Sie auf **Done**.

    ![bind with code 7](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    Das KVM erscheint in der Geraeteliste. Jetzt koennen Sie ueber den Cloud-Dienst remote darauf zugreifen.

    ![bind with code 8](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. Klicken Sie auf das Geraet, auf das Sie remote zugreifen moechten. 

    Sie werden auf eine neue Webseite mit der Domain `glkvm.xyz`, `glkvm.site` oder `glkvm.top` weitergeleitet. Diese Domains sind sicher und werden von GL.iNet bereitgestellt. Geben Sie das Admin-Passwort ein, um sich anzumelden.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Danach koennen Sie ueber die Cloud remote auf das KVM und das gesteuerte Geraet zugreifen.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## FAQ

1. **F: Wie lange ist der dynamische Code gueltig? Was kann ich tun, wenn er ablaeuft?** 

    A: Der dynamische Code ist 60 Sekunden gueltig. Wenn er ablaeuft, kehren Sie zur KVM-Konsole zurueck und klicken Sie auf **Regenerate Code**, um einen neuen Code zu erhalten.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **F: Was kann ich tun, wenn der dynamische Code nicht erzeugt werden kann?** 

    A: Wenn der dynamische Code nicht erzeugt werden kann, kann dies an einem instabilen Netzwerk oder an der Upstream-DNS-Konfiguration liegen. 
    
    - Pruefen Sie, ob Ihr Netzwerk stabil ist, oder wechseln Sie zu einem anderen Netzwerk und versuchen Sie es erneut.

    - Aendern Sie Ihre Upstream-DNS-Einstellungen und erzeugen Sie den Code erneut.
    
    Wenn das Problem weiterhin besteht, kontaktieren Sie unseren Support unter [support@gl-inet.com](mailto:support@gl-inet.com).

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
