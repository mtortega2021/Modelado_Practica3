# Práctica 3: Integración y Simulación de Robots con ROS2, Gazebo y MoveIt2
## Introducción

En esta práctica trabajé con el robot que diseñé en la práctica anterior y lo integré dentro de un entorno simulado con Gazebo. Además, configuré el sistema de control con MoveIt2 para poder ejecutar movimientos de tipo pick and place. La práctica está dividida en dos partes:
    * Parte A: Configuración y modelado del robot en ROS2.
    * Parte B: Integración del robot en un entorno simulado y análisis del comportamiento dinámico durante una tarea de manipulación.

## Parte A – Configuración del robot en ROS2
Empecé creando un paquete en ROS 2 con toda la descripción de mi robot.
Modelo URDF con Xacro y cumplimiento de estándares REP-103 y REP-105
Usé macros en Xacro para definir componentes como las inercias y las uniones del robot. El modelo tiene la jerarquía correcta, con base_footprint como padre de base_link. También añadí:
* Una cámara en el efector final.
* Una cámara frontal.
* Un sensor IMU en el centro de la base.

### Visualización en RViz
En la primera parte veremos en el visualizador rviz2, las tfs del robot, y como se muestra correctamente. 

![image](https://github.com/user-attachments/assets/7219992e-1038-4f36-a9e4-734ea890713b)


¡Hemos conseguido pasar el robot a ros2 y poder larnzarlo y visualizarlo con rviz!

Ahora vamos a la segunda parte en la qu eentra el juego Moveit.
## Parte B – Simulación y análisis en Gazebo + MoveIt2
En esta parte comencé creando todo el entorno para que fuera apto para poder cargarlo en Moveit. Esto nme supuso algunso problemas dadoq ue me decia qu eel paquete no estaba correctamente. 
Despues de hacer varios ajustes conseguimos que en moveit se nos visualizara el robot.

![Screenshot from 2025-05-15 11-41-51](https://github.com/user-attachments/assets/ae7d8d62-10de-444d-8dce-d2ede1966b58)

Ahora empezaremos a crear los grupos, uno para elm gripper y otro para el brazo scara.
Lo que ocurre es que al hacer los cambios despues de crear el paquete no he conseguido poder lanzar el robot_gazebo.launch.py no se me lanza porque directamente no se me crea es como si no existiera. 
Os entrego la practica con todos los documentos y codigos para que podais ver el trabajo que he reaizadp. me da miucha rabia no poder terminar el trabajo pero no logro solucionarlo. 


