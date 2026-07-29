# Comet X (GL-RM4PE) Schnellstart

## Geräte verbinden

Zur besseren Verständlichkeit bezeichnet Gerät A das steuernde Gerät und Gerät B das gesteuerte Gerät.

![connect1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. Verbinden Sie den Comet X über ein Ethernet-Kabel mit einem PoE-Switch oder versorgen Sie ihn über ein 5V/3A-Netzteil mit Strom.

    ![connect2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Hinweis**: Wenn Sie ein Netzteil für die Stromversorgung verwenden, verbinden Sie den Comet X über ein Ethernet-Kabel mit einem Netzwerkgerät (z. B. einem Router), um Internetzugang zu erhalten.*

2. Verbinden Sie den **HDMI IN**-Anschluss des Comet X über ein HDMI-Kabel mit Gerät B. Dadurch wird die Videosignalübertragung aktiviert.

    ![connect3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. Verbinden Sie den **USB-C**-Anschluss des Comet X über ein USB-Kabel mit Gerät B. Dieser USB-C-Anschluss muss mit dem entsprechenden HDMI IN-Anschluss gekoppelt sein, damit Tastatur- und Maussignale korrekt übertragen werden.

    ![connect4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

4. (Optional) Verbinden Sie den **HDMI OUT**-Anschluss des Comet X mit einem externen Monitor, um die Anzeige zu duplizieren (Video-Loopout). Details finden Sie unter [Lokale Steuerung](#local-control).

5. Die Verbindung ist abgeschlossen. Sie können nun lokal oder aus der Ferne auf die Konsole des Comet X zugreifen.

## Rack-Montage

Montieren Sie den Comet X bei Bedarf an den Schienen eines Serverracks.

1. Befestigen Sie die Montagehalterungen mit den mitgelieferten Schrauben am Comet X.

    ![install1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Befestigen Sie den Comet X mit Rack-Schrauben an den Rack-Schienen. **Rack-Schrauben sind nicht im Lieferumfang enthalten**.

    ![install2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## Lokale Steuerung {#local-control}

Steuern Sie das Gerät direkt über physische Kabel. Netzwerk, IP-Adresse oder Domainname sind nicht erforderlich.

Der Comet X verfügt über einen HDMI OUT-Anschluss und zwei zusätzliche USB-Anschlüsse und eignet sich damit ideal für lokale Fehlerbehebung, Konfiguration und Betriebssysteminstallation. Schließen Sie einfach Monitor, Maus und Tastatur an, um lokale Plug-and-play-Hardwaresteuerung zu nutzen.

1. Verbinden Sie den **HDMI OUT**-Anschluss auf der Rückseite des Comet X mit einem externen Monitor, um die Anzeige zu duplizieren (Video-Loopout).

    ![local control1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. Verbinden Sie eine Tastatur und eine Maus mit den USB-Anschlüssen auf der Vorderseite des Comet X.

    ![local control2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. Sie können die verbundenen Geräte nun mit Ihrer lokalen Tastatur und Maus steuern, während die Videosignale an den lokalen Monitor durchgeschleift werden.

## LAN-Zugriff {#lan-access}

Es gibt zwei Möglichkeiten, im lokalen Netzwerk auf den Comet X zuzugreifen: über den Domainnamen oder über die IP-Adresse.

Stellen Sie vor dem Zugriff sicher, dass sich Ihr steuerndes Gerät im selben LAN wie der Comet X befindet.

### Domain

1. Starten Sie auf dem steuernden Gerät einen Browser. Für eine bessere Kompatibilität werden Chrome oder Edge empfohlen.

2. Geben Sie `glkvm.local` in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie das Administratorpasswort ein.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Hinweis**: Beim ersten Zugriff müssen Sie Ihr Administratorpasswort einrichten.*

3. Danach können Sie lokal auf die Konsole des Comet X zugreifen und das gesteuerte Gerät bedienen.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### IP-Adresse

1. Ermitteln Sie die IP-Adresse des Comet X auf dem Touchscreen. In diesem Beispiel lautet die IP-Adresse des Comet X `192.168.8.197`.

2. Starten Sie einen Browser und geben Sie diese IP-Adresse in die Adressleiste ein. Sie werden zur GLKVM-Anmeldeseite weitergeleitet. Geben Sie das Administratorpasswort ein.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Hinweis**: Beim ersten Zugriff müssen Sie Ihr Administratorpasswort einrichten.*

3. Danach können Sie lokal auf die Konsole des Comet X zugreifen und das gesteuerte Gerät bedienen.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## Fernzugriff

Es gibt mehrere Möglichkeiten, per Fernzugriff auf den Comet X zuzugreifen: über den Cloud-Dienst, die GLKVM App, Tailscale und ZeroTier.

### Cloud-Dienst

1. Binden Sie Ihr Gerät an KVM Cloud. Dies muss im lokalen Netzwerk erfolgen.

    Es gibt zwei Möglichkeiten, Ihr KVM an die Cloud zu binden: Regular Binding oder Dynamic Code Binding. Hier verwenden wir Regular Binding als Beispiel. Wenn Sie Dynamic Code Binding bevorzugen, klicken Sie [hier](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}, um Details anzuzeigen.

    Greifen Sie zuerst lokal auf Ihren Comet X zu und navigieren Sie oben rechts zu **Cloud Service**. Klicken Sie auf **Bind To KVMCloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    Sie werden zu einer Anmeldeseite weitergeleitet. Melden Sie sich mit Ihrem glinet-Cloud-Konto an.

    ![cloud bind device1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    Bestätigen Sie anschließend Ihre Geräteinformationen und klicken Sie auf **Bind**.

    ![cloud bind device2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    Warten Sie einen Moment. Ihr Comet X wird an Ihr Konto gebunden. Klicken Sie auf **Done**.

    ![cloud bind device success](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. Fernzugriff über den Cloud-Dienst.

    Nachdem Sie auf Done geklickt haben, werden Sie zu einer Website mit der Domain `glkvm.com` weitergeleitet, auf der Sie Ihr Gerät sehen können.

    ![cloud devices list](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Tipp**: Wenn Sie nicht weitergeleitet werden, geben Sie `glkvm.com` manuell in die Adressleiste ein und melden Sie sich bei Ihrem glinet-Konto an. Nach der Anmeldung sehen Sie Ihr an Ihr Konto gebundenes Gerät.*
    
    Klicken Sie auf das Gerät, auf das Sie per Fernzugriff zugreifen möchten.
    
    ![cloud access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}
    
    Es öffnet sich eine neue Webseite. Geben Sie Ihr Administratorpasswort ein, um sich anzumelden.

    ![cloud access1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}
    
    Danach können Sie per Cloud aus der Ferne auf Ihren Comet X und das gesteuerte Gerät zugreifen.

    ![cloud access2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### GLKVM App

1. Installieren Sie die [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} auf Ihrem steuernden Gerät.

2. Melden Sie sich mit Ihrem GL.iNet-Konto an.

    ![log in](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    Wenn Sie noch kein Konto haben, registrieren Sie sich zuerst und melden Sie sich dann an.
    
    ![sign up](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. Binden Sie Ihr Gerät.

    Nach der Anmeldung wird die Seite wie folgt angezeigt. Klicken Sie auf **Add Device**.

    ![add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    Sie können Ihr Gerät auf drei Arten binden: Auto Discover, S/N Code und Dynamic Binding Code.

    ??? "Auto Discover"
    
        Dies muss im lokalen Netzwerk erfolgen. Stellen Sie sicher, dass sich Ihr steuerndes Gerät im selben LAN wie der Comet X befindet, und halten Sie die KVM Device ID bereit.
    
        Klicken Sie auf **Auto Discover**. Die Suche wird gestartet.
    
        ![auto discover 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}
        
        Suchen Sie Ihr KVM und geben Sie dessen **Device ID** ein, um es an Ihr Konto zu binden.
    
        ![auto discover 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![auto discover 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        Dies gilt für den Fall, dass Ihr KVM nicht erkannt wird oder sich nicht im selben LAN befindet, Sie aber über die Seriennummer (S/N) verfügen.
        
        Klicken Sie auf **S/N Code**. Legen Sie im Pop-up-Fenster einen Gerätenamen fest und geben Sie die S/N ein, die auf der Unterseite des KVM-Geräts aufgedruckt ist.
    
        ![sn code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        Dies muss im lokalen Netzwerk erfolgen. Stellen Sie sicher, dass sich Ihr steuerndes Gerät im selben LAN wie der Comet X befindet.
    
        1. Melden Sie sich lokal über Domain oder IP-Adresse bei Ihrem KVM an. Details finden Sie [hier](#lan-access).
    
        2. Navigieren Sie oben rechts zu **Cloud Service** und klicken Sie auf **Bind With Code**.
    
            ![bind with code 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}
    
        3. Für die Gerätebindung wird zufällig ein 8-stelliger dynamischer Code erzeugt, der 60 Sekunden lang gültig ist. Klicken Sie auf den Code, um ihn zu kopieren.
    
            ![bind with code 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}
    
        4. Kehren Sie zur GLKVM App zurück, geben Sie den dynamischen Bindungscode ein und klicken Sie auf **Bind**.
    
            ![dynamic code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. Fernzugriff über die GLKVM App.

    Sobald Ihr KVM-Gerät an Ihr Konto gebunden ist, wird es in der App als "Online" angezeigt.

    ![app device online](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    Klicken Sie auf Ihr KVM-Gerät. Es öffnet sich ein neues Fenster und die Verbindung wird hergestellt.

    ![app connecting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    Sobald die Verbindung hergestellt ist, geben Sie Ihr Administratorpasswort ein, um sich bei Ihrem Gerät anzumelden.

    ![app access1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    Danach greifen Sie auf Ihr KVM-Gerät zu, über das Sie das gesteuerte Gerät bedienen können.

    ![app access2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale

Comet X ist in Tailscale integriert, sodass Sie über das virtuelle Netzwerk von Tailscale per Fernzugriff darauf zugreifen können.

Navigieren Sie in der Konsole zu **Apps Center** -> **Tailscale**, aktivieren Sie Tailscale und binden Sie Ihren Comet X an Ihr Tailscale-Konto.

Binden Sie anschließend Ihr steuerndes Gerät an dasselbe Konto. Danach können Sie per Fernzugriff auf Ihren Comet X zugreifen, indem Sie dessen **Tailscale virtual IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier

Comet X ist in ZeroTier integriert, sodass Sie über das virtuelle Netzwerk von ZeroTier per Fernzugriff darauf zugreifen können.

Navigieren Sie in der Konsole zu **Apps Center** -> **ZeroTier** und aktivieren Sie ZeroTier.

Treten Sie anschließend mit dem Comet X und Ihrem steuernden Gerät demselben ZeroTier-Netzwerk bei (über eine 16-stellige alphanumerische Network ID). Danach können Sie per Fernzugriff auf Ihren Comet X zugreifen, indem Sie dessen **ZeroTier IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren.

Details finden Sie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"}.
