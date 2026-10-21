# Så kopplar du KVM-enheten till molnet med dynamisk kod {#how-to-bind-kvm-to-the-cloud-via-dynamic-code}

> Obs! Uppgradera KVM-enhetens firmware till version 1.7 innan du använder den här funktionen.

Den här guiden visar hur du enkelt kopplar GL.iNet KVM till molnet med en dynamisk kod.

## Steg för koppling {#binding-steps}

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

7. Enheten kopplas till ditt molnkonto. Klicka på **Done**.

    ![Koppla med kod 7](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    KVM-enheten visas i enhetslistan. Nu kan du komma åt den på distans via molntjänsten.

    ![Koppla med kod 8](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. Klicka på den enhet som du vill komma åt på distans. Ange administratörslösenordet på den nya webbsidan för att logga in.

    ![Administratörsinloggning vid fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Därefter kan du komma åt KVM-enheten och den styrda enheten på distans via molnet.

    ![Fjärråtkomst lyckades](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## Vanliga frågor {#faq}

1. **F: Hur länge är den dynamiska koden giltig, och vad gör jag om den har gått ut?**

    S: Den dynamiska koden är giltig i 60 sekunder. Om den dynamiska koden har gått ut går du tillbaka till KVM-konsolen och klickar på **Regenerate Code** för att få en ny.

    ![Generera ny kod](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **F: Vad gör jag om det inte går att generera någon dynamisk kod?**

    S: Om det inte går att generera någon dynamisk kod kan det bero på ett instabilt nätverk eller på DNS-konfigurationen uppströms.

    - Kontrollera om nätverket är stabilt, eller byt till ett annat nätverk och försök igen.

    - Ändra DNS-inställningarna uppströms och generera koden på nytt.

    Om problemet kvarstår kontaktar du vår support på [support@gl-inet.com](mailto:support@gl-inet.com).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
