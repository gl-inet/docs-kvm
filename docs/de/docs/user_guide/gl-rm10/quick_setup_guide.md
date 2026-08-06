# Comet Pro (GL-RM10) Schnellstart

Sehen Sie sich dieses Video an oder folgen Sie den Schritten unten, um Ihren Comet Pro einzurichten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/onxj5EEf9Ys" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Geräte verbinden

Zur besseren Verständlichkeit bezeichnet Gerät A das steuernde Gerät und Gerät B das gesteuerte Gerät.

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/connect-devices.png){class="glboxshadow"}

1. Verbinden Sie den Comet Pro mit der Stromversorgung.

    ![power on](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/01-power-on.png){class="glboxshadow"}

2. Verbinden Sie den HD IN-Anschluss des Comet Pro über ein HDMI-Kabel mit dem HD OUT-Anschluss von Gerät B. Verwenden Sie bei Bedarf ein weiteres HD-Kabel, um den HD OUT-Anschluss des Comet Pro mit einem externen Monitor zu verbinden.

    ![Connect the HD cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/02-hd-cable.png){class="glboxshadow"}

3. Verbinden Sie den USB Type-C-Anschluss des Comet Pro über ein USB-Kabel mit dem USB-Anschluss von Gerät B.

    ![Connect the USB cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/03-usb-cable.png){class="glboxshadow"}

4. Verbinden Sie den Comet Pro über ein Ethernet-Kabel oder Wi-Fi mit einer Netzwerkquelle.

    - Ethernet: Verbinden Sie den Ethernet-Anschluss des Comet Pro mit einer Netzwerkquelle.

        ![Connect via ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/04-ethernet.png){class="glboxshadow"}

    - Wi-Fi: Wischen Sie auf dem Touchscreen nach links und verbinden Sie den Comet Pro mit einem vorhandenen Wi-Fi-Netzwerk (2.4G/5G werden unterstützt).

        ![Connect via wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/04-wifi.png){class="glboxshadow"}

5. Die Geräteverbindung ist abgeschlossen. Sie können nun lokal oder aus der Ferne auf die Konsole des Comet Pro zugreifen.

## Lokaler Zugriff

Es gibt zwei Möglichkeiten, im lokalen Netzwerk auf den Comet Pro zuzugreifen: über den Domainnamen oder über die IP-Adresse.

Stellen Sie vor dem Zugriff sicher, dass sich Ihr steuerndes Gerät im selben LAN wie der Comet Pro befindet.

### Domain

1. Starten Sie auf dem steuernden Gerät einen Browser. Für eine bessere Kompatibilität werden Chrome oder Edge empfohlen.

2. Geben Sie `glkvm.local` in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie das Administratorpasswort ein.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Hinweis**: Beim ersten Zugriff müssen Sie Ihr Administratorpasswort einrichten.

3. Danach können Sie lokal auf die Konsole des Comet Pro zugreifen und das gesteuerte Gerät bedienen.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP-Adresse

1. Ermitteln Sie die IP-Adresse des Comet Pro auf dem Touchscreen. In diesem Beispiel lautet die IP-Adresse des Comet Pro `192.168.8.197`.

2. Starten Sie einen Browser und geben Sie diese IP-Adresse in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie das Administratorpasswort ein.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Hinweis**: Beim ersten Zugriff müssen Sie Ihr Administratorpasswort einrichten.

3. Danach können Sie lokal auf die Konsole des Comet Pro zugreifen und das gesteuerte Gerät bedienen.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Fernzugriff

Es gibt mehrere Möglichkeiten, per Fernzugriff auf den Comet Pro zuzugreifen: über den Cloud-Dienst, die GLKVM App, Tailscale, ZeroTier und NetBird.

### Cloud-Dienst

1. Binden Sie Ihr Gerät an KVM Cloud. Dies muss im lokalen Netzwerk erfolgen.

    Es gibt zwei Möglichkeiten, Ihr KVM an die Cloud zu binden: reguläre Bindung oder Bindung per dynamischem Code. Hier verwenden wir die reguläre Bindung als Beispiel. Wenn Sie die Bindung per dynamischem Code bevorzugen, klicken Sie [hier](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}, um Details anzuzeigen.

    Greifen Sie zuerst lokal auf Ihren Comet Pro zu und navigieren Sie oben rechts zu **Cloud Service**. Klicken Sie auf **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Sie werden zu einer Anmeldeseite weitergeleitet. Melden Sie sich mit Ihrem glinet-Cloud-Konto an.

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Bestätigen Sie anschließend Ihre Geräteinformationen und klicken Sie auf **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Warten Sie einen Moment. Ihr Comet Pro wird erfolgreich an Ihr Konto gebunden. Klicken Sie auf **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Fernzugriff über den Cloud-Dienst.

    Öffnen Sie einen Browser (hier wird Google Chrome als Beispiel verwendet) und geben Sie `glkvm.com` in die Adressleiste ein. Sie sehen eine Anmeldeseite. Melden Sie sich mit Ihrem glinet-Konto an.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Nach der Anmeldung sehen Sie die Geräte, die an Ihr Konto gebunden sind. Klicken Sie auf das Gerät, auf das Sie per Fernzugriff zugreifen möchten.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Geben Sie auf der neu geoeffneten Webseite Ihr Administratorpasswort ein, um sich anzumelden.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Danach können Sie ohne Installation der App per Cloud aus der Ferne auf Ihren Comet Pro und das gesteuerte Gerät zugreifen.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### GLKVM App

1. Installieren Sie die [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} auf Ihrem steuernden Gerät.

2. Melden Sie sich mit Ihrem GL.iNet-Konto an.

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Wenn Sie noch kein Konto haben, registrieren Sie sich zuerst und melden Sie sich dann an.
    
    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Binden Sie Ihr Gerät.

    Nach der Anmeldung wird die Seite wie folgt angezeigt. Klicken Sie auf **Add Device**.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    Sie können Ihr Gerät auf drei Arten binden: Auto Discover, S/N Code und Dynamic Binding Code.

    ??? "Auto Discover"
    
        Dies muss im lokalen Netzwerk erfolgen. Stellen Sie sicher, dass sich Ihr steuerndes Gerät im selben LAN wie der Comet Pro befindet.
    
        Klicken Sie auf **Auto Discover**. Die Suche wird automatisch gestartet.
    
        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}
        
        Suchen Sie Ihr KVM und geben Sie dessen Device ID ein, um es an Ihr Konto zu binden.
    
        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        Dies gilt für den Fall, dass Ihr KVM nicht erkannt wird oder sich nicht im selben LAN befindet, Sie aber über die Seriennummer (S/N) verfügen.
        
        Klicken Sie auf **S/N Code**. Passen Sie im Pop-up-Fenster den Gerätenamen an und geben Sie die S/N ein, die auf dem Etikett an der Unterseite Ihres KVM-Geräts aufgedruckt ist.
    
        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        Dies muss im lokalen Netzwerk erfolgen. Stellen Sie sicher, dass sich Ihr steuerndes Gerät im selben LAN wie der Comet Pro befindet.
    
        1. Melden Sie sich lokal über Domain oder IP-Adresse bei Ihrem KVM an. Klicken Sie [hier](../../faq/local_access_via_browser.md), um Details anzuzeigen.
    
        2. Navigieren Sie oben rechts zu **Cloud Service** und klicken Sie auf **Bind With Code**.
    
            ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}
    
        3. Für die Gerätebindung wird zufällig ein 8-stelliger dynamischer Code erzeugt, der 60 Sekunden lang gültig ist. Klicken Sie auf den Code, um ihn zu kopieren.
    
            ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}
    
        4. Kehren Sie zur GLKVM App zurück, geben Sie den dynamischen Bindungscode ein und klicken Sie auf **Bind**.
    
            ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Fernzugriff über die GLKVM App.

    Sobald Ihr KVM-Gerät an Ihr Konto gebunden ist, wird es in der App als "Online" angezeigt.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Klicken Sie auf Ihr KVM-Gerät. Es öffnet sich ein neues Fenster und die Verbindung wird hergestellt.

    ![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Sobald die Verbindung hergestellt ist, geben Sie das Administratorpasswort ein, um sich bei Ihrem Gerät anzumelden.

    ![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    Danach greifen Sie auf Ihr KVM-Gerät zu, über das Sie das gesteuerte Gerät bedienen können.

    ![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale

Comet Pro ist in Tailscale integriert, sodass Sie über das virtuelle Netzwerk von Tailscale per Fernzugriff darauf zugreifen können.

Navigieren Sie in der Konsole zu **Apps Center** -> **Tailscale**, aktivieren Sie Tailscale und binden Sie Ihren Comet Pro an Ihr Tailscale-Konto.

Binden Sie anschließend Ihr steuerndes Gerät an dasselbe Konto. Danach können Sie per Fernzugriff auf Ihren Comet Pro zugreifen, indem Sie dessen **Tailscale virtual IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier

Comet Pro ist in ZeroTier integriert, sodass Sie über das virtuelle Netzwerk von ZeroTier per Fernzugriff darauf zugreifen können.

Navigieren Sie in der Konsole zu **Apps Center** -> **ZeroTier** und aktivieren Sie ZeroTier.

Treten Sie anschließend mit dem Comet Pro und Ihrem steuernden Gerät demselben ZeroTier-Netzwerk bei (über eine 16-stellige alphanumerische Network ID). Danach können Sie per Fernzugriff auf Ihren Comet Pro zugreifen, indem Sie dessen **ZeroTier IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"}.

### NetBird

Comet Pro ist in NetBird integriert, sodass Sie über das virtuelle Netzwerk von NetBird per Fernzugriff darauf zugreifen können.

Navigieren Sie in der Konsole zu **Apps Center** -> **NetBird**, aktivieren Sie NetBird und binden Sie Ihren Comet Pro an Ihr NetBird-Konto.

Binden Sie anschließend Ihr steuerndes Gerät an dasselbe Konto. Danach können Sie per Fernzugriff auf Ihren Comet Pro zugreifen, indem Sie dessen **NetBird virtual IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_netbird.md){target="_blank"}.
