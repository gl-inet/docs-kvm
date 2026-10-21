# Vad är skillnaden mellan absolut och relativt musläge? {#what-is-the-difference-between-absolute-mouse-and-relative-mouse}

För GL.iNet KVM har **Mouse Mode** i konsolen två alternativ: **Absolute** och **Relative**. De två lägena skiljer sig avsevärt när det gäller musstyrningens beteende, användningsområden och användarupplevelse. Skillnaderna beskrivs nedan för att hjälpa dig att välja rätt läge utifrån dina behov.

![Musläge](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/mouse_mode.jpg){class="glboxshadow"}

## Absolut musläge {#absolute-mouse}

Absolut läge är utformat för sömlös och synkroniserad musstyrning mellan den lokala datorn och målenheten. När läget är aktiverat mappas muspekarna på både den lokala datorn och målenheten till samma koordinatsystem. Du kan flytta den lokala muspekaren smidigt och sömlöst mellan KVM-konsolen och fjärrskärmen – fjärrpekaren följer den lokala pekarens rörelser i realtid.

En liten fördröjning kan uppstå vid användning. Det är normalt och beror på nätverksöverföringen och videokodningen. Fördröjningen gör att fjärrpekaren rör sig något långsammare än den lokala, men påverkar inte den övergripande smidigheten.

![Absolut läge](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/absolute.gif)

## Relativt musläge {#relative-mouse}

Till skillnad från absolut läge synkroniserar relativt läge inte koordinaterna för den lokala och den fjärranslutna muspekaren, utan de arbetar i separata lager. Innan du kan styra målenheten måste du först klicka i fjärrfönstret så att det får pekarfokus.

I det här läget är fjärrpekaren "instängd" i fjärrfönstret och kan inte röra sig smidigt över gränsen till ditt lokala skrivbord. Fjärrfönstrets kanter fungerar som en barriär som håller kvar pekaren i den styrda miljön. Tryck på `Esc` för att släppa pekaren och återfå kontrollen över den lokala datorn.

![Relativt läge](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative.gif)

I relativt läge kan du justera **Relative Sensitivity**, som kan ställas in mellan 0,1 och 2,0.

![Relativ känslighet](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative_sensitivity.jpg){class="glboxshadow"}

## Viktiga skillnader {#key-differences}

| Egenskaper           | Absolut musläge                | Relativt musläge               |
| -------------------- | ------------------------------ | -----------------------------  |
| Pekarkoordinering    | Lokal pekare och fjärrpekare är synkroniserade (samma koordinatsystem) | Lokal pekare och fjärrpekare finns i separata lager (ingen koordinatsynkronisering) |
| Styrning             | Inget klick krävs för att få fokus, sömlös förflyttning mellan skärmar | Du måste klicka på fjärrskärmen för att få fokus, ingen sömlös förflyttning mellan skärmar |
| Fördröjning          | Liten fördröjning (nätverk/videokodning) | Nästan ingen fördröjning (skickar bara rörelseförändringar) |
| Användningsområden   | Smidig styrning av flera skärmar, frekventa växlingar, exakt positionering (distansarbete, grafisk design) | Äldre enheter/BIOS/UEFI som inte stöder absolut musläge, undvika oavsiktliga klick, instabila nätverk (lägre latens) |

## Sammanfattning {#summary}

Absolut musläge prioriterar en smidig och integrerad styrupplevelse, medan relativt musläge fokuserar på kompatibilitet och stabilitet.

För de flesta vardagliga fjärrstyrningsscenarier med GL.iNet KVM är absolut läge det rekommenderade standardalternativet. Relativt läge kan väljas vid kompatibilitetsproblem eller särskilda behov.

- Använd **absolut musläge** för smidig daglig fjärrstyrning.
- Använd **relativt musläge** för BIOS-åtkomst, äldre enheter som inte stöder absolut positionering eller för att undvika oavsiktliga klick.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
