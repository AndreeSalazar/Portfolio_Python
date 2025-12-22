# Fórmulas Avanzadas de Excel/Sheets

## 🔍 Funciones de Búsqueda

### VLOOKUP
```excel
=VLOOKUP(valor_buscado, tabla, columna, [tipo_coincidencia])
```
**Ejemplo:**
```excel
=VLOOKUP(A2, Productos!A:B, 2, FALSE)
```

### XLOOKUP (Excel 365/2021)
```excel
=XLOOKUP(valor_buscado, rango_busqueda, rango_resultado, [si_no_encontrado])
```
**Ejemplo:**
```excel
=XLOOKUP(A2, Productos!A:A, Productos!B:B, "No encontrado")
```

### INDEX/MATCH (Más flexible)
```excel
=INDEX(rango_resultado, MATCH(valor_buscado, rango_busqueda, 0))
```
**Ejemplo:**
```excel
=INDEX(Productos!B:B, MATCH(A2, Productos!A:A, 0))
```

## 📊 Funciones Estadísticas

### Básicas
```excel
=AVERAGE(rango)      # Promedio
=MEDIAN(rango)       # Mediana
=MODE.SNGL(rango)    # Moda
=STDEV.S(rango)      # Desviación estándar
=VAR.S(rango)        # Varianza
```

### Condicionales
```excel
=COUNTIF(rango, criterio)           # Contar con condición
=SUMIF(rango, criterio, rango_suma) # Sumar con condición
=AVERAGEIF(rango, criterio, rango)  # Promedio con condición
```

### Múltiples condiciones
```excel
=COUNTIFS(rango1, criterio1, rango2, criterio2)
=SUMIFS(rango_suma, rango1, criterio1, rango2, criterio2)
=AVERAGEIFS(rango, rango1, criterio1, rango2, criterio2)
```

## 📅 Funciones de Fecha

```excel
=TODAY()              # Fecha actual
=NOW()                # Fecha y hora actual
=YEAR(fecha)          # Año
=MONTH(fecha)         # Mes
=DAY(fecha)           # Día
=DATEDIF(fecha1, fecha2, "d")  # Diferencia en días
=EOMONTH(fecha, 0)    # Último día del mes
```

## 🔤 Funciones de Texto

```excel
=LEFT(texto, num_caracteres)
=RIGHT(texto, num_caracteres)
=MID(texto, inicio, num_caracteres)
=CONCATENATE(texto1, texto2)
=TEXT(valor, formato)
=UPPER(texto)
=LOWER(texto)
=TRIM(texto)          # Eliminar espacios
```

## 🔢 Funciones Lógicas

```excel
=IF(condición, valor_si_verdadero, valor_si_falso)
=AND(condición1, condición2)
=OR(condición1, condición2)
=NOT(condición)
=IFERROR(valor, valor_si_error)
```

## 📈 Tablas Dinámicas (Pivot Tables)

### Pasos:
1. Seleccionar datos
2. Insertar → Tabla dinámica
3. Arrastrar campos a:
   - Filas
   - Columnas
   - Valores
   - Filtros

### Funciones de valores:
- Suma
- Promedio
- Contar
- Máximo/Mínimo

## 🔄 Power Query (Excel)

### Pasos básicos:
1. Datos → Obtener datos → Desde archivo
2. Transformar datos
3. Aplicar cambios

### Transformaciones comunes:
- Filtrar filas
- Cambiar tipos de datos
- Agregar columnas
- Combinar consultas

## 📊 Gráficos Avanzados

### Tipos útiles:
- Gráfico de líneas (tendencias)
- Gráfico de barras (comparaciones)
- Gráfico circular (proporciones)
- Gráfico de dispersión (correlaciones)
- Gráfico combinado

## 💡 Tips Pro

1. **Nombres de rangos**: Asignar nombres a rangos para fórmulas más claras
2. **Tablas**: Convertir datos a tablas (Ctrl+T) para referencias dinámicas
3. **Validación de datos**: Controlar entradas con listas desplegables
4. **Formato condicional**: Resaltar datos importantes automáticamente
5. **Protección**: Proteger hojas y celdas importantes

---

**¡Practica con datos reales!** 📊

