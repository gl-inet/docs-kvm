# Was ist die WAN Network Detection and Failover-Logik von Comet 5G

1. Das System verwendet pingbasierte Erkennung, sendet alle **3 Sekunden** Prüfungen an alle Schnittstellen und bewertet alle **9 Sekunden** die Bedingungen für ein Failover.

2. Wenn innerhalb eines Zeitraums von **9 Sekunden** alle Ping-Tests zur Schnittstelle mit höherer Priorität fehlschlagen, während die Schnittstelle mit niedrigerer Priorität erreichbar bleibt, wird nach diesem Zeitraum ein Failover ausgelöst. Wenn alle Schnittstellen nicht erreichbar sind, erfolgt kein Failover.

3. Als offline markierte Schnittstellen erhalten weiterhin Ping-Prüfungen im Hintergrund.

4. Wiederherstellung: Wenn die Schnittstelle mit höherer Priorität innerhalb von **9 Sekunden** wieder per Ping erreichbar ist, schaltet das System nach diesem Zeitraum zu ihr zurück.
