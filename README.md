AI Log Anomaly Detector (PoC)
Descripción Técnica

Prueba de Concepto (PoC) para la detección automática de anomalías en logs de sistema utilizando modelos de lenguaje basados en Transformers. Este proyecto implementa un motor de análisis híbrido que combina la potencia de la Inteligencia Artificial con un sistema de fallback basado en firmas para garantizar la disponibilidad y precisión del análisis incluso en entornos restringidos.
Características Principales

    Detección Inteligente: Utiliza modelos de Sequence Classification para identificar patrones sospechosos que escapan a los filtros tradicionales.

    Motor Híbrido: En caso de fallo en la carga del modelo IA, el sistema conmuta automáticamente a un escaneo de palabras clave (firmas) de alta criticidad.

    Arquitectura Modular: Diseñado para ser integrado en flujos de auditoría web y monitoreo de infraestructura.
