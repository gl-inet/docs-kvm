# Wat moet ik doen als de relatieve muismodus niet werkt op een Reolink NVR? {#what-should-i-do-if-relative-mouse-mode-doesnt-work-on-reolink-nvr}

Wanneer u met een GL.iNet KVM een Reolink NVR (vooral modellen die geen twee muizen ondersteunen) of bepaalde oudere computers (zoals computers zonder USB-aansluitingen) bedient, werkt de relatieve muismodus mogelijk niet. Veelvoorkomende problemen zijn dat de modus helemaal niet werkt, of dat de muisbeweging wel wordt gevolgd maar klikken niet reageren.

Dit probleem komt voornamelijk voort uit een compatibiliteitsprobleem tussen de muissimulatie van de KVM en de beperkte mogelijkheden van apparaten zoals de Reolink NVR:

- **Vóór firmware v1.4.0**: de KVM was ontworpen om slechts één muis te simuleren. Voor het wisselen tussen de relatieve en de absolute modus moest u de KVM opnieuw opstarten, maar dit werkte goed met de meeste oudere of gespecialiseerde apparaten.

- **Vanaf firmware v1.4.0**: om zonder herstart naadloos van modus te kunnen wisselen, is de standaardlogica aangepast zodat er twee muizen tegelijk worden gesimuleerd (één voor de relatieve modus en één voor de absolute modus). De Reolink NVR en sommige oudere computers ondersteunen echter geen twee muizen, wat tot twee veelvoorkomende problemen leidt:

    - De relatieve muismodus werkt helemaal niet;
    - De muis wordt nog wel gevolgd, maar klikken reageren niet.

U kunt het probleem oplossen door de relatieve muismodus via de terminal af te dwingen. Volg deze stappen:

1. Open de KVM-console en ga naar **Toolbox** -> **Terminal**. Klik op **Access** om de KVM-terminal te openen.

2. Open het configuratiebestand met de volgende opdracht:

    `vi /etc/kvmd/override.yaml`

3. Voer het volgende in om de relatieve muismodus af te dwingen:

    ```
    kvmd:
        hid:
            mouse:
                absolute: false
    ```

4. Sla het bestand op en sluit de editor af.

5. Start het KVM-apparaat opnieuw op om de wijzigingen toe te passen.

!!! note "Opmerking"

    1. Als de bovenstaande methode niet werkt, probeer dan de firmware van uw KVM terug te zetten naar een versie van vóór v1.4 (indien beschikbaar). Die versie emuleert één muis en is compatibel met oudere apparaten.
    
    2. De zelfstandige GLKVM-app voor macOS ondersteunt de relatieve muismodus niet vanwege beperkingen van de browserkernel (geen ondersteuning voor de requestPointerLock-API). Gebruik in plaats daarvan de webconsole.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
