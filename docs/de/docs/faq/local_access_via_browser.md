# So greifen Sie lokal per Browser auf das KVM zu

Bevor Sie beginnen, stellen Sie bitte sicher, dass sich das steuernde Gerät und das KVM im selben LAN befinden.

Es gibt zwei Möglichkeiten, per Webbrowser lokal auf das KVM zuzugreifen: über einen Domainnamen oder über eine IP-Adresse.

## Lokaler Zugriff per Domain

1. Öffnen Sie auf dem steuernden Gerät einen Browser. Chrome oder Edge wird wegen besserer Kompatibilität empfohlen.

2. Geben Sie `glkvm.local` in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie Ihr Admin-Passwort ein.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    Sie können nun lokal auf Ihre KVM-Konsole und damit auf das gesteuerte Gerät zugreifen.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## Lokaler Zugriff per IP-Adresse

Suchen Sie die IP-Adresse Ihres KVM im vorgelagerten Netzwerk (z. B. auf Ihrem Router) und geben Sie diese IP-Adresse im Browser ein. Danach können Sie lokal auf Ihr KVM und damit auf das gesteuerte Gerät zugreifen.

Beispiel mit **GL-AXT1800** (Router) und **GL-RM1 Comet** (KVM): Comet ist über ein Ethernet-Kabel mit dem LAN-Port des GL-AXT1800-Routers verbunden. Das gesteuerte Gerät ist korrekt per HD-Kabel und USB-Kabel mit Comet verbunden.

Führen Sie die folgenden Schritte aus, um auf die KVM-Konsole zuzugreifen.

1. Melden Sie sich am Web-Admin-Panel des GL-AXT1800 an. Dieser Router muss für den Internetzugang konfiguriert sein.

    ![log in router](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. Gehen Sie im Admin-Panel des Routers zu **Client** und suchen Sie in der Client-Liste die IP-Adresse von Comet. Wie unten gezeigt, lautet die IP von Comet **192.168.8.197**.

    ![find glkvm ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. Öffnen Sie im Browser einen neuen Tab und geben Sie die IP von Comet, **192.168.8.197**, in die Adressleiste ein.

    Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie Ihr Admin-Passwort ein.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    Sie können nun lokal auf Ihre KVM-Konsole und damit auf das gesteuerte Gerät zugreifen.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
