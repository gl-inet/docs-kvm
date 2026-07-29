# So greifen Sie über Tailscale remote auf KVM zu

GL.iNet KVM integriert Tailscale, sodass Sie es für den Fernzugriff an das virtuelle Tailscale-Netzwerk binden können. Die GLKVM App muss dafür nicht installiert und der Cloud-Dienst nicht verwendet werden. Das ist besonders nützlich, wenn auf Ihrem steuernden Gerät kein Windows, macOS, Android oder iOS läuft und die GLKVM App daher nicht installiert werden kann, oder wenn Sie die GLKVM App beziehungsweise den Cloud-Dienst nicht nutzen möchten.

Führen Sie die folgenden Schritte aus, um über Tailscale remote auf Ihr GL.iNet KVM zuzugreifen.

## KVM an Tailscale binden

**Bevor Sie beginnen, verbinden Sie Ihr KVM und das steuernde Gerät mit demselben lokalen Netzwerk.**

1. Öffnen Sie auf dem steuernden Gerät einen Browser. Chrome oder Edge wird wegen besserer Kompatibilität empfohlen.

2. Melden Sie sich lokal per Domain oder IP-Adresse bei Ihrer KVM-Konsole an. Hier verwenden wir die Standarddomain als Beispiel.

    Geben Sie `glkvm.local` in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie Ihr Admin-Passwort ein.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. Gehen Sie nach der Anmeldung zu **Apps Center** -> **Tailscale**. Aktivieren Sie Tailscale und klicken Sie auf **Bind Device**.

    ![enable tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. Sie werden zur Tailscale-Anmeldeseite weitergeleitet. Geben Sie Ihre E-Mail-Adresse ein, um sich anzumelden.

    ![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. Nach der Anmeldung meldet die Seite, dass das Gerät glkvm mit Ihrem Tailnet verbunden werden soll. Klicken Sie auf **Connect**.

    ![connect kvm to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    Ihr KVM-Gerät wird anschließend erfolgreich an Ihr Tailnet gebunden.

    ![bind kvm successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}

6. Sie werden zu Ihrer Tailscale-Konsole weitergeleitet, in der ein Gerät mit der Bezeichnung **glkvm** unter **Machines** angezeigt wird.

    ![tailscale console 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## Steuerndes Gerät binden

Das folgende Beispiel zeigt, wie ein Windows-Laptop als steuerndes Gerät an das Tailscale-Netzwerk gebunden wird.

1. Installieren Sie Tailscale auf Ihrem Laptop über [diesen Link](https://tailscale.com/download){target="_blank"}.

2. Führen Sie Tailscale auf dem Laptop aus und melden Sie sich mit derselben E-Mail-Adresse an.

    ![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. Nach der Anmeldung meldet die Seite, dass der Laptop (also das steuernde Gerät) mit Ihrem Tailnet verbunden werden soll. Klicken Sie auf **Connect**.

    ![connect pc to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    Ihr Laptop wird anschließend erfolgreich an Ihr Tailnet gebunden.

    ![bind pc successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. Sie werden zu Ihrer Tailscale-Konsole weitergeleitet, in der auch das steuernde Gerät unter **Machines** angezeigt wird.

    ![tailscale console 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Fernzugriff über Tailscale

Klicken Sie in der Tailscale-Konsole auf die **Address** des glkvm (`100.104.185.26` in diesem Beispiel).

![get vittual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

Es werden vier Werte angezeigt:

- glkvm (Gerätename)
- glkvm.tail1fd0.ts.net (von Tailscale zugewiesene Domain)
- fd7a:115c:a1e0:301:b92f (virtuelle IPv6)
- 100.104.185.26 (virtuelle IPv4).

Diese Werte werden von Tailscale zur Geräteidentifikation und Kommunikation im virtuellen Netzwerk zugewiesen. Sie können über die von Tailscale zugewiesene Domain, die virtuelle IPv4-Adresse oder die virtuelle IPv6-Adresse remote auf Ihr KVM-Gerät zugreifen.

Beispiel mit der virtuellen IPv4-Adresse:

1. Kopieren Sie die virtuelle IPv4-Adresse Ihres KVM-Geräts.

2. Öffnen Sie einen neuen Tab und fügen Sie die IP-Adresse in die Adressleiste ein.

    ![access vitual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    Möglicherweise wird eine Datenschutzwarnung angezeigt. [Warum wird diese Datenschutzwarnung angezeigt?](privacy_error_from_your_browser.md){target="_blank"}

    ![privacy error](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    Klicken Sie auf **Advanced** und anschließend auf **Proceed to 100.104.185.26**. Sie werden zur GLKVM-Anmeldeseite weitergeleitet.

    ![proceed](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. Geben Sie Ihr Admin-Passwort ein, um sich anzumelden. Sie können nun über die virtuelle Tailscale-IP auf Ihr GL.iNet KVM und das gesteuerte Gerät zugreifen.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
