<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una aplicación web para inscripción de laboratorios</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  2024/07/28</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Programación Web 2</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td><td>16-Jul-2024</td><td>FECHA FIN:</td>
        <td>28-Jul-2024</td><td>DURACIÓN:</td><td>04 horas</td>
    </tr>
    <tr>
        <td colspan="3">Estudiantes:
        <ul>
        <li>Johan Vilca Flores - Jvilcafl@usna.edu.pe</li>
        <li>Jael Emerson Huarca Pallani - jhuarcap@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

##  Tipo de Sistema
    Se trata de una aplicación web construida con el framework Django 4, que permita la inscripción de los alumnos en los horarios de laboratorios establecidos cada inicio de semestre.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    - RQ01 : El sistema debe estar disponible en Internet a traves de una URL.
    - RQ02 : El sistema debe permitir el inicio/cierre de sesión.
    - RQ03 : El sistema debe permitir gestionar compradores, autos y usuarios.

##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -  Concensionarios:En esta entidad se almacena los datos de los clientes que se responsabilizan para la 
         futura compra de autos o de un bien .
    -  Ventas : En esta identidad se almacena la forma de pago que se realizara y sobre la informacionb de la 
        marca y el modelo que esta selccionando para comprar. 

    -   Clientes: En esta identidad se almacena los datos de los usarios para el futuro registro de la base de 
          datos a la vez los responsables para realizar cualquier compra.
    
    -   Vendedores: En esta identidad se almacena los datos de los usarios para el futuro registro de la base 
           de datos para realizar la venta.
           
    -   Pago:  En esta identidad se almacena los diferentes tipos de medio de pago.
   
##  Diccionario de datos

    En la construcción de software y en el diccionario de datos sobre todo se recomienda y se utilizará el idioma inglés para especificar objetos, atributos, etc.

| Concensionarios | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| code  | Numerico| No | Si | Ninguno | Código |
| name  | Cadena| No | No | Ninguno | Nombre |

|Clientes | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| code  | Numerico| No | Si | Ninguno | Código |
| nombre| Cadena| No | No | Ninguno | Nombres |
| usuario | Cadena| No | Si | Ninguno | Nombres |
| contraseña| Cadena| No | Si | Ninguno | Nombres |
| email | Cadena| No | No | Ninguno | Correo electrónico |

| Vendedores| | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| code  | Numerico| No | Si | Ninguno | Código |
| nombre | Cadena| No | No | Ninguno | Nombres |
| usuario | Cadena| No | Si | Ninguno | Nombres |
| contraseña| Cadena| No | Si | Ninguno | Nombres |
| email | Cadena| No | No | Ninguno | Correo electrónico |

| Ventas | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| brands | Cadena| No | No | Ninguno | Nombre |
| brands | Cadena| No | No | Ninguno | Nombre |
| pay | Numerico| No | Si | Ninguno | Nombre |
##  Diagrama Entidad-Relación
<td style="width:25%;"><img src="https://github.com/Johan-Vilca-Flores/Proyecto-Final-pweb/blob/main/img/MOdelo%20de%20identidad.png?raw=true" alt="EPIS" style="width:80%    </td> 

##  Administración con Django
    Se muestran el uso de Django en la aplicacion 
   <td style="width:25%;"><img src="https://github.com/Johan-Vilca-Flores/Proyecto-Final-pweb/blob/main/img/Django.jpg?raw=true" alt="EPIS" style="width:80%    </td> 
      <td style="width:25%;"><img src="https://github.com/Johan-Vilca-Flores/Proyecto-Final-pweb/blob/main/img/django.jpg?raw=true" alt="EPIS" style="width:80%    </td> 

##  Plantillas Bootstrap
    Se seleccionó la siguiente plantilla para el usuario final (No administrador).

    Demo online:
    URL: concesionario.systes.net

    Se muestran las actividades realizadas para adecuación de plantillas, vistas, formularios en Django.
    ...

##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
    1. El alumno inicia sesión.
    2. El alumno selecciona el o los cursos donde desea realizar una inscripción.
    3. El alumno selecciona el grupo de laboatorio donde desea incribirse.
    4. El alumno puede tener la posibilidad de anular una incripción por varias razones: cambio de grupo, corregir error, etc.
    5. El alumno puede ver el consolidado de sus inscripciones.
    6. El alumno cierra sesión.

    Todas y cada una de estas pantallas debe funcionar en la plantilla bootstrap.
    A continuación se muestran las actividades realizadas para su construcción:
    ...

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de cursos, grupos y horarios establecidos para que el alumno sobre todo vea esta información en cualquier otro medio. En formato JSON. 
    2. POST : Con este método se enviara el código del alumno y se devolvera sus inscripciones. En formato JSON.
    
    Ejemplo: Prueba en Página web, aplicación móvil, PDF, etc.
    Se especifican los pasos para crear el servicio RestFul
    ...

##  Operaciones asíncronas AJAX
    Se propone el uso de AJAX para realizar la asignación de carga académica a los docentes que estan registrados. Esta operación la realizará el usuario operador encargado por el DAISI.
    Se muestran los pasos necesarios a realizar.
    ....



Github del proyecto:

URL en Heroku:

URL Playlist YouTube.
Producción de un PlayList en Youtube explicando cada una de los requerimientos.
Video 01 -....
Video 02 - ...
Video 03 - ...
Video 04 - ...
Video 05- ...



## REFERENCIAS
-   

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
