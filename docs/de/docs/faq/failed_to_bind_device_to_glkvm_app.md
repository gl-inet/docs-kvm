# Was tun, wenn das Binden des Geräts an die GLKVM App fehlschlägt

Die [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} ermöglicht den Fernzugriff vom steuernden Gerät auf Ihr gesteuertes Gerät. Installieren Sie die App auf dem steuernden Gerät und binden Sie Ihr GL.iNet KVM-Gerät daran. Danach können Sie jederzeit und von überall remote auf das gesteuerte Gerät zugreifen.

Das Binden des Geräts kann jedoch aus verschiedenen Gründen fehlschlagen.

Klicken Sie unten auf die jeweilige Fehlermeldung, um die passende Lösung anzuzeigen.

??? "Binding failed, unable to obtain basic KVM device information."

    ![binding failed device info error](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. Prüfen Sie den LED-Status. Stellen Sie sicher, dass die LED dauerhaft weiß leuchtet und Ihr KVM-Gerät mit dem Internet verbunden ist.
    2. Starten Sie Ihr KVM-Gerät neu, warten Sie 2 Minuten und versuchen Sie erneut, es zu binden.
    3. Wenn Sie das Gerät per S/N-Code hinzufügen, stellen Sie sicher, dass Sie die richtige S/N eingeben.
    4. Führen Sie die folgenden Schritte aus, um das Netzwerk mit dem Befehl **Ping** zu prüfen.

        1. Verbinden Sie Ihr steuerndes Gerät mit demselben Netzwerk wie Ihr KVM.

        2. Öffnen Sie auf dem steuernden Gerät einen Browser (Chrome oder Edge wird empfohlen) und geben Sie `glkvm.local` in die Adressleiste ein. Geben Sie das Admin-Passwort ein, um sich anzumelden.

            ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Navigieren Sie nach der Anmeldung zu **Toolbox** -> **Terminal** und klicken Sie auf **Access**, um sich am Terminal anzumelden.

            ![access terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Pingen Sie `google.com`, um den Netzwerkstatus zu prüfen.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Wenn das Netzwerk ordnungsgemäß funktioniert, erhalten Sie das unten gezeigte Ergebnis.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Wenn das Netzwerk instabil oder nicht verfügbar ist, wenden Sie sich bitte an Ihren Internetanbieter oder den Support Ihres Routers.

??? "Device network error, binding failed."

    ![binding failed network error](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. Prüfen Sie den LED-Status. Stellen Sie sicher, dass die LED dauerhaft weiß leuchtet und Ihr KVM-Gerät mit dem Internet verbunden ist.
    2. Starten Sie Ihr KVM-Gerät neu, warten Sie 2 Minuten und versuchen Sie erneut, es zu binden.
    3. Stellen Sie sicher, dass der Cloud-Dienst aktiviert ist.

        Der Cloud-Dienst ist standardmäßig aktiviert. Wenn Sie ihn jedoch zuvor manuell deaktiviert haben, schlägt das erneute Binden des Geräts an die GLKVM App fehl. Greifen Sie lokal per Domain oder IP-Adresse auf Ihr KVM-Gerät zu, um den Cloud-Dienst wieder zu aktivieren.

    4. Führen Sie die folgenden Schritte aus, um das Netzwerk mit dem Befehl **Ping** zu prüfen.

        1. Verbinden Sie Ihr steuerndes Gerät mit demselben Netzwerk wie Ihr KVM.

        2. Öffnen Sie auf dem steuernden Gerät einen Browser (Chrome oder Edge wird empfohlen) und geben Sie `glkvm.local` in die Adressleiste ein. Geben Sie das Admin-Passwort ein, um sich anzumelden.

            ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Navigieren Sie nach der Anmeldung zu **Toolbox** -> **Terminal** und klicken Sie auf **Access**, um sich am Terminal anzumelden.

            ![access terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Pingen Sie `google.com`, um den Netzwerkstatus zu prüfen.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Wenn das Netzwerk ordnungsgemäß funktioniert, erhalten Sie das unten gezeigte Ergebnis.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Wenn das Netzwerk instabil oder nicht verfügbar ist, wenden Sie sich bitte an Ihren Internetanbieter oder den Support Ihres Routers.

??? "Binding failed, KVM is already bound by others."

    ![binding failed bound by others](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    Das bedeutet, dass das KVM-Gerät bereits an ein anderes Konto gebunden wurde.

    1. Prüfen Sie, ob Sie es an eine andere Ihrer E-Mail-Adressen gebunden haben. Probieren Sie gegebenenfalls andere Konten aus.

    2. Wenn Sie das Gerät per S/N-Code hinzufügen, stellen Sie sicher, dass Sie die richtige S/N eingeben.

??? "Incorrect Dynamic Binding Code. You have 4 attempts remaining."

    ![incorrect binding code](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    Das bedeutet, dass Sie einen ungültigen oder abgelaufenen Bindungscode eingegeben haben.

    1. Melden Sie sich lokal an der Admin-Konsole Ihres KVM an, navigieren Sie oben rechts zu **Cloud Service** und klicken Sie auf **Bind with Code**, um einen dynamischen Bindungscode zu erhalten.

    2. Beim Modell GL-RM10 (Comet Pro) können Sie den Code auch über den Touchscreen abrufen. Wischen Sie zum Bildschirm **Cloud Service** und klicken Sie auf **Generate Binding Code**. Danach wird auf dem Touchscreen ein dynamischer Bindungscode angezeigt. Geben Sie diesen Bindungscode in der GLKVM App ein, um das Binden abzuschließen.

        ![generate binding code](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_code_screen.png){class="glboxshadow"}

    3. Wenn der Bindungscode abläuft, klicken Sie auf **Regenerate**, um einen neuen Code zu erhalten.

??? "Incorrect Device ID. You have 4 attempts remaining."

    ![incorrect device id](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    Das bedeutet, dass Sie die falsche Device ID eingegeben haben.

    1. Prüfen Sie das Etikett auf der Unterseite auf die richtige Device ID.

    2. Wenn Sie das Etikett auf der Unterseite nicht prüfen können, versuchen Sie, Ihr Gerät über den lokalen Zugriff zu binden.

        Melden Sie sich lokal an der Admin-Konsole Ihres KVM an, navigieren Sie oben rechts zu **Cloud Service** und klicken Sie auf **Bind To KVM Cloud**. Danach werden Sie zur Bindungsseite mit einem eindeutigen Token weitergeleitet. Melden Sie sich mit Ihrem Cloud-Konto an und bestätigen Sie die Geräteinformationen, um das Binden abzuschließen.

??? "Other"

    Prüfen Sie, ob auf Ihrem steuernden Gerät, auf dem die GLKVM App installiert ist, ein VPN aktiviert ist.

    Deaktivieren Sie VPN- oder Proxy-Software, einschließlich AstroWarp, Tailscale und ZeroTier, und versuchen Sie anschließend erneut, Ihr KVM an die GLKVM App zu binden.

Wenn das Problem weiterhin besteht, kontaktieren Sie uns bitte unter [support@gl-inet.com](mailto:support@gl-inet.com) und geben Sie Gerätemodell, Firmware-Version und MAC-Adresse an.
