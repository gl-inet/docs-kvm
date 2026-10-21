# Vad gör jag om det inte kommer något ljud från den styrda enheten? {#what-should-i-do-if-theres-no-audio-from-the-controlled-device}

Om du inte hör något ljud från den styrda enheten efter att du har anslutit KVM-enheten och den styrda enheten (t.ex. inget ljud när du spelar upp video på enheten) kan du prova följande felsökningstips:

1. Kontrollera att högtalaren är aktiverad i KVM-konsolen.

    Gå till **Settings** -> **Remote Device Settings** -> **Speaker** i KVM-konsolen och kontrollera att högtalaren är aktiverad. Kontrollera samtidigt att ikonen i det nedre högra hörnet lyser (vilket anger att den är aktiv).

    ![Högtalare](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/speaker.png){class="glboxshadow"}

2. Kontrollera att alla kablar mellan KVM-enheten och den styrda enheten är ordentligt anslutna. Lösa kablar kan påverka ljudutgången.

3. Kontrollera om en HDMI-omvandlare är ansluten. Vissa omvandlare stöder inte ljud.

    Vi rekommenderar att du använder HDMI-kabeln som följer med i förpackningen, eftersom vissa HDMI-kablar av äldre standard kanske inte stöder ljudöverföring.

4. Kontrollera om värdenheten och den styrda enheten har ljudet avstängt.

5. Kontrollera utgångsinställningarna på den styrda enheten och se till att utgångsenheten är **GLKVM**.

    ??? "macOS"

        Gå till **Settings** -> **Sound** -> **Output & Input** -> **Output** på den styrda enheten och byt utgångsenhet till **GLKVM**.

        ![Utgångsinställningar i macOS](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        Gå till **Settings** -> **Sound** -> **Output** på den styrda enheten och byt utgångsenhet till **GLKVM**.

        ![Utgångsinställningar i Windows 1](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![Utgångsinställningar i Windows 2](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        Du kan också klicka på ljudikonen i det nedre högra hörnet på den styrda enheten och välja **GLKVM** som uppspelningsenhet.

        ![Utgångsinställningar i Windows 3](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. Kontrollera grafikkortets drivrutin på den styrda enheten. Om den styrda enheten saknar drivrutin för grafikkortet kan den inte mata ut ljud, och då hörs inget ljud på den styrande sidan.

7. Kontrollera de avancerade ljudinställningarna på värdenheten och se till att webbläsaren har en aktiv volymutgång.

    Nedan visas som referens ett exempel på de avancerade ljudinställningarna i Windows 10 Pro.

    Gå till **Settings** -> **Sound** -> **Advanced sound options**.

    ![Avancerade ljudalternativ](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/advanced_sound_options.png){class="glboxshadow"}

    Justera volymen för specifika appar och systemljud.

    ![Appvolym](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/app_volume.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
