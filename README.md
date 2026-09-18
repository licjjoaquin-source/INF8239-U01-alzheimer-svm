# INF-8239 — Unidad 01: Entorno Reproducible

## Sistema Operativo
- Windows 11
- PowerShell (terminal utilizada para todo el proceso)

## Herramientas y versiones
- Python: 3.13.5
- Git: 2.55.0.windows.5

## Estructura del proyecto
INF8239_U01/
├── data/
│ └── raw/
│ └── .gitkeep
├── notebooks/
│ └── 00_verificacion.ipynb
├── reports/
├── src/
│ └── inf8239_u01/
│ ├── init.py
│ └── environment.py
├── tests/
│ └── test_environment.py
├── .gitignore
├── requirements.txt
└── README.md

## Pasos ejecutados

### 1. Configuracion de Git
```powershell
git config --global user.name "Johanna Joaquin"
git config --global user.email "lic.jjoaquin@gmail.com"
```

### 2. Configuracion de SSH con GitHub
```powershell
ssh-keygen -t ed25519 -C "lic.jjoaquin@gmail.com"
Set-Service -Name ssh-agent -StartupType Manual
Start-Service ssh-agent
ssh-add C:\Users\yoany\.ssh\id_ed25519
ssh -T git@github.com
```

### 3. Creacion del entorno virtual
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Instalacion de dependencias
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Modulo y prueba
Se creo el modulo inf8239_u01 con la funcion environment_message() y su prueba correspondiente en tests/test_environment.py.

Ejecucion de la prueba:
```powershell
$env:PYTHONPATH="src"
python -m pytest -q
```
**Resultado:** 1 passed

### 6. Verificacion de Jupyter
Se creo el notebook notebooks/00_verificacion.ipynb, conectado al kernel .venv (Python 3.13.5), confirmando que el interprete usado corresponde al entorno virtual del proyecto.

### 7. Control de versiones
```powershell
git init
git add .
git commit -m "chore: create INF-8239 reproducible environment"
```
**Resultado:** working tree clean y commit visible con git log --oneline.

## Evidencias
- [x] Versiones de Python y Git
- [x] Ruta del interprete .venv desde el notebook
- [x] Salida 1 passed de pytest
- [x] Arbol de carpetas del proyecto
- [x] git log --oneline con el primer commit
- [x] Este README con sistema operativo y comandos usados

---

# LAB02 — Dataset propio: Alzheimer's Disease Dataset

## Instalacion y reproduccion

```powershell
git clone <URL_DE_TU_REPOSITORIO>
cd INF8239_U01
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Descarga del dataset

Este dataset proviene de Kaggle y requiere autenticacion via API:

1. Crea una cuenta en kaggle.com
2. Genera un token de API (Settings > API > Create New Token)
3. Guarda el token como variable de entorno:
```powershell
   [System.Environment]::SetEnvironmentVariable("KAGGLE_API_TOKEN", "TU_TOKEN", "User")
```
4. Descarga el dataset:
```powershell
   kaggle datasets download -d rabieelkharoua/alzheimers-disease-dataset -p data\raw --unzip
```

O bien, ejecuta la funcion encapsulada en el notebook:
```python
from inf8239_u01.data import download_kaggle_dataset
path = download_kaggle_dataset()
```

## Dataset

- Nombre: Alzheimer's Disease Dataset (Kaggle, Rabie El Kharoua, 2024)
- Filas/columnas: 2149 filas, 35 columnas
- Target: Diagnosis (0 = sin Alzheimer, 1 = con Alzheimer)
- Metrica principal: F1-macro (por desbalance moderado de clases: 64.6% / 35.4%)
- Columnas excluidas: PatientID (identificador), DoctorInCharge (valor constante)

## Ejecucion

```powershell
$env:PYTHONPATH="src"
python -m pytest -q
```
Resultado esperado: 7 passed

## Resultados

| Modelo | F1-macro |
|--------|----------|
| Dummy (baseline) | 0.393 |
| SVM (C=1, gamma=scale) | 0.816 |

## Conclusion

Este laboratorio permitio aplicar el pipeline desarrollado en el LAB01 a un dataset 
real y propio, seleccionado de forma independiente siguiendo criterios de aceptacion 
academica: procedencia documentada, licencia clara, tamano de muestra adecuado (2149 
filas) y un target binario observable. Se eligio el Alzheimer's Disease Dataset de 
Kaggle por su relevancia clinica y su estructura tabular, similar al problema resuelto 
previamente con el dataset de cancer de mama, pero con un reto adicional: la necesidad 
de autenticarse contra una API externa (Kaggle) para reproducir la descarga, lo cual 
se documento y encapsulo en una funcion dedicada (download_kaggle_dataset) en 
src/inf8239_u01/data.py.

Durante la auditoria se identificaron dos columnas problematicas: PatientID, un 
identificador sin valor predictivo que podria inducir sobreajuste si se incluyera, 
y DoctorInCharge, una columna con un unico valor constante que no aporta informacion 
util. Ambas fueron excluidas con una justificacion semantica explicita, evitando el 
error comun de eliminar columnas unicamente por mejorar metricas.

El modelo SVM con pipeline (StandardScaler + SVC con kernel RBF) supero ampliamente 
al baseline dummy (F1-macro de 0.816 frente a 0.393), confirmando que las variables 
clinicas, demograficas y de estilo de vida contienen senal predictiva real sobre el 
diagnostico de Alzheimer. Sin embargo, el analisis de la matriz de confusion revelo 
una asimetria importante: el recall de la clase Alzheimer (0.72) fue notablemente 
menor que el de la clase sana (0.90), es decir, aproximadamente 28% de los pacientes 
con Alzheimer fueron clasificados erroneamente como sanos.

Este hallazgo es clinicamente relevante porque, segun la ficha del dataset elaborada 
al inicio del laboratorio, el falso negativo fue identificado como el error mas 
costoso: un paciente con Alzheimer no detectado pierde la oportunidad de intervencion 
y seguimiento temprano. Esto sugiere que, para un despliegue real, seria necesario 
explorar tecnicas adicionales como el ajuste del umbral de decision, el uso de 
class_weight='balanced', o una busqueda de hiperparametros mas exhaustiva orientada 
especificamente a maximizar el recall de la clase minoritaria, en lugar de optimizar 
unicamente el F1-macro global.

En terminos de reproducibilidad, el proyecto completo (entorno virtual, dependencias, 
descarga de datos, pruebas automatizadas y control de versiones con Git) permite que 
cualquier persona con las credenciales de Kaggle correspondientes pueda replicar 
exactamente los resultados aqui presentados, cumpliendo con los principios de ciencia 
de datos reproducible establecidos en la Unidad 01 del curso.

---

# LAB03 - Ensambles, reduccion dimensional y Green AI

## Protocolo

Se reutilizo el mismo dataset, target (Diagnosis) y particion (80/20, random_state=42, estratificada) del Ejercicio 01/LAB02, sin modificaciones.

## Catalogo de modelos evaluados (6 configuraciones)

| Modelo | F1-macro | Fit mediana (s) | Predict (ms) | Tamano (KB) | Pareto |
|--------|----------|------------------|---------------|-------------|--------|
| boost | 0.944 | 0.296 | 7.10 | 358.4 | Si |
| rf_300 | 0.933 | 0.447 | 48.46 | 4130.7 | No |
| rf_100 | 0.919 | 0.185 | 58.33 | 1408.5 | Si |
| svm_c1 | 0.816 | 0.322 | 34.13 | 272.5 | No |
| svm_c10 | 0.812 | 0.543 | 32.05 | 285.5 | No |
| logistic | 0.799 | 0.019 | 4.20 | 5.7 | Si |

## PCA

PCA con 95% de varianza retenida conservo 30 de 32 componentes originales (reduccion marginal). F1-macro con PCA: 0.818 vs sin PCA: 0.816 (diferencia no significativa).

## t-SNE

Dos mapas con semillas distintas (42 y 7) muestran una estructura similar: nube densa con clases entremezcladas, sin separacion visual clara. Ver reports/tsne_two_seeds.png.

## Decision de Green AI

Se selecciono logistic como alternativa eficiente frente a boost (maximo F1):
- Diferencia de F1-macro: -0.145 (15.4% menor)
- Ahorro en tiempo de ajuste: 93.6%
- Ahorro en tiempo de inferencia: 40.8%
- Reduccion de tamano: 98.4% (5.7 KB vs 358.4 KB)

Ver analisis completo y limitaciones en notebooks/03_ensambles_green_ai.ipynb y reports/pareto.png.

## Entorno de ejecucion

- Python 3.13.5, Windows-11-10.0.26200-SP0
- Procesador: Intel64 Family 6 Model 154 Stepping 4
- scikit-learn 1.9.1

## Ejecucion

python -m pytest -q (con PYTHONPATH=src)
Resultado esperado: 9 passed
