# Så ställer du in en statisk IP-adress för KVM-enheten {#how-to-set-a-static-ip-for-kvm}

Den här guiden beskriver hur du ställer in en statisk IP-adress för din GL.iNet KVM direkt i konsolen när den överordnade routern inte kan tilldela någon.

Välj stegen som gäller för din firmwareversion.

## Firmware v1.9 och tidigare {#firmware-v19-and-earlier}

Stegen nedan använder Comet (GL-RM1) som exempel.

1. Logga in på Comets konsol och gå till **Settings** -> **Network**. Klicka på IP-adressen eller högerpilen.

    ![Nätverksinställningar](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/settings-network.png){class="glboxshadow"}

2. Växla till **Static**. Ange en IP-adress inom subnätets adresspool samt nätmask, gateway och DNS-servrar för din Comet och klicka sedan på **Confirm**.

    ![Statiska Ethernet-inställningar](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet-settings-static.png){class="glboxshadow"}

## Firmware v1.10 och senare {#firmware-v110-and-above}

Stegen nedan använder Comet Pro (GL-RM10) som exempel.

1. Logga in på Comet Pro:s konsol och klicka på inställningsikonen i navigeringsfältet för att öppna inställningssidan.

    ![Nätverksinställningar](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/setting_network.png){class="glboxshadow"}

2. Gå till **Network** och klicka på knappen **Static** under Ethernet Settings. Ange en IP-adress inom subnätets adresspool samt nätmask, gateway och DNS-servrar för din Comet Pro och klicka sedan på **Confirm**.

    ![Statiska Ethernet-inställningar](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet_settings_static.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
