# So greifen Sie über ZeroTier remote auf KVM zu

> Hinweis: Bitte aktualisieren Sie die Firmware Ihres KVM auf v1.8.0, bevor Sie diese Funktion verwenden.

GL.iNet KVM integriert ZeroTier, sodass Sie es für den Fernzugriff an das ZeroTier-Netzwerk binden können. Die GLKVM App muss dafür nicht installiert und der Cloud-Dienst nicht verwendet werden.

Führen Sie die folgenden Schritte aus, um über ZeroTier remote auf Ihr GL.iNet KVM zuzugreifen.

## ZeroTier aktivieren

**Bevor Sie beginnen, verbinden Sie Ihr KVM und das steuernde Gerät mit demselben lokalen Netzwerk.**

1. Öffnen Sie auf dem steuernden Gerät einen Browser. Chrome oder Edge wird wegen besserer Kompatibilität empfohlen.

2. Melden Sie sich lokal per Domain oder IP-Adresse bei Ihrer KVM-Konsole an. Hier verwenden wir die lokale IP-Adresse als Beispiel.

    Geben Sie die **LAN IP address** des KVM (auf dem Touchscreen oder in Ihrem Router zu finden) in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie Ihr Admin-Passwort ein.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. Gehen Sie nach der Anmeldung zu **Apps Center** -> **ZeroTier**. Aktivieren Sie ZeroTier. Danach wird ein gelber Hinweis wie unten angezeigt.

    Klicken Sie auf den Hyperlink oder [hier](https://my.zerotier.com/){target="_blank"}, um sich bei ZeroTier Central anzumelden und Ihr ZeroTier-Netzwerk zu erstellen.

    ![enable zerotier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}

## KVM an ZeroTier binden

1. Wenn Sie sich zum ersten Mal bei [ZeroTier](https://my.zerotier.com/){target="_blank"} anmelden, müssen Sie möglicherweise ZeroTier Central auswählen.

    ![select central](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    Wählen Sie die passende Version aus, um fortzufahren. Hier verwenden wir **New Central** als Beispiel.

    Melden Sie sich mit Ihrer E-Mail-Adresse und Ihrem Passwort an. Wenn Sie noch kein Konto haben, registrieren Sie zunächst eines.

    ![zerotier signin](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. Erstellen Sie nach der Anmeldung eine Organisation.

    ![create organization](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. Wählen Sie einen Tarif aus. Hier wählen wir beispielhaft den Tarif **Personal**, der 10 Geräte, 1 Netzwerkadministrator und 1 Netzwerk umfasst. Wenn Sie mehr Netzwerke erstellen, mehr Geräte hinzufügen oder benutzerdefinierte Routen und DNS hinzufügen müssen, wählen Sie den Tarif Essential oder Scale.

    ![select plan](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. Ihr ZeroTier-Netzwerk wurde nun erstellt. Kopieren Sie die **Network ID**, eine 16-stellige alphanumerische Zeichenfolge. Sie benötigen sie später, wenn Sie Geräte zu Ihrem ZeroTier-Netzwerk hinzufügen. Lassen Sie diesen Tab geöffnet.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. Kehren Sie zu Ihrer KVM-Konsole zurück und gehen Sie zu **Apps Center** -> **ZeroTier**. Suchen Sie **Network ID** und klicken Sie auf **Set**.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    Fügen Sie im Popup-Fenster die **Network ID** ein und klicken Sie auf **Confirm**.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    In der Konsole wird ein gelber Hinweis angezeigt, der darauf hinweist, dass dieses Gerät autorisiert werden muss.

    ![authorize1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. Wechseln Sie zurück zu ZeroTier Central. Dort sehen Sie ein Gerät (Ihr KVM), das auf Genehmigung wartet. Klicken Sie auf **Authorize**.

    ![authorize2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    Nach der Autorisierung wechselt der Status wie unten gezeigt in Grün zu Authorized.

    ![authorized1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    In der KVM-Konsole können Sie außerdem die **Network ID** und die **Virtual IP** anzeigen, wie unten gezeigt.

    ![authorized2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## Steuerndes Gerät binden

Das folgende Beispiel zeigt, wie ein Windows-Laptop als steuerndes Gerät an das ZeroTier-Netzwerk gebunden wird.

1. Installieren Sie ZeroTier auf Ihrem Laptop über [diesen Link](https://www.zerotier.com/download/){target="_blank"}.

2. Führen Sie ZeroTier auf dem Laptop aus und fügen Sie ihn demselben ZeroTier-Netzwerk hinzu.

    Beachten Sie, dass ZeroTier auf dem Desktop kein eigenes Fenster und keine separate Oberfläche anzeigt. Es befindet sich nur als Symbol im Infobereich (unten rechts). Alle Vorgänge werden über das Kontextmenü ausgeführt.

    Klicken Sie mit der rechten Maustaste auf das ZeroTier-Symbol und klicken Sie auf **Join New Network**. Geben Sie im Popup-Fenster dieselbe **Network ID** ein, um diesen PC demselben ZeroTier-Netzwerk hinzuzufügen.

    ![join network](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    Gehen Sie anschließend zu ZeroTier Central, suchen Sie das ausstehende Gerät und autorisieren Sie es.

    ![authorize](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

2. Nach der Autorisierung wechselt der Status wie unten gezeigt in Grün zu Authorized.

    ![authorized](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

3. Nun wurden Ihr KVM und der Laptop demselben ZeroTier-Netzwerk hinzugefügt. Das erkennen Sie an ihrer Network ID, wie unten gezeigt.

    ![same zt network](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## Fernzugriff über ZeroTier

Das folgende Beispiel zeigt, wie Sie über die ZeroTier-IP-Adresse remote auf die KVM-Konsole zugreifen.

1. Melden Sie sich auf Ihrem Laptop mit Ihrem Konto bei ZeroTier Central an, suchen Sie Ihr KVM-Gerät und klicken Sie auf dessen **ZT IP**, um sie zu kopieren.

    ![zerotier ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. Öffnen Sie einen neuen Browser-Tab, fügen Sie die kopierte ZeroTier-IP in die Adressleiste ein und drücken Sie die Eingabetaste. Sie werden zur GLKVM-Anmeldeseite weitergeleitet.

    Geben Sie Ihr Admin-Passwort ein, um sich anzumelden. Sie können nun über die ZeroTier-IP auf Ihr GL.iNet KVM und das gesteuerte Gerät zugreifen.

    ![remote access](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Tipp**: Beim ersten Zugriff auf diese ZeroTier-IP kann eine Datenschutzwarnung angezeigt werden. Klicken Sie einfach auf **Advanced** -> **Proceed**, um fortzufahren. Details finden Sie unter [Datenschutzwarnung im Browser](privacy_error_from_your_browser.md){target="_blank"}.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
