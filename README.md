# Contraste de Noticias Internacionales

## 1. Introducción

>	El alcance del proyecto tiene como objetivo cubrir la necesidad de proporcionar perspectiva a la hora de conocer cuántas noticias relativas a otros países que no son España se están difundiendo a través de los medios de comunicación de mayor audiencia. Aportando meta-información acerca de estas noticias internacionales, se puede ayudar a las personas a obtener una mejor percepción sobre los medios de comunicación a los que tiene acceso. 

## 2. Solución planteada

>	Se propone la clasificación, en países, de noticias de la sección internacional escogidas de los medios de comunicación escrita, en formato electrónico, con mayor audiencia. De esta forma será posible discutir acerca de qué noticias se están publicando bajo qué medios y poner en perspectiva las cifras con respecto a lo que está ocurriendo y agencias internacionales de noticias, a priori independientes, están cubriendo. 

>	Para ello, será necesario extraer las noticias de uno de los diarios que entren en el top 10 de prensa no deportiva más leída. Tras ello, se organizarán las noticias de forma que sean accesibles por un clasificador, que podrá ser un bot de Telegram. con las noticias clasificadas, llega el momento de realizar un análisis que permita extraer conclusiones y, para ello, se hará uso de la herramienta Tableau que, a su vez, permitirá presentar los datos. 

## 3. Metodología

>	Para la realización del proyecto se ha escogido la metodología sugerida por la [School of Data](https://schoolofdata.org/methodology/). Tal y como describe la propia entidad, esta metodología proporciona una aproximación para trabajar con datos de principio a fin de forma que, una vez establecida la forma de trabajar  y quién va a utilizar estos datos, se divide en pasos a seguir para llevar a cabo todo el proceso. 
>	Los pasos que la School of Data propone son los siguientes: 

1.	Definir: El problema a resolver. 
2.	Buscar: Los datos necesarios para la resolución del problema. 
3.	Obtener: La información de su lugar de origen. 
4.	Verificar: Que los datos obtenidos son válidos para conseguir nuestro propósito. 
5.	Limpieza: De datos para que se ajuste a nuestras necesidades. 
6. 	Análisis: De resultados mediante herramientas que aporten valor añadido a los datos. 
7.	Presentación: De conclusiones que permitan resolver el problema planteado. 

## 4. Resultados

>	Los resultados esperados no han podido ser obtenidos por falta de tiempo en el desarrollo de la solución. Esto es debido a que el proyecto ha sufrido suficientes cambios y ha encontrado barreras insalvables en un tiempo razonable. 

>	Actualmente el proyecto se encuentra en la fase de obtención de datos en lo que a clasificación se refiere. Las noticias se encuentran guardadas en una base de datos y el bot de Telegram es capaz de presentarlas a los usuarios que realicen, de forma manual, una clasificación. La fase de verificación y limpieza serían las encargadas de asegurar que no se han realizado clasificaciones incorrectas y después, mediante Tableau u otra herramienta gráfica para la presentación de datos, realizar un informe que ponga sobre un plano las cantidades de noticias publicadas por país. 

## 5. Guía de Uso

>	Como el resultado deseado no es posible mostrarlo mediante un cuadro de mando, sino que únicamente se han obtenido las noticias y se ha codificado un programa capaz clasificarlas, a continuación describiremos cómo hacer funcionar el software para la recolección de datos. 

>	Obtención de información de orígenes de datos web: Los ficheros con el código en Python que se encargan de la obtención de las noticias y los países existentes, así como su código alfa-2, se encuentran bajo el directorio sinf_scrapper. El programa lo componen los siguientes ficheros con sus correspondientes funcionalidades dentro del conjunto: 
-	getNews: Se encarga de extraer, mediante la técnica de scrapping, las noticias de la sección internacional del diario "El País" para insertarlos en una colección llamada 'noticias'en la base de datos . Nota: para que funcione, es necesario que se encuentre en el mismo directorio el fichero 'conn_conf.py', no incluído en el repositorio por razones de seguridad. 
-	getCountriesCC: Obtiene de la web <http://utils.mucattu.com/iso_3166-1.html> un listado con los nombres de los países junto a sus códigos ISO 3166-1 alfa-2 correspondientes, utilizados internacionalmente y que sería utilizado a posteriori para la clasificación de países y los inserta en la colección 'paises' de la base de datos. Nota: también hace uso del fichero 'conn_conf.py'.
-	limpiaRegistrosTabla: Este programa hubo que escribirlo a posteriori debido a que, cuando el bot recibe como respuesta un nombre de país, éste puede contener cualquier caracter, incluyendo acentos, espacios, mayúsculas y minúsculas y la búsqueda en la colección de países se complica sobremanera. Se decidió, pues, que los registros de la colección 'paises' debían contener una versión canónica del nombre del país, por lo que se decidió actualizar dichos registros de forma masiva mediante este script. 
-	conn_conf: Contiene la cadena de conexión a la base de datos, incluyendo las credenciales necesarias, así como la dirección IP del servidor que la contiene. Nota: se adjunta un dump de la base de datos con las noticias y los países. 

>	Bot de Telegram: Los ficheros para el bot se encuentran en el directorio sinf_bot y se encargan de ejecutar las rutinas que levantan un bot utilizable por Telegram. A continuación se listan los componentes del bot y su funcionalidad
-	country.bot.py: Es el programa principal encargado de dar vida al bot en Telegram. Extrae una noticia de la base de datos de noticias para presentarla al usuario y que este, mediante escritura con teclado, indique a qué país hace referencia. Nota: Hace uso del fichero que contiene el token de Telegram, tampoco incluído por motivos de seguridad. 
-	store.py: Contiene las rutinas que interactúan con la base de datos, desde recuperar una noticia a marcarla como 'inválida' (no clasificable por su ambigüedad) o actualizar el registro con el país candidato a ser el país de referencia. 
-	conn_conf.py: Es el mismo fichero que se describe en el anterior punto. Tampoco adjunto en el repositorio. 
-	telegramkey.py: Contiene el token proporcionado por Telegram para su uso con bots. Por motivos de seguridad, tampoco ha sido subido a los repositorios. 

### - Cómo hacer funcionar la aplicación:
>	La aplicación ha sido diseñada de forma modular. 

>	Por una parte, debe existir una instancia de la base de datos MongoDB, la cual debe estar configurada para dar soporte a la autenticación con las credenciales indicadas en los ficheros 'conn_conf.py'. Como alternativa, la aplicación puede conectarse a otra instancia de MongoDB siempre que se modifiquen los ficheros de conexión 'conn_conf.py' convenientemente. Actualmente se encuentra disponible un servidor ejecutando una instancia de MongoDB el cual satisface las peticiones que esta aplicación pueda realizar y seguirá estando disponible hasta el 31 de mayo de 2018, salvo caída del servicio. 

>	Para poblar la base de datos se ha programado una tarea periódica, en la máquina anteriormente mencionada, que cada hora comprueba si existen noticias que no han sido ya recogidas. Si se desea probar el funcionamiento de este scrapper, únicamente será necesario ejecutar el código utilizando Python3 y éste insertará las noticias que no se encuentren en la base de datos destino. 

>	De igual forma ocurre con el componente que obtiene los nombres de países 'getCountriesCC' el cual únicamente necesita ejecutarse una vez, cada vez que se desee regenerar la colección de países. Posterior a este proceso, debe ejecutarse el script 'limpiaRegistrosTabla.py', cuya funcionalidad, en esta versión de getCountriesCC, no ha sido integrada pero que es necesaria para el correcto funcionamiento del bot. 

>	Satisfechas las condiciones anteriores, el siguiente componente es el bot en sí mismo. Para ejecutarlo, de nuevo, es necesario utilizar la versión 3 de Python. El script que contiene el código del bot se llama 'country.bot.py' y debe dejarse corriendo en segundo plano para ser utilizado. 

>	Para realizar las pruebas es necesario disponer del software Telegram, disponible para la mayoría de las plataformas. En él, debe realizarse una búsqueda, para encontrar el bot, utilizando la siguiente cadena de texto: 'sinf_juasesoCNI2' sin las comillas.

>	Una vez dentro, con el comando '/inicio' se da comienzo a la conversación que permitirá la clasificación de la noticia. En el fichero 'Diagrama_conversacion_bot.pdf' se puede ver un diagrama con el flujo que la conversación puede seguir. 

>	La aplicación está inacabada, por tanto, queda pendiente programar un script que revise las respuestas proporcionadas para dar un país como resultado. Tras ello, los datos se pueden extraer para generar una visualización que ayude a resolver el problema propuesto. 

## 6. Términos de uso
 >	El contenido de este repositorio está sujeto a la licencia [GNU General Public License v3.0.](https://www.gnu.org/licenses/gpl-3.0.en.html)