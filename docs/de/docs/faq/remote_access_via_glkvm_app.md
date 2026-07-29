# So greifen Sie über die GLKVM App remote auf KVM zu

Bevor Sie beginnen, stellen Sie bitte sicher, dass das gesteuerte Gerät korrekt mit dem GL.iNet KVM verbunden ist und das KVM mit einem stabilen Netzwerk verbunden ist.

Führen Sie die folgenden Schritte aus, um über die GLKVM App remote auf Ihr KVM und das gesteuerte Gerät zuzugreifen.

## Installieren und anmelden

1. Installieren Sie die [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} auf Ihrem steuernden Gerät.

2. Öffnen Sie die GLKVM App und melden Sie sich mit Ihrem GL.iNet-Konto an.

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Wenn Sie kein GL.iNet-Konto haben, registrieren Sie eines und melden Sie sich danach an.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## KVM binden

Nach der Anmeldung wird die Seite wie folgt angezeigt. Klicken Sie auf **Add Device**.

Es gibt drei Möglichkeiten, Ihr KVM zu binden: Auto Discover, S/N Code und Dynamic Binding Code.

![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### Auto Discover

Dies muss innerhalb des lokalen Netzwerks erfolgen. Stellen Sie sicher, dass sich Ihr KVM und das steuernde Gerät im selben LAN befinden.

1. Klicken Sie auf **Auto Discover**. Die Suche nach verfügbaren KVM-Geräten startet automatisch.

    ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. Suchen Sie Ihr KVM und geben Sie seine **Device ID** ein, um es an Ihr Konto zu binden.

    ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### S/N Code

Diese Methode gilt für Fälle, in denen Ihr KVM nicht erkannt wird oder sich nicht im selben LAN befindet, Sie aber seine Seriennummer (S/N) haben.

1. Klicken Sie auf **S/N Code**.

2. Geben Sie im Popup-Fenster einen Namen für Ihr Gerät ein und tragen Sie die S/N ein, die auf dem Etikett an der Unterseite Ihres KVM-Geräts aufgedruckt ist.

    ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### Dynamic Binding Code

Bitte aktualisieren Sie die Firmware Ihres KVM auf v1.7, bevor Sie diese Funktion verwenden.

Dies muss innerhalb des lokalen Netzwerks erfolgen. Stellen Sie sicher, dass sich Ihr KVM und das steuernde Gerät im selben LAN befinden.

1. Melden Sie sich lokal per Domain oder IP-Adresse bei Ihrem KVM an. Details finden Sie [hier](../faq/local_access_via_browser.md).

2. Navigieren Sie nach der Anmeldung oben rechts zu **Cloud Service** und klicken Sie auf **Bind With Code**.

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Es wird zufällig ein 8-stelliger dynamischer Code für das Binden des Geräts erzeugt, der 60 Sekunden gültig ist. Klicken Sie auf den Code, um ihn zu kopieren.

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Kehren Sie zur GLKVM App zurück, geben Sie den dynamischen Bindungscode ein und klicken Sie auf **Bind**.

    ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## Fernzugriff

Sobald Ihr KVM-Gerät an Ihr Konto gebunden ist, wird es in der App als "Online" angezeigt.

![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

Klicken Sie auf Ihr KVM-Gerät. Ein neues Fenster wird geöffnet und die Verbindung wird gestartet.

![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

Sobald die Verbindung hergestellt ist, geben Sie Ihr Admin-Passwort ein, um sich anzumelden.

![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

Sie können nun auf Ihr KVM-Gerät zugreifen und darüber auf das gesteuerte Gerät zugreifen.

![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
