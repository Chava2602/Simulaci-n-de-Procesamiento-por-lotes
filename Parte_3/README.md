**Algoritmo FCFS en la simulación de procesamiento por lotes:**

El algoritmo FCFS se implementa en la función `running_process()`, que maneja la ejecución de los procesos en el orden en que llegan.

```python
def running_process():
    global pending_processes, current_process, finished_processes, current_process_number
    if not current_process and pending_processes:
        current_process = pending_processes.pop(0)
        current_process_number = len(finished_processes) + 1
        current_process.arrival_time = elapsed_seconds
    if current_process:
        if current_process.max_time > 0:
            current_process.max_time -= 1
        else:
            current_process.finish_time = elapsed_seconds
            finished_processes.append(current_process)
            current_process = None
    update_GUI_process_lbl_txt_box()
    lbl_global_clock.after(1000, running_process)
```

1. ***Inicio de un nuevo proceso***: Si no hay un proceso en ejecución y hay procesos pendientes en la lista, se selecciona el próximo proceso de la lista de procesos pendientes y se establece como el proceso actual. Se registra el tiempo de llegada del proceso.

2. ***Ejecución del proceso***: Si hay un proceso actual en ejecución, se reduce en uno su tiempo máximo de ejecución (max_time). Si el tiempo máximo de ejecución llega a cero, se registra el tiempo de finalización del proceso y se agrega a la lista de procesos finalizados.

3. ***Actualización de la interfaz gráfica***: Después de ejecutar un proceso, se actualiza la interfaz gráfica para reflejar el proceso en ejecución, los procesos en espera y los procesos finalizados.

4. ***Llamada recursiva***: La función running_process() se llama recursivamente después de un segundo para simular el tiempo de procesamiento y continuar con la ejecución de los procesos.