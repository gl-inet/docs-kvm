# So greifen Sie per Cloud remote auf KVM zu

Bevor Sie beginnen, stellen Sie bitte sicher:

- Das gesteuerte Gerät ist korrekt mit dem KVM verbunden.

- Das KVM ist mit einem stabilen Netzwerk verbunden.

- Sie können lokal auf das KVM zugreifen, da das Binden des Geräts an die Cloud innerhalb des lokalen Netzwerks erfolgen muss.

Führen Sie die folgenden Schritte aus, um über den Cloud-Dienst remote auf Ihr KVM und das gesteuerte Gerät zuzugreifen.

## KVM an die Cloud binden

Es gibt zwei Möglichkeiten, Ihr KVM an die Cloud zu binden: Regular Binding oder Dynamic Code Binding.

- **Regular Binding**: Klicken Sie in der KVM-Konsole auf "Bind To KVMCloud". Danach werden Sie zur Bindungsseite mit dem Token weitergeleitet. Melden Sie sich bei Ihrem Cloud-Konto an und bestätigen Sie die Geräteinformationen, um das Binden abzuschließen.

- **Dynamic Code Binding**: Klicken Sie in der KVM-Konsole auf "Bind With Code". Danach wird zufällig ein 8-stelliger dynamischer Code für das Binden des Geräts erzeugt. Melden Sie sich bei Ihrem Cloud-Konto an und geben Sie den Code ein, um das Binden abzuschließen.

### Regular Binding

Melden Sie sich lokal per IP-Adresse oder Domain bei Ihrem KVM an und navigieren Sie oben rechts zu **Cloud Service**. Klicken Sie auf **Bind To Cloud**.

![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

Sie werden zu einer Anmeldeseite weitergeleitet. Geben Sie Ihr glinet-Konto ein und klicken Sie auf **Log In**.

![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

Bestätigen Sie die Geräteinformationen und klicken Sie auf **Bind**.

![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

Warten Sie kurz, bis Ihr Gerät erfolgreich an Ihr Konto gebunden wurde. Klicken Sie dann auf **Done**.

![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### Dynamic Code Binding

Hinweis: Bitte aktualisieren Sie die Firmware Ihres KVM auf Version 1.7, bevor Sie diese Funktion verwenden.

1. Melden Sie sich lokal per Domain oder IP-Adresse bei Ihrem GL.iNet KVM an. Details finden Sie [hier](../faq/local_access_via_browser.md).

2. Navigieren Sie nach der Anmeldung oben rechts zu **Cloud Service** und klicken Sie auf **Bind With Code**.

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Es wird zufällig ein 8-stelliger dynamischer Code für das Binden des Geräts erzeugt, der 60 Sekunden gültig ist. Klicken Sie auf den Code, um ihn zu kopieren.

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Öffnen Sie [https://glkvm.com/](https://glkvm.com/){target="_blank"} und melden Sie sich mit Ihrem glinet-Cloud-Konto an.

    ![bind with code 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Nach der Anmeldung wird die Seite wie folgt angezeigt.

    ![bind with code 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Klicken Sie auf **Add Device** und wählen Sie **Bind with Code**.

    ![bind with code 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Geben Sie im Popup-Fenster den 8-stelligen dynamischen Code ein und klicken Sie auf **Bind**.

    ![bind with code 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Hinweis**: Der dynamische Code ist 60 Sekunden gültig. Wenn der dynamische Code abläuft, kehren Sie zur KVM-Konsole zurück und klicken Sie auf **Regenerate Code**, um einen neuen Code zu erhalten.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

    Anschließend wird das Gerät erfolgreich an Ihr Cloud-Konto gebunden.

## Fernzugriff über die Cloud

Öffnen Sie einen Browser (hier Google Chrome als Beispiel) und geben Sie `glkvm.com` in die Adressleiste ein. Sie sehen eine Anmeldeseite. Melden Sie sich mit Ihrem glinet-Konto an.

![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

Nach der Anmeldung sehen Sie die Geräte, die an Ihr Konto gebunden sind. Klicken Sie auf das Gerät, auf das Sie remote zugreifen möchten.

![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

Sie werden auf eine neue Webseite mit der Domain `glkvm.xyz`, `glkvm.site` oder `glkvm.top` weitergeleitet (zufällig zugewiesen). Diese Domains sind sicher und werden von GL.iNet bereitgestellt.

Geben Sie Ihr Admin-Passwort ein, um sich anzumelden.

![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

Sie können nun remote über die Cloud auf das KVM und das gesteuerte Gerät zugreifen.

![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
