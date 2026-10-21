# Så kommer du åt KVM-enheten på distans via GLKVM-appen {#how-to-access-kvm-remotely-via-glkvm-app}

Innan du börjar ska du kontrollera att den styrda enheten är korrekt ansluten till GL.iNet KVM och att KVM-enheten är ansluten till ett stabilt nätverk.

Följ stegen nedan för att komma åt KVM-enheten och den styrda enheten på distans via GLKVM-appen.

## Installera och logga in {#install-and-log-in}

1. Installera [GLKVM-appen](https://www.gl-inet.com/app-rm/){target="_blank"} på den styrande enheten.

2. Öppna GLKVM-appen och logga in med ditt GL.iNet-konto.

    ![Logga in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Om du inte har något GL.iNet-konto registrerar du dig först och loggar sedan in.

    ![Registrera dig](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## Koppla din KVM {#bind-your-kvm}

När du har loggat in visas sidan nedan. Klicka på **Add Device**.

Det finns tre sätt att koppla din KVM: Auto Discover, S/N Code och Dynamic Binding Code.

![Lägg till enhet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### Auto Discover {#auto-discover}

Detta måste göras i det lokala nätverket. Kontrollera att KVM-enheten och den styrande enheten finns i samma LAN.

1. Klicka på **Auto Discover**. Sökningen efter tillgängliga KVM-enheter startar automatiskt.

    ![Automatisk identifiering 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. Leta upp din KVM och ange dess **Device ID** för att koppla den till ditt konto.

    ![Automatisk identifiering 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### S/N Code {#sn-code}

Den här metoden gäller om din KVM inte hittas eller inte finns i samma LAN, men du har dess serienummer (S/N).

1. Klicka på **S/N Code**.

2. Ge enheten ett namn i popup-fönstret och ange dess serienummer, som finns tryckt på etiketten på undersidan av KVM-enheten.

    ![Serienummer](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### Dynamic Binding Code {#dynamic-binding-code}

Uppgradera KVM-enhetens firmware till v1.7 innan du använder den här funktionen.

Detta måste göras i det lokala nätverket. Kontrollera att KVM-enheten och den styrande enheten finns i samma LAN.

1. Logga in på din KVM lokalt via domännamn eller IP-adress. Klicka [här](../faq/local_access_via_browser.md) för mer information.

2. När du har loggat in går du till **Cloud Service** i det övre högra hörnet och klickar på **Bind With Code**.

    ![Koppla med kod 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. En slumpmässig, åttasiffrig dynamisk kod för koppling av enheten genereras. Den är giltig i 60 sekunder. Klicka på koden för att kopiera den.

    ![Koppla med kod 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Gå tillbaka till GLKVM-appen, ange den dynamiska kopplingskoden och klicka på **Bind**.

    ![Dynamisk kod](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## Fjärråtkomst {#remote-access}

När KVM-enheten har kopplats till ditt konto visas den som "Online" i appen.

![Enheten är online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

Klicka på din KVM-enhet. Ett nytt fönster öppnas och anslutningen startar.

![Ansluter](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

När anslutningen är upprättad anger du ditt administratörslösenord för att logga in.

![Inloggning efter anslutning](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

Nu kommer du åt KVM-enheten och via den den styrda enheten.

![Ansluten åtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
