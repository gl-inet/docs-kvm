# Så kommer du åt KVM-enheten lokalt via webbläsaren {#how-to-access-the-kvm-locally-via-browser}

Innan du börjar ska du kontrollera att den styrande enheten och KVM-enheten finns i samma LAN.

Det finns två sätt att komma åt KVM-enheten lokalt via en webbläsare: med ett domännamn eller en IP-adress.

## Lokal åtkomst via domännamn {#local-access-via-domain}

1. Öppna en webbläsare på den styrande enheten. Chrome eller Edge rekommenderas för bättre kompatibilitet.

2. Ange `glkvm.local` i adressfältet. Du kommer till inloggningssidan för GLKVM. Ange ditt administratörslösenord.

    ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    Nu kan du komma åt KVM-konsolen lokalt och därmed den styrda enheten.

    ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## Lokal åtkomst via IP-adress {#local-access-via-ip-address}

Ta reda på KVM-enhetens IP-adress i det överordnade nätverket (t.ex. i din router) och ange IP-adressen i webbläsaren. Därefter kan du komma åt KVM-enheten lokalt och därmed den styrda enheten.

Vi tar **GL-AXT1800** (routern) och **GL-RM1 Comet** (KVM-enheten) som exempel: Comet är ansluten till LAN-porten på routern GL-AXT1800 med en Ethernet-kabel. Den styrda enheten är korrekt ansluten till Comet med HD-kabel och USB-kabel.

Följ stegen nedan för att komma åt KVM-konsolen.

1. Logga in på webbadministrationspanelen för GL-AXT1800. Routern måste vara konfigurerad för internetåtkomst.

    ![Logga in på routern](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. Gå till **Client** i routerns administrationspanel och leta upp Comets IP-adress i klientlistan. Som bilden nedan visar är Comets IP-adress **192.168.8.197**.

    ![Hitta GLKVM:s IP-adress](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. Öppna en ny flik i webbläsaren och ange Comets IP-adress **192.168.8.197** i adressfältet.

    Du kommer till inloggningssidan för GLKVM. Ange ditt administratörslösenord.

    ![Lokal åtkomst via IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    Nu kan du komma åt KVM-konsolen lokalt och därmed den styrda enheten.

    ![Lokal åtkomst via IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
