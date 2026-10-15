# ⚽ LaLiga Fantasy Market Tracker (CLI)
Una herramienta de línea de comandos (CLI) desarrollada en Python para optimizar las decisiones de compra y venta en **LaLiga Fantasy**. A través de Web Scraping, el programa obtiene los precios actualizados del mercado y calcula las métricas financieras de tu plantilla en tiempo real.

---

## 🔥 Funcionalidades Principales

* 📊 **Seguimiento Diario de Valores:** Extracción automática de precios actualizados de futbolistas.
* 💰 **Cálculo de Rentabilidad (ROI):** Control del precio de compra vs. valor actual en `€` y `%`.
* 📈 **Análisis de Tendencias:** Métricas de fluctuación diaria desde la fecha de adquisición.
* ⏱️ **Proyección de Venta:** Estimación del tiempo óptimo de retención según la tendencia de subida para maximizar beneficios.

---

## 📁 Arquitectura del Proyecto

El código está estructurado de forma modular para facilitar su mantenimiento:

* **`main.py`**: Punto de entrada de la aplicación e interfaz de línea de comandos (CLI).
* **`fetcher.py`**: Gestión de peticiones HTTP para la descarga del contenido web.
* **`extractor.py`**: Lógica de Web Scraping y procesamiento del HTML extraído.
* **`analyzer.py`**: Algoritmos de cálculo financiero (ROI, fluctuaciones y proyecciones).
* **`constants.py`**: Configuración global, URLs, cabeceras HTTP y parámetros constantes.
