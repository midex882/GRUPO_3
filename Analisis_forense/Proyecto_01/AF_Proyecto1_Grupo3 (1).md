# Development of a Forensic Analysis 

# Introducción

Nuestra empresa de ciberseguridad nos ha encargado, como parte de su equipo forense, desarrollar una metodología de análisis forense propia. En este proyecto, presentaremos normas y estándares forenses reconocidos y, a partir de ellos, diseñaremos un proceso metódico para la adquisición, análisis y presentación de evidencias digitales.

# Informe técnico

Para el informe técnico hemos decidido hablar de los siguientes estándares forenses: la ISO/IEC 27037 (identificación, adquisición y preservación), ISO/IEC 27042 (análisis e interpretación) y NIST SP 800-86 (integración de forense en respuesta a incidentes), porque cubren de forma complementaria el ciclo técnico y operativo de la evidencia digital.​

1. ## ISO/IEC 27037

Establece directrices para la identificación, recopilación, adquisición y preservación de evidencia digital, con el objetivo de mantener integridad, autenticidad y fiabilidad desde el descubrimiento hasta su posible presentación. Trabajo con medios como almacenamiento, móviles, cámaras, redes. Incluye pautas sobre marcado, embalaje, transporte y documentación de la escena.​

* **Alcance**: manejo inicial de evidencia (identificación, colección, adquisición y preservación).  
* **Objetivo:** minimizar alteraciones y asegurar integridad, con documentación exhaustiva de todas las acciones.​  
* **Cobertura tecnológica:** desde soportes de PC hasta dispositivos móviles, cámaras, navegación y redes TCP/IP.​  
* **Enfoque jurídico-operativo:** pensado para facilitar transferencia entre jurisdicciones con procedimientos trazables.​


2. ## ISO/IEC 27042

Son normas para el análisis e interpretación de la evidencia digital para mantener una continuidad, validez, reproducibilidad y repetibilidad, exigiendo registro suficiente para que sea todo independiente. Permite seleccionar, diseñar e implementar procesos analíticos y justificar métodos empleados, incluyendo cómo demostrar competencia del equipo investigador. Reconoce que distintos métodos pueden influir en la interpretación y los métodos deben ser “apropiados para el propósito”.​

* **Principios clave:** continuidad del rastro, validez de métodos, reproducibilidad y repetibilidad del análisis.​  
* **Requisitos de documentación**: detalle de procesos y parámetros para permitir revisión por terceros.​  
* **Competencia:** mecanismos para demostrar aptitud y competencia del equipo analista.​  
* **Selección de técnicas:** justificar métodos y equivalencias frente a alternativas, adaptando el análisis al tipo de evidencia disponible.​


3. ## NIST SP 800-86

Es una guía para la integración de técnicas forenses en la respuesta a incidentes con un enfoque práctico sobre categorías de fuentes de datos, y sobre cómo realizar recolección, examen, análisis e informe. Consiste en metodologías consistentes, roles y formación, y en procedimientos que mantengan la efectividad y exactitud, especialmente cuando hay posibles actuaciones disciplinarias o judiciales. Conecta la práctica forense con las fases de IR (preparación, detección/análisis, contención/erradicación/recuperación y post-incidente)

* **Fases operativas**: recogida, examen, análisis e informe integradas en el flujo de respuesta a incidentes.​  
* **Buenas prácticas:** estandarizar procedimientos para acciones consistentes y admisibles cuando corresponda.​  
* **Capacidades organizativas:** clarifica roles, formación y cooperación entre primeros intervinientes y especialistas.​  
* **Cobertura técnica:** orientación por categorías de datos de sistemas operativos, tráfico de red y aplicaciones.​

# Comparativa de normas

Aquí tienes una comparativa clara entre ISO/IEC 27037, ISO/IEC 27042 y NIST SP 800-86 aplicada al análisis forense y orientada a diseñar una metodología propia DF/IR.

1. ## Alcance y propósito​

* ISO/IEC 27037: manejo inicial de evidencia (identificación, colección, adquisición y preservación) para asegurar integridad y admisibilidad.  
    
* ISO/IEC 27042: guía el estudio analítico de la evidencia, justificando métodos y garantizando repetibilidad y defendibilidad del análisis.  
    
* NIST SP 800-86: orienta a DFIR/CSIRT en integrar forense al ciclo de incident response (preparación a post-incidente) con procesos prácticos.​


2. ## Principios y documentación​

* ISO/IEC 27037: cadena de custodia rigurosa, identificación unívoca, registro de accesos, preservación bit a bit cuando sea aplicable.​  
    
* ISO/IEC 27042: continuidad del rastro, validación de herramientas, registro de parámetros y decisiones para revisión por terceros.  
    
* NIST SP 800-86: metodologías consistentes y admisibles, claridad de roles y formación, artefactos de sistema/red/aplicación como fuentes.  
  


3. ## Cobertura tecnológica

* ISO/IEC 27037: soportes de PC, móviles, cámaras y redes TCP/IP; lineamientos para embalaje, transporte y marcado.  
    
* ISO/IEC 27042: neutral respecto a tecnología, exige que el método sea apropiado al propósito y evidencia disponible.  
    
* NIST SP 800-86: categorías de datos del SO, tráfico de red y aplicaciones para orientar recolección y análisis.


4. ## Competencia y validación

* ISO/IEC 27042: demanda demostrar competencia del equipo y validación de herramientas y procesos analíticos.  
* Ecosistema de acreditación: casos reales muestran uso de ISO/IEC 17025 para laboratorios que operan siguiendo estas guías forenses.


5. ## Fortalezas y limitaciones

* ISO/IEC 27037: fuerte en preservación inicial y cadena de custodia; menos prescriptiva en análisis profundo.  
* ISO/IEC 27042: fuerte en calidad del análisis y defendibilidad; depende de que 27037 haya asegurado integridad previa.  
* NIST SP 800-86: fuerte en integración operativa con IR; menos formalista que ISO en requisitos de trazabilidad normativa.


6. ## Tabla comparativa

| Criterio | ISO/IEC 27037 | ISO/IEC 27042 | NIST SP 800-86 |
| :---- | :---- | :---- | :---- |
| ¿En qué se centra? | Empezar bien: encontrar, recoger y guardar la evidencia sin dañarla. | Analizar e interpretar la evidencia de forma correcta y repetible. | Integrar análisis forense en la respuesta a incidentes del equipo. |
| Cadena de custodia | Registrar cada paso y usar copias bit a bit con hashes cuando sea necesario. | Mantener trazabilidad de todas las decisiones y parámetros del análisis. | Ajustar la trazabilidad a los procesos y reportes del equipo de respuesta a incidentes. |
| Validación | Comprobar que la adquisición se hace con los medios y pasos adecuados. | Validar herramientas y métodos; demostrar que el equipo tiene la competencia necesaria. | Definir procedimientos claros y roles: quién hace qué y cómo. |
| Tecnología cubierta | Discos, móviles, cámaras y redes; pautas para manejarlos sin alterar datos. | Agnóstico: elegir el método más adecuado para cada caso y tipo de evidencia. | Fuentes típicas: sistema operativo, red y aplicaciones como base de trabajo. |
| Qué resultado persigue | Evidencia íntegra y lista para analizar o presentar. | Conclusiones que otros puedan repetir y defender. | Un proceso DFIR efectivo, coordinado y bien documentado. |
| Fortalezas | Muy fuerte en preservación inicial y cadena de custodia; reduce riesgos de contaminar la evidencia. | Asegura calidad del análisis y que otros puedan repetirlo; mejora la defendibilidad técnica. | Aterriza la forense en el día a día del SOC/CSIRT; facilita coordinación y tiempos de respuesta. |
| Debilidades | Cubre poco el análisis profundo; requiere formación y puede ser costoso de implantar. | Puede ser complejo y exigir alta especialización y validaciones continuas. | Menos formalista que ISO; puede variar su aplicación entre equipos si no se estandariza bien. |

# Metodología propia

La metodología de análisis forense desarrollada, desglosada por fases.

* Adquisición de evidencia digital.  
* Preservación y almacenamiento de la evidencia.  
* Análisis de las evidencias.  
* Documentación de hallazgos.  
* Presentación de resultados.


A continuación se reescribe la metodología propia basándose explícitamente en las tres normas elegidas y haciendo alusiones a ellas en cada fase cuando corresponde.

## **Metodología propia**

La metodología se organiza en seis fases: Preparación, Adquisición, Preservación y almacenamiento, Análisis, Documentación y Presentación de resultados, con controles transversales de cadena de custodia, validación de herramientas y revisión por pares, apoyándose en ISO/IEC 27037 para el manejo inicial de evidencias, ISO/IEC 27042 para el análisis e interpretación y NIST SP 800-86 para su integración en la respuesta a incidentes del equipo DFIR.

## **Fase 0: Preparación**

* **Objetivo**: garantizar que personas, procesos y herramientas están listos y validados antes de intervenir, alineando roles y flujo con la respuesta a incidentes.

* **Referencias y alusiones**: NIST SP 800-86 para preparación y encaje con el ciclo de IR (preparación, detección/análisis, contención/erradicación/recuperación y post-incidente); ISO/IEC 27042 para competencia y validación previa de herramientas; ISO/IEC 27037 para plantillas y procedimientos de manejo inicial de evidencias.

* **Acciones**: definición de roles (primer interviniente, analista, coordinador DFIR), inventario de herramientas con versiones y pruebas de validación, listas de chequeo por tipo de evidencia (endpoint, móvil, red, cloud) y plantillas de cadena de custodia.

## **Fase 1: Adquisición de evidencia digital**

* **Objetivo**: identificar, recolectar y adquirir la evidencia minimizando alteraciones y garantizando trazabilidad.

* **Referencias y alusiones**: ISO/IEC 27037 como guía principal para identificación, colección, adquisición y preservación inicial (incluye etiquetado, embalaje y transporte); NIST SP 800-86 para alinear la adquisición con el plan de respuesta y las fuentes de datos operativas; ISO/IEC 27042 para dejar condiciones iniciales que favorezcan un análisis repetible.

* **Procedimiento**: priorización por volatilidad, uso de bloqueadores de escritura, elección del tipo de adquisición “apropiado al propósito” (física/bit a bit, lógica, en vivo), cálculo de hashes antes y después, y prohibición de trabajar sobre originales.

* **Registro**: quién/cuándo/dónde, dispositivo/volumen, herramientas y parámetros, hashes calculados, incidencias y actualización de cadena de custodia.

## **Fase 2: Preservación y almacenamiento**

* **Objetivo**: mantener integridad, autenticidad y trazabilidad durante todo el ciclo de vida de la evidencia.

* **Referencias y alusiones**: ISO/IEC 27037 para salvaguarda física y documental de evidencias (marcado, embalaje, transporte, almacenamiento); ISO/IEC 27042 para continuidad del rastro de cara al análisis; NIST SP 800-86 para gobernanza y controles alineados a procesos de IR.

* **Medidas**: embalaje antiestático, sellos y etiquetado, almacenamiento seguro (repositorios inmutables/WORM), control de accesos por rol, verificación periódica de hashes e inventario auditable.

## **Fase 3: Análisis de las evidencias**

* **Objetivo**: producir hallazgos reproducibles y defendibles que expliquen qué, cómo, cuándo, quién (si procede) e impacto.

* **Referencias y alusiones**: ISO/IEC 27042 como eje del análisis para seleccionar y justificar métodos, registrar parámetros, garantizar repetibilidad y habilitar revisión por terceros; NIST SP 800-86 para articular el análisis con las fases de IR y fuentes típicas (SO, red, aplicaciones); ISO/IEC 27037 para respetar condiciones de preservación al montar y examinar imágenes.

* **Pasos**: preparación de entorno aislado, montaje de imágenes en solo lectura, triage y cronología (artefactos de sistema y registros), análisis focalizado (IOC, cuentas/credenciales, navegación, correo, móviles, tráfico de red, cloud), correlación entre fuentes y evaluación de alternativas plausibles.

* **Calidad**: validación de herramientas, registro de comandos/consultas/parámetros, conservación de artefactos derivados con hashes y revisión por pares cuando sea viable.

## **Fase 4: Documentación de hallazgos**

* **Objetivo**: crear un registro claro, completo y auditable de actividades y observaciones.

* **Referencias y alusiones:** ISO/IEC 27042 para el nivel de detalle, trazabilidad del proceso analítico y defendibilidad; NIST SP 800-86 para estructurar informes operativos alineados a IR y a audiencias técnicas/ejecutivas; ISO/IEC 27037 para garantizar que la evidencia referenciada mantiene su integridad y trazabilidad.

* **Contenido mínimo**: contexto y alcance, metodología aplicada con referencia explícita a las normas usadas, herramientas y versiones, parámetros críticos, limitaciones, hallazgos enlazados a evidencias y hashes, cronología y análisis de impacto.

## **Fase 5: Presentación de resultados**

* **Objetivo**: comunicar resultados a audiencias técnicas y ejecutivas, manteniendo admisibilidad y utilidad operativa.

* **Referencias y alusiones:** NIST SP 800-86 para formatos y mensajes alineados al ciclo de IR y a la toma de decisiones; ISO/IEC 27042 para asegurar que conclusiones sean reproducibles y defendibles; ISO/IEC 27037 para presentar evidencias conservando autenticidad e integridad.

* **Entregables**: informe técnico con apéndices (artefactos, parámetros, procedimientos), resumen ejecutivo orientado a riesgos/negocio y materiales visuales (líneas de tiempo, mapas de ataque).

## **Resumen esquemático**

Una vez acabado nuestro desarrollo de la metodología para el análisis forense, hemos elaborado un esquema sencillo en forma de mapa mental para ilustrar de forma concisa nuestro proceso y razonamiento.

**Bibliografía**

[https://www.intedya.com/internacional/819/noticia-las-diferencias-entre-la-norma-iso-iec-17025-y-17020-para-las-agencias-forenses.html](https://www.intedya.com/internacional/819/noticia-las-diferencias-entre-la-norma-iso-iec-17025-y-17020-para-las-agencias-forenses.html)

[https://www.zerolynx.com/eu/blogs/berriak/normativas-estandares-forense-1-de-3](https://www.zerolynx.com/eu/blogs/berriak/normativas-estandares-forense-1-de-3)

[https://oa.upm.es/37137/1/PFC\_JEREZ\_GUERERO\_JOSE\_LUIS.pdf](https://oa.upm.es/37137/1/PFC_JEREZ_GUERERO_JOSE_LUIS.pdf)

[https://es.linkedin.com/pulse/las-normas-isoiec-y-el-perito-inform%C3%A1tico-jos%C3%A9-luis-tamayo-rodr%C3%ADguez-gd2dc](https://es.linkedin.com/pulse/las-normas-isoiec-y-el-perito-inform%C3%A1tico-jos%C3%A9-luis-tamayo-rodr%C3%ADguez-gd2dc)

[https://peritosinformaticos.es/iso-27037-2012-perito-informatico/](https://peritosinformaticos.es/iso-27037-2012-perito-informatico/)

[https://es.scribd.com/document/758379268/GD-3064-ES-Documento-de-Orientacion-Forense-Redaccion-del-Alcance-de-la-Acreditacion-29547-2](https://es.scribd.com/document/758379268/GD-3064-ES-Documento-de-Orientacion-Forense-Redaccion-del-Alcance-de-la-Acreditacion-29547-2)

[https://ica.intedya.com/formacion/actualidad.php?id=819](https://ica.intedya.com/formacion/actualidad.php?id=819)

[https://iudicium.usal.es/numeros/2/files/assets/common/downloads/IUDICIUM.pdf](https://iudicium.usal.es/numeros/2/files/assets/common/downloads/IUDICIUM.pdf)

[https://www.enac.es/secrim-evidencia-digital](https://www.enac.es/secrim-evidencia-digital)

[https://www.studocu.com/co/document/corporacion-universitaria-iberoamericana/ingenieria-de-software/iso-iec-27037-2012-ing/77342954](https://www.studocu.com/co/document/corporacion-universitaria-iberoamericana/ingenieria-de-software/iso-iec-27037-2012-ing/77342954)

[https://ve.scielo.org/pdf/espacios/v46n4/0798-1015-espacios-46-04-35.pdf](https://ve.scielo.org/pdf/espacios/v46n4/0798-1015-espacios-46-04-35.pdf)

[https://www.neumetric.com/journal/digital-forensics-readiness-compliance-2416/](https://www.neumetric.com/journal/digital-forensics-readiness-compliance-2416/)

[https://journal-isi.org/index.php/isi/article/view/882](https://journal-isi.org/index.php/isi/article/view/882)

[https://www.diva-portal.org/smash/get/diva2:1871685/FULLTEXT01.pdf](https://www.diva-portal.org/smash/get/diva2:1871685/FULLTEXT01.pdf)

[https://www.semanticscholar.org/paper/ANALYSIS-AND-EVALUATION-DIGITAL-FORENSIC-FRAMEWORK-Sudyana-Prayudi/283e4895e9b58a062ad8d19aeafefba6e4bc4e87](https://www.semanticscholar.org/paper/ANALYSIS-AND-EVALUATION-DIGITAL-FORENSIC-FRAMEWORK-Sudyana-Prayudi/283e4895e9b58a062ad8d19aeafefba6e4bc4e87)

[https://faisalyahya.com/cybersecurity-response/digital-forensics-unlocking-the-secrets-of-cyber-investigations/](https://faisalyahya.com/cybersecurity-response/digital-forensics-unlocking-the-secrets-of-cyber-investigations/)

[https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8354.pdf](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8354.pdf)

[https://ve.scielo.org/pdf/espacios/v46n4/0798-1015-espacios-46-04-35.pdf](https://ve.scielo.org/pdf/espacios/v46n4/0798-1015-espacios-46-04-35.pdf)

[https://www.egepud.edu.pe/archivos/Contribuciones%20al%20an%C3%A1lisis%20forense%20de%20evidencias%20digitales%20procedentes%20de%20aplicaciones%20de%20mensajer%C3%ADa%20instant%C3%A1nea\_EGEPUD.pdf](https://www.egepud.edu.pe/archivos/Contribuciones%20al%20an%C3%A1lisis%20forense%20de%20evidencias%20digitales%20procedentes%20de%20aplicaciones%20de%20mensajer%C3%ADa%20instant%C3%A1nea_EGEPUD.pdf)

[https://repository.unad.edu.co/bitstream/handle/10596/48990/kkradaj.pdf?sequence=1\&isAllowed=y](https://repository.unad.edu.co/bitstream/handle/10596/48990/kkradaj.pdf?sequence=1&isAllowed=y)

[https://www.linkedin.com/pulse/normas-y-directrices-en-el-an%C3%A1lisis-forense-digital-e-maurice-w4pue](https://www.linkedin.com/pulse/normas-y-directrices-en-el-an%C3%A1lisis-forense-digital-e-maurice-w4pue)

[https://es.linkedin.com/pulse/las-normas-isoiec-y-el-perito-inform%C3%A1tico-jos%C3%A9-luis-tamayo-rodr%C3%ADguez-gd2dc](https://es.linkedin.com/pulse/las-normas-isoiec-y-el-perito-inform%C3%A1tico-jos%C3%A9-luis-tamayo-rodr%C3%ADguez-gd2dc)

[https://es.scribd.com/document/752460720/Fase-4-Metodologias-de-analisis-forense-en-redes-1](https://es.scribd.com/document/752460720/Fase-4-Metodologias-de-analisis-forense-en-redes-1)

[https://oa.upm.es/82685/1/MARIA\_BELEN\_JIMENEZ\_AMOROSO.pdf](https://oa.upm.es/82685/1/MARIA_BELEN_JIMENEZ_AMOROSO.pdf)

