## Simulador de Procesamiento por Lotes

El simulador de procesamiento por lotes es una aplicación desarrollada en Python con la interfaz gráfica tkinter. Esta herramienta simula el procesamiento de múltiples procesos en lotes, mostrando el estado de los procesos en ejecución, en espera y finalizados en tiempo real.

### Estructura del Código

El código se organiza en diferentes secciones, cada una con un propósito específico:

1. **Definición de Clases**: 
   - `Process`: Define la clase de un proceso con atributos como número de proceso, nombre del programador, datos de la operación, tiempo máximo de ejecución y resultado.

2. **Funciones de Generación de Procesos**: 
   - `generate_data_process()`: Genera datos aleatorios para el proceso, como el nombre del programador y el tiempo máximo de ejecución.
   - `generate_operation_process()`: Genera una operación aleatoria (+, -, *, /) con sus operandos y resultado.
   - `generate_process_txt(processes)`: Genera un archivo de texto con la lista de procesos pendientes.

3. **Funciones de Actualización de la Interfaz Gráfica**: 
   - `clear_text_boxes()`: Borra el contenido de los cuadros de texto.
   - `update_GUI_process_lbl_txt_box()`: Actualiza los cuadros de texto y etiquetas con la información de los procesos.

4. **Funciones de Control de Procesos**: 
   - `running_process()`: Simula la ejecución de los procesos, moviendo los procesos de la lista de espera a ejecución y de ejecución a finalizados.
   - `start_clock()`: Inicia el contador de tiempo global.
   - `update_elapsed_time()`: Actualiza el tiempo transcurrido en la interfaz gráfica.
   - `generate_process()`: Genera una nueva lista de procesos pendientes.
   - `generate_result_txt()`: Genera un archivo de texto con los resultados de los procesos finalizados.

5. **Funciones de Cálculo de Lotes**: 
   - `calculate_current_batch_number(current_process_number)`: Calcula el número de lote actual.
   - `calculate_current_batch_processes()`: Calcula el número de procesos en el lote actual.
   - `last_number_process_batch()`: Calcula el número de procesos en el último lote.
   - `calculate_number_of_batches()`: Calcula el número total de lotes.

6. **Interfaz Gráfica**:
   - `create_main_window()`: Crea la ventana principal de la aplicación con botones, etiquetas y cuadros de texto.

### Conclusiones

El simulador de procesamiento por lotes es una herramienta educativa y práctica para comprender los principios del procesamiento por lotes. Su estructura modular y su interfaz gráfica intuitiva lo hacen fácil de entender y de utilizar. Además, su capacidad para generar informes de resultados lo convierte en una herramienta útil para el análisis y la evaluación de procesos simulados.
