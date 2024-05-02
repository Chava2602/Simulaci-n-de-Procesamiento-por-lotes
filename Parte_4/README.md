## Algoritmo Round-Robin (RR)

El algoritmo Round-Robin (RR) es un algoritmo de planificación de procesos en el que cada proceso recibe un intervalo de tiempo de CPU, conocido como quantum, y los procesos se ejecutan en orden circular, de manera que cada proceso recibe una parte equitativa de la CPU. Si un proceso no ha terminado cuando su quantum expira, se coloca al final de la cola de procesos listos para ejecutarse.

En el contexto de la simulación de procesamiento por lotes en el código proporcionado, el algoritmo RR se implementa para administrar la ejecución de procesos. Aquí está el fragmento relevante de código:

```python
def round_robin():
    global pending_processes, current_process, finished_processes, current_process_number, current_quantum
    
    if not current_process and pending_processes:
        current_process = pending_processes.pop(0)
        current_process_number = len(finished_processes) + 1
        current_quantum = quantum
        
    if current_process:
        if current_quantum > 0:
            current_quantum -= 1
            current_process.max_time -= 1
            
            if current_process.max_time <= 0:
                current_process.finish_time = elapsed_seconds
                finished_processes.append(current_process)
                current_process = None
                
        else:
            pending_processes.insert(0, current_process)
            current_process = None
            
    update_GUI_process_lbl_txt_box()
    lbl_global_clock.after(1000, round_robin)
```

1. Verifica si hay un proceso en ejecución (current_process). Si no hay ninguno y hay procesos pendientes en la cola (pending_processes), selecciona el siguiente proceso de la cola para ejecutarlo.
Si hay un proceso en ejecución, lo ejecuta durante un intervalo de tiempo igual al quantum asignado (current_quantum). Durante este tiempo, se decrementa el quantum y el tiempo restante de ejecución del proceso.

2. Si el tiempo restante de ejecución de un proceso alcanza cero, se considera que el proceso ha terminado y se agrega a la lista de procesos terminados (finished_processes). El proceso actual se establece como None para indicar que no hay ningún proceso en ejecución.

3. Si un proceso no ha terminado al final del quantum, se interrumpe y se coloca al final de la cola de procesos pendientes.

4. Actualiza la interfaz gráfica para reflejar los cambios en los procesos en ejecución, los procesos en espera y los procesos terminados.

5. Programa la siguiente ejecución del algoritmo después de 1 segundo, utilizando after() de tkinter para mantener el funcionamiento continuo del algoritmo en el tiempo.