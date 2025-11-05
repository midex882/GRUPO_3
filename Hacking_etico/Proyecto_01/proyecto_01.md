# Proyecto 1: Cybersecurity Consulting (redes)

## Grupo 3: Daniel, Abel, Jose

# Índice

[**Descripción	2**](#descripción)

[**Área investigada	2**](#área-investigada)

[**Metodología	2**](#metodología)

[**Investigación de Vulnerabilidades	3**](#investigación-de-vulnerabilidades)

[Fase 1: Estudio de categorías de vulnerabilidades	3](#fase-1:-estudio-de-categorías-de-vulnerabilidades)

[Fase 2: Investigación de CVEs concretos	5](#fase-2:-investigación-de-cves-concretos)[​](#cves-concretos-en-bugs-en-pilas-tcp/ip-embebidas:-cve-2020-11896-—-ripple20/treck-\(ipv4-tunneling\)-vulnerabilidad-en-la-pila-tcp/ip-de-treck-al-procesar-paquetes-ipv4-tunelados-malformados-que-permite-ejecución-remota-de-código-o-dos-en-dispositivos-embebidos-con-ip-tunneling-habilitado.​)

[Fase 3: Clasificación para la empresa	8](#fase-3:-clasificación-para-la-empresa)

[**Contramedidas propuestas	12**](#contramedidas-propuestas)

[**Conclusión	17**](#conclusión)

# Descripción {#descripción}

Nuestra empresa TrustShield Financial nos ha encargado realizar un análisis exhaustivo de su infraestructura de redes. Nuestro objetivo es identificar vulnerabilidades críticas que podrían comprometer la confidencialidad, integridad y disponibilidad de los datos financieros.

# Área investigada {#área-investigada}

Como ya hemos comentado el área que se va a encargar nuestro equipo es la de redes y protocolos de comunicación. La investigación se centrará en las vulnerabilidades dentro de este campo, utilizando fuentes fiables como bases de datos de vulnerabilidades, informes de seguridad y literatura académica.

# Metodología {#metodología}

# Investigación de Vulnerabilidades {#investigación-de-vulnerabilidades}

En este punto trataremos las vulnerabilidades específicas del área de Redes y protocolos de comunicación. La investigación se dividirá en **dos fases:**

## Fase 1: Estudio de categorías de vulnerabilidades {#fase-1:-estudio-de-categorías-de-vulnerabilidades}

(Descripción breve, impacto y explotación) 

### **Bugs en pilas TCP/IP / stacks embebidos:** {#bugs-en-pilas-tcp/ip-/-stacks-embebidos:}

Los bugs en pilas TCP/IP embebidas son fallos en implementaciones de red de bajo nivel presentes en IoT, PLC y routers que pueden permitir ejecución remota de código, entre otros problemas.

* **Impacto:** RCE o DoS en dispositivos IoT/PLC/routers; afecta disponibilidad e integridad.  
* **Explotación típica:** paquetes malformados o secuencias específicas que desencadenan corrupción de memoria.

### **Configuraciones inseguras y credenciales por defecto:** {#configuraciones-inseguras-y-credenciales-por-defecto:}

### Dejar usuarios/contraseñas, puertos o ajustes tal como vienen de fábrica (routers, appliances, aplicaciones, paneles de administración) crea puertas de entrada fáciles porque las credenciales y configuraciones por defecto son conocidas o predecibles.

* ### **Impacto:** Acceso inicial facilitado a dispositivos o servicios, escalada de compromiso y pivoteo dentro de la red (el atacante aprovecha ese acceso para moverse a otros sistemas y elevar privilegios).

* ### **Explotación:** Escaneo de red para encontrar dispositivos/servicios, intento con credenciales conocidas/por defecto, acceso a paneles de administración expuestos y uso de esas cuentas para instalar malware, crear backdoors o obtener credenciales adicionales.

### **Servicios de acceso remoto inseguros (RDP, SSH mal configurado):**  {#servicios-de-acceso-remoto-inseguros-(rdp,-ssh-mal-configurado):}

### Son servicios que permiten controlar un ordenador o servidor desde otro sitio. Si están mal configurados o expuestos públicamente sin protecciones, un atacante puede conectarse y controlar el equipo.

* **Impacto:** Acceso remoto sin control (el atacante puede manejar sistemas), ejecución remota de código (instalar malware, cifrar datos o crear puertas traseras), escalada de privilegios (pasar de usuario normal a administrador)  
* **Explotación:** Ataques por fuerza bruta a contraseñas, uso de credenciales robadas, envío de paquetes o requests maliciosos que aprovechan vulnerabilidades sin parchear (ej. exploits como BlueKeep), o aprovechamiento de configuraciones débiles (autenticación por contraseña, puertos expuestos).

### **Vulnerabilidades en protocolos de compartición de archivos (SMB,NFS)** {#vulnerabilidades-en-protocolos-de-compartición-de-archivos-(smb,nfs)}

Los protocolos de compartición de archivos permiten que distintos equipos dentro de una red compartan archivos, impresoras y otros recursos. Son muy importantes en entornos corporativos, ya que facilitan la colaboración y acceso centralizado a la información. Sin embargo, tienen una alta exposición dentro de las redes y eso les convierte en un objetivo para los atacantes.

* **Impacto:** Acceso no autorizado a archivos compartidos dentro de la red, ataques tipo MITM, ransomware, caída de servidores y propagación automática de malware dentro de la red. Interrupción de servicios críticos, pérdida de datos confidenciales y daños de reputación.  
* **Explotación** El uso de versiones antiguas como SMBv1 o compartir carpetas sin autenticación ni restricciones de IP facilita ataques automáticos que se propagan por toda la red. Ataques “Man-in-the-middle”: un atacante en la misma red puede interceptar comunicaciones, capturar credenciales o manipular los datos en tránsito.

### **Fallos en protocolos de gestión (SNMP, DHCP, DNS)** {#fallos-en-protocolos-de-gestión-(snmp,-dhcp,-dns)}

Los fallos en protocolos de gestión como SNMP, DHCP y DNS exponen redes a captura de información, redirección de tráfico y denegaciones de servicio, especialmente en versiones sin actualizar y servicios sin autenticación fuerte o cifrado.

* **Impacto:** filtrado de información, redirección de tráfico, DoS.  
                     
* **Explotación**: spoofing, poisoning (e.g., DNS cache poisoning), respuestas manipuladas.

### **Protocolos criptográficos mal implementados (TLS/SSL/OpenSSL)** Si TLS/SSL o su librería (como OpenSSL) tienen errores en cómo negocian la conexión segura o validan certificados, un atacante puede colarse en medio, leer datos supuestamente cifrados o hacerse pasar por el servidor/cliente legítimo {#protocolos-criptográficos-mal-implementados-(tls/ssl/openssl)-si-tls/ssl-o-su-librería-(como-openssl)-tienen-errores-en-cómo-negocian-la-conexión-segura-o-validan-certificados,-un-atacante-puede-colarse-en-medio,-leer-datos-supuestamente-cifrados-o-hacerse-pasar-por-el-servidor/cliente-legítimo}

* **Impacto:** interceptación/descifrado de tráfico, suplantación.

* **Explotación:** fallos en handshake, comprobaciones de límites, bugs en librerías como OpenSSL

### **Amplificación y reflexión en UDP (NTP, DNS, SSDP, CLDAP, Memcached)** {#amplificación-y-reflexión-en-udp-(ntp,-dns,-ssdp,-cldap,-memcached)}

Los ataques de amplificación y reflexión en UDP aprovechan servicios que responden con muchos más bytes de los que reciben y la suplantación de IP para que esas respuestas “reboten” contra la víctima, multiplicando el volumen con muy poco esfuerzo del atacante.

* Impacto: DDoS de gran volumen que satura enlaces y derriba servicios  
  .  
* Explotación: envío de pequeñas consultas a servidores abiertos con IP origen falsificada; el servidor responde con grandes paquetes hacia la víctima.

## Fase 2: Investigación de CVEs concretos {#fase-2:-investigación-de-cves-concretos}

### [**CVEs concretos en configuraciones inseguras y credenciales por defecto**](#configuraciones-inseguras-y-credenciales-por-defecto:) {#cves-concretos-en-configuraciones-inseguras-y-credenciales-por-defecto}

**CVE-2024-51978** — Vulnerabilidad en impresoras (Brother y otras) que permite generar la contraseña administrativa por defecto a partir del número de serie, otorgando acceso remoto si no se cambia la credencial

**CVE-2023-43844** — Aten PE6208 (unidad de distribución de energía inteligente, diseñada para el control remoto): cuenta privilegiada del interfaz web con credenciales por defecto que no se obligan a cambiar, permitiendo acceso administrativo si se mantienen. 

**CVE-2024-41690** — SyroTech SY-GPON-1110-WDONT (router): credenciales por defecto almacenadas/en claro en el firmware que pueden permitir acceso no autorizado si se extrae/analiza el binario.

### [**CVEs concretos de servicios de acceso remoto inseguros (RDP, SSH mal configurado)**](#servicios-de-acceso-remoto-inseguros-\(rdp,-ssh-mal-configurado\):) {#cves-concretos-de-servicios-de-acceso-remoto-inseguros-(rdp,-ssh-mal-configurado)}

**CVE-2019-0708 (BlueKeep)** — Vulnerabilidad en Remote Desktop Services que permite ejecución remota de código al enviar peticiones RDP especialmente diseñadas a sistemas sin parchear.

**CVE-2018-15473 (OpenSSH user-enumeration)** — OpenSSH ≤7.7 permitía enumerar usuarios (diferencia de respuesta en el proceso de autenticación), facilitando ataques dirigidos contra cuentas válidas.

**CVE-2021-36368 (OpenSSH agent-forwarding / auth issue)** — Problema en OpenSSH \<8.9 que era un fallo que podría permitir a un atacante autenticarse indebidamente o aprovechar credenciales enviadas si la función de “agent forwarding” estaba activa.

### [**CVEs concretos en protocolos de compartición de archivos (SMB,NFS)**](#vulnerabilidades-en-protocolos-de-compartición-de-archivos-\(smb,nfs\)) {#cves-concretos-en-protocolos-de-compartición-de-archivos-(smb,nfs)}

**CVE-2020-0796 — SMBGhost (SMBv3)** Vulnerabilidad en la implementación de SMBv3 que provoca errores de manejo de memoria al procesar determinadas peticiones. Permite la **ejecución remota de código** en servidores o clientes vulnerables sin autenticación.

**CVE-2017-0144 — EternalBlue (SMBv1)** Vulnerabilidad crítica en SMBv1 que permite la **ejecución remota de código** mediante el envío de paquetes especialmente creados a servidores vulnerables. Fue explotada masivamente por el exploit conocido como EternalBlue.

**CVE-2017-7494 — SambaCry (Samba – Linux/UNIX SMB)** Vulnerabilidad en Samba que permitía a un cliente remoto subir una biblioteca compartida a un recurso y forzar el servidor a cargarla y ejecutarla. 

### [**CVEs concretos de protocolos criptográficos mal implementados (TLS/SSL/OpenSSL)**](#protocolos-criptográficos-mal-implementados-\(tls/ssl/openssl\)-si-tls/ssl-o-su-librería-\(como-openssl\)-tienen-errores-en-cómo-negocian-la-conexión-segura-o-validan-certificados,-un-atacante-puede-colarse-en-medio,-leer-datos-supuestamente-cifrados-o-hacerse-pasar-por-el-servidor/cliente-legítimo) {#cves-concretos-de-protocolos-criptográficos-mal-implementados-(tls/ssl/openssl)}

**CVE-2014-0160 — Hearthbleed (OpenSSL)** Vulnerabilidad crítica en la extensión Heartbeat del protocolo TLS implementado en OpenSSL (versiones 1.0.1 \- 1.0.1f).  
El fallo consiste en una lectura fuera de límites que permite a un atacante remoto obtener fragmentos de la memoria del servidor o cliente sin autenticación. Esto incluye contraseñas, cookies de sesión, claves privadas TLS y más información sensible.

**CVE-2015-4000 — Logjam (TLS, Diffie-Hellman)** Vulnerabilidad en las claves de Diffie-Hellman dentro del protocolo TLS. Permite a un atacante forzar el uso de un grupo criptográfico de 512 bits export-grade, lo que reduce drásticamente la seguridad del canal.

**CVE-2022-0778 — Infinite Loop en OpenSSL (DoS)** Error en el análisis de certificados X.509 en OpenSSL que provoca un bucle infinito al validar curvas elípticas manipuladas.   
Bloquea procesos que dependan de OpenSSL, afectando disponibilidad de servicios TLS.

### [**CVEs concretos en Amplificación y reflexión de UDP**](#amplificación-y-reflexión-en-udp-\(ntp,-dns,-ssdp,-cldap,-memcached\)) {#cves-concretos-en-amplificación-y-reflexión-de-udp}

**CVE-2013-5211 — NTP “monlist” (NTP)** Vulnerabilidad en ntpd previa a 4.2.7p26 donde la función monlist permite respuestas desproporcionadas que, combinadas con IP de origen falsificada, habilitan DDoS por reflexión y amplificación contra la víctima.​

**CVE-2018-1000115 — Memcached UDP amplification (Memcached)** Fallo en Memcached 1.5.5 que permite usar el servicio UDP (11211/UDP) como reflector con altísimo factor de amplificación, causando DDoS masivos; mitigado deshabilitando UDP o actualizando a versiones que lo desactivan por defecto.​

**CVE-2020-8616 — NXNSAttack (BIND DNS)** BIND no limita adecuadamente los “fetches” al procesar referrals manipulados, provocando ráfagas de consultas que actúan como amplificador/reflexor y derivan en DoS, corregido mediante parches que restringen estas solicitudes en cascada.​

### [**CVEs concretos de fallos en protocolos de gestión (SNMP, DHCP, DNS)**](#fallos-en-protocolos-de-gestión-\(snmp,-dhcp,-dns\)) {#cves-concretos-de-fallos-en-protocolos-de-gestión-(snmp,-dhcp,-dns)}

**CVE-2008-1447 — Kaminsky DNS cache poisoning (DNS: insuficiente entropía / ID predecible)** Vulnerabilidad histórica en la forma en que algunos servidores DNS realizaban las respuestas, lo que permitía a un atacante inyectar respuestas DNS falsas en cachés de resolvers recursivos (conocido como “Kaminsky bug”).   
Esta debilidad facilitaba el envenenamiento de la caché DNS y la publicación de registros falsos en resolvers que no implementaban mitigaciones.

**CVE-2024-3661 — “TunnelVision” (DHCP / rutas manipuladas por Option 121\)** Vulnerabilidad descubierta en 2024 que afecta escenarios donde un cliente confía en rutas proporcionadas por servidores DHCP. Un servidor DHCP controlado por un atacante puede inyectar rutas en la tabla de enrutamiento del cliente, provocando que tráfico que debería pasar por un túnel (por ejemplo, VPN) se filtre por interfaz física, lo que rompe la protección esperada por la VPN. Esta clase de fallo se conoce como route injection vía DHCP.

**CVE-2017-6742 — SNMP (Cisco IOS / IOS XE: divulgación/explotación por comunidades por defecto)** Vulnerabilidad en implementaciones SNMP que permitía a un atacante obtener información sensible o ejecutar acciones a través de SNMP cuando los dispositivos exponían servicios SNMP con configuraciones débiles. Este tipo de fallo ha sido explotado por personas interesadas en espionaje y movimiento lateral. Cisco emitió avisos y parches para múltiples versiones afectadas.

### [**CVEs concretos en bugs en pilas TCP/IP embebidas:**](#bugs-en-pilas-tcp/ip-/-stacks-embebidos:) **CVE-2020-11896 — Ripple20/Treck (IPv4 tunneling)** Vulnerabilidad en la pila TCP/IP de Treck al procesar paquetes IPv4 tunelados malformados que permite ejecución remota de código o DoS en dispositivos embebidos con IP tunneling habilitado.​ {#cves-concretos-en-bugs-en-pilas-tcp/ip-embebidas:-cve-2020-11896-—-ripple20/treck-(ipv4-tunneling)-vulnerabilidad-en-la-pila-tcp/ip-de-treck-al-procesar-paquetes-ipv4-tunelados-malformados-que-permite-ejecución-remota-de-código-o-dos-en-dispositivos-embebidos-con-ip-tunneling-habilitado.​}

**CVE-2019-12255 — URGENT/11 (VxWorks IPnet)** Error de entero por “TCP Urgent Pointer \= 0” en IPnet que posibilita RCE al procesar paquetes TCP especialmente formados en sistemas VxWorks y otros que integran esa pila.​

**CVE-2020-24336 — AMNESIA:33 (uIP DNS)** Validación insuficiente al analizar registros DNS en uIP que provoca corrupción/desbordamiento de memoria y potencial RCE mediante respuestas DNS malformadas en dispositivos IoT/embebidos.​

## Fase 3: Clasificación para la empresa {#fase-3:-clasificación-para-la-empresa}

En este Apartado vamos a clasificar estos CVE en cómo afectan a nuestra empresa

### [**CVEs concretos en configuraciones inseguras y credenciales por defecto**](#configuraciones-inseguras-y-credenciales-por-defecto:)

**CVE-2024-51978 — Impresoras (Brother y otras)**

* Gravedad: Crítica. Permite derivar la contraseña administrativa por defecto y tomar control del equipo, con impacto alto en confidencialidad e integridad.  
* Facilidad de explotación: Alta. Si el número de serie es accesible o deducible, la obtención de la clave es directa.  
* Relevancia para TrustShield Financial: Alta. Dispositivos de impresión en oficinas pueden facilitar movimiento lateral, filtración de escaneos y abuso de credenciales almacenadas.

**CVE-2023-43844 — Aten PE6208 (PDU)**

* Gravedad: Alta. Acceso administrativo por credenciales por defecto otorga control de energía (apagado/encendido), afectando disponibilidad e integridad operativa.  
* Facilidad de explotación: Alta. Si la interfaz web está accesible y no se cambiaron credenciales, el acceso es trivial.  
* Relevancia para TrustShield Financial: Alta. PDUs en CPDs/salas técnicas pueden causar interrupciones de servicios críticos y riesgos de seguridad física/operativa.

**CVE-2024-41690 — SyroTech SY-GPON-1110-WDONT (router)**

* Gravedad: Alta. Credenciales por defecto en firmware permiten acceso no autorizado al plano de gestión del router.  
* Facilidad de explotación: Media–Alta. Requiere acceso al binario/firmware o exposición del dispositivo, pero el vector es directo.  
* Relevancia para TrustShield Financial: Media. Riesgo mayor en sedes pequeñas o teletrabajo si estos equipos se usan como CPE; menor en entornos con equipamiento corporativo.

### [**CVEs concretos de servicios de acceso remoto inseguros (RDP, SSH mal configurado)**](#servicios-de-acceso-remoto-inseguros-\(rdp,-ssh-mal-configurado\):)

**CVE-2019-0708 — BlueKeep (RDP)**

* Gravedad: Crítica. RCE no autenticada en RDP compromete servidores Windows, con impacto total en confidencialidad, integridad y disponibilidad.  
* Facilidad de explotación: Alta. Existen exploits maduros y el vector es de red sin interacción.  
* Relevancia para TrustShield Financial: Muy alta. Superficies RDP expuestas o mal segmentadas son un vector clásico de intrusión y ransomware.

**CVE-2018-15473 — OpenSSH user-enumeration**

* Gravedad: Media. No otorga acceso directo, pero facilita ataques de fuerza bruta y focalización de cuentas válidas.  
* Facilidad de explotación: Alta. Se basa en diferencias de respuesta en autenticación.  
* Relevancia para TrustShield Financial: Media. Aumenta el riesgo sobre cuentas privilegiadas si no hay MFA y controles de lockout.

**CVE-2021-36368 — OpenSSH agent-forwarding / auth issue**

* Gravedad: Media–Alta. Riesgo de uso indebido de credenciales/agent con impacto en integridad y posible acceso lateral.  
* Facilidad de explotación: Media. Requiere condiciones de configuración (agent forwarding activo) y posicionamiento en la ruta.  
* Relevancia para TrustShield Financial: Alta. Plataformas de administración con saltos SSH son habituales; una mala configuración expone credenciales y sesiones.

### [**CVEs concretos en protocolos de compartición de archivos (SMB, NFS)**](#vulnerabilidades-en-protocolos-de-compartición-de-archivos-\(smb,nfs\))

**CVE-2020-0796 — SMBGhost (SMBv3)**

* Gravedad: Crítica. RCE no autenticada por manejo de memoria en SMBv3, impacto total en CIA.  
* Facilidad de explotación: Alta. Paquetes especialmente formados contra servicios vulnerables.  
* Relevancia para TrustShield Financial: Muy alta. Movimiento lateral rápido y despliegue de ransomware en redes Windows.

**CVE-2017-0144 — EternalBlue (SMBv1)**

* Gravedad: Crítica. RCE en SMBv1 explotada masivamente, base de brotes de ransomware.  
* Facilidad de explotación: Alta. Herramientas públicas y automatización consolidadas.  
* Relevancia para TrustShield Financial: Muy alta. Afecta continuidad de negocio y datos críticos si persisten sistemas legacy.

**CVE-2017-7494 — SambaCry (Samba)**

* Gravedad: Alta. Carga y ejecución de librería maliciosa vía share con permisos de escritura.  
* Facilidad de explotación: Media. Requiere recurso compartido con escritura y ruta alcanzable.  
* Relevancia para TrustShield Financial: Media–Alta. Riesgo en servidores de ficheros Linux/UNIX con shares amplios.

### [**CVEs concretos de protocolos criptográficos mal implementados (TLS/SSL/OpenSSL)**](#protocolos-criptográficos-mal-implementados-\(tls/ssl/openssl\)-si-tls/ssl-o-su-librería-\(como-openssl\)-tienen-errores-en-cómo-negocian-la-conexión-segura-o-validan-certificados,-un-atacante-puede-colarse-en-medio,-leer-datos-supuestamente-cifrados-o-hacerse-pasar-por-el-servidor/cliente-legítimo)

**CVE-2014-0160 — Heartbleed (OpenSSL)**

* Gravedad: Crítica. Lectura fuera de límites expone claves privadas, cookies y credenciales, comprometiendo la confidencialidad del canal y autenticidad del servicio.  
* Facilidad de explotación: Alta. Remoto y sin autenticación, con PoC ampliamente disponible.  
* Relevancia para TrustShield Financial: Muy alta. Impacta portales, APIs y túneles que dependan de OpenSSL vulnerable.

**CVE-2015-4000 — Logjam (TLS, Diffie-Hellman)**

* Gravedad: Alta. Degradación a grupos DH export debilita el cifrado y permite MitM/descifrado.  
* Facilidad de explotación: Media. Requiere posición de MitM y soporte de parámetros débiles.  
* Relevancia para TrustShield Financial: Media–Alta. Riesgo en servicios legacy o balanceadores con suites antiguas.

**CVE-2022-0778 — OpenSSL Infinite Loop (DoS)**

* Gravedad: Media–Alta. Bucle infinito al validar certificados X.509 afecta disponibilidad de procesos TLS.  
* Facilidad de explotación: Alta. Envío de certificados malformados provoca DoS.  
* Relevancia para TrustShield Financial: Alta. Puede tumbar terminadores TLS, APIs y servicios críticos si no están parcheados.

### [**CVEs concretos en Amplificación y reflexión de UDP**](#amplificación-y-reflexión-en-udp-\(ntp,-dns,-ssdp,-cldap,-memcached\))

**CVE-2013-5211 — NTP “monlist”**

* Gravedad: Alta. Amplificación por reflexión conduce a DDoS significativo (disponibilidad).  
* Facilidad de explotación: Alta. Consultas pequeñas con IP suplantada generan respuestas grandes.  
* Relevancia para TrustShield Financial: Media. Riesgo de ser objetivo de DDoS y de ser reflector si hay NTP expuesto.

**CVE-2018-1000115 — Memcached UDP amplification**

* Gravedad: Crítica. Altísimo factor de amplificación con impacto severo en disponibilidad.  
* Facilidad de explotación: Alta. Tráfico mínimo contra 11211/UDP público produce ráfagas masivas.  
* Relevancia para TrustShield Financial: Media. Evitar exposición de Memcached; principal riesgo como víctima de DDoS.

**CVE-2020-8616 — NXNSAttack (BIND DNS)**

* Gravedad: Alta. Genera cascadas de consultas (amplificación/reflexión) causando DoS.  
* Facilidad de explotación: Media. Requiere manipular referrals y configuraciones de recursión.  
* Relevancia para TrustShield Financial: Alta. Crítico si se operan resolutores recursivos o infraestructura DNS propia.

### [**CVEs concretos de fallos en protocolos de gestión (SNMP, DHCP, DNS)**](#fallos-en-protocolos-de-gestión-\(snmp,-dhcp,-dns\))

**CVE-2008-1447 — Kaminsky DNS cache poisoning**

* Gravedad: Alta. Permite envenenar cachés y redirigir tráfico, afectando confidencialidad e integridad.  
* Facilidad de explotación: Media. Requiere sincronizar respuestas/IDs en resolutores sin mitigaciones.  
* Relevancia para TrustShield Financial: Alta. Riesgo sobre resolutores internos/forwarders y navegación de usuarios.

**CVE-2024-3661 — “TunnelVision” (DHCP Option 121\)**

* Gravedad: Alta. Inyección de rutas filtra tráfico fuera de VPN, comprometiendo confidencialidad.  
* Facilidad de explotación: Media. Precisa servidor DHCP malicioso en el dominio de broadcast.  
* Relevancia para TrustShield Financial: Muy alta. Afecta teletrabajo y cumplimiento, exponiendo datos fuera del túnel.

**CVE-2017-6742 — SNMP (Cisco IOS/IOS XE)**

* Gravedad: Alta. Uso de comunidades/configuración débil permite acceso/acciones vía SNMP, impactando integridad y confidencialidad de dispositivos de red.  
* Facilidad de explotación: Media–Alta. Depende de exposición y controles de acceso.  
* Relevancia para TrustShield Financial: Muy alta. Compromiso de routers/switches afecta toda la red, visibilidad y continuidad.

### 

### 

### [**CVEs concretos en bugs en pilas TCP/IP embebidas**](#bugs-en-pilas-tcp/ip-/-stacks-embebidos:) {#cves-concretos-en-bugs-en-pilas-tcp/ip-embebidas}

**CVE-2020-11896 — Ripple20/Treck (IPv4 tunneling)**

* Gravedad: Crítica. RCE/DoS en dispositivos embebidos por parsing de paquetes tunelados.  
* Facilidad de explotación: Media. Requiere formar tramas específicas y que el feature esté habilitado.  
* Relevancia para TrustShield Financial: Media. Importante si hay equipos IoT/OT o appliances con Treck en red.

**CVE-2019-12255 — URGENT/11 (VxWorks IPnet)**

* Gravedad: Crítica. RCE por manejo de TCP Urgent Pointer en IPnet, con impacto total en dispositivos afectados.  
* Facilidad de explotación: Media. Paquetes TCP especiales; presencia amplia en dispositivos industriales/embebidos.  
* Relevancia para TrustShield Financial: Media–Alta. Riesgo en appliances de red/OT en sucursales o CPDs.

**CVE-2020-24336 — AMNESIA:33 (uIP DNS)**

* Gravedad: Alta. Corrupción de memoria por parsing DNS malformado con potencial RCE.  
* Facilidad de explotación: Media. Requiere posicionar respuestas DNS maliciosas hacia el dispositivo vulnerable.  
* Relevancia para TrustShield Financial: Media. Afecta a IoT y dispositivos embebidos; priorizar si coexisten en misma VLAN que activos críticos.

# Contramedidas propuestas {#contramedidas-propuestas}

| CVE | Contramedida | Descripción | Efectividad |
| :---- | :---- | :---- | :---- |
| [Configuraciones inseguras y credenciales por defecto](#cves-concretos-en-configuraciones-inseguras-y-credenciales-por-defecto) |  |  |  |
| CVE-2024-51978 | Actualizar firmware; cambiar credencial admin inmediatamente; segmentar/red restrictiva; deshabilitar interfaz remota si no es crítica | Impresoras permiten derivación de clave admin desde el número de serie; control total si no se cambia la credencial | Alta |
| CVE-2023-43844 | Cambiar credenciales; limitar acceso web; parchear/actualizar firmware; vigilar logs de acceso | PDU con interfaz web expuesta con credenciales por defecto; acceso privilegiado si no se modifica | Alta |
| CVE-2024-41690 | Cambiar y securizar credenciales; actualizar firmware; limitar acceso; evitar exposición en WAN | Router con credenciales por defecto en firmware; acceso no autorizado si se extrae el binario | Alta |
| [Servicios de acceso remoto inseguros (RDP/SSH)](#cves-concretos-de-servicios-de-acceso-remoto-inseguros-\(rdp,-ssh-mal-configurado\)) |  |  |  |
| CVE-2019-0708 | Aplicar parche MS; habilitar NLA; filtrar puerto 3389; segmentar acceso RDP | RCE por peticiones RDP especialmente diseñadas a sistemas sin parchear | Muy alta |
| CVE-2018-15473 | Actualizar OpenSSH (\>7.7); implementar MFA; anti-fuerza bruta; esconder errores detallados | Enumeración de usuarios por respuestas diferentes, facilita ataques dirigidos | Alta |
| CVE-2021-36368 | Actualizar OpenSSH (≥8.9); desactivar 'agent forwarding'; logging detallado | Uso indebido de forwarding/agente puede comprometer sesiones y credenciales | Alta |
| [Protocolos de compartición de archivos (SMB/NFS)](#cves-concretos-en-protocolos-de-compartición-de-archivos-\(smb,nfs\)) |  |  |  |
| CVE-2020-0796 | Parchear/actualizar; desactivar compresión SMBv3; segmentar y proteger acceso SMB; bloquear puertos externos | RCE en SMBv3 por manejo de memoria, se explota por red sin autenticación | Muy alta |
| CVE-2017-0144 | Aplicar MS17-010; deshabilitar SMBv1; monitorizar y segmentar acceso SMB | RCE masivo en SMBv1; base de brotes ransomware y movimientos laterales | Muy alta |
| CVE-2017-7494 | Actualizar Samba; restringir permisos escritura en shares; aislar servidores compartición | Cliente remoto puede cargar y ejecutar librería maliciosa en share con escritura | Alta |
| [Protocolos criptográficos mal implementados (TLS/SSL/OpenSSL)](#cves-concretos-de-protocolos-criptográficos-mal-implementados-\(tls/ssl/openssl\)) |  |  |  |
| CVE-2014-0160 | Actualizar OpenSSL (1.0.1g o superior); revocar y regenerar certificados y claves tras mitigación | Lectura fuera de límites obtiene memoria sensible (Heartbleed), incluidas claves privadas | Muy alta |
| CVE-2015-4000 | Deshabilitar/depreciar suites export-grade DHE; actualizar configuración cifrado; monitorizar ciphersuites débiles | Fuerza uso de grupo DH débil; permite MitM y descifrado tráfico TLS (Logjam) | Alta |
| CVE-2022-0778 | Actualizar OpenSSL (≥1.1.1n o 3.0.2); asignar políticas DoS; parchear aplicaciones afectadas | Bucle infinito validando X.509 manipulados; afecta disponibilidad de servicios TLS | Alta |
| [Amplificación y reflexión UDP (NTP, DNS, Memcached)](#cves-concretos-en-amplificación-y-reflexión-de-udp) |  |  |  |
| CVE-2013-5211 | Actualizar NTP (\>4.2.7p26); deshabilitar función monlist; restringir acceso UDP 123; bloquear en perímetro | Monlist permite amplificación masiva vía reflexión; DDoS/DoS sobre víctima por NTP | Alta |
| CVE-2018-1000115 | Actualizar Memcached (\>1.5.6); deshabilitar UDP en Memcached; filtrar puerto 11211 UDP; segmentar acceso | Uso de UDP en Memcached como amplificador/reflejo, factor masivo de DDoS | Alta |
| CVE-2020-8616 | Parchear BIND DNS; limitar fetches y recursion; actualizar versiones y aplicar hotfixes | Consultas de referrals manipuladas generan cascada de solicitudes, amplificador y DoS | Alta |
| [Fallos en protocolos de gestión (SNMP, DHCP, DNS)](#cves-concretos-de-fallos-en-protocolos-de-gestión-\(snmp,-dhcp,-dns\)) |  |  |  |
| CVE-2008-1447 | Aplicar parches; usar autenticación fuerte; incrementar entropía/aleatoriedad; usar DNSSEC y monitoreo | Respuestas DNS predecibles permiten envenenamiento de caché y falsificación de registros | Alta |
| CVE-2024-3661 | Actualizar clientes/servidores DHCP y VPN; segmentar y monitorizar tráfico DHCP; bloquear Option 121 si no es necesaria; usar IDS/NIDS | DHCP manipulado inyecta rutas para filtrar tráfico fuera de túnel VPN; exposición confidencialidad | Alta |
| CVE-2017-6742 | Actualizar Cisco IOS/IOS XE; restringir comunidad SNMP; segmentar acceso SNMP; aplicar políticas mínima exposición | Configuración SNMP débil permite acciones no autorizadas, divulgación/explotación | Muy alta |
| [Bugs en pilas TCP/IP embebidas (Ripple20, URGENT/11, AMNESIA:33)](#cves-concretos-en-bugs-en-pilas-tcp/ip-embebidas) |  |  |  |
| CVE-2020-11896 | Actualizar Treck TCP/IP a versión ≥6.0.1.66; desactivar IPv4 tunneling si no es esencial; segmentar dispositivos embebidos del perímetro | Parsing de IPv4 tunelado malformado habilita RCE/DoS en dispositivos embebidos | Alta |
| CVE-2019-12255 | Actualizar firmware/software de dispositivos afectados; segmentar activos embebidos; monitorizar tráfico TCP sospechoso | Error en TCP Urgent Pointer facilita RCE en sistemas VxWorks/IPnet | Alta |
| CVE-2020-24336 | Actualizar firmware (uIP DNS); reforzar validación DNS; segmentar dispositivos IoT/embebidos críticos | Validación insuficiente de DNS en pilas embebidas, corrupción/desbordamiento memoria y RCE | Alta |

# Conclusión {#conclusión}

En este informe técnico, nuestro equipo ha realizado un análisis exhaustivo de las principales vulnerabilidades que afectan a las redes y protocolos de comunicación, identificando tanto categorías generales como casos concretos (CVEs) que representan riesgos reales para TrustShield Financial (nuestra empresa).Nos hemos dado cuenta que muchas amenazas persisten debido a configuraciones inseguras, uso de credenciales por defecto, servicios mal protegidos y fallos en la implementación de protocolos críticos, así que hemos analizado la gravedad de estos casos y propuesto soluciones definitivas o que hagan que el riesgo sea más asumible.

TrustShield podrá fortalecer la confidencialidad, integridad y disponibilidad de su información con nuestro informe, reduciendo significativamente la superficie de ataque y mejorando su defensa frente a incidentes de ciberseguridad en redes y protocolos de comunicación .