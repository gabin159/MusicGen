# 🎵 MusicGen - Text to Music Generator

Un generador de música basado en Inteligencia Artificial que convierte descripciones de texto (prompts) en pistas de audio en formato `.wav` utilizando el modelo **MusicGen Small** de Meta/Facebook.

---

## 🚀 Características

* **Generación por Prompts:** Crea ritmos, melodías e instrumentos a partir de descripciones de texto simples o detalladas.
* **Procesamiento Eficiente:** Optimizado para ejecutarse localmente usando `torch` y `transformers`.
* **Exportación Directa:** Exporta la pista generada de forma automática como un archivo de audio de alta calidad (`musica.wav`).

---

## 🛠️ Requisitos Previos

Asegúrate de contar con [uv](https://astral.sh/uv) instalado en tu sistema:

```powershell
powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
