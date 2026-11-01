# Justificación de relaciones del modelo HelpDesk EDU

- **Solicitante:** un ticket tiene exactamente un `User` solicitante, mientras que un usuario puede no haber solicitado tickets o haber solicitado varios. Es una asociación: el usuario existe independientemente de cada ticket.
- **Técnico:** un ticket puede no tener técnico o tener uno. Un técnico puede atender cero o varios tickets. Es una asociación; el ciclo de vida del usuario técnico no depende del ticket.
- **Comentarios:** un ticket puede tener cero o varios comentarios y cada comentario pertenece a un ticket. Se representa como composición, con el rombo negro junto a `Ticket`: en el modelo conceptual el comentario forma parte del seguimiento de ese ticket y su ciclo de vida está ligado a él.
- **Historial:** un ticket puede tener cero o varios eventos de historial y cada evento pertenece a un ticket. Se modela con composición y rombo junto a `Ticket`, porque el evento documenta la historia de ese ticket y no se concibe como un registro independiente de él.
- **Artículos:** cada artículo tiene un usuario autor y un usuario puede ser autor de cero o varios artículos. Es una asociación, ya que el artículo no es un componente del usuario y sus ciclos de vida no se definen como dependientes.

El código es un esqueleto en memoria. `Ticket` crea sus listas por separado y agrega comentarios y eventos mediante sus métodos; no implementa persistencia ni un mecanismo de borrado en cascada. La notación de composición expresa el criterio conceptual de pertenencia y ciclo de vida.
