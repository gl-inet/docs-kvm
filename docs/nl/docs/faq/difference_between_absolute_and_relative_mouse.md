# Wat is het verschil tussen de absolute en de relatieve muismodus? {#what-is-the-difference-between-absolute-mouse-and-relative-mouse}

Bij de GL.iNet KVM biedt **Mouse Mode** in de console twee opties: **Absolute** en **Relative**. Deze twee modi verschillen sterk in muisgedrag, toepassingsgebieden en gebruikservaring. Hieronder worden ze toegelicht, zodat u de modus kunt kiezen die het best bij uw situatie past.

![Muismodus](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/mouse_mode.jpg){class="glboxshadow"}

## Absolute muismodus {#absolute-mouse}

De absolute muismodus is bedoeld voor naadloze, gesynchroniseerde muisbesturing tussen de lokale computer en het doelapparaat. In deze modus worden de muisaanwijzers op de lokale computer en op het doelapparaat aan hetzelfde coördinatensysteem gekoppeld. U kunt de lokale muisaanwijzer soepel en naadloos over de KVM-console en het externe scherm bewegen; de externe aanwijzer volgt de beweging van de lokale aanwijzer in realtime.

Tijdens het gebruik kan een kleine vertraging optreden. Dit is normaal en wordt veroorzaakt door de netwerkoverdracht en de videocodering. Door deze vertraging loopt de externe aanwijzer iets achter op de lokale aanwijzer, maar dit heeft geen invloed op de algehele soepelheid van de bediening.

![Absoluut](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/absolute.gif)

## Relatieve muismodus {#relative-mouse}

Anders dan bij de absolute muismodus worden de coördinaten van de lokale en de externe muisaanwijzer in de relatieve muismodus niet gesynchroniseerd; ze werken in afzonderlijke lagen. Voordat u het doelapparaat kunt bedienen, moet u eerst in het externe venster klikken om de aanwijzerfocus te krijgen.

In deze modus is de externe aanwijzer "opgesloten" in het externe venster en kan deze niet soepel over de rand naar uw lokale bureaublad bewegen. De randen van het externe venster werken als barrière en houden de aanwijzer binnen de bestuurde omgeving. Druk op de toets `Esc` om de aanwijzer vrij te geven en weer controle te krijgen over uw lokale computer.

![Relatief](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative.gif)

In de relatieve modus kunt u **Relative Sensitivity** aanpassen, met een bereik van 0,1 tot 2,0.

![Relatieve gevoeligheid](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative_sensitivity.jpg){class="glboxshadow"}

## Belangrijkste verschillen {#key-differences}

| Kenmerken            | Absolute muismodus             | Relatieve muismodus            |
| -------------------- | ------------------------------ | -----------------------------  |
| Coördinatie van de aanwijzer | Lokale en externe aanwijzer zijn gesynchroniseerd (zelfde coördinatensysteem) | Lokale en externe aanwijzer werken in afzonderlijke lagen (geen synchronisatie van coördinaten) |
| Bediening            | Geen klik nodig om de focus te krijgen; naadloze beweging over schermen heen | U moet op het externe scherm klikken om de focus te krijgen; geen naadloze beweging over schermen heen |
| Vertraging           | Lichte vertraging (netwerk/videocodering) | Vrijwel geen vertraging (alleen bewegingsstappen worden verzonden) |
| Toepassingen         | Soepele bediening van meerdere schermen, vaak wisselen, nauwkeurige positionering (werken op afstand, grafisch ontwerp) | Oudere apparaten/BIOS/UEFI die de absolute muismodus niet ondersteunen; onbedoelde klikken voorkomen; onstabiele netwerken (lagere latentie) |

## Samenvatting {#summary}

De absolute muismodus staat voor een soepele, geïntegreerde bedieningservaring, terwijl de relatieve muismodus de nadruk legt op compatibiliteit en stabiliteit.

Voor de meeste dagelijkse situaties waarin u de GL.iNet KVM op afstand bedient, is de absolute muismodus de aanbevolen standaardoptie. Kies de relatieve muismodus bij compatibiliteitsproblemen of speciale bedieningsbehoeften.

- Gebruik de **absolute muismodus** voor soepele dagelijkse bediening op afstand.
- Gebruik de **relatieve muismodus** voor toegang tot het BIOS, voor oudere apparaten die geen absolute positionering ondersteunen of om onbedoelde klikken te voorkomen.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
