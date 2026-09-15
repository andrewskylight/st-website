# Raymarine Evolution ACU-400 — Troubleshooting Guide / Guía de solución de problemas

**Languages / Idiomas:** [English](#english) · [Español](#español)

> Based on the Raymarine Evolution EV-1 / ACU installation instructions (doc. 87180) and field reports from boat owners. Always check the latest manual at www.raymarine.com.
>
> Basado en las instrucciones de instalación Raymarine Evolution EV-1 / ACU (doc. 87180) y en experiencias de propietarios. Consulta siempre el manual más reciente en www.raymarine.com.

---

<a name="english"></a>
# English

Most ACU-400 problems come down to power, SeaTalkNG wiring, or the drive and steering hardware, rather than a failed unit. Work through the sections in order.

## 1. Power and fuses

1. **Check the fuses.** The ACU uses standard automotive blade fuses. Spares are stored on the underside of the removable cover.
   - Main power fuse: **40 A**
   - SeaTalkNG fuse: **3 A**
   - Also check the breaker at your distribution panel.
2. **Measure voltage under load.** Measure at the ACU power terminals while someone commands a hard-over turn. A battery can read 12.6 V at rest and still sag badly when a Type 2 or 3 pump starts.
   - Undersized cable reduces power to the drive and causes malfunctions. If in doubt, use a heavier gauge.
   - Cable length counts as power run + drive run combined. Example: Type 3 drive on 12 V is limited to 0–5 m total with 10 mm² (8 AWG).
3. **Inspect terminals.** Look for loose or corroded screw terminals, especially the pluggable blocks. A loose negative wire in the connector is a known cause of "No Drive Detected".
4. **Check grounding.** The drain (screen) wire should go to the boat's RF ground point, or directly to the negative battery terminal if there is no RF ground system.
5. **Use a separate battery.** Raymarine recommends powering the system from a battery other than the engine-start battery, to avoid erratic behavior during cranking.

## 2. Status LEDs

- **ACU-400:** the LED is under the connector cover. Its specific flash codes are in section 6.5 of the current Evolution installation manual.
- **EV-1 heading sensor:**

| LED pattern | Meaning | Action |
|---|---|---|
| Solid green | Normal operation | None |
| 1 long green flash, repeats every 2 s | Initializing (normally under 1 minute) | Wait |
| 2 short red flashes, repeats every 4 s | No SeaTalkNG connection | Check network power, cables and connectors |
| 7 short red flashes, repeats every 9 s | Connected but not receiving data | Contact Raymarine support if it persists |

## 3. "No Pilot", "No Drive Detected" and communication faults

"No IPS (No Drive Detected)" means the EV-1 and ACU have lost communication.

1. **Check the SeaTalkNG power switch on the ACU.**
   - **ON:** the ACU powers the backbone. No other power feed may be connected.
   - **OFF:** the backbone needs its own separate power feed.
   - Two power sources, or none, is a common installation mistake.
2. **Check the backbone.**
   - Exactly two terminators, one at each end.
   - The power insertion point should sit near the middle of the network load.
3. **Check the heading source.** If the MFD shows depth and other data but no heading source, suspect the EV-1 or its spur cable. For "No Compass", unplug and reconnect the EV-1's SeaTalkNG cable to power cycle it.
4. **24 V boats:** SeaTalkNG supply and clutch share an 8 A limit at 12 V. A 4 A clutch leaves only 4 A for the network.

## 4. Drive and steering alarms

| Alarm | Likely causes | What to check |
|---|---|---|
| **DRIVE STOPPED** | No steering movement within 20 s of a command; excessive helm load; rudder limits exceeded; reset from bad wiring | Drive output voltage, connections at both ends, drive not stalled, steering system secure |
| **CURRENT OVERLOAD** | Short circuit, jammed or faulty drive/motor, steering lock-up | Disconnect drive and turn wheel by hand to feel for binding; on hydraulics check for leaks, low fluid, air in lines |
| **STALL DETECTED** | Faulty drive, steering fault, hard-over time set too slow | Drive operation, hard-over time setting |
| **CLUTCH OVERLOAD** | Clutch draws more current than the ACU supplies (max 4 A) | Clutch rating; clutch voltage switch setting (Raymarine 12 V and 24 V drives all use a **12 V clutch**) |
| **MOTOR POWER SWAPPED** | Motor and power cables on each other's terminals | Power off and swap them back |

## 5. Rudder reference

- **NO RUDDER REFERENCE:** sensor not detected, or it has moved outside its 50° operating range. Check linkage, mounting and wiring.
- **ACU-400 terminal order:** grey (screen), red, green, blue.
- **AUTO RELEASE** can also indicate a rudder reference fault.

## 6. Random resets or shutdowns

1. **"Unexpected Hardware Reset":** an external event (sleep switch, faulty wiring) power-cycled the components. Inspect all power wiring. A drive pulling the voltage down while it runs is a classic cause.
2. **Unit dies after running and recovers later:** likely overheating of an internal component. Usually requires Raymarine service.
3. **Sleep switch:** it disables the pilot while keeping SeaTalkNG powered. A faulty switch can look like a dead pilot even though displays work.

## 7. Good habits

- Update software on the p70/p70R, EV-1 and ACU through your Raymarine MFD.
- Re-run the dockside commissioning wizard after any repair, drive swap or rudder sensor adjustment.
- Keep autopilot cables at least 1 m from VHF radios, their cables and antennas, and about 2 m from SSB radios.
- The ACU-400 is only drip resistant. Never pressure-wash near it, and inspect inside for corrosion or water.

## 8. When to call for help

The ACU itself may be faulty if the problem persists even though:

- voltage at the terminals is correct under load,
- the network is correctly powered and terminated, and
- the drive runs when tested on its own.

The unit has no user-serviceable parts. Before contacting Raymarine support or a certified dealer, have ready: product name, product ID, serial number, software version, and a system diagram.

---

<a name="español"></a>
# Español

La mayoría de los fallos del ACU-400 se deben a la alimentación, al cableado SeaTalkNG o al sistema de gobierno, más que a una avería de la unidad. Sigue las secciones en orden.

## 1. Alimentación y fusibles

1. **Revisa los fusibles.** El ACU usa fusibles de cuchilla estándar de automoción. Hay repuestos en la parte inferior de la tapa desmontable.
   - Fusible de alimentación principal: **40 A**
   - Fusible SeaTalkNG: **3 A**
   - Comprueba también el disyuntor del cuadro de distribución.
2. **Mide la tensión con carga.** Mide en los bornes de alimentación del ACU mientras alguien ordena un giro de banda a banda. Una batería puede marcar 12,6 V en reposo y caer mucho cuando arranca una bomba Tipo 2 o 3.
   - Un cable de sección insuficiente reduce la potencia a la unidad motriz y provoca fallos. En caso de duda, usa un calibre mayor.
   - La longitud que cuenta es la suma del tramo de alimentación y el tramo hasta la unidad motriz. Ejemplo: una unidad Tipo 3 a 12 V admite como máximo 5 m en total con cable de 10 mm² (8 AWG).
3. **Inspecciona los bornes.** Busca bornes flojos o corroídos, sobre todo en los bloques enchufables. Un cable negativo suelto en el conector es una causa conocida de "No Drive Detected".
4. **Comprueba la toma de tierra.** El cable de drenaje (pantalla) debe ir al punto de tierra RF del barco o, si no existe, directamente al borne negativo de la batería.
5. **Usa una batería independiente.** Raymarine recomienda alimentar el sistema desde una batería distinta a la de arranque, para evitar un comportamiento errático al arrancar el motor.

## 2. LED de estado

- **ACU-400:** el LED está debajo de la tapa de conexiones. Sus códigos de parpadeo específicos están en la sección 6.5 del manual de instalación Evolution actual.
- **Sensor de rumbo EV-1:**

| Patrón del LED | Significado | Acción |
|---|---|---|
| Verde fijo | Funcionamiento normal | Ninguna |
| 1 destello verde largo, se repite cada 2 s | Inicializando (normalmente menos de 1 minuto) | Esperar |
| 2 destellos rojos cortos, se repite cada 4 s | Sin conexión SeaTalkNG | Revisar alimentación, cables y conectores de la red |
| 7 destellos rojos cortos, se repite cada 9 s | Conectado pero sin recibir datos | Contactar con Raymarine si persiste |

## 3. "No Pilot", "No Drive Detected" y fallos de comunicación

"No IPS (No Drive Detected)" indica que el EV-1 y el ACU han perdido la comunicación.

1. **Comprueba el interruptor de alimentación SeaTalkNG del ACU.**
   - **ON:** el ACU alimenta la troncal. No debe haber ninguna otra alimentación conectada.
   - **OFF:** la troncal necesita su propia alimentación.
   - Tener dos fuentes de alimentación, o ninguna, es un error de instalación frecuente.
2. **Revisa la troncal.**
   - Exactamente dos terminadores, uno en cada extremo.
   - El punto de alimentación debe estar aproximadamente en el centro de la carga de la red.
3. **Comprueba la fuente de rumbo.** Si el MFD muestra la profundidad y otros datos pero no hay fuente de rumbo, sospecha del EV-1 o de su cable de derivación. Para "No Compass", desconecta y vuelve a conectar el cable SeaTalkNG del EV-1 para reiniciarlo.
4. **Barcos de 24 V:** la alimentación SeaTalkNG y el embrague comparten un límite de 8 A a 12 V. Un embrague de 4 A deja solo 4 A para la red.

## 4. Alarmas de la unidad motriz y el gobierno

| Alarma | Causas probables | Qué revisar |
|---|---|---|
| **DRIVE STOPPED** | El timón no se mueve en 20 s tras una orden; carga excesiva; límites del timón superados; reinicio por cableado defectuoso | Tensión de salida, conexiones en ambos extremos, unidad no bloqueada, gobierno bien sujeto |
| **CURRENT OVERLOAD** | Cortocircuito, unidad motriz o motor atascado o averiado, gobierno bloqueado | Desconectar la unidad y girar el timón a mano; en hidráulicos, buscar fugas, nivel bajo de aceite o aire |
| **STALL DETECTED** | Unidad defectuosa, fallo del gobierno, tiempo de banda a banda demasiado lento | Funcionamiento de la unidad, ajuste del tiempo de banda a banda |
| **CLUTCH OVERLOAD** | El embrague consume más de lo que suministra el ACU (máx. 4 A) | Consumo del embrague; posición del selector de tensión (las unidades Raymarine de 12 V y 24 V llevan **embrague de 12 V**) |
| **MOTOR POWER SWAPPED** | Cables del motor y de alimentación intercambiados | Desconectar la alimentación e intercambiarlos |

## 5. Sensor de referencia del timón

- **NO RUDDER REFERENCE:** no se detecta el sensor o ha salido de su rango de 50°. Revisa la varilla de unión, el montaje y el cableado.
- **Orden de bornes en el ACU-400:** gris (pantalla), rojo, verde, azul.
- **AUTO RELEASE** también puede indicar un fallo del sensor de referencia del timón.

## 6. Reinicios o apagados aleatorios

1. **"Unexpected Hardware Reset":** un evento externo (interruptor de reposo, cableado defectuoso) ha reiniciado los componentes. Revisa todo el cableado de alimentación. Una unidad motriz que hace caer la tensión mientras funciona es una causa típica.
2. **La unidad se apaga tras un rato y vuelve más tarde:** probable sobrecalentamiento de un componente interno. Normalmente requiere el servicio técnico de Raymarine.
3. **Interruptor de reposo:** desactiva el piloto sin cortar la alimentación a SeaTalkNG. Un interruptor defectuoso puede parecer un piloto averiado aunque las pantallas funcionen.

## 7. Buenas prácticas

- Actualiza el software del p70/p70R, el EV-1 y el ACU desde tu MFD Raymarine.
- Repite el asistente de configuración en puerto después de cualquier reparación, cambio de unidad motriz o ajuste del sensor del timón.
- Mantén los cables del piloto a al menos 1 m de radios VHF, sus cables y antenas, y a unos 2 m de radios BLU (SSB).
- El ACU-400 solo es resistente al goteo. No lo laves a presión y revisa el interior en busca de corrosión o agua.

## 8. Cuándo pedir ayuda

Puede que el ACU esté averiado si el fallo continúa aunque:

- la tensión en los bornes es correcta con carga,
- la red está bien alimentada y terminada, y
- la unidad motriz funciona cuando se prueba por separado.

La unidad no tiene piezas reparables por el usuario. Antes de contactar con el soporte de Raymarine o un distribuidor autorizado, ten a mano: nombre del producto, identificación, número de serie, versión de software y un esquema del sistema.

---

## Sources / Fuentes

- Raymarine Evolution EV-1, ACU-100/200/300/400 Installation Instructions (87180): https://ca.binnacle.com/pdf/Evolution%20EV-1%20and%20ACU%20Installation%20Instructions.pdf
- Trawler Forum — ACU400 communication problem: https://www.trawlerforum.com/threads/raymarine-experts-acu400-comm-problem.75747/
- Trawler Forum — Raymarine autopilot issue: https://www.trawlerforum.com/threads/raymarine-autopilot-issue.56640/
- Raymarine support: https://www.raymarine.com
