# Práctica de Git

*Nombre completo:* Candelario de Jesús Carrizales Urbina  
*Matrícula:* 2630129  

## Nombre de la práctica
Creación y sincronización de repositorio con Git y GitHub

## Objetivo
El objetivo de esta práctica fue aprender a crear un repositorio local con Git, vincularlo con un repositorio remoto en GitHub y practicar la sincronización de cambios en ambos sentidos: desde mi computadora hacia GitHub y desde GitHub hacia mi computadora.

## Descripción del procedimiento
Primero creé una carpeta en mi computadora con el nombre de la práctica e inicialicé un repositorio de Git dentro de ella. Después creé los archivos README.md y datos.txt, los agregué al área de preparación y realicé el primer commit.  
Luego creé un repositorio vacío y público en GitHub con el mismo nombre, lo vinculé con mi repositorio local y subí los archivos por primera vez.  
Después edité el archivo datos.txt directamente desde GitHub, hice un commit desde ahí y descargué los cambios a mi computadora con git pull.  
Por último, modifiqué otra vez el archivo desde mi computadora, realicé un nuevo commit y lo subí a GitHub con git push para comprobar que todo quedara sincronizado.

## Comandos de Git utilizados y su función
- git init → Inicializa un nuevo repositorio de Git en la carpeta actual.
- git branch -M main → Cambia el nombre de la rama principal a “main”.
- git add . → Agrega todos los archivos modificados al área de preparación (Staging Area).
- git commit -m "mensaje" → Guarda de forma permanente los cambios que están en el Staging Area, creando un commit con un mensaje descriptivo.
- git remote add origin URL → Vincula el repositorio local con el repositorio remoto de GitHub.
- git push -u origin main → Sube los commits locales a GitHub y establece la rama main como la rama de seguimiento.
- git pull origin main → Descarga y combina los cambios que se hicieron en GitHub con el repositorio local.
- git status → Muestra el estado actual de los archivos (si están modificados, preparados o sin cambios).
- git remote -v → Muestra las URLs de los repositorios remotos configurados.

## Cómo se creó el repositorio local
Creé una carpeta llamada practica-git-candelario-carrizales, abrí PowerShell dentro de ella y ejecuté el comando git init. Después configuré la rama principal con git branch -M main y creé los archivos README.md y datos.txt.

## Cómo se vinculó el repositorio local con GitHub
Creé un repositorio vacío y público en GitHub con el mismo nombre. Luego, desde PowerShell, usé el comando git remote add origin seguido de la URL del repositorio de GitHub. Verifiqué la conexión con git remote -v y subí los archivos por primera vez con git push -u origin main.

## Sincronización Local → GitHub
Después de modificar el archivo datos.txt en mi computadora, usé git add ., luego git commit -m "Actualización desde repositorio local" y finalmente git push para enviar los cambios a GitHub.

## Sincronización GitHub → Local
Edité el archivo datos.txt directamente en la página de GitHub, realicé un commit desde ahí y después, en mi computadora, ejecuté git pull origin main para descargar esos cambios y verlos reflejados en mi archivo local.

## Archivos contenidos en el repositorio
- *README.md* → Contiene la documentación completa de la práctica, con mi información personal, el procedimiento realizado y la explicación de los comandos.
- *datos.txt* → Archivo de texto que se utilizó para practicar la edición y sincronización de cambios tanto desde GitHub como desde el repositorio local.

## Conclusión personal
Con esta práctica aprendí de forma práctica cómo funciona Git y GitHub. Ahora entiendo mejor el flujo de trabajo: Working Directory → Staging Area → Local Repository → GitHub.  
Me di cuenta de lo importante que es sincronizar los cambios para no perder información y de lo útil que es poder trabajar tanto desde la computadora como desde la web.  
Al principio se me hizo un poco confuso el tema de la autenticación, pero una vez que lo entendí, todo fluyó mejor. Me siento más seguro usando Git y listo para seguir practicando.