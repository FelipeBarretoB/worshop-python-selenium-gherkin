# Taller de automatización de pruebas con Selenium, Python, Cucumber, Gherkin, y el patrón Page Object Model (POM).

# Paso 1: Instalación de Herramientas

## Antes de iniciar, asegúrate de tener instaladas las siguientes herramientas:
	- Python (https://www.python.org/downloads/) 
	- Selenium (pip install selenium)
	- Behave para Cucumber con Python (pip install behave)
	- Cucumber para casos de prueba con Gherkin (Esto ya viene con Behave.)

Puedes usar el requirements.txt para instalar todas las dependencias de una vez. Para ello, ejecuta el siguiente comando en la terminal o consola de comandos:

```bash
pip install -r requirements.txt
```

## Para correr los tests, usa el comando:
	- behave (debes correrlo en la terminal o consola de comandos desde la raíz de tu proyecto.)

### Cambios
Se añado el argumento de headless para que puedas correr el navegador sin que se abra la ventana.
A este proyecto se le añado un nuevo caso llamado "Successful login and buying a backpack" que se encuentra en la carpeta features.
Para este caso ya existia el paso de login, pero de ahí en adelante tuvimos que crear todo.
Del login pasamos a la pagina del inventario, creamos esta pagina en la carpeta pages y tambien creamos los steps en la carpeta steps adentro de features.
Este proceso se repitio para cada una de las paginas que se visitan en el caso de prueba. 
Es decir de login a la pagina del inventario, del inventario al carrito, del carrito a la pagina de informacion, de la informacion al overview y por
ultimo del overview a la pagina de finalizacion.

En la carpeta de steps, en cada archivo estan los pasos a seguir para cada una de las paginas.