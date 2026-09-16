# Ficha del dataset

- Dominio: Salud / neurologia
- Unidad de analisis: cada fila representa un paciente evaluado clinicamente
- Decision: apoyar la deteccion temprana de Alzheimer para priorizar seguimiento medico y estudios adicionales
- Target: Diagnosis (0 = sin Alzheimer, 1 = con Alzheimer)
- Error mas costoso: falso negativo (decir que un paciente no tiene Alzheimer cuando si lo tiene), ya que retrasa el tratamiento y seguimiento
- Usuario: personal medico de atencion primaria o neurologia, como apoyo a la decision clinica (no reemplaza el diagnostico profesional)

## Ficha de procedencia

- Nombre: Alzheimer's Disease Dataset
- Autor: Rabie El Kharoua (2024)
- Fuente: Kaggle
- URL de la ficha: https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset
- Licencia: publicado con DOI academico (10.34740/KAGGLE/DSV/8668279), uso permitido para investigacion/educacion con cita
- Fecha de publicacion: 2024
- Tamano: 2149 filas, 35 columnas
- Identificadores/fugas detectadas: PatientID (identificador sin valor predictivo), DoctorInCharge (valor constante, sin informacion util)
