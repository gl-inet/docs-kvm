# Användarhandbok för Fingerbot (FGB-01) {#fingerbot-fgb-01-user-guide}

Fingerbot FGB-01 är ett tillbehör till GL.iNet KVM-enheter som gör fjärrhanteringen av strömmen ännu smidigare.

Fingerbot är en fysisk knapptryckare som är utformad för att starta och stänga av målenheten på distans. Den är enkel att fästa med tejp, har en batteritid på ungefär ett år vid daglig användning och kräver ingen komplicerad konfiguration.

**Obs!** Comet Q (GL-RMQ1) fungerar inte med Fingerbot.

![Översikt](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/overview.png){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

![Förpackningens innehåll](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/package_contents.png){class="glboxshadow"}

- 1 x FGB-01
- 1 x Hållare för bärbar dator
- 1 x Tillsats (Add-on)
- 1 x CR2-batteri (monterat i FGB-01)
- 1 x Självhäftande tejp
- 1 x Användarhandbok

Se uppackningsvideon för Fingerbot nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Aeu5yiDEt0Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Installation {#installation}

Se den här videon eller följ stegen nedan för att installera Fingerbot.

<iframe width="560" height="315" src="https://www.youtube.com/embed/_ExhJHhEcwg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Ta bort plastremsan som isolerar batteriet.

    ![Installation 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install1.png){class="glboxshadow"}

2. Öppna locket via skåran upptill på Fingerbot.

    ![Installation 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install2.png){class="glboxshadow"}

3. Ta fram USB-Bluetooth-mottagaren, sätt in den i USB-porten på GL.iNet KVM-enheten (t.ex. Comet GL-RM1) och sätt sedan tillbaka locket på Fingerbot.

    ![Installation 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install3.png){class="glboxshadow"}

    ![Installation 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install4.png){class="glboxshadow"}

4. Rengör ytan på den styrda enhetens strömknapp.

    ![Installation 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install5.png){class="glboxshadow"}

5. Dra av skyddsfilmen från tejpen på undersidan av Fingerbot.

    ![Installation 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install6.png){class="glboxshadow"}

6. Fäst Fingerbot nära den styrda enhetens strömknapp och se till att robotarmen når den fysiska strömknappen när den trycker.

    ![Installation 7](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install7.png){class="glboxshadow"}

7. Om den styrda enheten är en bärbar dator fäster du hållaren (medföljer i förpackningen) nära strömknappen och drar åt den.

    Obs! Använd bara hållaren om strömknappen sitter på sidokanten.

    ![Installation 8](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install8.png){class="glboxshadow"}

    Fäst sedan Fingerbot på hållaren och se till att robotarmen når den fysiska strömknappen när den trycker.

    ![Installation 9](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install9.png){class="glboxshadow"}

8. Installationen är klar. Som bilden nedan visar trycker Fingerbots robotarm på strömknappen, vilket gör det möjligt att fjärrstyra strömförsörjningen.

    ![Installation 10](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install10.jpg){class="glboxshadow"}

## Konfiguration {#setup}

1. Logga in på GL.iNet KVM-konsolen.

2. Gå till **Accessories** i KVM-konsolen. Du kan uppnå olika effekter genom att justera tryckets längd och styrka.

    ![Tillbehör](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/accessories.jpg){class="glboxshadow"}

    **Obs!** Tillbehörsinställningarna visas först efter installationen.

    - Time: hur länge Fingerbot trycker.

    - Strength: två nivåer av tryckstyrka finns, Light Press-läge och Hard Press-läge.

        - Light Press-läge: perfekt för korta eller lättryckta knappar.

        - Hard Press-läge: idealiskt för djupa eller tröga knappar.

        ![Tryckläge](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow"}

        Du kan också använda **testknappen** (inuti Fingerbot, synlig när du har tagit bort det övre locket) för att hitta den trycknivå du föredrar:

        ![Testknapp](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/test-button.png){class="glboxshadow"}

        1. Första trycket: Fingerbot fälls ut till Light Press.

        2. Andra trycket: Fingerbot fälls ut till Hard Press.

        3. Tredje trycket: Fingerbot dras tillbaka.

## Vanliga frågor {#faq}

**F1. Vilket protokoll använder USB-mottagaren till GL-Fingerbot?**

S1. Den använder Bluetooth-protokollet.

---

**F2. Är själva Fingerbot parkopplad med USB-Bluetooth-mottagaren? Kan jag använda en annan mottagare om jag tappar bort min?**

S2. Fingerbot och dess USB-Bluetooth-mottagare är unikt parkopplade. Andra mottagare kan inte användas med Fingerbot på grund av denna koppling.

---

**F3. Är GL-Fingerbot kompatibel med KVM-enheter som inte kommer från GL.iNet?**

S3. Nej. GL-Fingerbot är ett valfritt tillbehör till GL.iNet KVM-enheter och ska användas tillsammans med en GL.iNet KVM.

---

**F4. Kan jag använda en enda GL.iNet KVM för att styra flera Fingerbot?**

S4. Följande GL.iNet KVM-enheter kan bara styra en Fingerbot.

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)

Comet X (GL-RM4PE) stöder däremot upp till fyra Fingerbot samtidigt. Comet X har fyra oberoende kanaler på baksidan. Varje kanal har en HDMI-port för överföring av videosignal, en Type-C-port för överföring av tangentbords- och mussignaler och en USB 2.0-port för USB-kringutrustning (t.ex. Fingerbot eller ATX-kort).

**Obs!** Comet Q (GL-RMQ1) fungerar inte med Fingerbot.

---

**F5. Vad är tillsatsen (Add-on) till för, och hur används den?**

S5. Tillsatsen är avsedd för att styra vanliga strömbrytare, till exempel en ljusströmbrytare. Fingerbots finger riktas mot ena sidan av brytaren medan tillsatsen fästs på den andra sidan. När Fingerbot trycker ned slår den på brytaren, och när den drar tillbaka slår den av brytaren.

Fingerbot kan dock för närvarande bara användas med en GL.iNet KVM-enhet. Ta fram USB-Bluetooth-mottagaren inuti Fingerbot och sätt in den i USB-porten på GL.iNet KVM-enheten, så kan du fjärrstyra Fingerbot via en GL.iNet KVM.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
