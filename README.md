# 🐍 Python Tricks: El Arte de Escribir Código Pitónico

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Estado](https://img.shields.io/badge/Estado-En%20Construcción-orange.svg)
![Contribuciones](https://img.shields.io/badge/Contribuciones-Bienvenidas-brightgreen.svg)

## 📖 ¿Qué es esto?

Este repositorio es mi **cuaderno de bitácora digital** — el último módulo de mi formación como "Experto en Python" en Udemy. Aquí no hay teoría repetida: hay **código que corre**, ejemplos concretos y explicaciones directas de los trucos que diferencian a un programador funcional de uno que realmente domina Python.

Cada archivo es una lección práctica. Lo clonas, lo ejecutas, lo modificas y lo entiendes.

> *"No es magia, es Python bien escrito."*

---

## 🧠 ¿Qué vas a encontrar?

| Tema | Archivo | ¿Qué aprenderás? | Dificultad |
|------|---------|------------------|------------|
| 🧘 **Zen de Python** | `zen_python.py` | Los 19 principios que guían el diseño pitónico | ⭐ |
| 📐 **Nomenclatura** | `AtribMethod_nomesclatura.py`, `AtribMethod_nomesclatura2.py` | Convenciones de nombres, atributos privados y métodos especiales | ⭐⭐ |
| 🔧 **Guiones bajos** | `guion_bajo_simple.py`, `doble_PisoBajo.py`, `doble_PisoBajo2.py` | El significado secreto de `_variable`, `__variable` y `__variable__` | ⭐⭐ |
| 🎨 **Formato avanzado** | `formato_cadenas.py`, `formato_cadenas_n.py`, `Formato_colecciones.py` | f-strings, formato de colecciones y trucos de presentación | ⭐⭐ |
| 🔁 **Funciones poderosas** | `funciones.py`, `funciones2.py`, `funciones_lambda.py` | *args, **kwargs, lambdas y funciones como objetos | ⭐⭐⭐ |
| 🧩 **Decoradores** | `decoradores.py` | Añadir comportamiento a funciones sin modificar su código | ⭐⭐⭐⭐ |
| 🧬 **Clonación de objetos** | `clonacion_objetos.py` | Copias superficiales vs profundas – ¡evita efectos secundarios! | ⭐⭐⭐ |
| 🆔 **Identidad de objetos** | `identidad_objetos.py` | El operador `is` vs `==` – cuándo usar cada uno | ⭐⭐ |
| 📦 **Context Managers** | `Context_Manager.py` | Gestión automática de recursos con `with` | ⭐⭐⭐ |
| ⚠️ **Excepciones a medida** | `clases_excepcion.py` | Crear y lanzar tus propias excepciones | ⭐⭐⭐ |
| 🧙 **Métodos mágicos** | `dunder.py` | `__init__`, `__str__`, `__repr__` y otros poderes ocultos | ⭐⭐⭐⭐ |
| 📜 **Representación de objetos** | `repr_objetos.py` | La diferencia entre `__str__` y `__repr__` | ⭐⭐ |
| ✅ **Aserciones** | `Asersiones.py` | Validar condiciones en desarrollo con `assert` | ⭐ |
| ❌ **Retorno None** | `retorno_none.py` | Por qué las funciones sin `return` devuelven `None` y cómo usarlo | ⭐ |
| 📦 **Módulos** | `Modulo.py` | Cómo organizar y reutilizar código | ⭐⭐ |
| ... | **¡Y más por venir!** | Continuamente añadiendo nuevos tips | ... |

> 💡 **Nota:** La dificultad es orientativa. Un nivel 4 (⭐⭐⭐⭐) no significa que sea imposible, sino que requiere más práctica o nociones previas.

---

## 🗂️ Estructura del proyecto

```
Tips_And_Trick/
│
├── 🐍 Asersiones.py              # Assertions para validar condiciones
├── 🐍 AtribMethod_nomesclatura.py   # Convenciones de nombres
├── 🐍 clonacion_objetos.py       # Copia superficial y profunda
├── 🐍 Context_Manager.py         # Gestión de recursos con 'with'
├── 🐍 decoradores.py             # Decoradores paso a paso
├── 🐍 dunder.py                  # Métodos mágicos (__dunder__)
├── 🐍 formato_cadenas.py         # f-strings y formato avanzado
├── 🐍 funciones_lambda.py        # Funciones anónimas y list comprehensions
├── 🐍 zen_python.py              # Los 19 aforismos del Zen
│
├── 📁 __pycache__/               # Bytecode compilado (ignorar)
├── 📁 Txt/                       # Notas o ejemplos textuales
└── 📄 README.md                  # Este archivo
```

---

## 🚀 Cómo usar este repositorio

1. **Clónalo** donde quieras practicar:
   ```bash
   git clone https://github.com/Astharmin/Tips_And_Trick.git
   cd Tips_And_Trick
   ```

2. **Explora por orden o salta al tema que te interese**. Cada archivo está pensado para ejecutarse individualmente:
   ```bash
   python decoradores.py
   ```

3. **Modifica, rompe, arregla**. Jugar con el código es la única forma de interiorizar estos conceptos.

4. **Vuelve cuando quieras**. Este repo va a crecer con nuevos tips.

---

## 📈 Lo que viene (próximos tips)

- `generadores_yield.py` – Crear secuencias eficientes con `yield`
- `dataclasses.py` – Clases ligeras sin tanto boilerplate
- `tipado_fuerte.py` – Type hints y `mypy` para código más seguro
- `multiprocessing_vs_threading.py` – Cuándo usar cada uno
- `comprension_dicts_sets.py` – Diccionarios y sets por comprensión

---

## 🙌 Contribuciones

¿Tienes un tip que crees que debería estar aquí? ¡Abierto a sugerencias! Puedes:

- Abrir un **issue** con tu idea
- Enviar un **pull request** con un nuevo script (sigue el estilo simple + comentarios + ejemplo ejecutable)

---

## 🧾 Licencia

MIT — libre de usar, aprender y compartir. Si te sirve para llegar a experto, habrá valido la pena.

---

## ✍️ Autor

**Astharmin** – el que escribe código que primero entiende la máquina y luego sus compañeros.

> *"La diferencia entre un código que funciona y un código bien escrito está en los detalles. Aquí están todos esos detalles."*

---

⭐ **Si este repositorio te ayuda a dar el salto a experto, dale una estrella.** ⭐
