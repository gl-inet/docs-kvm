# Comet Q (GL-RMQ1) Schnellstart

## Geraete verbinden

Zur besseren Verstaendlichkeit bezeichnet Geraet A das steuernde Geraet und Geraet B das gesteuerte Geraet.

![connect 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect1.png){class="glboxshadow"}

1. Verbinden Sie das Type-C-Kabel des Comet Q mit dem Type-C-Anschluss von Geraet B.

    ![connect 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect2.png){class="glboxshadow"}

2. Wenn Geraet B ein mobiles Touchscreen-Geraet wie ein Smartphone oder Tablet ist, aktivieren Sie zuerst die Bedienungshilfen. Dadurch kann Comet Q den Touchscreen bedienen.

    - iOS: **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** aktivieren.

    - Android: Suchen Sie in den Einstellungen nach **Mouse** oder **Accessibility**. Die Menuepfade unterscheiden sich je nach Geraetemarke und Modell.

    ![connect 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect3.png){class="glboxshadow" width="600"}

3. Folgen Sie den Anweisungen auf dem Bildschirm, um die Ersteinrichtung abzuschliessen. Details finden Sie [hier](../gl-rmq1/product_overview.md#touchscreen).

    ![connect 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect4.png){class="glboxshadow"}

## Lokaler Zugriff

Es gibt zwei Moeglichkeiten, im lokalen Netzwerk auf Comet Q zuzugreifen: ueber den Domainnamen oder ueber die IP-Adresse.

Stellen Sie vor dem Zugriff sicher, dass sich Ihr steuerndes Geraet im selben LAN wie Comet Q befindet.

### Domain

1. Oeffnen Sie auf dem steuernden Geraet einen Browser. Fuer bessere Kompatibilitaet werden Chrome oder Edge empfohlen.

2. Geben Sie `glkvm.local` in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie das Admin-Passwort ein.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Hinweis**: Beim ersten Zugriff muessen Sie Ihr Admin-Passwort einrichten.

3. Danach koennen Sie lokal auf die Konsole des Comet Q und auf das gesteuerte Geraet zugreifen.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP-Adresse

1. Verbinden Sie Comet Q mit einem WLAN-Netzwerk und suchen Sie die IP-Adresse auf dem Touchscreen. In diesem Beispiel lautet die IP-Adresse des Comet Q `192.168.8.197`.

2. Oeffnen Sie einen Browser und geben Sie diese IP-Adresse in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie das Admin-Passwort ein.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Hinweis**: Beim ersten Zugriff muessen Sie Ihr Admin-Passwort einrichten.

3. Danach koennen Sie lokal auf die Konsole des Comet Q und auf das gesteuerte Geraet zugreifen.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Fernzugriff

Es gibt mehrere Moeglichkeiten, aus der Ferne auf Comet Q zuzugreifen: ueber den Cloud-Dienst, die GLKVM App, Tailscale und ZeroTier.

### Cloud-Dienst

1. Binden Sie Ihr Geraet an die KVM Cloud. Dies muss im lokalen Netzwerk erfolgen.

    Es gibt zwei Moeglichkeiten, Ihr KVM mit der Cloud zu binden: regulaere Bindung oder Bindung per dynamischem Code. Hier verwenden wir die regulaere Bindung als Beispiel. Wenn Sie die Bindung per dynamischem Code bevorzugen, finden Sie [hier](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} weitere Informationen.

    Greifen Sie zuerst lokal auf Ihren Comet Q zu und navigieren Sie oben rechts zu **Cloud Service**. Klicken Sie auf **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Sie werden zu einer Anmeldeseite weitergeleitet. Melden Sie sich mit Ihrem glinet Cloud-Konto an.

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Bestaetigen Sie anschliessend die Geraeteinformationen und klicken Sie auf **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Warten Sie einen Moment, bis Ihr Comet Q erfolgreich mit Ihrem Konto gebunden wurde. Klicken Sie auf **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Fernzugriff ueber den Cloud-Dienst.

    Oeffnen Sie einen Browser (hier Google Chrome als Beispiel) und geben Sie `glkvm.com` in die Adressleiste ein. Eine Anmeldeseite wird angezeigt. Melden Sie sich mit Ihrem glinet Konto an.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Nach der Anmeldung sehen Sie die mit Ihrem Konto gebundenen Geraete. Klicken Sie auf das Geraet, auf das Sie aus der Ferne zugreifen moechten.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Geben Sie auf der neu geoeffneten Webseite Ihr Admin-Passwort ein, um sich anzumelden.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Danach koennen Sie ueber die Cloud aus der Ferne auf Ihren Comet Q und das gesteuerte Geraet zugreifen, ohne die App zu installieren.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### GLKVM App

1. Installieren Sie die [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} auf Ihrem steuernden Geraet.

2. Melden Sie sich mit Ihrem GL.iNet Konto an.

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Wenn Sie noch kein Konto haben, registrieren Sie sich zuerst und melden Sie sich dann an.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Binden Sie Ihr Geraet.

    Nach der Anmeldung wird die folgende Seite angezeigt. Klicken Sie auf **Add Device**.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    Sie koennen Ihr Geraet auf drei Arten binden: Auto Discover, S/N Code und Dynamic Binding Code.

    ??? "Auto Discover"

        Dies muss im lokalen Netzwerk erfolgen. Stellen Sie sicher, dass sich Ihr steuerndes Geraet im selben LAN wie Comet Q befindet.

        Klicken Sie auf **Auto Discover**. Die Suche startet automatisch.

        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Suchen Sie Ihr KVM und geben Sie die Device ID ein, um es mit Ihrem Konto zu binden.

        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Dies gilt, wenn Ihr KVM nicht erkannt wird oder sich nicht im selben LAN befindet, Sie aber seine Seriennummer (S/N) haben.

        Klicken Sie auf **S/N Code**. Passen Sie im Pop-up-Fenster den Geraetenamen an und geben Sie die S/N ein, die auf dem Etikett an der Unterseite Ihres KVM-Geraets aufgedruckt ist.

        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Dies muss im lokalen Netzwerk erfolgen. Stellen Sie sicher, dass sich Ihr steuerndes Geraet im selben LAN wie Comet Q befindet.

        1. Melden Sie sich lokal ueber Domain oder IP-Adresse bei Ihrem KVM an. Details finden Sie [hier](../../faq/local_access_via_browser.md).

        2. Navigieren Sie oben rechts zu **Cloud Service** und klicken Sie auf **Bind With Code**.

            ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

        3. Es wird zufaellig ein 8-stelliger dynamischer Code fuer die Geraetebindung erzeugt, der 60 Sekunden lang gueltig ist. Klicken Sie auf den Code, um ihn zu kopieren.

            ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

        4. Kehren Sie zur GLKVM App zurueck, geben Sie den dynamischen Bindungscode ein und klicken Sie auf **Bind**.

            ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Fernzugriff ueber die GLKVM App.

    Sobald Ihr KVM-Geraet mit Ihrem Konto gebunden ist, wird es in der App als "Online" angezeigt.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Klicken Sie auf Ihr KVM-Geraet. Ein neues Fenster wird geoeffnet und die Verbindung wird aufgebaut.

    ![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Geben Sie nach dem Verbindungsaufbau das Admin-Passwort ein, um sich bei Ihrem Geraet anzumelden.

    ![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    Danach greifen Sie auf Ihr KVM-Geraet zu, ueber das Sie das gesteuerte Geraet bedienen koennen.

    ![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale

Comet Q ist in Tailscale integriert und ermoeglicht Fernzugriff ueber ein virtuelles Tailscale-Netzwerk.

Navigieren Sie in der Konsole zu **Apps Center** -> **Tailscale**, aktivieren Sie Tailscale und binden Sie Ihren Comet Q an Ihr Tailscale-Konto.

Binden Sie anschliessend Ihr steuerndes Geraet an dasselbe Konto. Danach koennen Sie aus der Ferne auf Ihren Comet Q zugreifen, indem Sie dessen **Tailscale virtual IP** in einem Webbrowser auf dem steuernden Geraet eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier

Comet Q ist in ZeroTier integriert und ermoeglicht Fernzugriff ueber ein virtuelles ZeroTier-Netzwerk.

Navigieren Sie in der Konsole zu **Apps Center** -> **ZeroTier** und aktivieren Sie ZeroTier.

Treten Sie anschliessend sowohl mit Comet Q als auch mit Ihrem steuernden Geraet demselben ZeroTier-Netzwerk bei (mithilfe einer 16-stelligen alphanumerischen Network ID). Danach koennen Sie aus der Ferne auf Ihren Comet Q zugreifen, indem Sie dessen **ZeroTier IP** in einem Webbrowser auf dem steuernden Geraet eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"}.
