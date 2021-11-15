# Locked By Coordinates

Este módulo agrega las siguientes funcionalidades a los métodos de envió para E-Commerce
- Se agrega al menú de "Configuración" en Sitio web, "Áreas restringidas" en el cual podremos crear por medio de un Form un área restringida para los envíos de ciertos "métodos de envió".
- Gracias a los módulos de Yopi Angi (gityopie) Web Google Maps Drawing y Web Google Maps los cuales han sido adaptados para este funcionamiento podremos dibujar cuales son las áreas restringidas por medio de api de google
- Este módulo utiliza la api de google geocode para localizar las coordenadas de la dirección del cliente para luego comprobarlas con las coordenadas de nuestra área restringida


## Instalación
- Este módulo utiliza API de Google por lo tanto necesitamos tener una Key válida para dichas API, nuestra key debemos ponerla en el módulo ati_locked_by_coordinates en el archivo "delivery_carrier.py" en la línea "key = "&key=YOUR-KEY" reemplazando "YOUR-KEY" por su API. También en el archivo "map_view_webiste_sale_delivery.xml" reemplazando en la línea "document.getElementById("custom_src").src="https://www.google.com/maps/embed/v1/place?key=YOUR-KEY&amp;q="+value+"&amp;attribution_source=Google+Maps+Embed+API&amp;attribution_web_url=https://YOUR-WEB/";}", en "YOUR-KEY" ira nuestra Key y en "YOUR-WEB ira nuestra web habilitada para la API
- Este módulo depende de Web Google Maps Drawing y Web Google Maps esto hace a que para un buen funcionamiento estos módulos no solo tengan que estar correctamente instalados sino también indicar en "Configuraciones" nuestras api y características como por ejemplo las librerías a utilizar, en este caso seria las siguientes librerías "geometry,places,drawing,visualization" y también nuestra Api Key de Google
- Para utilizar este módulo con productos de servicios tendremos que realizar las siguientes modificaciones:
- Para que verifique método de envió también en productos de servicios: 
odoo/addons/website_sale_delivery/controllers/main.py
Linea 87 cambiar"has_storable_products = any(line.product_id.type in ['consu', 'product'] for line in order.order_line)" por
"has_storable_products = any(line.product_id.type in ['consu', 'product', 'service'] for line in order.order_line)"
- Para que habilite botón "pagar ahora" sin estar seleccionado ningún método de envió: 
odoo/addons/website_sale_delivery/static/src/js/website_sale_delivery.js
Linea 29 cambiar "if ($carriers.filter(':checked').length === 0) {" por "if ($carriers.filter(':checked').length < 0) {"



Autores y Colaboradores:
Ivan Arriola - Autodidacta TI admin@autodidactati.com
Héctor Quiroz - Trixcom hectorquiroz@trixocom.com
