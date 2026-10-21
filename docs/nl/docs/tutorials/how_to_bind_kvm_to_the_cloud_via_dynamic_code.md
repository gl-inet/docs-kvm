# De KVM aan de cloud koppelen met een dynamische code {#how-to-bind-kvm-to-the-cloud-via-dynamic-code}

> Opmerking: voer een upgrade uit van de firmware van uw KVM naar versie 1.7 voordat u deze functie gebruikt.

In deze handleiding leest u hoe u een GL.iNet KVM eenvoudig met een dynamische code aan de cloud koppelt.

## Stappen voor het koppelen {#binding-steps}

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

7. Het apparaat wordt aan uw cloudaccount gekoppeld. Klik op **Done**.

    ![Koppelen met code 7](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    De KVM verschijnt in de apparatenlijst. U kunt het apparaat nu op afstand openen via de cloudservice.

    ![Koppelen met code 8](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. Klik op het apparaat dat u op afstand wilt openen. Voer op de nieuw geopende webpagina uw beheerderswachtwoord in om u aan te melden.

    ![Beheerderswachtwoord voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Daarna kunt u de KVM en het bestuurde apparaat via de cloud op afstand openen.

    ![Externe toegang gelukt](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## Veelgestelde vragen {#faq}

1. **V: Hoe lang is de dynamische code geldig? Wat moet ik doen als deze verlopen is?**

    A: De dynamische code is 60 seconden geldig. Als de dynamische code is verlopen, gaat u terug naar de KVM-console en klikt u op **Regenerate Code** om een nieuwe code te krijgen.

    ![Code opnieuw genereren](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **V: Wat moet ik doen als de dynamische code niet kan worden gegenereerd?**

    A: Als de dynamische code niet kan worden gegenereerd, kan dat komen door een onstabiel netwerk of door de DNS-configuratie van het bovenliggende netwerk.
    
    - Controleer of uw netwerk stabiel is, of schakel over naar een ander netwerk en probeer het opnieuw.

    - Wijzig de DNS-instellingen van het bovenliggende netwerk en genereer de code opnieuw.
    
    Als het probleem zich blijft voordoen, neemt u contact op met onze ondersteuning via [support@gl-inet.com](mailto:support@gl-inet.com).

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
