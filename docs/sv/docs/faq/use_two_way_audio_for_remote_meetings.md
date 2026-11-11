# Så använder du tvåvägsljud i fjärrmöten {#how-can-i-use-two-way-audio-for-remote-meetings}

När du arbetar hemifrån kan du använda KVM för att komma åt din kontorsdator och delta i ljudmöten i Zoom, Microsoft Teams eller en liknande app. Med tvåvägsljud i GL.iNet KVM kan du prata i den lokala datorns mikrofon och höra andra deltagare via datorns högtalare eller hörlurar.

## Snabbinstallation {#quick-setup}

Följ stegen nedan för att använda den lokala enhetens mikrofon och högtalare i fjärrmöten. I exemplet används ett Zoom-möte.

1. Innan du ansluter till mötet loggar du in på din KVM på den styrande datorn och går till **Session** -> **Audio & Camera**. Aktivera **Speaker** och **Microphone**. Kontrollera att båda ikonerna längst ned till höger är aktiva.

    ![Aktivera högtalare och mikrofon](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/enable-speaker-and-microphone.png){class="glboxshadow"}

    När du till exempel aktiverar **Microphone** kan webbläsaren be om åtkomst till mikrofonen. Välj den mikrofon du vill använda och tillåt åtkomst.

    ![Begäran om åtkomst till mikrofonen](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/microphone-permission-popup.png){class="glboxshadow"}

2. Öppna Zoom och anslut till mötet på den styrda datorn. Klicka på pilen bredvid ljudknappen och välj följande enheter, som i exemplet:

    - **Microphone**: Microphone (6-Comet Microphone)

    - **Speaker**: EPSON PJ (HD Audio Driver for Display Audio)

    ![Välja mikrofon och högtalare](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/select-microphone-and-speaker.png){class="glboxshadow"}

    Slå sedan på mikrofonljudet för att prata med de andra deltagarna. Du hör dem via den styrande datorns högtalare eller hörlurar.

    Om du även vill visa deltagarna bilden från den lokala kameran läser du [guiden till kameragenomkoppling](../faq/use_camera_passthrough_for_remote_meetings.md).

## Felsökning {#troubleshooting}

??? note "Vad gör jag om andra deltagare inte hör mig?"

    Gå till **Settings** -> **System** -> **Sound** på den styrda datorn och leta efter KVM-enhetens virtuella mikrofon under **Input**. I exemplet visas den som **Comet Microphone**. Kontrollera att den här mikrofonen också är vald i mötesappen.

    ![Kontrollera ljudingången](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-input.png){class="glboxshadow"}

    - Om den virtuella mikrofonen inte visas kontrollerar du USB-dataanslutningen mellan KVM-enheten och den styrda datorn. Mikrofonljudet överförs till den styrda datorn via den anslutningen.

    - Om den virtuella mikrofonen visas och är vald men inget ljud kommer in, kontrollera att mikrofonljudet är på både på den styrande datorn och i mötesappen på den styrda datorn. Kontrollera mikrofonbehörigheterna i systemet och webbläsaren på den styrande datorn och stäng andra appar eller webbläsarflikar som kan använda mikrofonen.

??? note "Vad gör jag om jag inte hör de andra deltagarna?"

    Gå till **Settings** -> **System** -> **Sound** på den styrda datorn. Leta under **Output** efter HDMI-ljudutgången som är ansluten till KVM-enheten. I exemplet visas den som **EPSON PJ**. Kontrollera att samma enhet är vald som högtalare i mötesappen.

    ![Kontrollera ljudutgången](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-output.png){class="glboxshadow"}

    - Om HDMI-ljudutgången inte visas kontrollerar du HDMI-anslutningen mellan den styrda datorn och KVM-enheten. Den överför ljudet från den styrda datorn. Om du använder en HDMI-adapter kontrollerar du att den stöder ljud.

    - Om HDMI-ljudutgången visas och är vald men du fortfarande inte hör de andra deltagarna, kontrollera att ljudet är på i den styrande datorn, i webbläsarfliken och i högtalarna eller hörlurarna.

    Mer information finns i [Inget ljud från den styrda enheten](../faq/no_audio_from_the_controlled_device.md).

??? note "Vad gör jag om ljudet försvinner efter att sidan har laddats om eller anslutningen har återupprättats?"

    Kontrollera **Speaker** och **Microphone** igen i KVM-konsolen. Webbläsarens säkerhetsregler kan stänga av ljuduppspelningen via högtalarna eller tysta mikrofonen efter att sidan har laddats om eller anslutningen har återupprättats.

    Mer information finns i [Varför sparas inte mina inställningar för högtalare och mikrofon?](../faq/speaker_microphone_settings_cannot_be_retained.md).

??? note "Vad gör jag om meddelandet 'Microphone Access Denied' visas?"

    Kontrollera följande på den styrande datorn:

    - **Systembehörigheter**: Gå till **Settings** -> **Privacy & security** -> **Microphone** i Windows 11. Aktivera **Microphone access**, **Let apps access your microphone** och **Let desktop apps access your microphone**.

    - **Webbläsarbehörigheter**: Tillåt att KVM-webbplatsen får åtkomst till mikrofonen. Om åtkomsten tidigare har blockerats uppdaterar du webbplatsens mikrofonbehörigheter och laddar om sidan.

    - **Mikrofonanvändning**: Stäng andra appar eller webbläsarflikar som kan använda mikrofonen.

    Aktivera **Microphone** igen i KVM-konsolen efter dessa kontroller.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
