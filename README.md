# Práctica 3: Integración y Simulación de Robots con ROS2, Gazebo y MoveIt2
## Introducción

En esta práctica se trabajó con el robot diseñado en la práctica anterior, integrándolo dentro de un entorno simulado con Gazebo. Además, se configuró el sistema de control mediante MoveIt 2 para ejecutar movimientos de tipo pick and place. La práctica se divide en dos partes:

    * Parte A: Configuración y modelado del robot en ROS 2.

    * Parte B: Integración del robot en un entorno simulado y análisis del comportamiento dinámico durante una tarea de manipulación.

## Parte A – Configuración del robot en ROS2
Se comenzó creando un paquete en ROS 2 que incluye toda la descripción del robot. El modelo se desarrolló en formato URDF utilizando Xacro, cumpliendo con los estándares REP-103 y REP-105. Se emplearon macros en Xacro para definir componentes como las inercias y las uniones del robot. El modelo presenta una jerarquía correcta, con base_footprint como padre de base_link.

Además, se incorporaron los siguientes sensores:

    * Una cámara en el efector final.

    * Una cámara frontal.

    * Un sensor IMU ubicado en el centro de la base.

### Visualización en RViz
En esta primera parte, se visualizó correctamente el robot en el visor rviz2, incluyendo los transforms (TFs) del modelo.
![image](https://github.com/user-attachments/assets/7219992e-1038-4f36-a9e4-734ea890713b)


Se logró portar el modelo del robot a ROS 2, pudiendo lanzarlo y visualizarlo satisfactoriamente en RViz.
Ahora vamos a la segunda parte en la qu eentra el juego Moveit.
## Parte B – Simulación y análisis en Gazebo + MoveIt2
En esta segunda parte, se configuró el entorno para permitir su carga en MoveIt 2. Durante el proceso surgieron algunos inconvenientes, ya que inicialmente el sistema indicaba que el paquete no estaba correctamente configurado. Tras realizar varios ajustes, se consiguió que MoveIt reconociera y visualizara el robot.

![Screenshot from 2025-05-15 11-41-51](https://github.com/user-attachments/assets/ae7d8d62-10de-444d-8dce-d2ede1966b58)

Se comenzaron a definir los grupos de planificación necesarios: uno para el gripper y otro para el brazo tipo SCARA. Sin embargo, tras realizar algunos cambios en la estructura del paquete, surgieron problemas al intentar lanzar el archivo robot_gazebo.launch.py, ya que el sistema no lo reconocía o no se generaba correctamente.

Aunque no se logró completar el proyecto en su totalidad, se entrega la práctica con todos los documentos y archivos de código desarrollados, como evidencia del trabajo realizado. A pesar del esfuerzo dedicado, no se consiguió resolver este último problema técnico, lo cual resultó especialmente frustrante.

## Cambios
Tras dar con el problema que no dejaba lanzar completamente los launchers, pudimos lanzar el launcher de los controladores y el de moveit que nos permite ya empezar a planear.
Cuando fuimos a lanzar el launcher para poder lanzar el gazebo con el mundo proporcionado por los profesores, nos encontroamos con que por la version que tenemos ros_gz_brige es un packete que no encuenrrta, hemos intentado instalarlo pero por la vercion que tengo no me lo permite, o no he consedguido hacerlo.


## Ros2 Bags
![image](https://github.com/user-attachments/assets/68139763-9a7b-4762-b646-bc79b19b2636)
aqui se muestra una imagen del ros2 bag en el cual recojo toda la informacion que se muestra al lanzar todos los launcher, en el que se muestrar toda la informacion de todos los topic


## Video lanzamiento de launchers
Lanzamiento de launchers:

[modelado_grabacionPantalla.webm](https://github.com/user-attachments/assets/d37dc5d7-54e6-4968-a9a3-4564afe8e5bb)

Imagen de rviz: 

v![image](https://github.com/user-attachments/assets/bd81c7ef-1bf7-4eb2-b53d-9e75b88a289c)

## Lanzamiento del launcher de gazebo

Gazebo por los motivos que se explican, no se lanza, pero al intentar lanzar el laucnher podemos observar en esta captura que esta reconociendo todos los links del robot.
![image](https://github.com/user-attachments/assets/474e7071-edd9-43ac-91ed-a2aeac07a5cf)

## Como continuaria
Si todo funcionara correctamente, lanzariamos todos los launchers, y podrias empezar a teleoperar el robot, y realizar el plan mediante la herramienta de Moveit. 
Realizariamos un ros bag record de la informacion de las fuerzas que realizan las articulaciones del brazo y con esa informacion podriamos graficarla. 

El problema que tiene el codigo es el ros_bridge esto ocurre porque mi version de ubuntu no esta actualizada al igual que en ros tengo la version de humble y esto hace que varias partes de la practica no funcionen correctamente. 




