# Vad gör jag om tangentbordet inte matar in eller ut tecken som förväntat? {#what-shoud-i-do-if-keyboard-does-not-input-or-output-as-expected}

Om den styrande och den styrda enheten använder **olika inmatningsmetoder eller tangentbordslayouter** kan symboler och tecken som "!", "@" och "#" som du skriver lokalt visas felaktigt på fjärrsidan.

## Varför händer detta? {#why-does-it-happen}

KVM-enheten uppfattas som ett tangentbord av den styrda enheten. De tangenter som du trycker på på den styrande enhetens tangentbord överförs till KVM-enheten utifrån tangenternas positioner och mappas sedan till den styrda enheten.

Om inmatningsmetoden/tangentbordet på den styrande enheten inte överensstämmer med den styrda enhetens har vissa symboler/bokstäver olika positioner på tangentbordet. Det gör att tecknen som den styrda sidan matar ut inte stämmer överens med det som matas in på den styrande sidan.

![Jämförelse mellan amerikanskt tangentbord och JIS-tangentbord](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow"}

## Lösningar {#solutions}

Du kan installera en inmatningsmetod eller ett tangentbord för motsvarande språk på den styrda enheten för att få en konsekvent tangentmappning.

??? "Windows"

    1. Gå till **Settings** -> **Time & Language** -> **Language** -> **Preferred Language**. Klicka på **Add a language**.

        ![Lägg till ett språk](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. Välj ett språk att installera.

        ![Välj ett språk](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "MacOS"

    1. Välj **Apple menu** > **System Settings** på din Mac och klicka sedan på **Keyboard** i sidofältet. (Du kan behöva rulla nedåt.)

    2. Gå till **Text Input** och klicka sedan på **Edit**.

    3. Klicka på knappen **Add** och sök sedan efter ett språk. Välj en eller flera inmatningskällor för varje språk som du vill använda och klicka sedan på **Add**.

    4. Om du vill börja skriva på ett annat språk väljer du språket i inmatningsmenyn i menyraden.

        Du kan klicka på **Show Keyboard Viewer** i inmatningsmenyn för att se tangentbordslayouten för det språk som är valt.

        När du har lagt till en inmatningskälla visas inmatningsmenyn automatiskt i menyraden. Inmatningskällans språk läggs automatiskt till i listan över önskade språk i inställningarna för språk och region, och i listan över dikteringsspråk (om sådan finns) i tangentbordsinställningarna.

    Referenser: [Write in another language on Mac – Apple Support](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
