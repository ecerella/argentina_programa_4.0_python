"""
Se pide implementar una clase CalendarioMes con los siguientes métodos:

__init__(): toma como parámetro un entero que representa el número de días del mes (entre 28 y 31). Debe lanar una excepción si no es un día válido.

agregar_evento(): toma como parámetro un día (número entero) y el nombre de un evento (cadena) y lo almacena en el calendario. Debe lanar una excepción si no es un día válido.

eliminar_evento(): toma como parámetro un día y el nombre de un evento y lo elimina del calendario.

Debe lanzar una excepción si no existe un evento con ese nombre.

obtener_eventos_dia(): toma como parámetro un día y devuelve una lista con los eventos programados para ese día, o la lista vacía si no hay eventos en ese día. Debe lanar una excepción si no es un día válido.
"""