# Was ist der Unterschied zwischen absolutem und relativem Mausmodus

Beim GL.iNet KVM bietet der **Mouse Mode** in der Konsole zwei Optionen: **Absolute** und **Relative**. Diese beiden Modi unterscheiden sich deutlich im Verhalten der Maussteuerung, in den Einsatzszenarien und in der Bedienerfahrung. Die folgenden Erläuterungen helfen Ihnen, den passenden Modus für Ihren Bedarf auszuwählen.

![mouse mode](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/mouse_mode.jpg){class="glboxshadow"}

## Absoluter Mausmodus

Der absolute Mausmodus ist für eine nahtlose und synchronisierte Maussteuerung zwischen lokalem Computer und Zielgerät ausgelegt. Wenn dieser Modus aktiviert ist, werden die Mauszeiger auf dem lokalen Computer und auf dem Zielgerät demselben Koordinatensystem zugeordnet. Sie können den lokalen Mauszeiger flüssig über die KVM-Konsole und den Remote-Bildschirm bewegen. Der Remote-Zeiger folgt der Bewegung des lokalen Zeigers in Echtzeit.

Während der Nutzung kann eine geringe Verzögerung auftreten. Das ist normal und wird durch Netzwerkübertragung und Videocodierung verursacht. Diese Verzögerung lässt den Remote-Zeiger etwas langsamer reagieren als den lokalen Zeiger, beeinträchtigt die grundsätzliche Bedienung aber nicht.

![absolute](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/absolute.gif)

## Relativer Mausmodus

Anders als der absolute Mausmodus synchronisiert der relative Mausmodus die Koordinaten des lokalen und des entfernten Mauszeigers nicht; beide arbeiten in getrennten Ebenen. Bevor Sie das Zielgerät steuern können, müssen Sie zuerst in das Remote-Fenster klicken, um den Zeigerfokus zu erfassen.

In diesem Modus ist der Remote-Zeiger auf das Remote-Fenster beschränkt und kann nicht fließend über dessen Rand auf Ihren lokalen Desktop bewegt werden. Die Ränder des Remote-Fensters wirken als Begrenzung und halten den Zeiger innerhalb der gesteuerten Umgebung. Um den Zeiger freizugeben und wieder die Kontrolle über Ihren lokalen Computer zu erhalten, drücken Sie einfach die Taste `Esc`.

![relative](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative.gif)

Im relativen Modus können Sie die **Relative Sensitivity** im Bereich von 0.1 bis 2.0 anpassen.

![relative sensitivity](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative_sensitivity.jpg){class="glboxshadow"}

## Wichtige Unterschiede

| Funktionen           | Absolute Mouse                 | Relative Mouse                 |
| -------------------- | ------------------------------ | -----------------------------  |
| Zeigerkoordination   | Lokaler und entfernter Zeiger sind synchronisiert (gleiches Koordinatensystem) | Lokaler und entfernter Zeiger befinden sich in getrennten Ebenen (keine Koordinatensynchronisierung) |
| Bedienung            | Kein Klick zum Erfassen des Fokus erforderlich; nahtlose Bewegung über Bildschirmgrenzen hinweg | Remote-Bildschirm muss angeklickt werden, um den Fokus zu erhalten; keine nahtlose Bewegung über Bildschirmgrenzen hinweg |
| Verzögerung          | Geringe Verzögerung (Netzwerk/Videocodierung) | Nahezu keine Verzögerung (sendet nur Bewegungsinkremente) |
| Einsatzszenarien     | Flüssige Multi-Screen-Steuerung, häufiges Wechseln, präzise Positionierung (Remote-Arbeit, Grafikdesign) | Ältere Geräte / BIOS / UEFI ohne Unterstützung für Absolute Mouse; Vermeidung versehentlicher Klicks; instabile Netzwerke (geringere Latenz) |

## Zusammenfassung

Absolute Mouse priorisiert eine flüssige und integrierte Steuerung, während Relative Mouse auf Kompatibilität und Stabilität ausgelegt ist.

Für die meisten alltäglichen Fernsteuerungsszenarien mit GL.iNet KVM ist Absolute Mode die empfohlene Standardeinstellung. Relative Mode kann gewählt werden, wenn Kompatibilitätsprobleme auftreten oder besondere Bedienanforderungen bestehen.

- Verwenden Sie **Absolute Mouse** für eine flüssige tägliche Fernsteuerung.
- Verwenden Sie **Relative Mouse** für BIOS-Zugriff, ältere Geräte ohne Unterstützung für absolute Positionierung oder zur Vermeidung versehentlicher Klicks.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
