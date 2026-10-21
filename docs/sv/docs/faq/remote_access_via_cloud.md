# Så kommer du åt KVM-enheten på distans via molnet {#how-to-access-kvm-remotely-via-cloud}

Kontrollera följande innan du börjar:

- Den styrda enheten är korrekt ansluten till KVM-enheten.

- KVM-enheten är ansluten till ett stabilt nätverk.

- Du kan komma åt KVM-enheten lokalt, eftersom kopplingen av enheten till molnet måste göras i det lokala nätverket.

Följ stegen nedan för att komma åt KVM-enheten och den styrda enheten på distans via molntjänsten.

## Koppla din KVM till molnet {#bind-your-kvm-to-the-cloud}

Det finns två sätt att koppla din KVM till molnet: vanlig koppling eller koppling med dynamisk kod.

- **Vanlig koppling**: klicka på "Bind To KVMCloud" i KVM-konsolen, så omdirigeras du till kopplingssidan med en token. Logga in på ditt molnkonto och bekräfta enhetsinformationen för att slutföra kopplingen.

- **Koppling med dynamisk kod**: klicka på "Bind With Code" i KVM-konsolen, så genereras en slumpmässig, åttasiffrig dynamisk kod för koppling av enheten. Logga in på ditt molnkonto och ange koden för att slutföra kopplingen.

### Vanlig koppling {#regular-binding}

Logga in på din KVM lokalt via IP-adress eller domännamn och gå till **Cloud Service** i det övre högra hörnet. Klicka på **Bind To Cloud**.

![Koppla till molnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

Du omdirigeras till en inloggningssida. Ange uppgifterna för ditt GL.iNet-konto och klicka på **Log In**.

![Inloggning för att koppla enheten](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

Bekräfta enhetsinformationen och klicka på **Bind**.

![Bekräfta koppling av enheten](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

Vänta ett ögonblick så kopplas enheten till ditt konto. Klicka på **Done**.

![Enheten har kopplats](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### Koppling med dynamisk kod {#dynamic-code-binding}

Obs! Uppgradera KVM-enhetens firmware till version 1.7 innan du använder den här funktionen.

1. Logga in på din GL.iNet KVM lokalt via domännamn eller IP-adress. Klicka [här](../faq/local_access_via_browser.md) för mer information.

2. När du har loggat in går du till **Cloud Service** i det övre högra hörnet och klickar på **Bind With Code**.

    ![Koppla med kod 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. En slumpmässig, åttasiffrig dynamisk kod för koppling av enheten genereras. Den är giltig i 60 sekunder. Klicka på koden för att kopiera den.

    ![Koppla med kod 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Gå till [https://glkvm.com/](https://glkvm.com/){target="_blank"} och logga in med ditt GL.iNet-molnkonto.

    ![Koppla med kod 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. När du har loggat in visas sidan nedan.

    ![Koppla med kod 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Klicka på **Add Device** och välj **Bind with Code**.

    ![Koppla med kod 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Ange den åttasiffriga dynamiska koden i popup-fönstret och klicka på **Bind**.

    ![Koppla med kod 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Obs!** Den dynamiska koden är giltig i 60 sekunder. Om den dynamiska koden har gått ut går du tillbaka till KVM-konsolen och klickar på **Regenerate Code** för att få en ny.

    ![Generera ny kod](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

    Enheten kopplas sedan till ditt molnkonto.

## Fjärråtkomst via molnet {#remote-access-via-cloud}

Öppna en webbläsare (här används Google Chrome som exempel) och ange `glkvm.com` i adressfältet. En inloggningssida visas. Logga in med ditt GL.iNet-konto.

![Inloggning för fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

När du har loggat in visas de enheter som är kopplade till ditt konto. Klicka på den enhet som du vill komma åt på distans.

![Välj enhet för fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

Ange administratörslösenordet på den nya webbsidan för att logga in.

![Administratörsinloggning vid fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

Nu kan du komma åt KVM-enheten och den styrda enheten på distans via molnet.

![Fjärråtkomst lyckades](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
