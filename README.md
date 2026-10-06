# Calculadora Pro 🧮

Una herramienta rápida y ligera desarrollada en Python.

---

## 📥 Métodos de Instalación

Puedes instalar **Calculadora Pro** de tres formas diferentes, dependiendo de si prefieres la versión empaquetada o el script directo.

### 1. Instalación mediante Repositorio APT (Recomendado para Debian/Ubuntu/Linux Mint)
La forma más profesional y fácil de mantener actualizada la herramienta en sistemas basados en Debian:

```bash
# Agregar el repositorio a tus fuentes
echo "deb [arch=amd64 trusted=yes] [https://amirsote.github.io/](https://amirsote.github.io/) stable main" | sudo tee /etc/apt/sources.list.d/calculadora-pro.list

# Actualizar la lista de paquetes
sudo apt update

# Instalar la calculadora
sudo apt install calculadora-pro

2. También puedes descargar el .deb (Recomendado para Debian, Ubuntu y sus derivados)

    Descarga el archivo .deb desde los Releases.

    Hazle doble clic para abrirlo con el instalador gráfico y pulsa Instalar.

3. Por Python (Ejecución local)
Bash

# Asegurarte de tener Python 3 instalado
sudo apt install python3

# Abrir el programa desde la carpeta del proyecto
python3 calculadora.py
