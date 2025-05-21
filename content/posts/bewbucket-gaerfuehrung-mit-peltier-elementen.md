---
title: "Meine BewBucket Gärführung mit Peltier Elementen"
date: 2017-05-22
tags: ["brau-gerätschaft"]
---

Mein Wunsch nach temperaturgesteuerter Gärführung für meinem [SS Brewtech Brewbucket](https://www.ssbrewtech.com/collections/fermenters/products/the-brewmaster-bucket) führte zu folgender Lösung:

Ich habe eine Aluminium Flachstange [ebay](http://www.ebay.de/itm/Aluminium-Flachstange-130x25mm-Lange-wahlbar-Alu-Flachmaterial-AlCuMgPb-Flach-/182399412276?var=&amp;hash=item2a77da2834:m:mfndqO9nZPhZocdnEi-O_sw) exakt auf die Oberfläche des BrewBuckets fräsen lassen (thanks Steve!), um eine plane Oberfläche für die Montage der [Peltier-Elemente](http://www.ebay.de/itm/2Stk-TEC1-12705-12708-12709-12712-12715-12V-Peltierelement-Modul-Peltier-Element-/272552329154?var=&amp;hash=item3f75627fc2) (12709, 90W) zu haben, welche mit [CPU-Kühlern mit Lüftern](http://www.ebay.de/itm/Turbo-Cooler-CPU-Prozessor-Kuhler-Lufter-PC-Rechner-Computer-/222400810720?hash=item33c81f0ee0:g:iN4AAOSw4shYBGOp) gekühlt werden.

![Achtung Fräs-Betrieb!](/images/fraes.jpg)
Achtung Fräs-Betrieb!

![Aufgeschraubt](/images/proto1jpg.jpg)
Aufgeschraubt

Die geformte Alu-Platte wird am BrewBucket befestigt, indem unten am Gefäß ein Wulst aus "UHU Repair All powerkitt" geformt wurde, auf dem die Platte aufstehen kann. Dann wird das Ganze mit Spanngurten befestigt.

![Wulst unter der Alu-Platte und Spanngurt](/images/wulst.jpg)
Wulst unter der Alu-Platte und Spanngurt

![Aufbau fertig](/images/montiert.jpg)
Aufbau fertig

Um den Temperaturübergang zwischen Bucket und Alu-Block zu verbessern, aber kein Geschmiere mit Wärmeleitpaste zu haben, benutze ich einfach Alufolie.

Für die elektrische Seite habe ich den entsprechenden STC-1000 bei AliExpress bestellt und auf [alternative Firmware](https://github.com/matsstaff/stc1000p) umgeflasht, um automatisch Temperatur-Rampen steuern zu können. Diesen habe ich dann zusammen mit dem [Netzteil (12V 20A)](http://www.ebay.de/itm/DC-12V-24V-5A-8-5A-10A-15A-20A-25A-30A-Trafo-Netzteil-Driver-LED-Streifen-Lampen-/252408420730?var=&amp;hash=item3ac4b6d97a:m:mJ2pI_KlgrtPRHfBzl9JCHw") mit Schalter, Steckern, etc. in einen Werkzeugkoffer eingebaut.

![Kühlung in Betrieb!](/images/fertig.jpg)
Kühlung in Betrieb!

Eigenschaften:

- elektrisch
- raumsparend
- wenig Änderungen am BrewBucket
- abnehmbar zur Reinigung
- günstig

*Kosten ca. 130 EUR + 1 Kiste Selbstgebrautes*

Kühl-Leistung bei 20L und einer Umgebungstemperatur von 20°C:

- von 21°C auf 18°C in 3 Stunden
- von 18°C auf 15°C in 4 Stunden
- gemessene Strom-Leistung 150W; Kühlung läuft bei Zieltemperatur ca. 15-20% der Zeit

Verbesserungsmöglichkeiten:

- Isolierung des Buckets
- temperaturgesteuerte Lüfter, um den Lüfter-Lärm zu reduzieren


