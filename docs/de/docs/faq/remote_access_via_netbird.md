# So greifen Sie über NetBird remote auf KVM zu

> Hinweis: Bitte aktualisieren Sie die Firmware Ihres KVM auf v1.9.0, bevor Sie diese Funktion verwenden.

[NetBird](https://netbird.io/){target="_blank"} ist eine Open-Source-Zero-Trust-Netzwerkplattform, mit der Sie sichere private Netzwerke für den privaten und geschäftlichen Einsatz erstellen können. Als WireGuard®-basiertes Overlay-Netzwerk ermöglicht NetBird jederzeit und überall sicheren Zugriff auf Ihre Geräte.

GL.iNet KVM integriert NetBird, sodass Sie es für den Fernzugriff an das virtuelle NetBird-Netzwerk binden können. Die GLKVM App muss dafür nicht installiert und der Cloud-Dienst nicht verwendet werden.

Führen Sie die folgenden Schritte aus, um über NetBird remote auf Ihr GL.iNet KVM zuzugreifen.

## KVM an NetBird binden

**Bevor Sie beginnen, verbinden Sie Ihr KVM und das steuernde Gerät mit demselben lokalen Netzwerk.**

1. Melden Sie sich lokal per Domain oder IP-Adresse bei Ihrer KVM-Konsole an und gehen Sie anschließend zu **Apps Center** -> **NetBird**. Aktivieren Sie NetBird und klicken Sie auf **Bind Device**.

    ![bind device](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. Sie werden zur Bestätigungsseite für das Gerät weitergeleitet. Klicken Sie auf **Confirm**.

    ![confirm device](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. Melden Sie sich bei Ihrem NetBird-Konto an. Wenn Sie noch kein Konto haben, registrieren Sie zunächst eines.

    ![netbird sign in](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. Nach der Anmeldung wird das KVM-Gerät automatisch an Ihr Konto gebunden.

    ![kvm connected](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    Im NetBird-Dashboard sehen Sie Ihr KVM außerdem auf der Seite **Peers**.

    ![netbird dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## Steuerndes Gerät binden

Das folgende Beispiel zeigt, wie ein Windows-Laptop als steuerndes Gerät an das NetBird-Netzwerk gebunden wird.

1. Installieren Sie NetBird auf Ihrem Laptop über [diesen Link](https://app.netbird.io/install){target="_blank"}.

    ![install netbird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. Führen Sie NetBird auf dem Laptop aus und fügen Sie ihn demselben NetBird-Netzwerk hinzu.

    NetBird zeigt auf dem Desktop kein eigenes Fenster und keine separate Oberfläche an. Es befindet sich nur als Symbol im Infobereich (unten rechts). Alle Vorgänge werden über das Kontextmenü ausgeführt.

    Klicken Sie mit der rechten Maustaste auf das NetBird-Symbol und klicken Sie auf **Connect**.

    ![pc connect](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. Klicken Sie im Popup-Fenster auf **Accept**, um zu autorisieren.

    ![authorize](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    Ihr Laptop wird automatisch an Ihr Konto gebunden und demselben NetBird-Netzwerk hinzugefügt.

    ![pc connected](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. Im NetBird-Dashboard werden auf der Seite **Peers** zwei Geräte angezeigt: Ihr KVM und der steuernde Laptop.

    ![netbird dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## Fernzugriff über NetBird

Das folgende Beispiel zeigt, wie Sie über die virtuelle NetBird-IP-Adresse remote auf die KVM-Konsole zugreifen.

1. Melden Sie sich auf Ihrem Laptop beim NetBird-Dashboard an und navigieren Sie zu **Peers**.

    Suchen Sie Ihr KVM-Gerät und klicken Sie auf dessen **NetBird IP** (`100.100.141.229` in diesem Beispiel), um die virtuelle IP zu kopieren.

    ![kvm netbird ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    Bewegen Sie den Mauszeiger über die IP-Adresse, um weitere Details wie Public IP, Domain und Region anzuzeigen.

2. Öffnen Sie einen neuen Browser-Tab, fügen Sie die kopierte NetBird-IP in die Adressleiste ein und drücken Sie die Eingabetaste. Sie werden zur GLKVM-Anmeldeseite weitergeleitet.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    Geben Sie Ihr Admin-Passwort ein, um sich anzumelden. Sie können nun über die NetBird-IP auf Ihr GL.iNet KVM und das gesteuerte Gerät zugreifen.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Tipp**: Beim ersten Zugriff auf diese NetBird-IP kann eine Datenschutzwarnung angezeigt werden. Klicken Sie einfach auf **Advanced** -> **Proceed**, um fortzufahren. Details finden Sie unter [Datenschutzwarnung im Browser](privacy_error_from_your_browser.md){target="_blank"}.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
