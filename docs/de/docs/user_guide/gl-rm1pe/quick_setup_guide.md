# Comet PoE (GL-RM1PE) Schnellstart

Sehen Sie sich dieses Video an oder folgen Sie den Schritten unten, um Ihren Comet PoE einzurichten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/QsPceu7OKco" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Geraete verbinden

Zur besseren Verstaendlichkeit bezeichnet Geraet A das steuernde Geraet und Geraet B das gesteuerte Geraet.

![distinguish devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/quick_setup/connect-1.png){class="glboxshadow"}

1. Verbinden Sie den Comet PoE ueber ein Ethernet-Kabel mit dem PoE-Switch.

    ![connect ethernet cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/quick_setup/connect-2.png){class="glboxshadow gl-80-desktop"}

2. Verbinden Sie den HD IN-Anschluss des Comet PoE ueber ein HDMI-Kabel mit dem HD OUT-Anschluss von Geraet B.

    ![connect hdmi cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/quick_setup/connect-3.png){class="glboxshadow gl-80-desktop"}

3. Verbinden Sie den USB-Anschluss des Comet PoE ueber ein USB-Kabel mit der USB-Schnittstelle von Geraet B.

    ![Connect USB cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/quick_setup/connect-4.png){class="glboxshadow gl-80-desktop"}

4. Die Geraeteverbindung ist abgeschlossen. Jetzt koennen Sie lokal oder aus der Ferne auf die Konsole des Comet PoE zugreifen.

## Lokaler Zugriff

Es gibt zwei Moeglichkeiten, im lokalen Netzwerk auf Comet PoE zuzugreifen: ueber den Domainnamen oder ueber die IP-Adresse.

Stellen Sie vor dem Zugriff sicher, dass sich Ihr steuerndes Geraet im selben LAN wie Comet PoE befindet.

### Domain

1. Oeffnen Sie auf dem steuernden Geraet einen Browser. Fuer bessere Kompatibilitaet werden Chrome oder Edge empfohlen.

2. Geben Sie `glkvm.local` in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie das Admin-Passwort ein.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Hinweis**: Beim ersten Zugriff muessen Sie Ihr Admin-Passwort einrichten.

3. Danach koennen Sie lokal auf die Konsole des Comet PoE und auf das gesteuerte Geraet zugreifen.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP-Adresse

1. Suchen Sie die IP-Adresse des Comet PoE im uebergeordneten Router.

    Beispiel: Comet PoE ist ueber ein Ethernet-Kabel mit dem LAN-Port eines GL.iNet Routers GL-AXT1800 verbunden.

    Melden Sie sich im Web-Admin-Panel des GL-AXT1800 an und suchen Sie die IP-Adresse des Comet PoE in der Client-Liste, wie unten gezeigt.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

2. Oeffnen Sie im Browser einen neuen Tab und geben Sie die IP-Adresse des Comet PoE in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie das Admin-Passwort ein.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Hinweis**: Beim ersten Zugriff muessen Sie Ihr Admin-Passwort einrichten.

3. Danach koennen Sie lokal auf die Konsole des Comet PoE und auf das gesteuerte Geraet zugreifen.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Fernzugriff

Es gibt mehrere Moeglichkeiten, aus der Ferne auf Comet PoE zuzugreifen: ueber den Cloud-Dienst, die GLKVM App, Tailscale, ZeroTier und NetBird.

### Cloud-Dienst

1. Binden Sie Ihr Geraet an die KVM Cloud. Dies muss im lokalen Netzwerk erfolgen.

    Es gibt zwei Moeglichkeiten, Ihr KVM mit der Cloud zu binden: regulaere Bindung oder Bindung per dynamischem Code. Hier verwenden wir die regulaere Bindung als Beispiel. Wenn Sie die Bindung per dynamischem Code bevorzugen, finden Sie [hier](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} weitere Informationen.

    Greifen Sie zuerst lokal auf Ihren Comet PoE zu und navigieren Sie oben rechts zu **Cloud Service**. Klicken Sie auf **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Sie werden zu einer Anmeldeseite weitergeleitet. Melden Sie sich mit Ihrem glinet Cloud-Konto an.

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Bestaetigen Sie anschliessend die Geraeteinformationen und klicken Sie auf **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Warten Sie einen Moment, bis Ihr Geraet erfolgreich mit Ihrem Konto gebunden wurde. Klicken Sie auf **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Fernzugriff ueber den Cloud-Dienst.

    Oeffnen Sie einen Browser (hier Google Chrome als Beispiel) und geben Sie `glkvm.com` in die Adressleiste ein. Eine Anmeldeseite wird angezeigt. Melden Sie sich mit Ihrem glinet Konto an.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Nach der Anmeldung sehen Sie die mit Ihrem Konto gebundenen Geraete. Klicken Sie auf das Geraet, auf das Sie aus der Ferne zugreifen moechten.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Geben Sie auf der neu geoeffneten Webseite Ihr Admin-Passwort ein, um sich anzumelden.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Danach koennen Sie ueber die Cloud aus der Ferne auf den Comet PoE und das gesteuerte Geraet zugreifen, ohne die App zu installieren.

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

        Dies muss im lokalen Netzwerk erfolgen. Stellen Sie sicher, dass sich Ihr steuerndes Geraet im selben LAN wie Comet PoE befindet.

        Klicken Sie auf **Auto Discover**. Die Suche startet automatisch.

        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Suchen Sie Ihr KVM und geben Sie die Device ID ein, um es mit Ihrem Konto zu binden.

        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Dies gilt, wenn Ihr KVM nicht erkannt wird oder sich nicht im selben LAN befindet, Sie aber seine Seriennummer (S/N) haben.

        Klicken Sie auf **S/N Code**. Passen Sie im Pop-up-Fenster den Geraetenamen an und geben Sie die S/N ein, die auf dem Etikett an der Unterseite Ihres KVM-Geraets aufgedruckt ist.

        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Dies muss im lokalen Netzwerk erfolgen. Stellen Sie sicher, dass sich Ihr steuerndes Geraet im selben LAN wie Comet PoE befindet.

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

Comet PoE ist in Tailscale integriert und ermoeglicht Fernzugriff ueber ein virtuelles Tailscale-Netzwerk.

Navigieren Sie in der Konsole des Comet PoE zu **Apps Center** -> **Tailscale**, aktivieren Sie Tailscale und binden Sie Comet PoE an Ihr Tailscale-Konto.

Binden Sie anschliessend Ihr steuerndes Geraet an dasselbe Konto. Danach koennen Sie aus der Ferne auf Ihren Comet PoE zugreifen, indem Sie dessen **Tailscale virtual IP** in einem Webbrowser auf dem steuernden Geraet eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier

Comet PoE ist in ZeroTier integriert und ermoeglicht Fernzugriff ueber ein virtuelles ZeroTier-Netzwerk.

Navigieren Sie in der Konsole des Comet PoE zu **Apps Center** -> **ZeroTier** und aktivieren Sie ZeroTier.

Treten Sie anschliessend sowohl mit Comet PoE als auch mit Ihrem steuernden Geraet demselben ZeroTier-Netzwerk bei (mithilfe einer 16-stelligen alphanumerischen Network ID). Danach koennen Sie aus der Ferne auf Ihren Comet PoE zugreifen, indem Sie dessen **ZeroTier IP** in einem Webbrowser auf dem steuernden Geraet eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"}.

### NetBird

Comet PoE ist in NetBird integriert und ermoeglicht Fernzugriff ueber ein virtuelles NetBird-Netzwerk.

Navigieren Sie in der Konsole des Comet PoE zu **Apps Center** -> **NetBird**, aktivieren Sie NetBird und binden Sie Ihren Comet PoE an Ihr NetBird-Konto.

Binden Sie anschliessend Ihr steuerndes Geraet an dasselbe Konto. Danach koennen Sie aus der Ferne auf Ihren Comet PoE zugreifen, indem Sie dessen **NetBird virtual IP** in einem Webbrowser auf dem steuernden Geraet eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_netbird.md){target="_blank"}.
