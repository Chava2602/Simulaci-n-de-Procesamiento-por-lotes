### Funcionamiento de `error_process()` y `break_process()`

#### `error_process()`
- **Descripción:** Esta función simula un error en la ejecución de un proceso, marcándolo como interrumpido y moviéndolo a la lista de procesos finalizados.
- **Funcionamiento:** Cuando se llama a `error_process()`, comprueba si hay un proceso en ejecución. Si es así, marca ese proceso como interrumpido y lo mueve a la lista de procesos finalizados. Esto simula un escenario donde un proceso no puede completarse correctamente debido a un error.

#### `break_process()`
- **Descripción:** La función `break_process()` simula la capacidad de interrumpir un proceso en ejecución y moverlo a la lista de procesos en espera.
- **Funcionamiento:** Al llamar a `break_process()`, se comprueba si hay un proceso en ejecución. Si es así, se determina la posición original del proceso en la lista de procesos y se mueve a esa posición en la lista de procesos en espera. Esto simula la capacidad de detener un proceso en ejecución y continuar su ejecución más tarde.
