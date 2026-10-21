# De KVM op afstand openen via de cloud {#how-to-access-kvm-remotely-via-cloud}

Controleer voordat u begint het volgende:

- Het bestuurde apparaat is correct op de KVM aangesloten.
    
- De KVM is verbonden met een stabiel netwerk.

- U kunt de KVM lokaal openen, want het koppelen van het apparaat aan de cloud moet in het lokale netwerk gebeuren.

Volg de onderstaande stappen om uw KVM en het bestuurde apparaat op afstand te openen via de cloudservice.

## Uw KVM aan de cloud koppelen {#bind-your-kvm-to-the-cloud}

U kunt uw KVM op twee manieren aan de cloud koppelen: via reguliere koppeling of via koppeling met een dynamische code.

- **Reguliere koppeling**: klik in de KVM-console op "Bind To KVMCloud". U wordt dan met het token doorgestuurd naar de koppelingspagina. Meld u aan bij uw cloudaccount en bevestig de apparaatgegevens om de koppeling te voltooien.

- **Koppeling met een dynamische code**: klik in de KVM-console op "Bind With Code". Er wordt dan willekeurig een dynamische code van 8 cijfers voor de apparaatkoppeling gegenereerd. Meld u aan bij uw cloudaccount en voer de code in om de koppeling te voltooien.

### Reguliere koppeling {#regular-binding}

Meld u lokaal aan bij uw KVM via het IP-adres of de domeinnaam en ga rechtsboven naar **Cloud Service**. Klik op **Bind To Cloud**.

![Aan de cloud koppelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

U wordt doorgestuurd naar een aanmeldpagina. Voer de gegevens van uw GL.iNet-account in en klik op **Log In**.

![Aanmelden om het apparaat te koppelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

Controleer de apparaatgegevens en klik op **Bind**.

![Apparaatkoppeling bevestigen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

Even later is uw apparaat aan uw account gekoppeld. Klik op **Done**.

![Apparaat gekoppeld](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### Koppeling met een dynamische code {#dynamic-code-binding}

Opmerking: voer een upgrade uit van de firmware van uw KVM naar versie 1.7 voordat u deze functie gebruikt.

1. Meld u lokaal aan bij uw GL.iNet KVM via de domeinnaam of het IP-adres. Klik [hier](../faq/local_access_via_browser.md) voor meer informatie.

2. Ga na het aanmelden rechtsboven naar **Cloud Service** en klik op **Bind With Code**.

    ![Koppelen met code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Er wordt willekeurig een dynamische code van 8 cijfers voor de apparaatkoppeling gegenereerd, die 60 seconden geldig is. Klik op de code om deze te kopiëren.

    ![Koppelen met code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Ga naar [https://glkvm.com/](https://glkvm.com/){target="_blank"} en meld u aan met uw GL.iNet-cloudaccount.

    ![Koppelen met code 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Na het aanmelden ziet de pagina er als volgt uit.

    ![Koppelen met code 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Klik op **Add Device** en selecteer **Bind with Code**.

    ![Koppelen met code 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Voer in het pop-upvenster de dynamische code van 8 cijfers in en klik op **Bind**.

    ![Koppelen met code 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Opmerking**: De dynamische code is 60 seconden geldig. Als de dynamische code is verlopen, gaat u terug naar de KVM-console en klikt u op **Regenerate Code** om een nieuwe code te krijgen.

    ![Code opnieuw genereren](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

    Het apparaat wordt dan aan uw cloudaccount gekoppeld.

## Externe toegang via de cloud {#remote-access-via-cloud}

Open een browser (bijvoorbeeld Google Chrome) en voer `glkvm.com` in de adresbalk in. Er verschijnt een aanmeldpagina. Meld u aan met uw GL.iNet-account.

![Aanmelden voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

Na het aanmelden ziet u de apparaten die aan uw account zijn gekoppeld. Klik op het apparaat dat u op afstand wilt openen.

![Apparaat kiezen voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

Voer op de nieuw geopende webpagina uw beheerderswachtwoord in om u aan te melden.

![Beheerderswachtwoord voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

U kunt de KVM en het bestuurde apparaat nu via de cloud op afstand openen.

![Externe toegang gelukt](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
